# video/animated assets

depends on bandwidth costs, may use youtube or other host

- tech?
- character frames?

# foldable content

"cards" should be folded (content hidden) by default, and can show content by clicking the "card"

# additional hard stats

- enemy pathing speed (how would we display this?)
- enemy attack type?
- enemy "interruptible" in their attack? (foxes and gargoyles are, golems aren't)
- enemy knockback
- enemy "weight" (e.g. if put airborne)?
- boolean for enemy grounded wall pathing?
- character gained height for jump
- character time dilation for attacks
- character time to full speed from neutral

# other

- enemies should be grouped with their children, but is it right that children have their own entry? investigate if we can drop it in as a h4 under the enemy

- what is "porcupine quill hitbox overlap" from pastebin?

- sort tech in groups by significance, optionally with ###-NAME.md, e.g. 010-tutorial.md scheme

- add level for nexus - one for each area?

- is level pre or post-DX

- dustblock calculation may count dustblocks not on layer 19

- does the guide say that you can cancel attacks on the frame following the "frontswing", otherwise you lose up to `*attack_total_frames - *attack_frontswing_frames - 1`

- talk about refresh rates that aren't a multiple of 60hz causing issues on vanilla

- write about changing facing direction in air using 2 attacks
