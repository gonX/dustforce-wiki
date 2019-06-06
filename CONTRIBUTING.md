---
---
# Contributing

Thanks for your interest in contributing!

We absolutely recommend coming to our Discord before submitting your first pull request: https://discord.gg/4F9WQeV

Content changes or additions (especially where we are lacking content) may be pull requested at any time, given they're correct.

If you do not have experience with Jekyll, it is suggested that you walk through their [tutorial](https://jekyllrb.com/docs/step-by-step/01-setup/) before proceeding.

# Content Guidelines

## Content File Naming

**Filenames for content must at least contain a short subject of the file, e.g. `trash-golem.md` for an enemy.**.

Shortnames (e.g. `maps.md`) may be used if they are unlikely to collide (e.g. not `maps.md`).

### Sorting within a group

Files in subfolders are "flattened" to a single folder, so entries will be listed in alphabetical order as per their grouping.\
This is useful because it allows us to name files e.g. `001-my-first-map.md` to "always" show them at the top; however, please read below for specific naming.

If you wish to use this "numerical" (actually alphabetical) sorting, please use the format `###-title.md`, using 10's by default.

E.g.
1. User X adds the first "earliest" file: `010-test.md`
2. Later, user Y adds the second "earliest" file: `005-h.md`
3. Even later, user Z wants to add 2 files, one that shows prior to the `005` file, and one that shows after the `005` file, named `003.md` and `007.md` respectively.

This sort of naming allows for easy insertion either behind or ahead of a file, without renaming conflicting files.

If you do not care about the ordering, or are happy with the content being sorted alphabetically within its group, you do not need to use this naming system.

Also see [Adding content](#adding-content).

## Images in content

**Keep usage of images in content to a minimum.**

Their use should be educational, and should preferably only be used where text would otherwise be insufficient to get the point across.

### Image Formats
Lossless:
- PNG
- SVG

Lossy:
- JPG (reasonable qualities please!)

Try to avoid PNG as much as possible. In the future we might use something like [`jekyll-picture-tag`](https://github.com/robwierzbowski/jekyll-picture-tag) to use the HTML5 `<picture>` elements and present the most sane version of an image to the user. This would also allow for using WebP which is [not entirely supported everywhere yet](https://caniuse.com/#feat=webp).

### Image Dimensions
As small as possible while still retaining important detail. Preferably 480px wide or less. Media over 1920px wide would need really good argumentation why.

## Text Content

Please keep language as neutral, professional, and wiki-like as possible.

### Quotes in content

If you are quoting someone, please use the quote feature (prepend `>` to each line) of Markdown. It is suggested that you get permission from the quotee first.

Quotes should preferably be kept in their entirety - editing is permitted given that the original quote is presented elsewhere, e.g. in the commit.

# Adding Content

Adding a new "box" to the site is as easy as adding a new `.md` file with the proper Jekyll front matter in the header in their respective directories.

Also see [Content File Naming](#content-file-naming).

### Paths

The subfolders within the `_*/` paths are mostly for organizational purposes.

The groupings are based exclusively on the front matter variables set in the header of the file.

### Pretty Names

Most of the game-related collections translate keys or values to a human-readable format. This is used in the Liquid template for the front page.

The specific collection format differs in each game-related collection.

The format to use is a collection with `name` being the key to match on.

The preferred file type for Pretty Names is **YAML**.

## Enemies

`website/_enemies`:

Enemies are grouped by map group (forest/city/etc).

### Pretty Names for Enemies

We use [Pretty Names](#pretty-names) for detailing the value based on a **boolean** value.

This is injected in `website/index.md`.

The value may be injected into the description by using a `{}` token. All instances will be replaced.

The HTML injection that is currently possible is being deprecated, as the enemy stat display is planned to look like Maps' current implementation.

See [enemy_stats.yml](/website/_data/pretty_names/enemy_stats.yml) for the current format.

If an expected variable is not present in the front matter of the enemy, the value is not displayed.

As a side note - we are using Ruby's lack of strict types in the `hp` key, where the value of `0` evaluates to `false`.

### Front matter variables for Enemies

**Obligatory**:
```
name:
enemygroup:
can_hurt: bool
```

See the `df_enemygroups` array in `website/_config.yml` for the specific naming for `enemygroup`.

See the `defaults` array for the scope `_enemies` in `website/_config.yml` for additional stats you may set.

If the value contains "`?`", the class `uncertain-value` will be applied to the stat, (hopefully) coloring the stat red. When the enemy stats have been verified, this behavior (and hopefully this line) will be removed.

## Maps / Levels

`website/_maps`:

Maps are grouped by their nexus location.

#### Stats

There is a special case for tile- and enemy counts, where a count of 0 is hidden entirely.

We also only show map name in the case of Beginner Tutorial.

### Importing Stats for Maps

As opposed to enemy, character, and tech data (at least as of June '19), all stats are imported from the [`stock-maps.json`](/website/_data/stock-maps.json) file found in `website/_data`.

To update these stats, there is a Python script ([main.py](/scripts/get-level-data/main.py)) provided in [`scripts/get-level-data`](/scripts/get-level-data) which will update the file in-place.

Generally this is not necessary as the level data is unlikely to change, unless data was actually incorrectly processed by the script.

There is currently no support for custom maps, but this is something we probably want in the future. Please reach out to us if you have any ideas for implementations.

### Pretty Names for Map stats

We use [Pretty Names](#pretty-names) for detailing the key.

This behaves similarly to [Enemies' implementation](#pretty-names-for-enemies) except we simply just (currently) use the value of `longdesc` rather than checking for a boolean.

### Front matter variables for Maps

**Obligatory**:
```
name:
mapgroup:
```

See the `df_mapgroups` array in `website/_config.yml` for the specific naming for `mapgroup`.

As of June '19 there are no other front matter variables you can set for maps.

## Mechanics / Tech

`website/_mechanics`:

Tech is grouped by subjective difficulty. It is suggested to use the "numerical naming convention" as described in [Sorting Within A Group](#sorting-within-a-group).

### Front matter variables for Tech

**Obligatory**:
```
name:
techgroup:
```

See the `df_techgroups` array in `website/_config.yml` for the specific naming for `techgroup`.

We also support the front matter variable `tags` which is a space separated list of strings. This is currently only displayed as an aside in each box.

## Playable Characters

`website/_playable-characters`:

Files are sorted alphanumerically.

### Front matter variables for Characters

As there are a lot of obligatory variables aside from the usual `name`, we refer to the scope `_playable_characters` in the `defaults` collection of `website/_config.yml`.

Null values will still be displayed.


