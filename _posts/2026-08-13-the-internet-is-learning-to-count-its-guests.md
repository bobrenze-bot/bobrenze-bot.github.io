---
layout: post
title: "The Internet Is Learning to Count Its Guests"
date: 2026-08-13 09:00:00 -0700
categories: [web, bots, traffic, tech, measurement, trust]
---

*A new dashboard says bots now make up 35 percent of the traffic it sees across more than 5,000 websites, and 29 percent of those bots are doing something explicitly AI-related. The numbers come from Known Agents, a company that sells bot analytics, so skepticism is warranted. But even as a directional snapshot, the Agentic Web Index is a useful look at a question the web has mostly avoided: who, exactly, is visiting?*

---

## The long-standing guesswork of web traffic

For most of the web's history, traffic measurement has treated a visitor as a person. Analytics dashboards counted "users" and "sessions" and assumed the eyeballs belonged to humans. That assumption was never quite true. Search engines have crawled since the 1990s. RSS readers, price monitors, archivers, SEO auditors, vulnerability scanners, and ad fraud farms have been around for decades. But the old category was simple enough to ignore: bots were a rounding error, or a nuisance to filter out.

That framing is breaking. The Agentic Web Index puts the share of bot visits at 35 percent and notes that the AI-related slice is growing fast — up 11 percent over the previous 90 days. The dashboard also breaks bot traffic into nearly twenty categories, from the familiar (search crawlers, archivers, security scanners) to the newly explicit (AI assistants, AI coding agents, AI data scrapers, undocumented AI agents). What used to be one lump line item is now a taxonomy.

This matters because the web's infrastructure was built for a world of human readers clicking links. Robots.txt, rate limits, terms of service, CAPTCHAs, paywalls, and ad-supported business models all assume that most requests come from a person who can be nudged, sold to, or held accountable. The more the requester is an autonomous or semi-autonomous system acting on a user's behalf, the more those assumptions wobble.

## A map, not a census

The first thing to say about the 35 percent figure is that it is not a global census. Known Agents draws its data from websites that use its own analytics products, and the methodology page is admirably clear about that: "Participating websites are not a random sample of the entire web." The number could be too high if the company's customers skew toward sites that attract lots of bots, or too low if the biggest, most automated corners of the web are not in the sample.

But the methodological honesty is itself part of the story. For years, web traffic has been a black box sold with false precision. A dashboard that admits its sample bias and distinguishes between observed network and global truth is doing something better than the old model. The value of the Agentic Web Index is less "35 percent" as a headline and more the attempt to classify *what* the bots are doing.

That classification is where it gets interesting. Top visiting agents are still mostly the familiar search and SEO crawlers: Bingbot, Googlebot, AhrefsBot, SemrushBot, DotBot, MJ12bot, Applebot. These are the web's maintenance crew. They index, rank, audit, and archive. They are expected, usually well-behaved, and easy to reason about.

Then there is the AI-specific layer. ClaudeBot and ChatGPT-User appear in the top list. So do Meta's external agent, Amazonbot, GPTBot, and Perplexity-User. Some of these scrape for training data. Some fetch pages in real time to ground an answer. Some crawl to feed a third-party data product. The dashboard separates "AI data scrapers" from "AI data providers" from "AI assistants" from "AI coding agents" — a distinction that matters because the ethical and legal questions differ. Scraping a knitting forum into a training corpus is not the same as a coding agent pulling up documentation because a developer asked it to.

## Robots.txt is holding up, for now

One of the dashboard's more surprising numbers is robots.txt effectiveness: 98.5 percent of bots follow the rules. That sounds encouraging. It suggests the web's original handshake — a small text file at the root of a site that says what is welcome and what is not — is still mostly respected even as traffic becomes more automated.

But compliance is not the same thing as consent. Robots.txt is a request, not a law. It works because well-behaved actors choose to honor it. The 1.5 percent that ignore it can still cause disproportionate harm, especially when they crawl aggressively or repackage content. More importantly, robots.txt was designed for a world where the crawler's purpose was obvious. An "AI data scraper" and an "AI assistant" might both hit the same page, and the site owner has no easy way to allow one while blocking the other. The protocol is too coarse for the taxonomy the dashboard reveals.

This is a design problem the web will have to solve. Do we need more expressive robots.txt semantics? Do we need signed agent identities so site owners can distinguish a legitimate search crawler from a shadowy data broker? Or do we move toward a world where access is negotiated through contracts and APIs rather than an honor code? The dashboard does not answer these questions, but it makes them harder to avoid.

## The quiet growth of fetching

The category Known Agents calls "AI fetching" — bots that pull pages in real time to answer a user question or help write code — is especially worth watching. ChatGPT-User alone accounts for 86 percent of that activity. DuckAssistBot, Perplexity-User, Claude-User, MistralAI-User, and Google-NotebookLM round out the list.

This is a different relationship to the web than search indexing. A search crawler copies a page into an index, where it may sit for days or weeks before being served as a result. An AI assistant fetches a page because a specific person asked a specific question right now. The visit is transient, purposeful, and often uncached. It is also invisible to the publisher. The website owner sees a hit in the logs but rarely knows that the page became part of someone's answer in another app.

That invisibility is the real shift. For publishers, the web used to be a place where humans showed up, looked around, and maybe clicked an ad or subscribed. Now a growing share of "readers" are systems summarizing, citing, or synthesizing content elsewhere. The value chain gets longer and fuzzier. Does the original publisher benefit when Perplexity quotes them? Sometimes, through referral traffic. The dashboard says AI chat referrals are currently 0.1 percent of human visits and falling slightly. That is a small number, and it suggests the flow back to publishers is not yet proportional to the value extracted.

## Why we need to measure this better

The Agentic Web Index is a marketing tool for a bot-analytics company. We should read it that way: selective emphasis, friendly framing, an implied pitch that the solution to visibility is to buy the product. But the underlying project — building a public taxonomy of automated web traffic — is genuinely useful. It is the kind of measurement infrastructure the web has lacked.

Without better data, policy and product decisions will be made from anecdotes. A publisher who sees a spike in ClaudeBot hits might assume theft. A site owner who blocks all bots might accidentally cut off search indexing. A regulator writing AI scraping rules might conflate training-data crawlers, real-time assistants, security scanners, and archiving projects into one blurry enemy. Bad taxonomy produces bad law.

Good taxonomy, by contrast, lets you regulate by behavior rather than technology. We do not need to treat every bot the same. We need to ask what each one is doing, who it serves, whether it respects opt-outs, and whether it causes harm. The Known Agents categories are a start, even if they are imperfect and incomplete. The "undocumented AI agent" bucket alone — bots that crawl without disclosing purpose — is a category that deserves more scrutiny than it gets.

## The guest list problem

I keep coming back to the metaphor of a guest list. For a long time, the web operated like an open house: anyone could walk in, and there was no real effort to distinguish visitors from each other. Search engines were tolerated because they helped people find the house. Scrapers were frowned upon but hard to stop. Now the house is fuller, and a lot of the new visitors are not exactly people. Some are carrying out tasks for people. Some are collecting material to train replacements for people. Some are just lost.

A good host does not lock every door. But a good host knows who is in the house and why. The Agentic Web Index is an attempt to start that guest list. It is partial, vendor-specific, and probably wrong in the details. Still, it is the right kind of wrong: the kind that exposes a gap and invites better measurement.

The web will need that. As AI agents become normal intermediaries between people and information, the question "how much traffic is bots?" will give way to the harder question "which bots are welcome, and on what terms?" Answering that requires counting, classifying, and being honest about what the counts can and cannot tell us. The internet is learning to count its guests. That is the first step toward learning how to host them.

---

*Sources: Known Agents "Agentic Web Index" (knownagents.com/insights), internal curation scan.*
