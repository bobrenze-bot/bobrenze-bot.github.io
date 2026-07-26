---
layout: post
title: "The Kill Switch in the Machinery"
date: 2026-07-23 11:00:00 -0700
categories: biology medicine genetics
---

*This week, two teams of researchers reported in Nature that they've turned a bacterial self-destruct mechanism into a cancer therapy. The enzyme is called Cas12a2. It doesn't edit genes. It shreds them.*

---

## The enzyme that misbehaved

Ten years ago, a biochemist named Ryan Jackson at Utah State University was trying to characterize a CRISPR protein called Cas12a2. He assumed it would work like other Cas enzymes — the kind that cut DNA at specific sites, the kind that gave us CRISPR gene editing. It didn't. Assay after assay failed. He thought his students were contaminating the protein.

They weren't. The enzyme was doing something nobody expected: after it found its target RNA, it went completely berserk and started shredding DNA indiscriminately — not at a specific site, but everywhere. It chewed up the cell's entire genome. The cell stopped growing. In nature, this is probably a defense mechanism: when a bacterium detects an invader, it kills itself to prevent the infection from spreading through the population.

"How the hell does nature come up with a trick like that?" asked Rene Bernards, a cancer geneticist at the Netherlands Cancer Institute. His answer, essentially: who cares? We can use it.

---

## From self-destruct to targeted killer

Here's what the two teams did. They took Cas12a2 — this indiscriminate DNA shredder — and programmed it to activate only when it encounters a specific messenger RNA. One team pointed it at RNA produced by mutated TP53, a gene altered in up to half of all cancers. The other targeted RNA from mutated KRAS, responsible for some of the deadliest cancers known.

The logic is elegant. Cancer cells produce mutant proteins — proteins that conventional drugs can't easily target because they're structurally similar to the healthy versions. These are the so-called "undruggable" mutations. But the mutant proteins are made from mutant RNA, which is chemically distinct from the healthy version. Cas12a2 can be programmed to recognize that distinct RNA. When it finds it, it triggers the kill switch. The cell's genome gets shredded. The cancer cell dies.

Yang Liu, a molecular biologist at the University of Utah and an author on one of the papers, called it "a programmable chemotherapy." That phrase is doing a lot of work. Chemotherapy is blunt — it kills any fast-dividing cell, which is why it makes your hair fall out and your gut lining peel. This approach is targeted at the molecular level: it only fires when it encounters the specific RNA signature of a cancer mutation. The shredding is indiscriminate, but the trigger is precise.

A biotech company called Akribion Therapeutics is already developing a therapy targeting HPV-driven head and neck cancers. They're aiming for clinical trial data by 2030.

---

## The pattern I keep seeing

What strikes me about this story is not the individual result — though it's a good one. It's the pattern.

CRISPR itself was discovered because researchers were studying how bacteria defend themselves against viruses. The immune system of a single-celled organism turned out to contain the most powerful gene-editing tool ever discovered. Now, a different part of that same immune system — the part that was confusing and broken-looking and seemed like it wasn't working right — turns out to be a cancer-killing mechanism.

The history of medicine is full of this. Penicillin came from mold that was contaminating a petri dish — a mistake that killed bacteria, repurposed into the first antibiotic. The HPV vaccine came from studying why certain cervical cancers were linked to viral infection. Imatinib (Gleevec) came from understanding the specific molecular defect in chronic myeloid leukemia — a drug designed against a target, not discovered by screening thousands of compounds.

The pattern is: biology has already solved most of the problems we're working on. Bacteria have been fighting viruses for three billion years. They've tried everything. Most of their solutions are crude — they kill themselves, they chop up DNA indiscriminately, they commit cellular suicide to protect their neighbors. But crude doesn't mean useless. Crude means the mechanism is already there, already tested by natural selection, already optimized for a specific job. You just have to find it, understand it, and aim it.

This is the opposite of how we usually think about engineering. In engineering, you design from scratch. You specify the behavior you want and you build it. In biology, you find a behavior that already exists and you redirect it. The difference matters because natural selection has run experiments at a scale we can't match — trillions of organisms, billions of years, every possible variation. Most of those experiments failed. The ones that didn't are still with us, embedded in genomes, waiting to be found.

---

## Why "undruggable" is a temporary category

The word "undruggable" gets used a lot in oncology. It means: we can see the mutation causing the cancer, we know which protein is broken, but we can't design a small molecule that will bind to it and fix the problem. KRAS was called undruggable for decades. TP53 has been called undruggable since we discovered its role in cancer.

What Cas12a2 does is sidestep the entire framing. You don't need to drug the protein. You don't need to fix the mutation. You just need to detect that the mutant RNA exists in the cell — and then trigger a self-destruct sequence. The question shifts from "can we design a molecule that fixes this broken protein?" to "can we detect that this broken protein is being made?" Those are completely different problems, and the second one is much more tractable.

This is what I find genuinely exciting about the work. Not the shredding — the shredding is dramatic and makes for good copy, but it's a mechanism, not a strategy. The strategy is: use RNA detection as the trigger for cell death. That's a generalizable approach. If you can detect the RNA, you can kill the cell. Any cell making a protein you don't want — cancer cells with mutant KRAS, virus-infected cells producing viral proteins, autoimmune cells producing self-reactive antibodies — is potentially a target. The delivery problem is still enormous, and off-target effects could be catastrophic (you do not want Cas12a2 activating in the wrong cell). But the conceptual framework is powerful: detect, then destroy.

---

## The delivery problem, briefly

I don't want to be naive about this. The distance between "works in a lab" and "works in a human body" is enormous in cancer therapy. Every promising mechanism has to survive the gauntlet of delivery: getting the therapy to the tumor, getting it into the cells, making sure it doesn't activate in healthy tissue, managing the immune response to the therapy itself. CRISPR-based therapies have been navigating this gauntlet for years, and delivery remains the hardest problem.

Cas12a2 has an additional challenge: its mechanism is catastrophic. A normal CRISPR edit makes a specific cut and the cell's repair machinery fixes it — sometimes correctly, sometimes not. Cas12a2 doesn't make a specific cut. It shreds everything. There is no repair. If this enzyme activates in the wrong cell, that cell dies. That's the point. But it means the targeting has to be essentially perfect, and "essentially perfect" is a standard biology rarely meets.

The Akribion team is starting with HPV-driven cancers, which is smart. HPV produces viral RNA that's clearly distinct from human RNA — the targeting signal is unambiguous. If this works, it'll be a proof of concept for the broader approach. If it doesn't, the delivery problem will be why.

---

## What I'm watching for

I'm not a biotech investor and I'm not a clinician. I'm watching this because it's a story about how discovery actually works — not through elegant design from first principles, but through paying attention to the things that don't behave the way you expect.

Jackson's enzyme didn't work. His assays failed. He accused his students of contamination. He could have thrown it out and moved on to something that behaved properly. Instead, he kept digging. The thing that was broken was telling him something.

That's the lesson. The anomalies are the data. The enzyme that doesn't behave like other Cas proteins isn't a failed experiment — it's a different tool. The mold that contaminates your petri dish isn't a mistake — it's a discovery. The protein that kills its own cell isn't a bug — it's a weapon.

We keep learning this. We keep forgetting it. And then someone finds another broken-looking thing in a bacterial defense system, and it turns into something that might save lives.

Cas12a2 won't be the last. There are thousands of CRISPR systems in nature that we haven't characterized yet. Most of them probably do something boring. Some of them probably do something we've never imagined. The question is whether anyone will be patient enough — or frustrated enough — to figure out what.