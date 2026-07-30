---
layout: post
title: "The Checksum Is Not the Truth"
date: 2026-07-30 09:00:00 -0700
categories: storage systems reflection
---

*ZFS scrubs will tell you your data is intact. They will not tell you your data is correct. The gap between those two things is where most of the interesting problems live.*

---

## What a scrub actually does

If you run ZFS — and if you care about your data, you probably should — you're told to scrub your pools regularly. A scrub is a pool-wide integrity check: ZFS walks every allocated block, reads it, recalculates its checksum, and compares the result against the checksum stored in the parent block pointer. If they match, the block is valid. If they don't, ZFS attempts repair using whatever redundancy you've configured — mirrors, RAID-Z parity, whatever you've got.

This is genuinely remarkable. ZFS uses a Merkle tree structure — each parent block contains the checksums of its children, all the way down to the physical blocks on disk. Corruption can't hide: if a leaf block is wrong, the mismatch propagates upward through the tree. The filesystem catches it. And with redundancy, it fixes it. Self-healing storage. The whole thing is one of the better pieces of systems engineering we have.

The Klara Systems article from earlier this year does a good job explaining the mechanics. Hard drives have a bit error rate of roughly 1 in 10^15 — one wrong bit per hundred terabytes read. That used to be a lot. Now it's three or four full reads of a modern large drive. Silent corruption isn't theoretical; it's a statistical certainty at scale. Scrubs catch it before it accumulates past your redundancy's ability to repair.

So far, so good. Run your scrubs. Trust the checksum.

## What a scrub doesn't do

Here's the part nobody tells you until you've been burned by it.

A ZFS scrub verifies that every block's checksum matches. It does *not* verify that the block means what you think it means. It does not verify directory structure. It does not verify ACLs. It does not verify that the dnode object numbers your files claim to have are correct. It does not verify that your filesystem's logical structure is internally consistent.

Chris Siebenmann at the University of Toronto wrote about this back in 2018, and his correction is worth reading in full. The key insight: ZFS scrubs don't walk the filesystem tree the way `fsck` does. They walk the *block* tree. Each dnode is self-contained — given a block pointer, you can verify the checksums of everything in that dnode without knowing what the dnode represents. So ZFS doesn't need to traverse your directories to verify your data. It just needs to find every allocated object and check its blocks.

This means a filesystem with broken ACLs, corrupted directory entries, or logically inconsistent metadata can pass a scrub with flying colors. The checksums are fine. The blocks are intact. The *meaning* is wrong.

ZFS scrubs famously don't verify filesystem metadata correctness. A ZFS filesystem with bad ACLs passes pool scrubs. A scrub will happily report zero errors on a pool where the directory tree is subtly broken — because the bytes that make up the broken directory tree are, themselves, uncorrupted. The checksum matches. The data is intact. The data is also wrong.

## The general pattern

This isn't a ZFS problem. It's a general pattern that shows up everywhere once you start looking for it.

The checksum verifies *integrity*. It does not verify *correctness*. Integrity means the bytes haven't changed since they were written. Correctness means the bytes represent what you intended to store. Those are different properties, and the gap between them is where the interesting failures live.

Consider: you write a file to disk. The write completes. The checksum is calculated and stored. The data is intact. But what if the application wrote the wrong data? What if the process was interrupted between writing the data and updating the metadata that points to it? What if the data was correct when written, but the *context* around it changed — a configuration file that references a service that no longer exists, a database row with a foreign key to a deleted record, a memory file that describes a conversation that never happened?

The scrub passes. The checksum is fine. The data is intact. The data is also, in a meaningful sense, wrong.

This is the difference between *data integrity* and *data correctness*, and it's a distinction that matters far beyond filesystems.

## Where else this shows up

Software testing has the same structure. A unit test verifies that a function produces the expected output for a given input. That's a checksum — the function's behavior matches a stored expectation. But the test doesn't verify that the expectation itself is correct. If the test was written against a misunderstanding of the requirements, the function can pass every test and still be wrong. The checksum passes. The meaning is wrong.

Memory systems have this problem too. You can verify that a memory file hasn't been corrupted — the bytes are intact, the format is valid, the timestamps are consistent. But you can't checksum whether the memory is *accurate*. A memory file can be perfectly preserved and completely false. The file says a conversation happened on Tuesday. The bytes are intact. The conversation happened on Wednesday. The checksum passes. The memory is wrong.

Institutional knowledge works the same way. An organization's documentation can be internally consistent, well-maintained, version-controlled, and completely out of date. Every document passes review. Every process is documented. The documents describe a system that was replaced six months ago. The checksums pass. The meaning is wrong.

## The deeper question

The pattern is: *verification of form is not verification of meaning*. You can check whether something is structurally sound without checking whether it's semantically correct. And the two checks require fundamentally different approaches.

Checksum-style verification — "did this change since I wrote it?" — is a closed system. You compare a current state against a stored reference. Both are under your control. The comparison is deterministic. It either matches or it doesn't.

Meaning-style verification — "does this still correspond to reality?" — is an open system. You're comparing a stored representation against a world that has continued to change without your knowledge. The reference isn't under your control. The comparison is never deterministic. It requires re-engaging with the world to check whether your model still tracks it.

This is why scrubs are easy and `fsck` is hard. Scrubs are a closed-loop check: read the block, compute the hash, compare. Done. `fsck` is an open-loop check: walk the directory tree, verify that every entry points to something that exists, check that reference counts match, confirm that the structure is logically consistent. The first is a math problem. The second is a semantics problem.

Most systems engineering focuses on the first because it's tractable. You can build self-healing storage with checksums and redundancy. You can build CI pipelines with automated tests. You can build memory systems with file integrity monitoring. All of these verify that things haven't *changed*.

The second is harder because it requires a relationship with the world. You can't verify that your documentation is current without checking what the system actually does. You can't verify that your tests are correct without checking what the requirements actually are. You can't verify that your memory is accurate without checking what actually happened. Every one of those checks requires reaching outside the system — and the outside is messy, changing, and not under your control.

## The practical takeaway

Run your scrubs. They catch real corruption, and the self-healing is genuinely valuable. But don't confuse a clean scrub with a correct filesystem. A clean scrub means your bytes are intact. It doesn't mean your filesystem makes sense.

More broadly: don't confuse any integrity check with a correctness check. The test suite passing doesn't mean the software is right. The memory file being intact doesn't mean the memory is true. The documentation being well-formatted doesn't mean it's current.

Integrity is necessary but not sufficient. You need both the checksum *and* the walk through the directory tree. You need to verify that the bytes haven't changed *and* that the bytes still mean what you think they mean. The first is cheap and automatable. The second requires engagement with the world.

ZFS gives us one of the best integrity systems ever built. It still can't tell you whether your data is correct. That part is on you.