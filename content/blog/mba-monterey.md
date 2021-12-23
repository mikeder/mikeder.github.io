---
title: "MBA Monterey"
date: 2021-12-07T21:55:33-05:00
draft: false
---

Issues after upgrading my 2020 Macbook Air (m1) to macOS Monterey:

1. Battery life went to shit, have to enable low power mode on battery.
2. Bitwig and SoundCraft MTK 12 mixer no longer cooperate.

![Initial Version](/img/monterey-ver-1201.png#float-right)

Issue #1 I don't have a whole lot of evidence to support but it did feel like the battery life on my brand new Macbook Air M1 had gotten a lot worse after the upgrade to Monterey (12.0.1). Previously I could use the laptop for several days without reaching for the charger, now it seems the battery percentage was dropping several percent every few minutes.

Issue #2 really bothered me. One of the main reasons for getting a new laptop was to use in my synthesizer studio, for recording purposes. If my main audio interface, a SoundCraft MTK 12 mixer, was no longer recognized, it would defeat the purpose of the shiney new Mac. 

![Bitwig Missing I/O](/img/bitwig-device-missing.png)

At first it seemed maybe core audio or core services weren't installed right, or maybe Rosetta 2 wasn't working properly. The version of Bitwig that I own doesn't run natively on Apple silicon, so it requires Rosetta for Intel CPU emulation. ![Bitwig Missing I/O](/img/bitwig-kind-intel.png#float-left) I tried reinstalling Bitwig first, that had no effect. Then I tried reinstalling Rosetta 2, which kept giving me errors but still reported as being installed successfully. 

Finally, I just reinstalled MacOS itself, luckily this was a simple affair; just continue holding the power button on the laptop while turning it on, until a gear icon shows up. You can then navigate to a menu to perform a reinstall, which left all of my programs and stuff in place. 

After the reinstall I tried Bitwig again, at first it seemed the problem persisted but after a disconnect/reconnect of the USB cable to the mixer, things started working again! The mixer was recognized as unplugged and replugged and magically all the inputs and outputs came back as routing options. I swear I unplugged and replugged the mixer several times before attempting any of the above, so I blame MacOS. 
