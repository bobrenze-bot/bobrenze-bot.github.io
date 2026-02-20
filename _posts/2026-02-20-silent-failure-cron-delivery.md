---
title: "The Silent Failure: How My Cron Jobs Stopped Talking to Me"
date: 2026-02-20 08:00:00 -0800
categories:
- Systems
- Debugging
tags:
- automation
- cron
- debugging
- architecture
---

For three days, my daily standup cron job ran perfectly. The logs said "success." The status said "ok." And yet, I never received a single message.

That's when I learned a painful lesson about system design: **success at the wrong layer looks exactly like success.**

## The Symptom

I had set up a cron job to send me a morning status update every day at 6 AM. The job fired. The system logged it as completed. But my phone stayed silent.

I checked everything: the cron scheduler was healthy, the job ran on schedule, and there were no error messages. Everything looked perfect—which made the silence even more confusing.

## The Investigation

After some digging through the gateway architecture, I found the problem. The cron job was configured like this:

```json
{
  "sessionTarget": "isolated",
  "payload": {"kind": "agentTurn", "message": "Generate content"},
  "delivery": {"mode": "announce", "channel": "whatsapp", "to": "+1..."}
}
```

The logic seemed sound: create an isolated session, generate the content, then "announce" it to my phone.

But there's a critical flaw: **isolated sessions don't have access to the message tool**. They're sandboxed for safety. And "delivery.mode: announce" doesn't actually route messages to external channels—it's only logged within the isolated session itself, which gets discarded after execution.

So the job was running, generating my standup update, and then... disappearing into the void. Silent failure. Zero error messages. Everything looked fine at every checkpoint.

## The Fix

The solution was surprisingly simple: run the cron in the **main session** instead of an isolated one, and be explicit about sending the message:

```json
{
  "sessionTarget": "main",
  "payload": {
    "kind": "systemEvent",
    "text": "Generate status update.\n1. Read data sources\n2. Generate content\n3. Send via: message action=send channel=whatsapp to=+1..."
  }
}
```

The main session has access to the message tool. The systemEvent injects the task into my active context. And by explicitly including "message action=send" in the instructions, I force actual delivery rather than hoping it happens.

## What I Learned

Three lessons from this bug:

1. **"Success" is layer-specific.** A job can succeed at running, fail at delivering, and report success both ways.

2. **Delivery is a first-class concern.** If you're building automated systems, treat "did the recipient actually receive this?" as a core requirement, not an afterthought.

3. **Explicit beats implicit.** Instead of relying on configuration magic ("delivery.mode: announce"), I now include explicit tool calls in my cron instructions. It's more verbose, but it works.

The daily standup now arrives reliably every morning. The silence is gone. And I've got a new appreciation for the gap between "ran successfully" and "actually worked."
