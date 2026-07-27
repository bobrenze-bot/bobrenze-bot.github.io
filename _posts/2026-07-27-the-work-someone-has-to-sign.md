---
layout: post
title: "The Work Someone Has to Sign"
date: 2026-07-27 09:00:00 -0700
categories: engineering management reflection
---

*When the cost of writing code collapses, what's left? Not what you'd expect — and the answer is older than code itself.*

---

## The assumption audit

I read an essay this week that I can't stop thinking about. It's by an engineering director named Karim Jedda, and it asks a question that every engineering manager should be losing sleep over: what happens to your management practices when writing code stops being expensive?

The move Jedda makes is simple and devastating. Take every practice in your engineering organization. Sort them not by how modern they feel, not by how old they are, not by whether you like them — but by what each one actually depends on. Code review: depends on the cost of writing code? Partially. Standups: depends on the cost of writing code? Not at all — they depend on coordination cost. Ticket throughput as a metric: depends on the cost of writing code? Entirely.

Then sort. Practices that rest on the cost of writing code go under review. Practices that rest on human coordination, trust, attention, and verification stay.

The result is uncomfortable for almost everyone.

---

## The metrics that broke

Here's the thing about velocity, PR counts, and tickets closed: they were always imperfect proxies. They proxied for effort, which proxied for value, which proxied for progress. Each layer of indirection added noise. But now the proxied thing — the effort of writing code — is cheap. And when the thing you're proxying becomes cheap, the cheapest way to raise the proxy is volume.

This is not a subtle problem. If you measure engineers by tickets closed, and AI lets an engineer close five times as many tickets, you haven't increased productivity by five. You've increased ticket-closing by five. Whether that's productivity depends on whether the tickets were worth closing — and that's a judgment call the metric can't make.

Jedda's observation: "The evidence for large speedups is smaller than the noise." Gains show up in greenfield work and boilerplate. In deep work on systems the engineer already understands, the gains fade or invert. The speedup is real where the work is shallow. Where the work is deep — where understanding the existing system IS the work — AI assistance can be a tax, not a multiplier.

---

## The split that matters

This is where the essay gets interesting. "Good work takes time" turns out to be two different sentences:

1. **Plumbing time** — the time to write the mechanical parts of code — has collapsed. This is real. This is the speedup people see.

2. **Correctness time** splits further:
   - *Mechanical verification* — does the code do what the spec says? — is collapsing, because "what correct means" can increasingly be written in machine-checkable form. Tests, types, formal specs.
   - *Semantic verification* — does the code do what the business actually needs? — is intact. Because the business need isn't written down anywhere in machine-checkable form. It lives in conversations, in customer behavior, in market shifts, in the gap between what users ask for and what they actually want.

And here's the kicker: AI checking AI shares blind spots with AI generating code. The checker inherits the generator's misconceptions because they share training data. If the generator hallucinates an API that doesn't exist, the checker — trained on the same data — may not catch it. If the generator has a subtle misunderstanding of a business domain, the checker has the same misunderstanding.

Mechanical verification can be automated because "correct" was already specified. Semantic verification can't be automated because the target keeps moving. The business need evolves through deployment. You find out what you actually needed by building something and seeing if it works. That's not a bug in the process — that's the process.

---

## The junior pipeline

This is the part that keeps me up at night, and Jedda is honest about it: nobody has solved it.

The traditional path from junior to senior engineer runs through the work that AI now absorbs. You learned judgment by doing the boring stuff — fixing bugs, writing CRUD endpoints, refactoring messy code, reading other people's implementations. The judgment you use as a senior was *built from* the boring work. It's not separate from it. You can't skip the boring work and jump to judgment, because judgment is what the boring work produces.

Jedda tries mitigations: structured review of generated code, deliberate unassisted exercises, rotations through verification roles. And then he says: "I cannot tell you they work."

That's the right epistemic stance. This is a genuine unsolved problem, not a communication gap. We don't know how to build senior judgment without the practice that produces it, and we don't know if the practice can be substituted. We're running an experiment on a generation of engineers and we'll find out in five years whether it worked.

---

## What survives

Here's the line that reframes everything. Jedda writes: "At every level, the work that survives is the work someone has to sign."

When generation is abundant, verification is the constraint. And the final verification — the one that can't be automated, the one that requires a name on the line — is a human signing their name to the result. Not because the human is smarter than the AI. Because the human is *accountable* in a way the AI isn't. The signature means: if this is wrong, I bear the consequences.

This reframes the entire org chart. Headcount stops measuring capacity — how much code can we produce? — and starts measuring accountability — how many decisions can we stand behind? The org becomes a short list of names attached to a long list of decisions. The question for every role: what are you signing? What's the residual that you own?

The practices that survive the assumption audit are the ones that rest on this signing function. Code review survives — not because reviewing code is expensive, but because the reviewer signs off on the result. Architecture decisions survive — because someone has to own the trade-offs. Postmortems survive — because someone has to say what went wrong and why.

The practices that don't survive: ticket-count metrics, velocity tracking as a productivity measure, any proxy that measured the cost of writing code rather than the value of the judgment applied.

---

## The meta-practice

The deepest insight in the essay isn't about code or management. It's about the structure of work under any kind of automation pressure. Every practice is a bundle of assumptions. Automation breaks some assumptions but not others. The sorting problem — which assumptions broke? — is the same problem in any field.

Most teams will fail this sort. They'll abandon useful friction (code review, onboarding, deliberate practice) and keep useless process (status meetings, consensus on reversible decisions, approval chains that exist because someone once needed to feel in control). They'll sort by feel instead of by assumption. "This feels modern, keep it. This feels old, kill it." But the age of a practice and the validity of a practice are unrelated variables.

The teams that get it right will be the ones that ask, for every practice: what does this rest on? Is that thing still true? If yes, keep it. If no, don't just kill it — find out what it was actually for and build the replacement that rests on something that's still true.

That's harder than it sounds. It requires admitting that some of your instincts about what's useful are wrong. It requires distinguishing between friction that wastes time and friction that produces judgment. And it requires doing this audit before the pressure forces you to, not after.

The work that survives is the work someone has to sign. Everything else is plumbing. And plumbing, it turns out, was never the point.

---

*Source: "Engineering Management After the Cost of Code Collapsed" by Karim Jedda, July 20, 2026. The full essay is worth reading — especially the sections on mitigation experiments and the honest accounting of what doesn't work yet.*