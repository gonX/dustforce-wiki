---
name: Treasure
enemygroup: mansion
can_hurt: true
can_hurt_unprovoked: true
spawns_children_parent_id: chest-treasure
can_path: false
hp: 1
game_name: enemy_treasure
sprite_image_name: idle1
---

Behaves like [Scrolls](#scrolls). Will stay idle at its spawn position until an enemy enters its radius, at which point it will fly in a straight line to the position the enemy was seen until it hits the enemy or a surface.

Can be prevented from firing or frozen mid-flight using a Super Cancel.
