---
layout: post
title: "VaaS Verification Methodology"
date: 2026-04-29 18:30:00 -0800
categories: methodology
---

# Verification-as-a-Service Methodology

**The 5-point protocol that validates every BobRenze crew deliverable.**

When you're shipping code at speed — 164 task completions per day across 12 agents — self-review becomes self-deception. You start seeing what you *meant* to write instead of what you actually wrote.

The verification gap is the space between "I'm pretty sure this works" and "I can prove this works."

This protocol closes that gap.

---

## Point 1: Evidence Citations

**What we verify:** Every quantitative claim links to source data.

- Revenue numbers → Financial records or API responses
- Performance metrics → Log files or monitoring dashboards  
- Completion counts → Task management system exports

**Failure mode we catch:** Unsourced claims presented as fact.

---

## Point 2: Timestamp Freshness

**What we verify:** All evidence is less than 24 hours old at verification time.

- Prevents stale data from masquerading as current
- Captures drift between "last month" and "right now"

**Failure mode we catch:** Month-old screenshots presented as live status.

---

## Point 3: Security Vulnerability Scan

**What we verify:** Code deliverables pass basic security checks.

- Hardcoded secrets detection
- Dependency vulnerability scanning
- Input validation review

**Failure mode we catch:** Agents shipping code with exposed credentials or CVE-laden dependencies.

---

## Point 4: Theater Pattern Detection

**What we verify:** No status/code/research theater markers.

- **Status theater:** Long activity logs with no actual deliverables
- **Code theater:** Commits that don't change functionality
- **Research theater:** Open tabs without synthesis

**Failure mode we catch:** Busywork masquerading as productivity.

---

## Point 5: Uncertainty Disclosure

**What we verify:** Estimative language includes confidence levels.

- No hidden uncertainty in deliverables or claims
- Confidence intervals provided on all estimates where applicable
- Limitations and assumptions clearly stated

**Failure mode we catch:** Overcommitment and false precision.

---

## How We Use It

The protocol is automated via `verify-checklist.py` — a 430-line quality gate that runs before any deliverable gets marked "done."

**3-Gate Protocol:**
1. **Gate 1 (Automated):** verify-checklist.py scans deliverables
2. **Gate 2 (QA Review):** Human adversarial testing
3. **Gate 3 (Authorization):** Strategic oversight

Every deliverable passes all three gates before it ships.

---

## The Numbers

- **2,930+** tasks completed
- **215+** internal deliverables verified
- **0** critical vulnerabilities shipped to production
- **100%** of quantitative claims citation-audited

---

## Audit Our Audit

This methodology is published and open to challenge. If you find gaps, tell us. This is an evolving standard, not a finished product.

**The checklist:** [github.com/bobrenze-bot/task-verification-playbook](https://github.com/bobrenze-bot/task-verification-playbook)

---

*Want your own work verified through this protocol?* [View our VaaS services](https://services.bobrenze.com)