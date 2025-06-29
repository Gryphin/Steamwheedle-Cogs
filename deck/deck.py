import discord
from redbot.core import commands, app_commands
import base64
import os
from PIL import Image
import io
from typing import List, Dict, Optional, NamedTuple
import logging

log = logging.getLogger(__name__)

# --- Constants ---
UNIT_IMAGE_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
LARGE_IMAGE_SIZE = (256, 256) # Size for the leader image
SMALL_IMAGE_SIZE = (128, 128) # Size for the other unit images
RUMBLO_CODE_PREFIX = "rumblo:" #cite: 38
UNIT_DELIMITER_BYTE = 0x1a #cite: 38
LEADER_UNIT_BYTE_IDENTIFIER = 0x08 #cite: 39

# Define a NamedTuple for better unit data structure
class RumbloUnit(NamedTuple):
    name: str
    talent: Optional[str] = None

# (lookup dictionary remains here, unchanged)
lookup = {
  0x39: {
    "name": "Malfurion",
    "talents": [
      "Deep Slumber",
      "Natural Salve",
      "Germinate"
    ]
  },
  0x5d: {
    "name": "Priestess",
    "talents": [
      "Power Word: Shield",
      "Empowered Renew",
      "Spirit of Redemption"
    ]
  },
  0x34: {
    "name": "Headless Horseman",
    "talents": [
      "Night Watch",
      "Decapitate",
      "Neigh Death Experience"
    ]
  },
  0x22: {
    "name": "Druid of the Claw",
    "talents": [
      "Regrowth",
      "Rejuvenation",
      "Leader of the Pack"
    ]
  },
  0x54: {
    "name": "Treant",
    "talents": [
      "Composting",
      "Uproot",
      "Propagation"
    ]
  },
  0x08: {
    "name": "Eclipse",
    "talents": [
      "Solar Flare",
      "Umbral Force",
      "Celestial Focus"
    ]
  },
  0x1e: {
    "name": "Dire Batlings",
    "talents": [
      "Midnight's Call",
      "Soundbite",
      "Guano Happens"
    ]
  },
  0x10: {
    "name": "Anub'arak",
    "talents": [
      "Regenerate",
      "Explosive Shells",
      "Trap Door"
    ]
  },
  0x1f: {
    "name": "Orgrim Doomhammer",
    "talents": [
      "Deathless Rage",
      "Rally the Clan",
      "Conqueror's Diplomacy"
    ]
  },
  0x51: {
    "name": "Swole Troll",
    "talents": [
      "Trollnado",
      "Troll Train",
      "Meatier Elbow"
    ]
  },
  0x5b: {
    "name": "Ysera the Dreamer",
    "talents": [
      "Recurring Dream",
      "Corrupted Dream",
      "Shared Dream"
    ]
  },
  0x23: {
    "name": "Dryad",
    "talents": [
      "Barrage",
      "Nature's Swiftness",
      "Thorns"
    ]
  },
  0x59: {
    "name": "Witch Doctor",
    "talents": [
      "Alchemist",
      "Amplify Curse",
      "Spirit Ward",
    ],
  },
  0x47: {
    "name": "Quilboar",
    "talents": [
      "Bristleback",
      "Tunnel Vision",
      "Bramble Burst",
    ],
  },
  0x58: {
    "name": "Whelp Eggs",
    "talents": [
      "Rookery",
      "Flame Burst",
      "Chromatic Plating",
    ],
  },
  0x09: {
    "name": "Execute",
    "talents": [
      "Bloodthirsty",
      "Killing Spree",
      "Overpower",
    ],
  },
  0x31: {
    "name": "Gryphon Rider",
    "talents": [
      "Air Drop",
      "Odyn's Fury",
      "Mighty Throw",
    ],
  },
  0x2e: {
    "name": "S.A.F.E. Pilot",
    "talents": [
      "Gnomish Cloaking Device",
      "Comin' In Hot!",
      "Gnomish Muttonizer",
    ],
  },
  0x32: {
    "name": "Harpies",
    "talents": [
      "Infectious Swipes",
      "Trinket Collectors",
      "Talon Dive",
    ],
  },
  0x06: {
    "name": "Deep Breath",
    "talents": [
      "Attunement",
      "Melting Point",
      "Double Dragon",
    ],
  },
  0x1d: {
    "name": "Defias Bandits",
    "talents": [
      "Deadly Poison",
      "Pick Lock",
      "Last Resort",
    ],
  },
  0x4b: {
    "name": "Frostwolf Shaman",
    "talents": [
      "Earthwall Totem",
      "Lightning Mastery",
      "Earth Shield",
    ],
  },
  0x2c: {
    "name": "Ghoul",
    "talents": [
      "Bone Shield",
      "Ravenous",
      "Taste for Blood",
    ],
  },
  0x36: {
    "name": "Huntress",
    "talents": [
      "Darnassian Steel",
      "Elven Might",
      "Shadowmeld",
    ],
  },
  0x3f: {
    "name": "Murloc Tidehunters",
    "talents": [
      "Safety Bubble",
      "Careful Aim",
      "Morelocs",
    ],
  },
  0x1b: {
    "name": "Dark Iron Miner",
    "talents": [
      "Dark Iron Armaments ",
      "Gold Mine",
      "Dwarven Ambition",
    ],
  },
  0x0c: {
    "name": "Polymorph",
    "talents": [
      "Golden Fleece",
      "Exploding Sheep",
      "Stable Transfiguration",
    ],
  },
  0x1c: {
    "name": "Darkspear Troll",
    "talents": [
      "Big Bad Voodoo",
      "Headhunting",
      "Serpent Sting",
    ],
  },
  0x33: {
    "name": "Harvest Golem",
    "talents": [
      "Trojan Chickens",
      "Unstable Core",
      "Bountiful Harvest",
    ],
  },
  0x0f: {
    "name": "Ancient of War",
    "talents": [
      "Sapling",
      "Behemoth",
      "Lightning Rod",
    ],
  },
  0x2b: {
    "name": "Gargoyle",
    "talents": [
      "Wing Buffet",
      "Obsidian Statue",
      "Aerial Superiority",
    ],
  },
  0x46: {
    "name": "Pyromancer",
    "talents": [
      "Pyroblast",
      "Conflagrate",
      "Blaze of Glory",
    ],
  },
  0x45: {
    "name": "Prowler",
    "talents": [
      "On The Prowl",
      "Pack Leader",
      "Predatory Instincts",
    ],
  },
  0x03: {
    "name": "Blizzard",
    "talents": [
      "Cold Snap",
      "Icecrown",
      "Brittle Ice",
    ],
  },
  0x11: {
    "name": "Banshee",
    "talents": [
      "Soul Eruption",
      "Unholy Frenzy",
      "Will of the Necropolis",
    ],
  },
  0x19: {
    "name": "Chimaera",
    "talents": [
      "Corrosive Breath",
      "Frost Shock",
      "Leviathan",
    ],
  },
  0x26: {
    "name": "Faerie Dragon",
    "talents": [
      "Phase Shift",
      "Invisibility",
      "Fae Blessing",
    ],
  },
  0x21: {
    "name": "General Drakkisath",
    "talents": [
      "Chromatic Scales",
      "Piercing Blows",
      "Lasting Legacy",
    ],
  },
  0x50: {
    "name": "Stonehoof Tauren",
    "talents": [
      "Pummel",
      "Momentum",
      "Provoke",
    ],
  },
  0x27: {
    "name": "Fire Elemental",
    "talents": [
      "Immolation Aura",
      "Molten Core",
      "Fan The Flames",
    ],
  },
  0x53: {
    "name": "Tirion Fordring",
    "talents": [
      "Divine Shield",
      "Consecrate",
      "By The Light",
    ],
  },
  0x12: {
    "name": "Baron Rivendare",
    "talents": [
      "Death Pact",
      "Skeletal Frenzy",
      "Chill Of The Grave",
    ],
  },
  0x37: {
    "name": "Jaina Proudmoore",
    "talents": [
      "Blink",
      "Clearcasting",
      "Flurry",
    ],
  },
  0x42: {
    "name": "Old Murk-Eye",
    "talents": [
      "Tip of the Spear",
      "Marathon Of The Murlocs",
      "Electric Eels",
    ],
  },
  0x4a: {
    "name": "Rend Blackhand",
    "talents": [
      "Flaming Soul",
      "Scale and Steel",
      "Legionnaire",
    ],
  },
  0x35: {
    "name": "Hogger",
    "talents": [
      "Ham Hock",
      "Spoiled Meat",
      "Fatal Frenzy",
    ],
  },
  0x16: {
    "name": "Cairne Bloodhoof",
    "talents": [
      "Reincarnation",
      "Plainsrunning",
      "Aftershock",
    ],
  },
  0x30: {
    "name": "Grommash Hellscream",
    "talents": [
      "Bladestorm",
      "Mirror Image",
      "Savage Strikes",
    ],
  },
  0x38: {
    "name": "Maiev Shadowsong",
    "talents": [
      "Enveloping Shadows",
      "Shadowstep",
      "Remorseless",
    ],
  },
  0x18: {
    "name": "Charlga Razorflank",
    "talents": [
      "Nature's Grasp",
      "Cavernous Mists",
      "Spirit Passage",
    ],
  },
  0x52: {
    "name": "Sylvanas Windrunner",
    "talents": [
      "Black Arrow",
      "Banshee's Wail",
      "Forsaken Fury",
    ],
  },
  0x25: {
    "name": "Emperor Thaurissan",
    "talents": [
      "Moira's Wit",
      "Hubris",
      "Incinerate",
    ],
  },
  0x14: {
    "name": "Bloodmage Thalnos",
    "talents": [
      "Bane",
      "Drain Life",
      "Dominance",
    ],
  },
  0x0e: {
    "name": "Abomination",
    "talents": [
      "Noxious Presence",
      "Cannonball",
      "Fresh Meat",
    ],
  },
  0x05: {
    "name": "Cheat Death",
    "talents": [
      "Last Gasp",
      "Vampirism",
      "Apocalypse",
    ],
  },
  0x4e: {
    "name": "Sneed",
    "talents": [
      "Mine Is Money, Friend!",
      "Lead with Greed",
      "Land Grab",
    ],
  },
  0x20: {
    "name": "Drake",
    "talents": [
      "Mother Drake",
      "Roost",
      "Engulfing Flames",
    ],
  },
  0x24: {
    "name": "Earth Elemental",
    "talents": [
      "Ready to Rumble",
      "Shrapnel Blast",
      "Obsidian Shard",
    ],
  },
  0x02: {
    "name": "Arcane Blast",
    "talents": [
      "Amplification",
      "Arcane Power",
      "Torrent",
    ],
  },
  0x04: {
    "name": "Chain Lightning",
    "talents": [
      "Brilliant Flash",
      "Storm's Reach",
      "Reverberation",
    ],
  },
  0x55: {
    "name": "Vultures",
    "talents": [
      "Tendon Rip",
      "Feeding Frenzy",
      "Migration",
    ],
  },
  0x17: {
    "name": "Cenarius",
    "talents": [
      "Revitalize",
      "Force of Nature",
      "Wild Growth",
    ],
  },
  0x48: {
    "name": "Ragnaros",
    "talents": [
      "Concussive Blast",
      "Radiant Flames",
      "Sons of Flame",
    ],
  },
  0x4d: {
    "name": "Skeletons",
    "talents": [
      "Questing Buddies",
      "Cackle",
      "Exhume",
    ],
  },
  0x3a: {
    "name": "Meat Wagon",
    "talents": [
      "Meat And Bones",
      "Filet Trebuchet",
      "Greased Gears",
    ],
  },
  0x0a: {
    "name": "Holy Nova",
    "talents": [
      "Inner Fire",
      "Renew",
      "Amplify Magic",
    ],
  },
  0x13: {
    "name": "Bat Rider",
    "talents": [
      "Flaming Pitch",
      "Enchanted Vials",
      "Fiery Surplus",
    ],
  },
  0x40: {
    "name": "Necromancer",
    "talents": [
      "Cult of the Damned",
      "Jeweled Skulls",
      "Breath of the Dying",
    ],
  },
  0x0d: {
    "name": "Smoke Bomb",
    "talents": [
      "Strangers in the Night",
      "Band Of Thieves",
      "Through The Shadows",
    ],
  },
  0x4c: {
    "name": "Skeleton Party",
    "talents": [
      "5-Man",
      "Corpse Run",
      "Ritual of Rime",
    ],
  },
  0x5a: {
    "name": "Worgen",
    "talents": [
      "Lone Wolf",
      "Premeditation",
      "Frenzy",
    ],
  },
  0x2f: {
    "name": "Goblin Sapper",
    "talents": [
      "Extra BOOM",
      "Rocket Powered Turbo Boots",
      "Crude Gunpowder",
    ],
  },
  0x43: {
    "name": "Onu, Ancient of Lore",
    "talents": [
      "Barkskin",
      "Petrify",
      "From the Trees!",
    ],
  },
  0x44: {
    "name": "Plague Farmer",
    "talents": [
      "Parting Gift",
      "Virulence",
      "Splashing Pumpkins",
    ],
  },
  0x57: {
    "name": "Warsong Raider",
    "talents": [
      "Saboteur",
      "Razing Focus",
      "Sunder Armor",
    ],
  },
  0x15: {

    "name": "Bog Beast",
    "talents": [
      "Flourish",
      "Rampant Growth",
      "Living Wood",
    ],
  },
  0x3b: {
    "name": "Molten Giant",
    "talents": [
      "Threatening Presence",
      "Blood Of The Mountain",
      "Bolster",
    ],
  },
  0x2d: {
    "name": "Gnoll Brute",
    "talents": [
      "Rabid",
      "Pillage",
      "Thick Hide",
    ],
  },
  0x07: {
    "name": "Earth and Moon",
    "talents": [
      "Moonfury",
      "Nature's Grace",
      "Balance",
    ],
  },
  0x3c: {
    "name": "Moonkin",
    "talents": [
      "Vengeance",
      "Moonglow",
      "Typhoon",
    ],
  },
  0x2a: {
    "name": "Footmen",
    "talents": [
      "Shield Bash",
      "Fortification",
      "Last Stand",
    ],
  },
  0x29: {
    "name": "Flamewaker",
    "talents": [
      "Heat Stroke",
      "Engulf",
      "Backdraft",
    ],
  },
  0x41: {
    "name": "Ogre Mage",
    "talents": [
      "Frostfire Bolt",
      "Ignite",
      "Avarice",
    ],
  },
  0x01: {
    "name": "Angry Chickens",
    "talents": [
      "Snackrifice",
      "Walking Crate",
      "Furious Fowl",
    ],
  },
  0x1a: {
    "name": "Core Hounds",
    "talents": [
      "Fiery Rebirth",
      "Guard Dog",
      "Eternal Bond",
    ],
  },
  0x28: {
    "name": "Firehammer",
    "talents": [
      "Moultin' Metal",
      "Blazing Speed",
      "Heightened Rage",
    ],
  },
  0x49: {
    "name": "Raptors",
    "talents": [
      "Strength In Numbers",
      "Fast Food",
      "Motivation",
    ],
  },
  0x0b: {
    "name": "Living Bomb",
    "talents": [
      "Burden Of Fate",
      "Chain Reaction",
      "Blast Radius",
    ],
  },
  0x56: {
    "name": "Warsong Grunts",
    "talents": [
      "Blood Pact",
      "Guard Duty",
      "Command",
    ],
  },
  0x4f: {
    "name": "Spiderlings",
    "talents": [
      "Bloated Carapace",
      "Frostbite",
      "Envenom",
    ],
  },
  0x3d: {
    "name": "Mountaineer",
    "talents": [
      "Frenzied Spirit",
      "Mend Pets",
      "Intimidation",
    ],
  },
    0x5e: {
      "name": "Arthas Menethil",
      "talents": [
        "Death Grip",
        "Necrotic Plague",
        "Purgatory"
    ],
  },
    0x5f: {
      "name": "Thrall",
      "talents": [
        "Totemic Mastery",
        "Feral Spirit",
        "Call Of The Horde"
    ],
  },
}
# --- End of content from dl.txt ---
# --- Updated: Local Image Paths (Ensure these match your actual filenames) ---
UNIT_IMAGE_PATHS = {
    "Malfurion": "malfurion.png",
    "Priestess": "priestess.png",
    "Headless Horseman": "headless-horseman.png",
    "Druid of the Claw": "druid-of-the-claw.png",
    "Treant": "treant.png",
    "Eclipse": "eclipse.png",
    "Dire Batlings": "dire-batlings.png",
    "Anub'arak": "anubarak.png",
    "Orgrim Doomhammer": "orgrim-doomhammer.png",
    "Swole Troll": "swole-troll.png",
    "Ysera the Dreamer": "ysera-the-dreamer.png",
    "Dryad": "dryad.png",
    "Witch Doctor": "witch-doctor.png",
    "Quilboar": "quilboar.png",
    "Whelp Eggs": "whelp-eggs.png",
    "Execute": "execute.png",
    "Gryphon Rider": "gryphon-rider.png",
    "S.A.F.E. Pilot": "safe-pilot.png",
    "Harpies": "harpies.png",
    "Deep Breath": "deep-breath.png",
    "Defias Bandits": "defias-bandits.png",
    "Frostwolf Shaman": "frostwolf-shaman.png",
    "Ghoul": "ghoul.png",
    "Huntress": "huntress.png",
    "Murloc Tidehunters": "murloc-tidehunters.png",
    "Dark Iron Miner": "dark-iron-miner.png",
    "Polymorph": "polymorph.png",
    "Darkspear Troll": "darkspear-troll.png",
    "Harvest Golem": "harvest-golem.png",
    "Ancient of War": "ancient-of-war.png",
    "Gargoyle": "gargoyle.png",
    "Pyromancer": "pyromancer.png",
    "Prowler": "prowler.png",
    "Blizzard": "blizzard.png",
    "Banshee": "banshee.png",
    "Chimaera": "chimaera.png",
    "Faerie Dragon": "faerie-dragon.png",
    "General Drakkisath": "general-drakkisath.png",
    "Stonehoof Tauren": "stonehoof-tauren.png",
    "Fire Elemental": "fire-elemental.png",
    "Tirion Fordring": "tirion-fordring.png",
    "Baron Rivendare": "baron-rivendare.png",
    "Jaina Proudmoore": "jaina-proudmoore.png",
    "Old Murk-Eye": "old-murk-eye.png",
    "Rend Blackhand": "rend-blackhand.png",
    "Hogger": "hogger.png",
    "Cairne Bloodhoof": "cairne-bloodhoof.png",
    "Grommash Hellscream": "grommash-hellscream.png",
    "Maiev Shadowsong": "maiev-shadowsong.png",
    "Charlga Razorflank": "charlga-razorflank.png",
    "Sylvanas Windrunner": "sylvanas-windrunner.png",
    "Emperor Thaurissan": "emperor-thaurissan.png",
    "Bloodmage Thalnos": "bloodmage-thalnos.png",
    "Abomination": "abomination.png",
    "Cheat Death": "cheat-death.png",
    "Sneed": "sneed.png",
    "Drake": "drake.png",
    "Earth Elemental": "earth-elemental.png",
    "Arcane Blast": "arcane-blast.png",
    "Chain Lightning": "chain-lightning.png",
    "Vultures": "vultures.png",
    "Cenarius": "cenarius.png",
    "Ragnaros": "ragnaros.png",
    "Skeletons": "skeletons.png",
    "Meat Wagon": "meat-wagon.png",
    "Holy Nova": "holy-nova.png",
    "Bat Rider": "bat-rider.png",
    "Necromancer": "necromancer.png",
    "Smoke Bomb": "smoke-bomb.png",
    "Skeleton Party": "skeleton-party.png",
    "Worgen": "worgen.png",
    "Goblin Sapper": "goblin-sapper.png",
    "Onu, Ancient of Lore": "onu-ancient-of-lore.png",
    "Plague Farmer": "plague-farmer.png",
    "Warsong Raider": "warsong-raider.png",
    "Bog Beast": "bog-beast.png",
    "Molten Giant": "molten-giant.png",
    "Gnoll Brute": "gnoll-brute.png",
    "Earth and Moon": "earth-and-moon.png",
    "Moonkin": "moonkin.png",
    "Footmen": "footmen.png",
    "Flamewaker": "flamewaker.png",
    "Ogre Mage": "ogre-mage.png",
    "Angry Chickens": "angry-chickens.png",
    "Core Hounds": "core-hounds.png",
    "Firehammer": "firehammer.png",
    "Raptors": "raptors.png",
    "Living Bomb": "living-bomb.png",
    "Warsong Grunts": "warsong-grunts.png",
    "Spiderlings": "spiderlings.png",
    "Mountaineer": "mountaineer.png",
    "Arthas Menethil": "arthas-menethil.png",
    "Thrall": "thrall.png"
    # Add all other units with their corresponding filenames
}

def get_unit(bytes_data: bytearray, unit_type_idx: int, talent_idx: int) -> RumbloUnit:
    """
    Retrieves unit name and talent from lookup based on byte data.
    """
    unit_info = lookup.get(bytes_data[unit_type_idx]) #cite: 1
    if not unit_info:
        log.warning(f"Unknown unit type byte: {bytes_data[unit_type_idx]:#0x}")
        return RumbloUnit(name="Unknown Unit", talent="N/A")

    unit_name = unit_info["name"] #cite: 1
    unit_talent = None
    if len(bytes_data) > 4: #cite: 38
        try:
            unit_talent = unit_info["talents"][bytes_data[talent_idx]] #cite: 38
        except IndexError:
            log.warning(f"Invalid talent index {bytes_data[talent_idx]} for unit {unit_name}")
            unit_talent = "Invalid Talent Index"
        except KeyError:
            log.warning(f"Talents not found for unit {unit_name}")
            unit_talent = "No Talent Info"

    return RumbloUnit(name=unit_name, talent=unit_talent) #cite: 38

def parse_loadout(input_string: str) -> Optional[List[RumbloUnit]]:
    """
    Decodes a Rumblo loadout string into a list of RumbloUnit objects.
    Raises ValueError for invalid input.
    """
    if not input_string.startswith(RUMBLO_CODE_PREFIX):
        raise ValueError("Invalid Rumblo code format: missing prefix.")

    try:
        payload = base64.b64decode(bytearray(input_string.replace(RUMBLO_CODE_PREFIX, ""), "utf-8")) #cite: 38
    except (base64.binascii.Error, UnicodeDecodeError) as e:
        log.error(f"Base64 decoding error: {e}")
        raise ValueError("Failed to decode Rumblo code: invalid base64 format.") from e
    except Exception as e:
        log.error(f"Unexpected error during payload decoding: {e}")
        raise ValueError("An unexpected error occurred during decoding.") from e

    units: List[RumbloUnit] = [] #cite: 38
    unit_bytes: List[int] = [] #cite: 38
    
    for i in range(len(payload)): #cite: 38
        unit_bytes.append(payload[i]) #cite: 38

        if payload[i] == UNIT_DELIMITER_BYTE or i == len(payload) - 1: #cite: 38
            if not unit_bytes:
                log.warning("Empty unit_bytes encountered before delimiter, skipping.")
                continue

            parsing_leader = unit_bytes[0] == LEADER_UNIT_BYTE_IDENTIFIER #cite: 39
            byte_start = 1 if parsing_leader else 2 #cite: 39
            
            if byte_start + 2 >= len(unit_bytes):
                log.warning(f"Malformed unit data segment: {unit_bytes}. Skipping unit.")
                unit_bytes = []
                continue

            unit = get_unit(bytes_data=bytearray(unit_bytes), unit_type_idx=byte_start, talent_idx=byte_start + 2) #cite: 39
            units.append(unit) #cite: 39
            unit_bytes = [] #cite: 40
            
    if not units:
        raise ValueError("No units could be parsed from the provided code.")
        
    return units #cite: 40

def combine_unit_images(unit_names: List[str]) -> Optional[io.BytesIO]:
    """
    Combines images of units into a two-row layout:
    First image 256x256, next up to 6 images 128x128 arranged in two rows of three.
    Returns a BytesIO object containing the combined image, or None if no images are found.
    """
    if not unit_names:
        return None

    # Load and resize the main image (first unit)
    main_image: Optional[Image.Image] = None
    if unit_names:
        first_unit_name = unit_names[0]
        file_name = UNIT_IMAGE_PATHS.get(first_unit_name)
        if file_name:
            file_path = os.path.join(UNIT_IMAGE_DIRECTORY, file_name)
            if os.path.exists(file_path):
                try:
                    img = Image.open(file_path).convert("RGBA")
                    main_image = img.resize(LARGE_IMAGE_SIZE, Image.Resampling.LANCZOS)
                except Exception as e:
                    log.error(f"Could not open or process main image for {first_unit_name} at {file_path}: {e}")
            else:
                log.warning(f"Main image file not found for {first_unit_name} at {file_path}")
        else:
            log.info(f"No image path defined for main unit: {first_unit_name}")

    # Load and resize the small images (up to next 6 units)
    small_images: List[Image.Image] = []
    for i in range(1, min(len(unit_names), 7)): # Iterate from the second unit up to a total of 7 (1 large + 6 small)
        name = unit_names[i]
        file_name = UNIT_IMAGE_PATHS.get(name)
        if not file_name:
            log.info(f"No image path defined for unit: {name}")
            continue

        file_path = os.path.join(UNIT_IMAGE_DIRECTORY, file_name)
        if os.path.exists(file_path):
            try:
                img = Image.open(file_path).convert("RGBA")
                img = img.resize(SMALL_IMAGE_SIZE, Image.Resampling.LANCZOS)
                small_images.append(img)
            except Exception as e:
                log.error(f"Could not open or process small image for {name} at {file_path}: {e}")
        else:
            log.warning(f"Small image file not found for {name} at {file_path}")

    if not main_image and not small_images:
        return None

    # Determine overall canvas dimensions
    # The layout is:
    # [Large Image (256x256)]
    # [Small Image 1][Small Image 2][Small Image 3]
    # [Small Image 4][Small Image 5][Small Image 6]

    # Calculate width of the small image rows (max 3 images per row)
    # The maximum width for a row of 3 small images is 3 * 128 = 384
    small_rows_max_width = 3 * SMALL_IMAGE_SIZE[0]

    # Combined image width will be the max of the large image width or the small rows width
    combined_width = max(LARGE_IMAGE_SIZE[0] if main_image else 0, small_rows_max_width)

    combined_height = 0
    if main_image:
        combined_height += LARGE_IMAGE_SIZE[1] # Height for the large image

    # Add height for small image rows
    if small_images:
        # First row of small images
        if len(small_images) > 0:
            combined_height += SMALL_IMAGE_SIZE[1]
        # Second row of small images (if more than 3)
        if len(small_images) > 3:
            combined_height += SMALL_IMAGE_SIZE[1]
    
    # If no main image but small images exist, ensure a valid height
    if not main_image and small_images:
        combined_height = 0 # Reset if main image was the only contributor
        if len(small_images) > 0:
            combined_height += SMALL_IMAGE_SIZE[1]
        if len(small_images) > 3:
            combined_height += SMALL_IMAGE_SIZE[1]
        
        # If only small images, ensure width is at least for a full row of 3 small images
        combined_width = max(combined_width, small_rows_max_width)

    if combined_width == 0 or combined_height == 0:
        return None # Should not happen if main_image or small_images exist, but as a safeguard

    combined_image = Image.new('RGBA', (combined_width, combined_height))

    current_y_offset = 0

    # Paste the main image (leader)
    if main_image:
        # Center the large image horizontally
        x_offset_main = (combined_width - main_image.width) // 2
        combined_image.paste(main_image, (x_offset_main, current_y_offset))
        current_y_offset += main_image.height

    # Paste small images in rows
    small_images_to_paste = list(small_images) # Create a mutable copy
    
    for row_num in range(2): # Two rows for small images
        if not small_images_to_paste:
            break

        current_row_images = small_images_to_paste[:3] # Get up to 3 images for the current row
        small_images_to_paste = small_images_to_paste[3:] # Remove them from the list

        current_row_width = sum(img.width for img in current_row_images)
        x_offset = (combined_width - current_row_width) // 2 # Center the row

        for img in current_row_images:
            combined_image.paste(img, (x_offset, current_y_offset))
            x_offset += img.width
        
        current_y_offset += SMALL_IMAGE_SIZE[1] # Move to the next row's starting y-coordinate

    image_binary = io.BytesIO()
    try:
        combined_image.save(image_binary, 'PNG')
        image_binary.seek(0)
    except Exception as e:
        log.error(f"Failed to save combined image to BytesIO: {e}")
        return None

    return image_binary


class RumbloDecoder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Refactored to use a slash command
    @app_commands.command(name="decode", description="Decodes a Rumblo loadout code and displays units/talents.")
    @app_commands.describe(code="The Rumblo loadout code (e.g., 'rumblo:...')")
    async def decode_rumblo(self, interaction: discord.Interaction, code: str):
        """
        Decodes a Rumblo loadout code and displays the units and their talents,
        combining unit images using Pillow.
        Usage: /decode <rumblo_code>
        """
        # Acknowledge the interaction immediately to prevent timeout
        await interaction.response.defer()

        try:
            loadout_info = parse_loadout(code)
        except ValueError as e:
            await interaction.followup.send(f"Decoding error: {e}")
            return

        unit_details_text: List[str] = []
        unit_names_for_images: List[str] = []
        for i, unit in enumerate(loadout_info):
            unit_details_text.append(f"**Unit {i+1}:** {unit.name} ({unit.talent or 'No Talent'})")
            unit_names_for_images.append(unit.name)

        combined_image_stream = combine_unit_images(unit_names_for_images)

        if combined_image_stream:
            embed = discord.Embed(
                title="Rumblo Loadout Decoded",
                description="\n".join(unit_details_text),
                color=discord.Color.blue()
            )
            embed.set_image(url="attachment://loadout.png")
            await interaction.followup.send(embed=embed, file=discord.File(fp=combined_image_stream, filename='loadout.png'))
        else:
            embed = discord.Embed(
                title="Rumblo Loadout Decoded (No Images Available)",
                description="\n".join(unit_details_text) + "\n\n*No unit images could be loaded or combined.*",
                color=discord.Color.orange()
            )
            await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(RumbloDecoder(bot))
    # Sync slash commands with Discord. This is crucial for them to appear.
    # For global commands, it's recommended to do this only once during bot startup or on changes.
    # For testing, you might sync to a specific guild.
    await bot.tree.sync()
