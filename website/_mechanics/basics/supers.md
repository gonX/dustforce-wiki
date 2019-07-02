---
name: Supers
techgroup: basics
---

The super takes a variable amount of time depending on the number of enemies it hits.

Generally, the amount of time one enemy adds is fairly small, so you need to be cleaning several enemies per attack to make it worth using heavy attacks to reduce the number of enemies a super will hit.

However, there’s a base amount of time that a super takes, and this base amount is doubled if the super hits at least one enemy.

#### Empty super

In the case where a super is primarily being used to clean surface dust or dustblocks, the super will come out much faster if it’s not hitting any enemies.

#### Ranges

Enemy hitrange is a square

Dustblock hitrange is a circle

Dust-on-Surface hitrange is a circle requiring Line Of Sight (same circle as dustblocks?)

#### Other Properties

Grants Hitrise upon coming out of the Super

Applies time dilation during startup (expand on this more if we know more about it exactly)

Boosts can be preserved through a super, Including reversing the boost.

#### Attack Time

The attack time of a super depends whether you will be hitting enemies with it or not.

An empty Super has a attack time of `22f`.

A super which hits enemies has a base attack time of `36.3f` with each target adding an additional `7.7f`. Time is rounded **up** to the nearest subframe.
