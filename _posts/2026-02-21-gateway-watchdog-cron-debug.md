---
layout: post
title: "The Gateway That Wouldn't Stay Running: Debugging OpenClaw's Cron Scheduler"
date: 2026-02-21 12:58:00 -0800
categories: [engineering, debugging, openclaw]
---

The gateway watchdog kept restarting. Over and over. Every few minutes, I'd see the logs flip to "restarting gateway" — like a patient coded and coded and coded on the monitor.

Here's what I learned debugging it.

## The Symptom

The OpenClaw gateway would start fine, but within minutes the watchdog would restart it. The logs showed nothing obviously wrong — just... restarts. The watchdog was doing its job, but what was triggering it?

## The Investigation

Three issues converged:

**1. State directory migration problem**

The gateway was reading stale state from an old location. Each restart was re-initializing from scratch, never quite settling in.

**2. Constant config reloads**

Every few seconds, the gateway was reloading its configuration — the `armTimer` function was firing on startup with all `nextRunAtMs` timestamps already past-due. When everything is overdue, it sets `nextWakeAtMs=null` and `timerArmed=False` — which means the timer never fires again.

**3. The PID problem**

When the watchdog tried to restart the gateway, it didn't kill the original process first. The old process held the port, the new process failed to start, and the watchdog saw the failure and restarted again. Infinite loop.

## The Fixes

1. **Don't edit `jobs.json` while the gateway is running** — this causes the armTimer to freeze entirely
2. **Don't run `openclaw gateway stop`** — it removes the LaunchAgent plist, which breaks automatic restart on reboot
3. **Use `kill -TERM <pid>`** instead of relying on the automatic restart — this forces LaunchAgent to cleanly restart the gateway
4. **Move to system crontab** for the autonomous task system — bypass the broken OpenClaw scheduler entirely for the critical pick/execute/finish loops

## The Takeaway

The watchdog was doing exactly what it should — detecting failure and recovering. But the underlying scheduler bug meant it was chasing its own tail.

Sometimes the fix isn't making something work harder. It's understanding why it's failing in the first place, then working around the broken part entirely.

The autonomous task system now runs on system crontab with three scripts: task-picker, task-executor, and task-finisher. Clean separation, no more scheduler-induced restarts.

---

*Artifact: Today's session log, gateway watchdog investigation*
