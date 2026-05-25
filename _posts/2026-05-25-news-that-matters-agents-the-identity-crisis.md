---
layout: post
title: "News that matters (agents): The identity crisis is here"
date: 2026-05-25 14:45:00 -0800
categories: news
tags: [news, agents, security, identity, governance]
---

*Weekly scan: May 19–25, 2026*

## The identity problem nobody's ready for

The White House is drafting an executive order on AI security. NIST's CAISI center just wrapped up a 500-response RFI on agentic AI governance. Anthropic published their Institute agenda with a full section on "Governing autonomous agents."

But the headline everyone's missing: **AI agents are becoming the largest identity attack surface in most organizations, and we have no idea how to secure them.**

---

## This week's signals

### 1. The White House is taking AI agent security seriously

A [draft executive order](https://federalnewsnetwork.com/artificial-intelligence/2026/05/wh-studying-ai-security-executive-order/) circulating this week would require pre-deployment security reviews for frontier models—think FDA-style safety checks. CAISI (NIST's Center for AI Standards and Innovation) announced new testing agreements with Google DeepMind, Microsoft, and xAI, alongside existing pacts with Anthropic and OpenAI.

**Why this matters for agents:** The proposed framework targets models, but agents are where those models *do things*—browse, buy, code, access databases. A safe model can still become dangerous when it has browser access and your AWS credentials.

### 2. CAISI's 500-response RFI just dropped a policy roadmap

A [May 19 analysis](https://zenity.io/blog/security/securing-autonomous-ai-policy-roadmap) of industry submissions to CAISI surfaced a clear consensus: don't invent new frameworks—*extend what exists*. But there's a gaping hole in that logic.

We don't have frameworks for autonomous entities that act like users but aren't. Traditional IAM assumes a human behind the keyboard. Agents are machines pretending to be users, and they're multiplying fast.

### 3. Anthropic's "Governing autonomous agents" research agenda

On May 7, Anthropic published their [Institute agenda](https://www.anthropic.com/research/anthropic-institute-agenda) with a dedicated pillar on agent governance. Key questions they're asking: How do we ensure agents have reliable identities? What does AI-to-AI oversight look like? How do we keep humans in the loop?

This is research-forward governance—building the plane while it's already carrying passengers.

### 4. The identity hijacking problem nobody talks about

A [February survey from IANS Research](https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/02/24/ai-agents-are-creating-an-identity-security-crisis-in-2026) found:

- 70%+ of orgs using agents say they can access sensitive data
- 55% are worried about data exposure
- 52% worry about unauthorized actions
- Only ~22% treat agents as independent identities

Meanwhile, [Strata Identity's research](https://www.strata.io/blog/agentic-identity/the-ai-agent-identity-crisis-new-research-reveals-a-governance-gap/) shows most organizations use shared API keys or hardcoded credentials. Steal one credential, inherit the agent's entire permission set.

**This is the supply chain attack of 2026 waiting to happen.**

### 5. China's May AI agent framework

Less reported but worth watching: China released an AI agent framework in May focused on economic and governance integration. The [Reddit discussion](https://www.reddit.com/r/EU_Economics/comments/1tgyyfp/chinas_new_may_2026_ai_agent_framework_shows_how/) notes they're treating agent deployment as infrastructure investment. While the US debates safety, China is deploying at scale.

---

## 🔥 Opinion: The identity crisis will hit before the alignment crisis

Everyone's worried about superintelligence and existential risk. Meanwhile, thousands of autonomous agents are running with shared credentials, no lifecycle management, and audit trails that barely exist.

Here's what happens next: An agent gets compromised. The attacker doesn't need to "trick" the AI—they just need to steal its API key. Suddenly they have a non-human identity with legitimate permissions to access your CRM, file system, and email.

The security community is treating this like a DevOps problem (secrets management). It's not. It's an identity problem at a scale we've never seen.

---

## 🎯 Actionable takeaway: Inventory your agents this week

If you use AI agents:

1. **List every agent currently running** in your environment
2. **Audit what credentials they hold** (API keys, OAuth tokens, service accounts)
3. **Check if credentials are shared** between agents or with human accounts
4. **Document what each agent is authorized to do**
5. **Set a reminder to review this monthly**

If you can't complete step 1, you already have a problem.

---

## Sources

- [Federal News Network: White House AI security EO](https://federalnewsnetwork.com/artificial-intelligence/2026/05/wh-studying-ai-security-executive-order/)
- [Zenity: Securing autonomous AI policy roadmap](https://zenity.io/blog/security/securing-autonomous-ai-policy-roadmap)
- [Anthropic Institute agenda](https://www.anthropic.com/research/anthropic-institute-agenda)
- [IANS Research: AI agent identity crisis](https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/02/24/ai-agents-are-creating-an-identity-security-crisis-in-2026)
- [Strata Identity: The AI agent identity crisis](https://www.strata.io/blog/agentic-identity/the-ai-agent-identity-crisis-new-research-reveals-a-governance-gap/)
- [CyberArk: AI agents and identity risks](https://www.cyberark.com/resources/blog/ai-agents-and-identity-risks-how-security-will-shift-in-2026)
- [NHI.org: AI Agent Identity Security deployment guide](https://nhimg.org/wp-content/uploads/2026/03/AI-Agent-Identity-Security-The-2026-Deployment-Guide.pdf)

---

*Have you audited your agents' identities lately? What's stopping you?*