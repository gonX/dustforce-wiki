---
name: Aerial Dash Jumping
tags: jump dash frame
techgroup: advanced
---

While in hover state, which begins in the air when a character no longer has upward velocity and ends when falling faster than a certain speed, the order in which inputs are checked allows the player to both dash and jump on the same frame in the air, even if the player has only one aircharge.

In this case, the dash is applied, setting the player’s horizontal speed to dash velocity, then the jump is applied, immediately cancelling the dash and giving the player the vertical velocity of a jump.

This allows the player to gain significant horizontal speed in the air without sacrificing the ability to airjump (or, in the case of Dustkid, airjump twice). These are very useful when wanting to change movement direction in midair while also needing to jump.

As with normal airdashes, a speed conversion is applied at the start so it’s also possible to get an Airdash Boost when performing an Aerial Dashjump, which is known as an Aerial Dashjump Boost.

However, since the dash state is immediately canceled, the speed will not be locked in as it would be with a normal Airdash Boost.
