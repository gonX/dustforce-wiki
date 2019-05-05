---
name: Facegrinding / Toegrinding
techgroup: expert
---

During the first 10 frames of jump state or during an attack, the player cannot grab walls.

If the player is adjacent to a wall during this time and presses toward the wall, the mechanics for speed conversion upon hitting a surface will be run every subframe, causing the character to lose a significant amount of vertical speed per frame, and when this property was discovered it was called “facegrinding” (particularly when travelling upward) because of the harsh speed loss.

This is usually a situation to be avoided, though occasionally it’s necessary to slow the character down so that we have an opportunity to grab a wall before the character passes it completely
