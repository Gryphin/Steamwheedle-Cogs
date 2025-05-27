import discord
from redbot.core import commands, app_commands
import base64
import os
import io
from PIL import Image
# --- Start of content from dl.txt (unchanged from previous response) ---
# --- Start of content from dl.txt (unchanged from previous response) ---
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
  }
}

def get_unit(bytes_data, unit_type_idx, talent_idx): # Renamed 'bytes' parameter to 'bytes_data' to avoid conflict with built-in 'bytes'
    unit_info = lookup[bytes_data[unit_type_idx]] # cite: 1
    unit = { "name": unit_info["name"] } # cite: 1

    if len(bytes_data) > 4: # cite: 38
        unit["talent"] = unit_info["talents"][bytes_data[talent_idx]] # cite: 38

    return unit # cite: 38

def parse_loadout(input_string): # Renamed 'input' parameter to 'input_string' to avoid conflict with built-in 'input'
    try:
        payload = base64.b64decode(bytearray(input_string.replace("rumblo:", ""), "utf-8")) # cite: 38

        units = [] # cite: 38
        unit_bytes = [] # cite: 38
        for i in range(len(payload)): # cite: 38
            unit_bytes.append(payload[i]) # cite: 38

            if payload[i] == 0x1a or i == len(payload) - 1: # cite: 38
                parsing_leader = unit_bytes[0] == 0x08 # cite: 39
                byte_start = 1 if parsing_leader else 2 # cite: 39
                unit = get_unit(bytes_data=unit_bytes, unit_type_idx=byte_start, talent_idx=byte_start + 2) # cite: 39
                units.append(unit) # cite: 39
                unit_bytes = [] # cite: 40
                
        return units # cite: 40
    except Exception as err:
        print("Error:", err) # cite: 40
        return None
# --- End of content from dl.txt ---

# --- Updated: Local Image Paths ---
# You MUST populate this with the correct filenames for your local images.
# Example: "Malfurion": "malfurion.png" if you have images/malfurion.png
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
    # Add all other units with their corresponding filenames
}

class RumbloDecoder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="decode")
    async def decode_rumblo(self, ctx, code: str):
        """
        Decodes a Rumblo loadout code and displays the units and their talents with local images.
        Usage: !decode <rumblo_code>
        """
        if not code.startswith("rumblo:"):
            await ctx.send("Please provide a valid Rumblo code starting with 'rumblo:'.")
            return

        loadout_info = parse_loadout(code)

        if loadout_info:
            for i, unit in enumerate(loadout_info):
                name = unit.get("name", "Unknown Unit")
                talent = unit.get("talent", "No Talent")

                embed = discord.Embed(
                    title=f"Unit {i+1}: {name}",
                    description=f"**Talent:** {talent}",
                    color=discord.Color.blue()
                )

                file_path = None
                if name in UNIT_IMAGE_PATHS:
                    # Construct the full path to the image file
                    file_name = UNIT_IMAGE_PATHS[name]
                    file_path = os.path.abspath(images, file_name)

                if file_path and os.path.exists(file_path):
                    # Create a discord.File object
                    file = discord.File(file_path, filename=file_name)
                    # Set the image of the embed to reference the attached file
                    embed.set_image(url=f"attachment://{file_name}")
                    # Send the embed and the file together
                    await ctx.send(embed=embed, file=file)
                else:
                    # If image not found, send embed without image
                    if file_path:
                        await ctx.send(f"Warning: Image not found for {name} at {file_path}")
                    await ctx.send(embed=embed)
        else:
            await ctx.send("Failed to decode the Rumblo code. Please check the code's validity.")

async def setup(bot):
    await bot.add_cog(RumbloDecoder(bot))
