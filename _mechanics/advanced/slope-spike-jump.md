---
name: Slope and Spike jumps
techgroup: advanced
---

As vaguely mentioned in [Ground Jump](#ground-jump), a jump from slopeslide state has no startup. As such it can never be a shorthop.

It is also a grounded jump, so X speed conversion happens as with other ground jumps.

##### Spike Jumps

Notably, it’s possible to transition from hover or fall state, to land state, to slopeslide state, and then jump all within a single subframe.

This means that in the case of a spiked slope, it’s possible to actually land on the spikes and jump back off before the game checks if the spikes should kill you. This is known as a “spikejump.”

Spikejumps normally require buffering the jump input and thus requires that you have used your aircharge, but with precise positioning it’s possible to spikejump even when you still have an aircharge by aligning yourself to land on the first subframe.

Similarly, dustblock slopes can be jumped off of before the game checks that you should collect them.

However, you will always collect the surface dust from a solid slope even if you jump off it immediately.
