---
name: Jumps
tags: frame jump tech ledgejump shorthop fulljump frames
techgroup: basics
---

#### Ground Jump

When not in slopeslide state, a ground jump has 7.5 frames (rounding up to 7 frames and 3 subframes, like with dashes) of startup.

This startup will end immediately if the player would become airborne, leading to a “ledgejump.”

If the player is still holding jump when jump startup completes, the player gets a “fulljump,” if not then a “shorthop” will occur.

A shorthop normally gets slightly less initial upward velocity, and experiences significantly more gravity during the rising part of the jump.

At the start of the jump, your upward velocity is increased to your character’s jump velocity if it is less. However, if you already have more upward velocity (almost always because of a significant speed boost which you have transfered to an upward ramp), then you will instead keep your current Y velocity, even in the case of a shorthop.

When jumping from the ground, your total speed is converted to X velocity in the direction of the jump, then capped based on your new Y velocity.

This means that when travelling up or down slopes, you may gain some X speed because you no longer have the angle of the ground working against you, and when turning around as you jump you can most of your speed in the opposite direction.

However, friction during jump crouch will significantly reduce your speed, and the speed cap usually limits horizontal velocity to not much above dash speed (exactly how fast depends on your character’s initial jump velocity), even if you were previously going much faster.

In the case of a “ledgejump,” however, the jump doesn’t consume an aircharge, but uses the airjump rules for X velocity. (See below.)

You must wait 5 frames after a jump before you can jump or dash, and must wait 10 frames before you can enter a Wall Grab state.

#### Air Jump

A jump perform in midair has no jumpsquat or startup delay, and thus occurs instantly.

As such, jumps in midair cannot be a shorthop and will always give the same height as a “fulljump.

At the start of an air jump, your Y velocity is set (or left alone) using the same rules as with ground jumps, above. However, your X velocity is set according to what direction you’re pressing:

- If pressing neither left nor right and your X velocity is between positive and negative 300, it’s immediately set to 0. Otherwise, it’s left at its current value.
- If pressing a direction, then your X velocity is set to a minimum of 300 in that direction if it’s less (or in the opposite direction)
-- If it’s already 300 or greater in the appropriate direction, then it’s left at its current value.

{:.no_toc}
### Aerial Dash Jumping (Air Dashjump)

See [Aerial Dash Jumping](#aerial-dash-jumping)
