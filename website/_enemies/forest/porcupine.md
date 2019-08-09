---
name: Porcupine
enemygroup: forest
can_hurt: yes
can_hurt_unprovoked: true
spawns_children: true
spawns_children_child_id: quill
can_path: true
can_path_grounded: true
can_path_flying: false
pacified_when_flying: true
hp: 1
game_name: enemy_porcupine
---

Attacks by spawning three quills, directed forward and diagonally forward from the surface it is on.

Behaves strangely when not on a surface. If placed in the air, it will remain static and unable to attack. If it is removed from a surface while moving, bugs may occur as seen in [4 Lexie](http://atlas.dustforce.com/3815/4-lexie)