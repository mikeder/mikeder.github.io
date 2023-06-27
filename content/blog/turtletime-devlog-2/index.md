---
title: "Turtletime Devlog 2"
date: 2023-06-26T09:24:43-04:00
draft: true
---


Topics for future:

* Tearing down peer-to-peer sessions without panic.
* Multiple game state states, how to control flow and run conditions.
* Despawning SyncTestSession rollback components.
* Finding sources of non-deterministic entity handling
  * hash all rollback components
  * run sync test
  * ordered round cleanup
* Adding the first NPC
* rollback audio


## Rollback Audio

Initial implementation tried to use events to trigger playing sounds, but this lead to multiple sounds being played/overlayed on top of each other due to rollbacks.


Original implementation ideas - https://github.com/mwbryant/rpg-bevy-tutorial/blob/tutorial7/src/audio.rs

_audio.rs_
```rust
pub struct FireballShotEvent;

fn play_fireball_shot_sound(
    audio: Res<AudioChannel<SFXChannel>>,
    audio_assets: Res<AudioAssets>,
    mut fireball_shot_event: EventReader<FireballShotEvent>,
) {
    if fireball_shot_event.iter().count() > 0 {
        audio.play(audio_assets.fireball_shot.clone());
    }
}
```

Johan blog post on mitigations - https://johanhelsing.studio/posts/cargo-space-devlog-4
