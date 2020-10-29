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
- enemy lureability (true for: wolves, stonebro, stoneboss, knight) (thanks Skyhawk)
- map checkpoint count
- boolean for enemy grounded wall pathing?
- character gained height for jump
- character time dilation for attacks
- character time to full speed from neutral

# missing maps

- infini (thanks to chipi)
- old tutorial (thanks to chipi)

# missing tech

- explanation of units (tile size, speed, more?), probably in basic game mechanics (thanks Zaandaa)
- twirlies (thanks to Zaandaa/IsaVulpes)
- "clearing dust through walls with attacks" (seam attacks?)
- changing facing direction mid-air using 2 attacks
- super cancels
- clipping
- TAS techs (thx Zaandaa)
-- RLJ
-- LSJ
-- other??

# other

- missing mapmaking section: (put below tech?)
-- talk about sublayer fog triggers (https://pastebin.com/Ua5gfDYU)

- enemies should be grouped with their children, but is it right that children have their own entry? investigate if we can drop it in as a h4 under the enemy

- what is "porcupine quill hitbox overlap" from pastebin?

- sort tech in groups by significance, optionally with ###-NAME.md, e.g. 010-tutorial.md scheme

- add level for nexus - one for each area?

- is level pre or post-DX

- dustblock calculation may count dustblocks not on layer 19

- does the guide say that you can cancel attacks on the frame following the "frontswing", otherwise you lose up to `*attack_total_frames - *attack_frontswing_frames - 1`

- talk about refresh rates that aren't a multiple of 60hz causing issues on vanilla

- subcategories (e.g. tech->basics->Super->ranges) should have better anchors (now: #ranges, should be #super-ranges)

- write about how atlas ranking is based on points awarded per map and per comment (https://discordapp.com/channels/83037671227658240/275015117236731905/633776460359925790)

- insert blurb about the different settings available in the original client, as well as Dustmod

- lazy loading of images (`loading` attribute on `<img>`)

- add Linux Dustmod guide (desktop file and `update-desktop-database` etc (https://discordapp.com/channels/83037671227658240/276106941875355658/751985083581333626)

- refactor scss

- leaderboard link on each map panel (thanks to chipi)

- resizing window breaks camera
