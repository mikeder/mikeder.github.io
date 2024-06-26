---
title: Minecraft Status
date: 2020-03-16 21:05:48
updated: 2020-04-02 20:49:56
categories:
- archive
tags:
- archive
draft: false
---

I spent the better part of the day yesterday working on a Minecraft status checker package for the site. The Minecraft query protocol is somewhat tricky to implement for a novice like me but apparently it changes a bit when there are plugins involved on the server. I'll update this post later with some of my findings.

For now, there is a neat, albeit somewhat basic status page [here](https://sqweeb.net/minecraft)

Well, I tried to update this post but apparently my token went invalid while I was typing it and I lost it all when I hit "Save". I'll have to increase the JWT expiry on this server before I attempt another "large" entry update like that :(
    
Edit: 4/2/2020
OK, I've added some auth token refresh handling to the server and front end so I can stay logged in without issue now. I've also abandoned my own implementation of the Minecraft query protocol and decided to use a package I found on GitHub called [go-mc](https://github.com/Tnze/go-mc)

This package uses the latest protocol and has a lot nicer encapsulation around packet encoding and localization that I was too lazy to bother with. It also has a much larger portion of the API implemented so I could potentially write a bot to do some player level interaction in the future. For now though, I've updated the `/minecraft` API on this server to use the new package and also keep track of players that have joined the server. Player names, uuid's, "first seen" and "last seen" time stamps are now recorded in the database. I may expand on this to include play time calculations and other fun stuff.

I've updated the `/minecraft` page to show which players are currently online, as well as changed the "Server Highlights" from cards to a carousel display. That should do it for this entry, I'll probably start a new one for further updates to the backend stuff.
