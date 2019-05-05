---
name: Character States
tags: tech frames
techgroup: expert
---

Your movement abilities generally correspond to a state that you will be put into that lasts for some duration.

These states, and the transitions between states are what makes up a large portion of the movement techniques seen within the TAS.

Dustforce accepts inputs at 60 fps. However, for the player physics, steps are done at a rate of 5 per frame, we count each of these physics steps as 1 “subframe”.

States may not last a “clean” whole frame number, and instead might end on a subframe instead.

Inputs are only registered on a full-frame basis, but manipulating our inputs so that a specific event occurs at a specific subframe is still often possible.

