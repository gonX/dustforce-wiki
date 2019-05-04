---
name: Basic Game Mechanics
tags: beginner tutorial
techgroup: basics
---

{::options auto_ids="false" /}

The basics of the game are that you have 4 directional keys for movement, a Dash, Jump, and a Light attack, and Heavy attack button.

Dust on surfaces act as collectibles that we must route to gather along our way.

Characters can jump or dash once in midair, downdash to rapidly begin falling, run up walls briefly, climb over ledges, jump and dash off of walls, slide or run along ceilings and slide on slopes.

After collecting 100 dust, your character has charged up a “special attack” (aka super) which cleans dust on surfaces within line of sight, dustblocks and enemies around you in a limited range. (see [Super](#super))

Routing where to use Super(s) is one of the primary considerations we had to make when optimizing a level.

{:.no_toc}
#### Attacks

Your attacks are multi purpose, both serving as combat tools for enemies, as extra reach for cleaning dust on surfaces, and as a mobility tool.
Hitting an enemy or Dustblock in midair cancels your fall, and fully cleaning an enemy restores your aircharges allowing you to air-jump or air-dash again.

There are two types of attacks, with heavy attacks dealing 3 times as much damage and hitting a larger area, but their startup time is much longer and they can’t be chained as easily into followup attacks.

Additionally, enemies cleaned by a heavy attack as the final blow will spread dust on nearby surfaces based on the attack direction.

Your attacks can differ when performed in the air or on the ground, and different versions of the attack will be performed depending on your directional keys.

Each attack applies some time dilation and when hitting enemies causes hitstop, thus to maximize time, it is almost always better to hit as many enemies in as few attacks as possible, including using the knockback of an attack to push an enemy towards another enemy to hit them both.

The 4 characters do have mechanical differences, and they greatly affect our choice for which is used at which points in the TAS. Their attack hitbox differences are shown to exact scale in [this album](http://imgur.com/a/jtzG0) (This album is for attacks on enemies only. Attacks on dustblocks and to clean dust on surfaces have some variable range based on the quadrant you are located in etc. The general sizes and shapes are still roughly what is shown in the album)

insert link to #hitboxes here

