
# Division2 API Server

Remade an old project that was made by someone else. This is an API Server for Tracker.gg Division2 Stats.

The server essentially creates the bridge between whatever server you want and tracker.gg 
It uses tracker's internal API so no API keys are needed.


## Features

- Api Authentication
- API Reponse Logging



## Installation

Before installing make sure you edit config.json to your liking and then import the .sql file

```bash
  
  python -m pip install -r requirements.txt
  python server.py or 
  waitress-serve --host 0.0.0.0 --port=105 main:app
```
    
## Usage/Examples

```javascript
/api/help
/api/query-data
```

Reponse example

```json
{
    "status": true,
    "data": [
        {
            "platformSlug": "uplay"
        },
        {
            "platformUserId": "43fe181a-d92a-408f-9f84-c43042197baf"
        },
        {
            "avatarUrl": "https://ubisoft-avatars.akamaized.net/43fe181a-d92a-408f-9f84-c43042197baf/default_146_146.png"
        },
        {
            "timePlayed": {
                "rank": null,
                "percentile": 99.7,
                "displayName": "Time Played",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 18868677,
                "displayValue": "5,241h",
                "displayType": "TimeSeconds"
            }
        },
        {
            "killsPvP": {
                "rank": null,
                "percentile": 93,
                "displayName": "PvP Kills",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 844,
                "displayValue": "844",
                "displayType": "Number"
            }
        },
        {
            "killsNpc": {
                "rank": null,
                "percentile": 99.4,
                "displayName": "NPC Kills",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 377987,
                "displayValue": "377,987",
                "displayType": "Number"
            }
        },
        {
            "killsSkill": {
                "rank": null,
                "percentile": 98,
                "displayName": "Skill Kills",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 63757,
                "displayValue": "63,757",
                "displayType": "Number"
            }
        },
        {
            "headshots": {
                "rank": null,
                "percentile": 99.9,
                "displayName": "Headshots",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 3434219,
                "displayValue": "3,434,219",
                "displayType": "Number"
            }
        },
        {
            "itemsLooted": {
                "rank": null,
                "percentile": 98.6,
                "displayName": "Items Looted",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 73159,
                "displayValue": "73,159",
                "displayType": "Number"
            }
        },
        {
            "xPTotal": {
                "rank": null,
                "percentile": 88,
                "displayName": "Total XP",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 392591120,
                "displayValue": "392,591,120",
                "displayType": "Number"
            }
        },
        {
            "xPClan": {
                "rank": null,
                "percentile": null,
                "displayName": "Clan XP",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
            }
        },
        {
            "specialization": {
                "rank": null,
                "percentile": null,
                "displayName": "Specialization",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": "Demolitionist",
                "displayValue": "Demolitionist",
                "displayType": "String"
            }
        },
        {
            "killsSpecializationSharpshooter": {
                "rank": null,
                "percentile": 92,
                "displayName": "Sharpshooter Kills",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 37624,
                "displayValue": "37,624",
                "displayType": "Number"
            }
        },
        {
            "killsSpecializationSurvivalist": {
                "rank": null,
                "percentile": 97.7,
                "displayName": "Survivalist Kills",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 54196,
                "displayValue": "54,196",
                "displayType": "Number"
            }
        },
        {
            "killsSpecializationDemolitionist": {
                "rank": null,
                "percentile": 79,
                "displayName": "Demolitionist Kills",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 20824,
                "displayValue": "20,824",
                "displayType": "Number"
            }
        },
        {
            "eCreditBalance": {
                "rank": null,
                "percentile": 81,
                "displayName": "E-Credit Balance",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 477270,
                "displayValue": "477,270",
                "displayType": "Number"
            }
        },
        {
            "commendationCount": {
                "rank": null,
                "percentile": 96.8,
                "displayName": "Commendations",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 805,
                "displayValue": "805",
                "displayType": "Number"
            }
        },
        {
            "commendationScore": {
                "rank": null,
                "percentile": 78,
                "displayName": "Curr Comm. Score",
                "displayCategory": "General",
                "category": "general",
                "metadata": {},
                "value": 2690,
                "displayValue": "2,690",
                "displayType": "Number"
            }
        },
        {
            "latestGearScore": {
                "rank": null,
                "percentile": 83,
                "displayName": "Gear Score",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 922,
                "displayValue": "922",
                "displayType": "Number"
            }
        },
        {
            "highestPlayerLevel": {
                "rank": null,
                "percentile": 74,
                "displayName": "Player Level",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 40,
                "displayValue": "40",
                "displayType": "Number"
            }
        },
        {
            "xPPve": {
                "rank": null,
                "percentile": 98.5,
                "displayName": "PvE XP",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 391403259,
                "displayValue": "391,403,259",
                "displayType": "Number"
            }
        },
        {
            "timePlayedPve": {
                "rank": null,
                "percentile": 98.7,
                "displayName": "Time Played",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 9944613,
                "displayValue": "2,762h",
                "displayType": "TimeSeconds"
            }
        },
        {
            "killsRoleElite": {
                "rank": null,
                "percentile": null,
                "displayName": "Elite Kills",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
            }
        },
        {
            "killsRoleNamed": {
                "rank": null,
                "percentile": 99.5,
                "displayName": "Named Kills",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 22778,
                "displayValue": "22,778",
                "displayType": "Number"
            }
        },
        {
            "killsFactionBlackbloc": {
                "rank": null,
                "percentile": 96.1,
                "displayName": "Hyena Kills",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 27946,
                "displayValue": "27,946",
                "displayType": "Number"
            }
        },
        {
            "killsFactionCultists": {
                "rank": null,
                "percentile": 99.5,
                "displayName": "OutCasts Kills",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 75851,
                "displayValue": "75,851",
                "displayType": "Number"
            }
        },
        {
            "killsFactionMilitia": {
                "rank": null,
                "percentile": 99.3,
                "displayName": "TrueSons Kills",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 82288,
                "displayValue": "82,288",
                "displayType": "Number"
            }
        },
        {
            "killsFactionEndgame": {
                "rank": null,
                "percentile": 97.5,
                "displayName": "BlackTusk Kills",
                "displayCategory": "PvE",
                "category": "pve",
                "metadata": {},
                "value": 74602,
                "displayValue": "74,602",
                "displayType": "Number"
            }
        },
        {
            "rankDZ": {
                "rank": null,
                "percentile": 72,
                "displayName": "DZ Level",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 50,
                "displayValue": "50",
                "displayType": "Number"
            }
        },
        {
            "xPDZ": {
                "rank": null,
                "percentile": 99.3,
                "displayName": "DZ XP",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 710491,
                "displayValue": "710,491",
                "displayType": "Number"
            }
        },
        {
            "timePlayedDarkZone": {
                "rank": null,
                "percentile": 99.9,
                "displayName": "Time Played",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 8797045,
                "displayValue": "2,443h",
                "displayType": "TimeSeconds"
            }
        },
        {
            "roguesKilled": {
                "rank": null,
                "percentile": 99.8,
                "displayName": "Rogues Killed",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 14324,
                "displayValue": "14,324",
                "displayType": "Number"
            }
        },
        {
            "timePlayedRogue": {
                "rank": null,
                "percentile": 99.9,
                "displayName": "Rogue Time Played",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 4951201,
                "displayValue": "1,375h",
                "displayType": "TimeSeconds"
            }
        },
        {
            "timePlayedRogueLongest": {
                "rank": null,
                "percentile": 98.5,
                "displayName": "Rogue Longest Time Played",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 3543,
                "displayValue": "59m 03s",
                "displayType": "TimeSeconds"
            }
        },
        {
            "killsFactionDzBlackbloc": {
                "rank": null,
                "percentile": 98.2,
                "displayName": "Hyena Kills",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 5871,
                "displayValue": "5,871",
                "displayType": "Number"
            }
        },
        {
            "killsFactionDzCultists": {
                "rank": null,
                "percentile": 98.4,
                "displayName": "OutCasts Kills",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 5801,
                "displayValue": "5,801",
                "displayType": "Number"
            }
        },
        {
            "killsFactionDzMilitia": {
                "rank": null,
                "percentile": 98.1,
                "displayName": "TrueSons Kills",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 5805,
                "displayValue": "5,805",
                "displayType": "Number"
            }
        },
        {
            "killsFactionDzEndgame": {
                "rank": null,
                "percentile": null,
                "displayName": "BlackTusk Kills",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
            }
        },
        {
            "killsRoleDzElite": {
                "rank": null,
                "percentile": 99.1,
                "displayName": "Elite Kills",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 19884,
                "displayValue": "19,884",
                "displayType": "Number"
            }
        },
        {
            "killsRoleDzNamed": {
                "rank": null,
                "percentile": null,
                "displayName": "Named Kills",
                "displayCategory": "Dark Zone",
                "category": "darkZone",
                "metadata": {},
                "value": 0,
                "displayValue": "0",
                "displayType": "Number"
            }
        },
        {
            "latestConflictRank": {
                "rank": null,
                "percentile": 93,
                "displayName": "Conflict Rank",
                "displayCategory": "Conflict PvP",
                "category": "conflictPvp",
                "metadata": {},
                "value": 57,
                "displayValue": "57",
                "displayType": "Number"
            }
        },
        {
            "xPPvp": {
                "rank": null,
                "percentile": 92,
                "displayName": "Conflict XP",
                "displayCategory": "Conflict PvP",
                "category": "conflictPvp",
                "metadata": {},
                "value": 477370,
                "displayValue": "477,370",
                "displayType": "Number"
            }
        },
        {
            "timePlayedConflict": {
                "rank": null,
                "percentile": 93,
                "displayName": "Time Played",
                "displayCategory": "Conflict PvP",
                "category": "conflictPvp",
                "metadata": {},
                "value": 126708,
                "displayValue": "35h",
                "displayType": "TimeSeconds"
            }
        },
        {
            "killsBleeding": {
                "rank": null,
                "percentile": 99.3,
                "displayName": "Bleeding Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 20132,
                "displayValue": "20,132",
                "displayType": "Number"
            }
        },
        {
            "killsBurning": {
                "rank": null,
                "percentile": 98.9,
                "displayName": "Burning Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 18661,
                "displayValue": "18,661",
                "displayType": "Number"
            }
        },
        {
            "killsShocked": {
                "rank": null,
                "percentile": 98.3,
                "displayName": "Shocked Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 3932,
                "displayValue": "3,932",
                "displayType": "Number"
            }
        },
        {
            "killsEnsnare": {
                "rank": null,
                "percentile": 98.8,
                "displayName": "Ensnare Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 5108,
                "displayValue": "5,108",
                "displayType": "Number"
            }
        },
        {
            "killsHeadshot": {
                "rank": null,
                "percentile": 99.8,
                "displayName": "Headshot Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 142921,
                "displayValue": "142,921",
                "displayType": "Number"
            }
        },
        {
            "killsWeaponShotgun": {
                "rank": null,
                "percentile": 99.8,
                "displayName": "Shotgun Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 68364,
                "displayValue": "68,364",
                "displayType": "Number"
            }
        },
        {
            "killsWeaponSubMachinegun": {
                "rank": null,
                "percentile": 89,
                "displayName": "SMG Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 5092,
                "displayValue": "5,092",
                "displayType": "Number"
            }
        },
        {
            "killsWeaponMounted": {
                "rank": null,
                "percentile": 69,
                "displayName": "Turret Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 148,
                "displayValue": "148",
                "displayType": "Number"
            }
        },
        {
            "killsWeaponPistol": {
                "rank": null,
                "percentile": 99.8,
                "displayName": "Pistol Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 33042,
                "displayValue": "33,042",
                "displayType": "Number"
            }
        },
        {
            "killsWeaponRifle": {
                "rank": null,
                "percentile": 70,
                "displayName": "Rifle Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 153,
                "displayValue": "153",
                "displayType": "Number"
            }
        },
        {
            "killsWeaponGrenade": {
                "rank": null,
                "percentile": 98.3,
                "displayName": "Grenade Kills",
                "displayCategory": "Kills",
                "category": "kills",
                "metadata": {},
                "value": 975,
                "displayValue": "975",
                "displayType": "Number"
            }
        },
        {
            "itemsLootedPerMin": {
                "rank": null,
                "percentile": null,
                "displayName": "Items Looted/Min",
                "displayCategory": "",
                "category": null,
                "metadata": {},
                "value": 0,
                "displayValue": "0.00",
                "displayType": "NumberPrecision2"
            }
        },
        {
            "killsPvPPerMin": {
                "rank": null,
                "percentile": null,
                "displayName": "PvP Kills/Min",
                "displayCategory": "",
                "category": null,
                "metadata": {},
                "value": 0,
                "displayValue": "0.00",
                "displayType": "NumberPrecision2"
            }
        },
        {
            "killsNpcPerMin": {
                "rank": null,
                "percentile": 15,
                "displayName": "NPC Kills/Min",
                "displayCategory": "",
                "category": null,
                "metadata": {},
                "value": 0.02,
                "displayValue": "0.02",
                "displayType": "NumberPrecision2"
            }
        },
        {
            "playersKilled": {
                "rank": null,
                "percentile": 99.8,
                "displayName": "Players Killed",
                "displayCategory": "",
                "category": null,
                "metadata": {},
                "value": 63690,
                "displayValue": "63,690",
                "displayType": "Number"
            }
        },
        {
            "killsSkillPerMin": {
                "rank": null,
                "percentile": null,
                "displayName": "Skill Kills/Min",
                "displayCategory": "",
                "category": null,
                "metadata": {},
                "value": 0,
                "displayValue": "0.00",
                "displayType": "NumberPrecision2"
            }
        }
    ]
}
```

