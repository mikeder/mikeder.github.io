---
title: "Jupiter 6 Issues 2022"
date: 2022-03-12T19:41:15-05:00
draft: false
---

Jupiter 6 w/ Europa fails to boot, shows code F6.

Opened it up, reseated all connectors around main boards and problem went away.

Will revist at another time, if its working, its working.



### Update 2022-10-23

The JP-6 was acting up again tonight. At this point I think I'll contact [BellToneSynthWorks](https://belltonesynthworks.com/contact/) in Philadelphia, PA to see if they can help. Before I do that I want to collect my notes on previous attempts to address the issues that have been plaguing this synth since I bought it.

I found an old [VSE thread](https://forum.vintagesynth.com/viewtopic.php?t=96637#p787192) from 12/09/2016 where I was taking a look at the reset circuit in the synth. In the end it seemed the reset was working as it should, but I'm going to copy some excerpts here because some of the pictures are already gone from the thread.

> My Jupiter 6 won't boot sometimes. In checking the CPU reset circuit I found that the duration of the on time is only about 35-40ms. The service notes say that this time should be about 80ms, is this true? Their picture shows the ramp up taking ~20ms and the ON time ~80ms. My whole cycle is done in ~50-55ms.

>  I've replaced C33 and C43 and while the reset duration is a more consistent 40ms ON time. Overall it still seems short, so what else could cause this? OR am I looking in the wrong place?

__Reset Signal Scoped__
![reset-scope](/img/jp6/reset-sig1.jpg)

Other similar threads:

* [Jupiter 6 filter chip failure?](https://forum.vintagesynth.com/viewtopic.php?f=5&t=63476&p=636462#p635698)
    * Post by sqweebking » Mon Aug 01, 2011 10:58 pm
* [My Jupiter 6 seems like its dying..](https://forum.vintagesynth.com/viewtopic.php?f=5&t=75555&p=725836#p725836)
    * Post by sqweebking » Wed May 14, 2014 3:54 pm
* [Remove Europa from Jupiter 6](https://forum.vintagesynth.com/viewtopic.php?f=5&t=96551&p=787025#p786760)
    * Post by sqweebking » Mon Nov 28, 2016 4:37 pm
* [Need help with Jupiter 6 CPU reset circuit](https://forum.vintagesynth.com/viewtopic.php?f=5&t=96637&p=787223#p787192)
    * Post by sqweebking » Fri Dec 09, 2016 3:29 am
* [my jupiter 6 is having pretty weird issues](https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/653154-my-jupiter-6-having-pretty-weird-issues.html)
    * 29th September 2011
* [Jupiter 6 Frozen](https://gearspace.com/board/electronic-music-instruments-and-electronic-music-production/1265717-jupiter-6-frozen.html)
    * 21st May 2019 