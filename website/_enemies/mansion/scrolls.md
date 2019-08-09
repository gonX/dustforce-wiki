---
name: Scrolls
enemygroup: mansion
can_hurt: true
can_hurt_unprovoked: true
spawns_children_parent_id: chest-scrolls
can_path: false
hp: 1
game_name: enemy_scrolls
sprite_folder_name: scroll
---

Behaves like [Treasure](#treasure). Will stay idle at its spawn position until an enemy enters its radius, at which point it will fly in a straight line to the position the enemy was seen until it hits the enemy or a surface.

Can be prevented from firing or frozen mid-flight using a Super Cancel.
