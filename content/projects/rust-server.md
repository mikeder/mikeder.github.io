---
title: "Rust Server"
date: 2023-10-19T11:51:30-04:00
draft: false
---

Self hosting a Rust dedicated server to learn and screw around on. 
Map wipe schedule may change depending on server performance and force wipe schedule, blueprints will not wipe unless forced by Facepunch.

[![[tS] Iron Oxide | Creative/Free Build/Low Upkeep | Monthly US-E](https://cdn.battlemetrics.com/b/horizontal500x80px/29842867.png?foreground=%23EEEEEE&background=%23222222&lines=%23333333&linkColor=%231185ec&chartColor=%23FF0700)]((https://www.battlemetrics.com/servers/rust/29842867))

## Server Name

- `[tS] Iron Oxide | Creative/Free Build/Low Upkeep | Monthly US-E`

## Wipe Schedule

- Monthly, force wipe - 1st Thursday of the month.

## Wipe Stats

| #   | Start    | End      | Unique Players | Map Info                                 |
| --- | -------- | -------- | -------------- | ---------------------------------------- |
| 1   | 9/21/23  | 10/19/23 | 49             | https://rustmaps.com/map/4250_66972398   |
| 2   | 10/19/23 | 11/02/23 | 50             | https://rustmaps.com/map/3500_1393213226 |
| 3   | 11/02/23 | 12/07/23 | 133            | https://rustmaps.com/map/3700_325381121  |
| 4   | 12/07/23 | 01/04/24 | 210            | https://rustmaps.com/map/3700_132977593  |
| 5   | 01/04/24 | 02/01/24 | 254            | https://rustmaps.com/map/3500_1512592980 |
| 6   | 02/01/24 | 03/07/24 | 679            | https://rustmaps.com/map/3500_1423566289 |
| 7   | 03/07/24 | 04/04/24 | 845            | https://rustmaps.com/map/3500_1684990273 |
| 8   | 04/04/24 | 05/02/24 | 404            | https://rustmaps.com/map/3500_480540019  |
| 9   | 05/02/24 | 06/06/24 | TBD            | https://rustmaps.com/map/4000_38977098   |
| 10  | 11/07/24 | 12/04/24 | 298            | https://rustmaps.com/map/4000_1052569440 |
| 11  | 12/04/24 | TBD      | TBD            | https://rustmaps.com/map/4250_1219710478 |


## Notes

IP change killed the BattleMetrics integration for the [original server](https://www.battlemetrics.com/servers/rust/23805986) on 12/5. The player list under "Most Time Played" capped out at 133 unique players - most of which played for 10 minutes or less.

A [new server](https://www.battlemetrics.com/servers/rust/24761720) was picked up by BattleMetrics and is the current server as of wipe 4.

Wipe 8 "Unique Players" seems to have taken a dive due to BattleMetrics leaderboard rollover, or something. It was a fairly popular wipe, some folks even deciding to team up for next wipe.


Wipe 10 is when I started with the "creative" settings enabled. Most people that joined were confused that there weren't free build plugins and all blueprints unlocked.

### Map Candidates

* https://rustmaps.com/map/4000_1008938238
* https://rustmaps.com/map/3700_132977593 ( Wipe 4 )
* https://rustmaps.com/map/3500_1512592980 ( Wipe 5 )
* https://rustmaps.com/map/3500_1840583110
* https://rustmaps.com/map/4000_2098199338
* https://rustmaps.com/map/4000_38977098
* https://rustmaps.com/map/4250_1219710478

### Creative Mode Notes

Console toggles for creative mode, prefix w/ `sv` if using in the F1 console.

```shell
# Toggle creative mode for all users
creative.allusers 
# Toggle creative mode for a specific user
creative.toggleCreativeModeUser (username)
# Repair structures without consuming resources or waiting for cooldowns. Keep building without interruptions!
creative.freeRepair
# Build structures and upgrade or downgrade them using the Hammer for free. Experiment with different grades of materials effortlessly.
creative.freeBuild
# Place objects without the usual restrictions. Build within building blocked zones, overlap with other objects, and place in TC zones more freely.
creative.freePlacement
# Unlimited IO line points. Extend wiring distances up to 200m and utilize a new invisible color option on the color wheel.
creative.unlimitedIo
```

### Custom Settings


`~/serverfiles/server/rustserver/cfg/server.cfg`

```shell
#  A text description of your server. For a new line add:  \n
server.description "Free build, low upkeep and otherwise vanilla server. \n Craft building plan and hammer so you can build and upgrade for free. \n TC is still required if you don't want your base to decay! \n Once crafted or found, deployables are unlimited! \n Wipes first Thursday of every month."

# A URL to the image which shows up on the server details screen (dimensions are 512x256).
server.headerimage "https://git.io/JYdmK"

# The URL to your servers website.
server.url "https://linuxgsm.com/"

# Slower Decay
decay.upkeep_period_minutes 7200 # default 1440

# Creative Mode
creative.allusers true
creative.freeBuild true
creative.freeRepair true

# Tags are additional bits of information that describe Rust servers.
# Up to three of them will be displayed on the Rust server browser and filtering will be supported one day.
# Supported Tags can be found here:
# https://wiki.facepunch.com/rust/server-browser-tags
server.tags monthly,vanilla,NA,rs0003e0rAi4000/q
```