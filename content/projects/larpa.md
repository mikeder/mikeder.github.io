---
title: "LARPA"
date: 2024-08-01T20:17:42-04:00
draft: true
---

Building an MMORPG, because thats an easy and sane thing to do for a solo dev - right?

## First Try:

* Rust
* Bevy
* Lightyear
* Procgen World
* Multiplayer Projectiles

I made decent progress on the procedural generation, inspired by early Mythfall (UnitOfTime) videos. I added some random trees, rocks, zombies and prefab structures with collisions. Added basic multiplayer, networked projectiles, map download. Beyond that though, there was no gameplay. I got hung up on the multiplayer networking, prediction, rollback, reconciliation and couldn't quite get 2 or more players to behave properly. So I gave up on this attempt.

## Second Try:

* Go
* Ebitengine
* Donburi ECS
* NECS Networked ECS

I'm way more familiar with Go than I am Rust so I figured I'd check out a popular 2d game engine. I got roughly as far along as the first attempt but again hung up on performant networking of entities. I like the added ECS pattern and networked entities in theory, but again I struggled to get much happening in game without it lagging into oblivion. So I gave up on this attempt, too.

## Third Try:

* Godot + GDScript
* Netfox
* Kenney Assets

Godot is a fully featured, modern, open source, game engine. Its really good and easy to use. After starting with "code only" engines it is a very different workflow but it allows you to get up and going and do pretty complex things pretty effortlessly. Once you get the hang of scripting and wiring up scenes you can quickly feel like you're building an actual game rather than just moving things on the screen. I also toiled with network code in Godot for a bit, but once I found Netfox I largely set and forget my replication and syncronization systems.
  
