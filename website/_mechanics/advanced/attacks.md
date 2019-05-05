---
name: Attacks
techgroup: advanced
tags: frames
---

Attacks have 3 phases, startup (aka windup), hit, and recovery.

Light and Heavy attacks have three possible angles: Up, Down, or Neutral.

At the beginning of attack startup, the attack’s direction, either in terms of left/right or up/down, can be changed via directional inputs.

The period where these changes can occur lasts 2 frames for light attacks, 4 frames for vertical direction changes to heavy attacks, and 8 frames for horizontal direction changes to heavy attacks.

Once the player has attacked “behind” them, their attack facing cannot be changed again, even in followup attacks, until they’ve completely recovered from attacking.

In order to attack “forward,” they must either wait to completely finish attack recovery, or cancel recovery with an action other than attack (such as grabbing a wall or jumping).

(TODO: merge with [basics](#basic-game-mechanics)?)

#### Time Dilation

During attack startup, the character’s time rate is adjusted such that they move and accelerate less during each subframe, as though time was moving slower for them.

This is referred to as “Time Dilation.”

Only 70% as much time passes for the player during light attack windup, and 2/3rds as much time passes during heavy attack windup (except for Kid, whose heavy attacks still dilate time at the 70% rate).

During this time, shifts in subframe boundaries and the granular nature of movement/acceleration calculations can produce a slightly different end result in movement that should theoretically just be the same movement but iterated through more slowly.

Taking advantage of these calculation differences to produce a more favorable result is referred to as “Time Manipulation,” but this is done fairly rarely since the Time Dilation itself will always have a time cost.

Notably, attack startup on the ground forces the character into idle state, which has stronger friction than even holding opposite to your current movement direction, and thus allows you to slow down more quickly.

Idle state also allows the character to open doors while still moving.

One exception is on a ground slope, where holding down will keep the character in slopeslide state rather than idle state, which is preferable when high friction is not a desired effect of the attack.

At the end of startup, the attack makes a single check to see what the attack hits, with no lingering hitbox.

When an attack connects with enemies, if the character is in midair, their upward velocity will be increased to a certain minimum if it is less.

This slight upward nudge is referred to as [Hitrise](#hitrise)

When the player hits dustblocks in midair, they don’t get an upward nudge but their vertical velocity will be set to 0 if they were travelling downward.

#### Hitstop

When an attack hits an enemy or dustblocks, the character (and the targets in the case of enemies) will be “frozen in time” for a period of time based on the attack and what was being hit.

This is referred to as “hitstop,” and it lasts 1 frame for hits on dustblocks, and 2.5 or 7.5 frames (0.5 rounding up to 3 subframes as with dashes) respectively for light and heavy attacks on enemies.

This hitstop begins one frame after the character detects that the attack has finished, so there’s usually one frame when the player can input actions that cannot be performed during attack startup (e.g. ground dashes) but before hitstop occurs.

Hitstop will still apply afterward as normal, but in particular it is often highly favorable to dash immediately upon an attack connecting to minimize time spent outside of dash state, and sometimes to convert the hitrise to forward speed via an [Airdash Boost](#aerial-dash-boosting).

This concept is demonstrated in the top replays of the Atlas map [taskid by fishmcmuffins](http://dustkid.com/level/taskid-7195)

#### Iteration Order of Attacks

Though the attack will hit enemies after a consistent amount of time, the character will react to the hit having completed (and clean surface dust) dependent on the Iteration Order of the attack hitbox in comparison to your character.

This can sometimes be manipulated favorably via Iteration Boundaries.

While it's unlikely, iteration order can occasionally cause dust that would otherwise be cleaned by an attack to be iterated after the level completion (e.g. hitting the enemy), resulting in A completion where S completion would have been expected. This is demonstrated in [this replay by gonX](http://dustkid.com/replay/-10885349) of the Atlas map [Big Metal Shaft by Kuitar](http://dustkid.com/level/Big-Metal-Shaft-8379)

#### Attack Recovery

Attack Recovery can be cancelled via jumps, dashes or [grabbing a wall](#wall-grab). This is Known as Heavy Cancelling, or Light Cancelling.

Cancelling recovery used on nearly every single attack in the entire TAS.

Light or Heavy attacks can be completely canceled during startup with a walldash or super attack input, and downward-angled aerial Light attacks are cancelled by landing on the ground.

Cancelling attack startup with a super input can be useful for time manipulation and positioning, and cancelling light startup by landing can be helpful to buffer certain ground actions from the air, though a light attack canceled in this way always results in at least one subframe of “land” state which has fairly unfavorable friction properties.
