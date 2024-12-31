---
title: "Homelab"
date: 2024-12-31T14:12:57-05:00
draft: false
---

## Proxmox Host

* CPU: AMD Ryzen 3 2200G @ 2528 MHz
* Memory: 14GB DDR4 
* Storage:
  * Disks:
    * 1x 120G SanDisk SDSSDA12 (Proxmox LVM boot disk)
    * 2x 1TB WD Black WDC WD1003FZEX-0 (Proxmox ISO/VM storage)
    * 5x 2TB WD Red WDC WD20EFRX-68E (Passthru to Freenas VM)
  * HBA: LSI Logic / Symbios Logic SAS2308 PCI-Express Fusion-MPT SAS-2 (rev 05)

## Virtual Machines

1. Docker
2. FreeNAS/TrueNAS

