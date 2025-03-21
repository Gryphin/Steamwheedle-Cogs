import base64

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

def get_unit(bytes, unit_type_idx, talent_idx):
    unit_info = lookup[bytes[unit_type_idx]]
    unit = { "name": unit_info["name"] }

    if len(bytes) > 4:
        unit["talent"] = unit_info["talents"][bytes[talent_idx]]

    return unit

def parse_loadout(input):
    try:
        payload = base64.b64decode(bytearray(input.replace("rumblo:", ""), "utf-8"))

        units = []
        unit_bytes = []
        for i in range(len(payload)):
            unit_bytes.append(payload[i])

            if payload[i] == 0x1a or i == len(payload) - 1:
                parsing_leader = unit_bytes[0] == 0x08
                byte_start = 1 if parsing_leader else 2
                unit = get_unit(bytes=unit_bytes, unit_type_idx=byte_start, talent_idx=byte_start + 2)
                units.append(unit)
                
                unit_bytes = []
                
        return units
    except Exception as err:
        print("Error:", err)

# demo 
loadout = parse_loadout("rumblo:CBAQARoECB4QAhoECEcQAhoECE0QAhoECB0QARoECFkQAhoECEwQAg==")
if loadout:
    print(loadout)