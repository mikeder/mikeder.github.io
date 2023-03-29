---
title: "How to Alert"
date: 2023-01-26T08:31:59-05:00
draft: true
---

1. Define SLI's and SLO's
   1. We have to define what is successful operation of the service. Burger World example:
      1. Burger World has 3 main objectives:
         1. Serve customer orders at drive through in 3min or less
         2. Serve customer orders at walk up counter in 5min or less
         3. Less than 1% of orders result in corrective action
      2. First assume that all other operations are working as designed, we only monitor and alert on deviations from the primary objectives.
2. Monitor for the success or failure to meet those definitions
3. Alert on deviation from agreed upon SLO's
4. Identify root cause of deviations
5. Write KB's for how to address root cause of deviations
6. Create new alerts for root cause
7. Repeat.