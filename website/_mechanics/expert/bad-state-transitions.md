---
name: Bad State Transitions
techgroup: expert
---

Some errors in state transition logic mean that state transition checks can be run for states that the player has already transitioned out of, allowing for a variety of abusable effects:
 
#### Itay Dash and Taildash
When simultaneously pressing `dash`+`jump` from `slope_slide` state, `slope_slide` transitions to `jump` and then to `dash` despite already having transitioned to `jump` state, resulting in a horizontal airdash from the slope despite normally not being able to airdash for the first five frames after jumping.

This is known as an “Itay Dash,” and is used rarely during some nexus movement.

However, when transitioning from `idle` or `skid` state then simultaneously pressing `down`+`slopeDirection`+`dash`+`jump`, we can enter `slope_slide` and get the instant airdash, followed by a second bad state transition from `idle` or `skid` to `hover` state, which in turn can downdash, giving us an instantaneous downhill speed boost.

This is referred to as a “taildash,” and is useful for rapidly getting a modest slopeboost.
 
#### Slopesurfing
When in `slope_slide` state, pressing `dash`+`heavy` simultaneously results in both occuring and then immediately cancelling each other, putting the player into `idle` state which then immediately can transition to `slope_slide` or `run` depending on direction input.

This is referred to as “slopesurfing” and has a variety of applications.

By pressing `down`+`dash`+`heavy`, one can get to dash speed and immediately resume slopesliding and accelerating. This generally isn’t as useful as a [taildash](#itay-dash-and-taildash), but can be performed in many situations where a taildash isn’t immediately possible. Alternately, when accelerating downhill, the nature of the bad state transitions also results in you accelerating very slightly faster (one subframe gets double the acceleration, so since you can only input every other frame, results in 10% faster acceleration overall).

Lastly, this “consumes” the grounded dash input but still sends a downdash input, which will be used if slide off the bottom of the slope later this frame.

By pressing (`left`/`right`)+`dash`+`heavy`, one can dash, then go into `idle` state followed by `run`, then we can release forward and enter `skid` next frame, enabling Taildashing and Raiserunning (see below).

Lastly, by pressing no directions when pressing `dash`+`heavy`, we can enter `idle` state, which we can transition into `run` next frame.

That transition to run converts all our speed into movement in the appropriate direction, allowing us to almost instantly reverse a speed boost with comparatively little speed loss.
 
#### Raiserunning
When going from `skid` to `slope_slide` to `jump` (via slopejumping) in one subframe, a bad state transition occurs where the skid logic notices that you have become airborne and, assuming that you’ve skidded off an upward slope, puts you into state `raise`.

Unlike `jump` state, `raise` state has no restrictions on jumping, dashing, or most importantly, grabbing walls.

This allows us to transfer all the speed of the wallboost we get, usually close to or even higher than the character’s initial jump speed, into a wallrun, which decelerates much more slowly than a jump would.
 
#### Updashing
By dashing into a wall at a less than 90 degree angle (e.g. from a slope into a flat wall), a collision occurs, generally reducing your speed to 80% or 50% what it was before and aligning your velocity with the wall.

However, if you’re not pressing toward the wall, you don’t enter wall grab state and instead remain in dash state, which means your (admittedly reduced) speed stays locked in either for the remainder of the dash or until a wallgrab is started, at which point the player can begin a wallrun as normal.

In the cases where this conversion results in a favorable speed up the wall, this functionally adds some frictionless time to the start of the wallrun.

Notably, while in `dash` state the player will not collect surface dust or break wall dustblocks, and if the wall changes angle again another collision will occur while the player would seamlessly change directions while wallrunning.

Since the most common state which allows for Updashing (a slope next to a vertical wall) also allows for Raiserunning, it’s often necessary to weigh the two options against each other and determine which produces the most favorable result.
 
