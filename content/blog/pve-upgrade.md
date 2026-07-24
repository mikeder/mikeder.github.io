---
title: "Pve Upgrade"
date: 2026-06-23T21:56:19-04:00
draft: true
---

In place upgrade of Proxmox VE node from 5.4 to 8 something.


Upgrade Debian `bullseye` -> `bookworm`


Update `apt` sources lists releases
```bash
sed -i 's/bullseye/bookworm/g' /etc/apt/sources.list
sed -i 's/bullseye/bookworm/g' /etc/apt/sources.list.d/*.sources
```

Update and upgrade, fix shit in place

```bash
apt update && apt-upgrade


mv /etc/kernel/postinst.d/zz-pve-efiboot ~
```



References:
https://forum.proxmox.com/threads/problems-after-upgrading-from-6-x-to-7-4-3.125079/
https://forum.proxmox.com/threads/problems-after-6-to-7.131754/