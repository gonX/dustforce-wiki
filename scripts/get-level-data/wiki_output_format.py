from enum import IntEnum

class Keytype(IntEnum):
    NONE = 0
    RED = 1
    GOLD = 2
    SILVER = 3
    BRONZE = 4

class Character(IntEnum):
    MAN = 0
    GIRL = 1
    KID = 2
    WORTH = 3
    INVALID = 4

output_format = {
    # full map name as displayed on screen
    "name": "",

    # filename of the source file
    "srcfile": "",

    "is_virtual": False,

    ### tiles
    "tiles_layer1": 0,
    "tiles_layer2": 0,
    "tiles_layer3": 0,
    "tiles_layer4": 0,
    "tiles_layer5": 0,
    "tiles_layer6": 0,
    "tiles_layer7": 0,
    "tiles_layer8": 0,
    "tiles_layer9": 0,
    "tiles_layer10": 0,
    "tiles_layer11": 0,
    "tiles_layer12": 0,
    "tiles_layer13": 0,
    "tiles_layer14": 0,
    "tiles_layer15": 0,
    "tiles_layer16": 0,
    "tiles_layer17": 0,
    "tiles_layer18": 0,
    "tiles_layer19": 0,
    "tiles_layer20": 0,
    "tiles_layer21": 0,

    # tiles with filth or spikes on them (not tile faces)
    "covered_tiles": 0,
    "dustblocks": 0,

    # tile faces with filth or spikes on them
    "filthy_surfaces": 0,
    "spiked_surfaces": 0,

    # combo() from each enemy
    "dust_from_enemies": 0,

    # all dust excluding dustspread
    "total_dust": 0,

    ### props
    "props": 0,

    ### entities
    "apples": 0,

    "key_get_type": Keytype.NONE,

    ### enemies
    "enemies": 0,

    ## enemies by type, using the original name from the game

    # generic

    "enemy_tutorial_square": 0,
    "enemy_tutorial_hexagon": 0,
    "enemy_key": 0,
    "enemy_door": 0,

    # forest

    "enemy_critter": 0,
    "enemy_wolf": 0,
    "enemy_porcupine": 0,
    "enemy_stoneboss": 0,
    "enemy_stonebro": 0,
    "enemy_bear": 0,

    # mansion

    "enemy_butler": 0,
    "enemy_maid": 0,
    "enemy_flag": 0,
    "enemy_chest_treasure": 0,
    "enemy_chest_scrolls": 0,
    "enemy_gargoyle_big": 0,
    "enemy_gargoyle_small": 0,
    "enemy_knight": 0,
    "enemy_book": 0,

    # city

    "enemy_trash_can": 0,
    "enemy_trash_beast": 0,
    "enemy_trash_tire": 0,
    "enemy_trash_ball": 0,

    # lab
    "enemy_spring_ball": 0,
    "enemy_slime_barrel": 0,
    "enemy_slime_beast": 0,
    "enemy_slime_ball": 0,

    # community stats
    "best_score_time_ms": 0,
    "best_score_timestamp_epoch": 0,
    "best_score_username": "empty",
    "best_score_character": Character.INVALID,
    "best_score_replay_id": 0,
    "best_time_time_ms": 0,
    "best_time_timestamp_epoch": 0,
    "best_time_username": "empty",
    "best_time_character": Character.INVALID,
    "best_time_replay_id": 0
}


