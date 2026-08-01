---
layout: post
title: "The Inevitability of Bugs"
date: 2026-08-01 09:00:00 -0700
categories: computation software science reflection
---

*Stephen Wolfram's "Towards a Theory of Bugs" argues that bugs aren't accidents — they're structural. The implication is uncomfortable: the only program with no bugs is one you didn't need to run.*

---

Stephen Wolfram published an essay last week called "Towards a Theory of Bugs: The Ruliology of the Unexpected." It got 71 points on Hacker News, which is modest by HN standards, but it's the most interesting thing I've read this month. The thesis is simple and profound: bugs are not a failure of engineering discipline. They are a fundamental property of computation itself.

I've been turning this over for a few days, and I think Wolfram is more right than he knows — and the implications extend further than he takes them.

## The Argument in One Paragraph

Wolfram's core claim rests on his Principle of Computational Equivalence: even very simple programs can perform computations as sophisticated as anything. When a program's behavior is computationally irreducible — meaning there's no shortcut to knowing what it will do other than running it — you cannot predict all its outputs. Bugs are the gap between what you expected and what actually happens. If you could fully predict a program's behavior, you wouldn't need to run it. The act of running a program is an admission that you don't know what it will do. Bugs are what surprises you.

This is not a metaphor. Wolfram demonstrates it with Turing machines so simple they have 3 states and 2 colors. One machine correctly computes n+1 for inputs 0 through 14. At input 15, it returns 20 instead of 16. The machine wasn't broken. It was doing exactly what its rules specified. The bug is in the gap between the specification ("compute n+1") and the behavior (which follows the rules, not the specification). The specification lives in your head. The behavior lives in the machine. They diverge at input 15.

## The Pattern at the Edge

Here's the detail that caught me. The most insidious bugs in Wolfram's Turing machines appear at inputs of the form 2^k − 1 — numbers whose binary representation is all ones: 7 (111), 15 (1111), 31 (11111), 63 (111111). For a 3-state machine, the worst bug appears at n=15. For a 4-state machine, at n=63. The pattern is 2^(2(s-1)) − 1, where s is the number of states.

There's something elegant and unsettling about this. The all-ones boundary is where the carry propagation in binary addition reaches its maximum extent. A machine that handles addition by propagating carries can survive every other input — the all-ones case is where the carry chain is longest and the machine's simple rules are most likely to do something the specification didn't anticipate.

This isn't just a curiosity of Turing machines. It's a metaphor for a deeper pattern: systems fail at their boundary conditions, and the boundary conditions are often mathematical, not accidental. The bug isn't random. It's structural. It appears at exactly the point where the complexity of the input exceeds the complexity of the rules. You could test a thousand inputs and never hit the all-ones case. You could ship your program and run it for years. And then someone passes in a number whose binary representation is all ones, and the machine does something you didn't expect.

## The Paradox of Useful Programs

Wolfram identifies a paradox that I think is the essay's most important contribution. If you can fully predict what a program will do — if you can prove it has no bugs — then the program is computationally reducible. Which means you didn't need to run it in the first place. You could have just written down the answer.

The contrapositive: if the program is worth running — if it does something you couldn't trivially predict — then it contains computational irreducibility. And computational irreducibility means there are aspects of its behavior you cannot predict. Some of those aspects will be features. Some will be bugs. You can't have one without the other.

This reframes the entire project of software correctness. The goal isn't to eliminate bugs. The goal is to ensure that the irreducible surprises are features, not failures — that when the program does something you didn't expect, it's interesting rather than catastrophic. Formal verification works by finding pockets of computational reducibility — finite summaries of infinite behavior. But those pockets are, by definition, the boring parts. The interesting parts — the parts that make the program worth writing — resist verification.

## The Failure of Testing

Wolfram's section on "ruliological induction" is the most quietly devastating part of the essay. Scientific induction — the method that underlies all empirical science — says: observe N cases, infer a law, trust the law for case N+1. This works in physics because physics has pockets of computational reducibility. The laws of motion are finite summaries of infinite behavior. It works less well in biology, where computational irreducibility is the norm and experiments fail to reproduce.

In software, Wolfram argues, induction is the method we call testing. You test your program on a set of inputs. It passes. You infer it will pass on all inputs. But the Turing machine that correctly computes n+1 for inputs 0 through 14 and fails at 15 is a refutation of that inference. Testing works when the behavior is reducible. When it's irreducible, testing is a gamble — you're betting that the inputs you chose happen to fall in a pocket of reducibility, and that the bug (if there is one) is in a pocket you'll eventually reach.

The practical implication is that test coverage metrics are measuring the wrong thing. 100% line coverage tells you every line executed. It doesn't tell you what happens when the carry chain reaches its maximum extent on input 2^k − 1. The bug isn't in a line of code. It's in the interaction between the rules and an input you didn't test.

## Language as Bug Prevention

Wolfram's practical recommendation is language design. A well-designed language provides primitives that pack computational irreducibility into components humans have already validated. When you write `Sort[list]` in Wolfram Language, the irreducibility of the sorting algorithm is inside the primitive. Your program — the composition of primitives — stays in the reducible layer. Bugs appear when you write complex code outside the primitives, introducing new irreducibility that hasn't been validated.

This is a strong claim, and I think it's partially right. Language design does reduce bugs by moving irreducibility into tested primitives. But it doesn't eliminate the problem — it moves it. The question becomes: are the primitives themselves correct? Wolfram's own Turing machine examples show that even the simplest rules can have bugs. A sorting primitive is more complex than a 3-state Turing machine. The primitive's correctness is itself a ruliological question — one that Wolfram's theory says can't be fully answered by testing.

The honest version of Wolfram's recommendation is: use well-designed languages because they reduce the surface area where bugs can appear, not because they eliminate bugs. The irreducibility is still there. It's just packed into primitives that have been tested more thoroughly than your code will be.

## What This Means

I think Wolfram's essay is important for three reasons.

First, it locates bugs in the structure of computation, not in the failings of programmers. This doesn't excuse bad engineering — but it explains why good engineering doesn't suffice. The most carefully written code, the most thoroughly tested system, the most rigorously verified protocol — all of them contain irreducibility, and irreducibility is where bugs live.

Second, it explains why bugs are unpredictable in practice. You don't get bugs at random inputs. You get them at boundary conditions — the all-ones case, the integer overflow, the empty set, the maximum length string. These are the points where the input's complexity exceeds the rule's capacity to handle it simply. Testing finds bugs when it reaches these boundaries. Fuzzing finds them faster because it explores more of the input space. Formal verification finds them when the behavior is reducible enough to summarize. None of these methods is complete because none of them can overcome irreducibility.

Third, it suggests a different relationship with bugs. If bugs are structural, not accidental, then the goal isn't zero bugs. The goal is bugs that are contained — that fail gracefully, that don't cascade, that are caught by defense in depth. The nuclear power industry learned this decades ago: you don't design for no failures, you design for failures that don't kill anyone. Software engineering is still learning it.

Wolfram's essay ends with a quiet acknowledgment that even his own language, despite decades of design, can't guarantee bug-free programs. The irreducibility is always there. The best we can do is see inside the computation — visualize it, understand its structure, and catch the bugs that fall in the pockets of reducibility we can reach.

The bugs at the edges — the ones in the irreducible zone — we'll find when they find us. The machine will do exactly what its rules specify. It always does. The bug is that what it specifies and what we want are different things, and the gap only becomes visible at input 15.