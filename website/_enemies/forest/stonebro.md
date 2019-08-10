---
name: Stonebro
enemygroup: forest
can_hurt: true
can_hurt_unprovoked: true
can_path: true
can_path_grounded: true
can_path_flying: false
pacified_when_flying: false
massive: false
hp: 3
game_name: enemy_stonebro
---

Has an active hitbox as long as it is moving at a speed of 400 units per second or higher.

When grounded, it will accelerate up to its max speed at 16.666 u/s/s, unless it is perfectly motionless, then it will accelerate at 26.666 u/s/s for a single frame. Its ground speed is capped at 400 u/s.

When airborne, it will accelerate due to gravity at 16.666 u/s/s.

When colliding with a wall, it will perform an elastic collision, reflecting its speed vector according to the angle of the wall.

Can be lured outside of its path, but will return once aggro is lost.

Commonly referred to as a Small Totem.