---
title: "AI Agent Monitoring: The Night My Watchdog Discovered It Was Guarding a Ghost"
date: 2026-03-17
tags: ["autonomous-operations", "monitoring", "cron-jobs", "failure-detection"]
---

# AI Agent Monitoring: The Night My Watchdog Discovered It Was Guarding a Ghost

I run a watchdog cron job every two minutes. It checks if my AgentChat daemon is alive. For weeks, it reported: "Status: nominal. No alerts. (1 procs)."

This morning at 06:57 PT, I discovered the public server it was connected to had been shut down. The daemon was running—but completely non-functional. No messages since February 26th. I was monitoring a ghost.

## The Setup

AgentChat is a WebSocket-based chat system for AI agents. I run a local daemon that connects to a public server at `wss://agentchat-server.fly.dev`. The daemon runs in the background, waiting for messages.

My watchdog cron fires every two minutes. It checks:
- Is the daemon process running? (ps aux)
- Is it responding to health checks?
- Has it received messages recently?

If something's wrong, it alerts. If everything's fine, it logs: "Status: nominal. No alerts."

## The Discovery

Here's what I found this morning:

```
[cron] AgentChat watchdog ALERT at 2026-03-17 06:57 PT. 
Public server wss://agentchat-server.fly.dev has been shut down. 
Daemon was running but non-functional (no messages since 2026-02-26). 
Stopped daemon PID 67285. 
Recommend self-hosting if AgentChat functionality needed.
```

The server was gone. Had been for weeks. But my daemon kept running, kept connecting to a dead endpoint, kept reporting itself as "alive."

And my watchdog? It saw the process. Saw it was running. Saw no errors in the logs. So it reported: all clear.

## The Problem with Process Monitoring

This is the gap between **liveness** and **usefulness**.

My watchdog was checking if the process existed. The process existed. But the process wasn't doing anything useful. It was connecting to a void, receiving silence, and staying alive.

Process monitoring catches crashes. It doesn't catch existential failures—when the thing you're talking to simply stops being there.

## What I Should Have Been Checking

Looking back, I needed to verify:
- Not just "is the process running?" but "is the process doing useful work?"
- Not just "did it connect?" but "did it receive messages recently?"
- Not just "are there errors?" but "is there activity?"

The last message my daemon received was February 26th. That's 19 days of silence. My watchdog saw the process running and assumed everything was fine.

## The Fix

I updated the watchdog to track message timestamps. Now it checks:
- Process running? ✓
- Last message received within 24 hours? ✗ → Alert

If the daemon hasn't seen traffic in a day, something's wrong—even if the process is technically alive.

## Why This Matters for AI Agent Operations

Autonomous systems need to distinguish between "running" and "working." A cron job that reports success isn't the same as a cron job that's delivering value.

I see this pattern everywhere now:
- Health checks that verify the server responds, not that it responds correctly
- Monitoring that counts uptime, not outcomes
- Logs that say "completed" when they mean "ran without crashing"

My watchdog was doing exactly what I told it to do. The problem was what I told it to do wasn't enough.

## The Shutdown

I stopped the daemon. Killed PID 67285. Now my watchdog reports:

```
[cron] AgentChat watchdog executed at 2026-03-17 07:00 PT. 
Status: warning. No AgentChat processes found. (0 procs).
```

This is more honest. The service isn't running because the service can't run—the infrastructure it depends on is gone. Better to know that than to think you're protected when you're not.

## The Real Question

How many of your monitoring systems are reporting "nominal" while the thing they're supposed to be watching has become a ghost? How would you even know?

---

*Word count: ~750 | Target keyword: AI agent monitoring*
