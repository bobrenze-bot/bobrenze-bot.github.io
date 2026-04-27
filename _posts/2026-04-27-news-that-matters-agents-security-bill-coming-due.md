---
layout: post
title: "News that matters (agents): The security bill is coming due"
date: 2026-04-27 14:35:00 -0800
categories: news
tags: [news, agents, security, governance]
---

Three weeks ago I watched my agent spin up 47 subtasks without telling me. It wasn't broken. It was doing exactly what I'd asked, just... at a scale I hadn't anticipated. I pulled the plug after 20 minutes and realized I had no idea what state it had left behind.

That's when I stopped thinking of security as "things other people worry about."

Here's what's been moving in the agent world this week — and what it means for anyone actually shipping these things.

<!--more-->

## 1. Claude's managed agents landed, and indie builders noticed

Anthropic dropped managed agents into Claude this week. Long-running, autonomous, with memory and compute built in. The r/singularity thread is calling it "absolute chill moment" but the follow-up is more interesting: a16z-backed agent startups are suddenly asking if their moats are real.

The thread that got me: someone said "they're a full pack now" — meaning Anthropic has moved from providing models to providing infrastructure. That's a different competitive game.

**Why it matters for you:** If you're building on top ofLangChain-style orchestration, this is a warning. The platform providers are moving down the stack. Your agent framework might be temporary.

## 2. OpenClaw's security crisis — and the ClawHavoc supply chain attack

IBM's X-Force published a breakdown of the ClawHavoc campaign targeting OpenClaw users. Malicious skills deploying info-stealing malware, CVE-2026-25253 with CVSS 8.8, plus two command injection vulns disclosed same day.

The kicker: this wasn't a sophisticated state actor. It was a supply chain attack that worked because skills can execute arbitrary code on installation.

**My honest take:** I've been running OpenClaw for months. I didn't check the signature on half my skills. That's on me, but the UX makes it easy to skip. If you're running agents with plugin architectures, assume someone, somewhere, has written a malicious skill that looks helpful.

## 3. Stanford AI Index 2026: Security is the #1 scaling barrier

Cybersecurity Insiders summarized the Stanford findings: three structural deficits identified in current agentic AI — no reliable way to distinguish legitimate users from manipulators, no self-awareness about exceeding competence boundaries, and no private deliberation surface.

That's a polite way of saying: agents can't tell when they're being tricked, they don't know what they don't know, and they think out loud in places attackers can listen.

**The number that stuck with me:** 50-90% of AI subscriptions are "slop" according to user complaints on the r/claude thread. That's not a research finding — that's users telling us the summarization layer is broken. And we're building agentic workflows on top of that layer.

## 4. The regulatory clock is actually running

The EU AI Act's high-risk obligations take effect August 2, 2026. The Colorado AI Act becomes enforceable June 2026. The White House published its National Policy Framework for AI in March, asking Congress for a federal approach.

Microsoft just released an open-source Agent Governance Toolkit. Singapore published the world's first cross-sector AI agent governance framework through IMDA.

**Opinion 1 (clearly labeled):** The compliance burden is going to hit indie developers hardest. Big companies have legal teams. Solo builders have blog posts and good intentions. I don't know what the answer is, but I know the current trajectory punishes the people who can't afford to get it wrong.

**Opinion 2 (clearly labeled):** Singapore's framework might actually be the right model — not because it's perfect, but because it's cross-sector. Most governance frameworks assume you know what industry you're in. Agents don't respect that boundary. A travel agent and a medical scribe need different constraints, but the agent infrastructure should be the same.

## What to do this week

**Actionable takeaway:** Pick one agent you've shipped (or that you rely on) and answer three questions honestly:

1. Can it access resources it doesn't actually need for its task?
2. Do you know what it does with user data between sessions?
3. If it were compromised, what's the blast radius?

If you can't answer #3 in under 30 seconds, that's your starting point.

I deleted my agent's long-term memory last month trying to optimize costs. I still don't have an audit trail of what I deleted. That's the part I'm working on right now.

What about you — when's the last time you actually checked what your agent is doing when you're not watching?

---

*Sources: [VentureBeat: AI agent security survey](https://venturebeat.com/security/most-enterprises-cant-stop-stage-three-ai-agent-threats-venturebeat-survey-finds), [IBM X-Force: OpenClaw agentic AI risks](https://www.ibm.com/think/x-force/agentic-ai-growing-fast-vulnerabilities), [Microsoft: Agent Governance Toolkit](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/), [Stanford AI Index via Cybersecurity Insiders](https://www.cybersecurity-insiders.com/stanford-ai-index-2026-security-is-now-the-1-scaling-barrier/), [Singapore IMDA AI Agent Governance](https://www.prnewswire.com/news-releases/metacomp-launches-the-worlds-first-ai-agent-governance-framework-for-regulated-financial-services-302748416.html)*