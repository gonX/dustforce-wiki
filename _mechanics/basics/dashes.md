---
name: Dashes
tags: tech frames dash adb
techgroup: basics
---

When you dash, first your speed is converted to horizontal (possibly with some loss) if in midair, then if your speed is below your character’s dash speed it is increased to that value.

After these conversions occur, your velocity is locked in (barring collisions with surfaces) for the duration of the dash (12.5 frames, which due to subframe counts rounds up to 12 frames and 3 subframes under normal circumstances).

#### Dash Rhythm

When your character has a boost, dashing to lock the speed value is very important. Dash inputs will buffer for the remainder of the frame on which the input is sent.

Due to the input buffering, this allows a new dash to begin directly after the previous dash ends, even when that occurs on a subframe that normally does not accept inputs.

This is what we call “perfect dash rhythm” and results in a repeating sequence of 5 dashes.

This rhythm normally follows a 12-13-12-13-13 pattern due to the three subframes of spillover each dash.

If your dash input is processed on the first subframe, your dash will always begin at the beginning of the sequence.

If your dash input is buffered, you can start anywhere in the sequence, based on what subframe the dash started.

When you have an available air charge to use, buffering a ground dash is normally only possible if you would land within one subframe, as otherwise an airdash to occur.

If it’s not possible to buffer a dash or precisely time your landing, you may undergo up to 4 subframes of landing state friction before you can dash, significantly reducing your speed, though this can sometimes be reduced to 1 subframe through use of a land-canceled downlight. This means buffered or timed dashes are usually much preferred for keeping maximum speed.

#### Aerial Dash Boosting

When dashing in midair, if your speed vector angle before the dash is within 18 degrees of horizontal, in either direction, 100% of your total speed is transferred into the dash, giving you a horizontal speed boost.

This is known as Aerial Dash Boosting. When outside of this 18 degree range, you still keep a portion of your speed `(1-[change in angle]/90°)` so it’s still possible to airdash faster than normal dash speed when travelling at a sharp angle, but a significant amount of speed will be lost.
