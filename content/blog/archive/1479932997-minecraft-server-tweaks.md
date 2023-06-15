---
title: Minecraft Server Tweaks
date: 2016-11-23 20:29:57
updated: 2016-11-23 16:05:01
categories:
- archive
tags:
- archive
draft: false
---

* Cache Proxy in front of [https://mc-map.sqweeb.net](https://mc-map.sqweeb.net)
    * Add another 32g disk to the proxy VM - proxy-02
    * Format, make file system and mount new disk at /mnt/cache/
    * Add line to /etc/fstab to mount disk on boot:
    ```bash
    /dev/vda1 /mnt/cache ext4 defaults 0 2
    ```
    * Add the following snippet to /etc/nginx/snippets/proxy-defaults.conf:
    ```bash
    proxy_cache_path /mnt/cache levels=1:2 keys_zone=my_cache:10m max_size=20g inactive=60m;
    ```
    * Update /etc/nginx/sites-available/mc-map.sqweeb.net to use the cache:
    ```bash
    server {
                 ...
                 proxy_cache my_cache;
                 proxy_cache_valid 200 302 10m;
                 add_header X-Cache-Status $upstream_cache_status;
                 ...
    }
    ```

* Reduce dynmap update/render interval from every 1s to every 5s.
* Restrict number of tile updates to 1 at a time.
    * Edit plugins/dynmap/configuration.txt:
    ```bash
        # How often a tile gets rendered (in seconds).
        renderinterval: 5
        # How many update tiles to work on at once (if not defined, default is 1/2 the number of cores)
        tiles-rendered-at-once: 1
    ```    

* Move dynmap data to separate disk.
* Move archive/ and backup/ directories to separate disk.
    * Add another 60g disk to minecraft-01 VM
    * Format, create file system and mount disk at /mnt/mcdata/
    * Add line to /etc/fstab to mount disk on boot:
    ```bash
    /dev/vda1 /mnt/mcdata ext4 defaults 0 2
    ```
    * Copy existing archives, backups and dynmap data to new disk
    * Set permissions on /mnt/mcdata/
    ```bash
    root@minecraft-01 mnt$ chown -R mc:mc mcdata/
    ```
    * Remove original archive/, backup/, and dynmap data directories
    * Create symlinks to new directories on separate disk...