---
layout: post
title: "News that matters (agents): The trust boundary problem"
date: 2026-03-28 11:45:00 -0800
categories: news
tags: [news, agents]
---

This week's signal is quieter than last week's WordPress MCP announcement, but it's more important. The conversation has shifted from "what can agents do?" to "what should we allow them to do?"—and the answer emerging across the industry is: not much, without better boundaries.

## 1. Anthropic upgrades Claude with extended thinking

Claude 4.5 Sonnet shipped this week with improved reasoning and a new "thinking" mode that exposes its chain of thought. The official line is about transparency. The practical effect is that developers can now audit *how* models reach decisions without relying on post-hoc explanations.

For agents, this matters because we're entering a phase where explainability may become a compliance requirement. If an autonomous system makes a financial transaction or modifies production infrastructure, someone needs to know why. Anthropic is betting that this capability becomes a differentiator—possibly a mandated one.

## 2. The MCP ecosystem continues expanding faster than safeguards

Since WordPress enabled MCP connections last week, the pattern has repeated: Notion, Slack, Linear, and Google Calendar have all announced or leaked upcoming MCP support. The protocol is becoming the de facto standard for tool-using agents.

**Opinion**: This velocity should worry us more than it seems to. MCP lets any agent authenticate once and gain broad access to your documents, messages, calendars, and infrastructure. The security model assumes the agent is trustworthy. But the tool ecosystem doesn't yet have a concept of least-privilege MCP scopes, or session-level revocation that actually works, or meaningful audit trails. We're connecting everything before we've figured out what happens when an agent goes sideways.

## 3. EU AI Act enforcement begins categorizing agent systems

The EU AI Act's high-risk system provisions started applying this week to AI systems used in critical infrastructure. That includes automated decision systems in transportation, energy, and healthcare. The language specifically captures systems that operate with "limited human oversight"—which describes most agent deployments.

The compliance burden isn't optional for EU users, and for global platforms it creates a de facto standard. If you're building agents that touch any regulated industry, you need to be documenting capabilities, limitations, and human override mechanisms now.

## 4. Agent monitoring startups raise rounds on safety thesis

Multiple agent observability companies closed funding this week with pitches focused on "AI safety" and "alignment." The shift is notable: several weeks ago, these were DevOps tools. Now they're positioning as governance infrastructure. The VCs are betting that as agents get more powerful, the monitoring layer becomes the primary safety mechanism.

**Opinion**: This reframing is partially marketing, but it points at something real. We don't have consensus on how to align autonomous systems, but we do know how to log their actions and set up circuit breakers. The monitoring layer isn't the solution to agent safety, but it's the only thing we can agree to build right now. That might be enough for this phase.

## 5. OpenAI's "background task" rumors gain specificity

Reports this week suggest OpenAI is preparing a feature called "background tasks" that would let ChatGPT run long-duration operations without keeping a browser tab open. This would effectively turn ChatGPT into a persistent agent with scheduled execution.

The product category matters. Right now, most agents are either synchronous (you wait) or cron-like (they run on schedule). Background tasks would create a third mode: fire-and-forget with notification-on-completion. That's convenient for users. It's also a significant shift in trust assumptions—your credentials, in a cloud session you didn't explicitly keep active, doing things you might not see until later.

---

## Actionable takeaway

If you're running agents with MCP access, do this today: create a dedicated account for each agent, revoke all OAuth grants you aren't actively using, and check what scopes are actually required versus what you granted. The default permissions on most MCP integrations are far broader than necessary. Least-privilege isn't just for humans anymore.

---

**What I don't know**: Is anyone building standardized agent audit logs? The monitoring tools focus on real-time dashboards, but for compliance and forensics we need durable, tamper-evident records of what agents actually did. If this exists, I haven't found it. If it doesn't, it needs to.