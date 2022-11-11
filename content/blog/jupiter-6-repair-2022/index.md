---
title: "Jupiter 6 Repairs 2022"
date: 2022-11-09T19:48:40-05:00
draft: true
tags:
- Vintage
- Synthesizer
- Repair
---

I've begun to address the [issues](/blog/jupiter-6-issues-2022) with my Jupiter 6 so I figured I'd start a new post to write specific to this repair attempt. Also to note, this synth has previously been serviced by Pi Keyboards & Audio Inc in Cleveland Ohio (216)-741-2211 and its serial number is 322280. ~~I'll have to try contacting them to see if they still have a record of what was done previously.~~ Looks like they're gone, possibly went out of business in 1992. 

Since I had already confirmed the PSU and all the power rails to be within spec, I decided to move forward with replacing these apparently problematic capacitors.

I bought replacement ceramic caps from Digi-Key to replace the orange polystyrene caps in the VCO and VCF circuits.

| Index | Quantity | Part Number     | Manufacturer Part Number | Description                    | Unit Price | Extended Price |
| ----- | -------- | --------------- | ------------------------ | ------------------------------ | ---------- | -------------- |
| 1     | 40       | 445-180761-1-ND | FA28C0G2E331JNU06        | CAP CER 330PF 250V C0G RADIAL  | 0.26300    | $10.52         |
| 2     | 18       | 445-173558-1-ND | FG28C0G2E102JNT06        | CAP CER 1000PF 250V C0G RADIAL | 0.23300    | $4.19          |
|       |          |                 |                          |                                |            |

Here are the locations of these caps on the 2 and 4 voice boards within the JP6:

__Two Voice Board__
![2 voice board](JP6-two-voice-board.jpeg)

__Four Voice Board__
![4 voice board](JP6-four-voice-board.jpeg)

## Factory Board Mods

Once I had the voice boards out I found there had been a couple, apparently factory, board modifications made. The [service manual](https://www.synthxl.com/wp-content/uploads/2018/02/Roland-Jupiter-6-jp6-Service-Manual.pdf) describes a "Reducting LFO leakage" countermeasure where a trace is cut and bypassed with a piece of wire.

> LFO leakage can be audible with VCA LFO at 10. 
> This preventative modification is at the factory with SN 301700. This modification is also effective on early products.
> Related pattern areas remain the same, even PCBs revised.

![lfo leakage mod](JP6-LFO-leakage-mod.png)

__Two Voice Board Mods__
![2v-mods](JP6-two-voice-mods.jpeg)

__Four Voice Board Mods__
![4v-mods](JP6-four-voice-mods.jpeg)

The second board modification was a 330Ω resistor between pin 9 of IC16 and pin 4 of IC23 (2v and 4v) and pin 9 of IC18 and pin 4 of IC25 (4v). The 4 voice board also has a jumper on VCO 2 between pin 1 of RA-5A and pin 10 of IC36A (CEM 3340).

## Replacing the caps

Removing the old caps from these boards was a little tricky, it took a combination of vacuum de-soldering and solder wicking braid to get them out. I had to be especially careful in the VCO section as the board is pretty densely populated with parts literally touching each other. There are also the original CEM 3340 VCO chips in this section that I had to be careful not to overheat. Overall it took about 3hrs to get all the old caps out and get the pads cleaned up in prep for soldering the new caps in. I managed to get them all removed w/o damaging any of the reportedly fragile solder pads, which was great.



[Link to previous issues post](/blog/jupiter-6-issues-2022)


