---
title: "Turtle Time Game Devlog 1"
date: 2023-04-26T10:16:08-04:00
draft: true
tags:
- gamedev
- programming
- rust
- bevy
- networking
---

Turtle Time is my first attempt at game development. I discovered the [Bevy Engine](https://bevyengine.org/), which is written in [Rust](), and wanted to experiment a little and learn something new outside of my usual backend server programming work.

I started with and took inspiration from some of the Bevy tutorials on YouTube:

1. Logic Projects [Bevy 0.6-0.7 Intro Videos](https://youtube.com/playlist?list=PLT_D88-MTFOOh_S9YifHfo6KETvEmRmYh) series inspired the 2D game idea.
2. Logic Projects [Bevy Intro Tutorials](https://youtube.com/playlist?list=PLT_D88-MTFOPPl75g4WshL1Gx2bnGTUkz) series inspired a little more in-depth menu options and moving enemies and collision detection.
3. Johan Helsing's [Extreme Bevy](https://johanhelsing.studio/posts/extreme-bevy) blog series, which introduced me to [bevy_ggrs](https://github.com/gschup/bevy_ggrs) and [matchbox_server](https://github.com/johanhelsing/matchbox/tree/main/matchbox_server) for peer to peer networking and matchmaking in a battle type game.
4. Jacques [Learn Bevy Engine 0.10 Beginner Tutorial Series](https://youtube.com/playlist?list=PLVnntJRoP85JHGX7rGDu6LaF3fmDDbqyd) which brought me up to speed on more movement, random entity spawns and UI using the more current Bevy `0.10`.
5. NiklasEi's [bevy_game_template](https://github.com/NiklasEi/bevy_game_template) repo got me started with a decent framework with which to layer on my components and systems.

## Template Repo

The `bevy_game_template` repo is a really nice way to start a new Bevy `0.10` project. It comes with everything you need to get started on a new game and maybe some extras that you don't need right away but will come in handy later down the line. 

The things I really appreciated were the GitHub actions for building, testing and linting the project as well as the "deploy to GitHub pages" action that builds a web assembly (WASM) binary and deploys it to the `gh-pages` branch of your repo. Having a game that can be built and distributed via a website in around 12 minutes is invaluable for testing your work, especially on a multiplayer game that you don't want to force people to download and install for each iterative fix.

## Initial Gameplay Loop

Initially I started with quite a few concepts from `Logic Projects` Bevy intro videos for building an RPG type game. I used some of his examples to spawn a 2D arena, spawn a player, a camera to follow that player, movement controls so the player can move around and wall collision checks to keep the player inside the bounds of the basic arena.


![initial concept](initial_concept.png)


## Adding Multiplayer

When searching around for Bevy tutorials I discovered an excellent dev blog series by [Johan Helsing](https://johanhelsing.studio/posts/extreme-bevy) in which he builds a p2p web game in rust with rollback netcode. This sounded very interesting to me, despite being totally over my head at the time. I wanted to try it out.

I followed some of his examples in the [extreme_bevy](https://github.com/johanhelsing/extreme_bevy/tree/part-1) repo to get started. After a little while I had all the pieces in place, but started running into traps for a newcomer when implementing multiplayer systems.

### Struggles of a Noob

1. Most of my initial game was built around a single player - multiplayer games are much different.

First of all there was the problem of spawning multiple players and keeping track of which one is the "local" player. You need to know which player should be controlled by the local inputs and have the camera follow that person.

My initial camera follow system looked like this:
```rust
fn camera_follow(
    player_query: Query<&Transform, With<Player>>,
    mut camera_query: Query<&mut Transform, (Without<Player>, With<Camera2d>)>,
) {
    let player_transform = player_query.single();
    let mut camera_transform = camera_query.single_mut();

    camera_transform.translation.x = player_transform.translation.x;
    camera_transform.translation.y = player_transform.translation.y;
}
```

There are several problems to address when adapting this to a multiplayer game. First the `player_query.single()` line will `panic` if there is more than one player. Second, we have no way to know which player returned in that query is the local player.

In order to make this work I needed to add an optional `LocalHandle` resource to keep track of the local player handle. This can get inserted from 2 systems, either the "local" play `SyncTestSession` or in the online "lobby system" which adds all the peers to a `P2PSession` once they've all connected.


Local Sync Session:
```rust
fn create_synctest_session(commands: &mut Commands, num_players: usize) {
    let mut sess_build = SessionBuilder::<GGRSConfig>::new()
        .with_num_players(num_players)
        .with_max_prediction_window(MAX_PREDICTION)
        .with_fps(FPS)
        .expect("Invalid FPS")
        .with_input_delay(INPUT_DELAY)
        .with_check_distance(CHECK_DISTANCE);

    let mut peer_ids = Vec::new();
    for i in 0..num_players {
        sess_build = sess_build
            .add_player(PlayerType::Local, i)
            .expect("Could not add local player");
        peer_ids.push(PeerId(Uuid::new_v4()))
    }

    let sess = sess_build.start_synctest_session().expect("");

    commands.insert_resource(Session::SyncTestSession(sess));
    commands.insert_resource(LocalHandle(0)); // <-- Set local handle to 0
}
```


