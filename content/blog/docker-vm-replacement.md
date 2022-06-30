---
title: "Docker VM Replacement"
date: 2022-01-01T11:23:07-05:00
draft: false
---

Installation notes for replacement of old Debian docker VM.

Trying Alpine linux as a host, just to try something else. I started w/ the Alpine "Standard" install in `sys` mode.

Install and setup of Alpine was easy enough, just boot the ISO image and perform setup. It took a few minutes to get going.
Once the OS was installed I followed the [docs](https://wiki.alpinelinux.org/wiki/Docker) for installing `docker` and `docker-compose`.

Docker installed fine and worked as expected, docker-compose however did not work.

```bash
docker:/home/meder# apk add docker docker-compose
...
docker:/home/meder# docker -v
Docker version 20.10.11, build dea9396e184290f638ea873c76db7c80efd5a1d2
docker:/home/meder# docker-compose --version
Traceback (most recent call last):
  File "/usr/bin/docker-compose", line 33, in <module>
    sys.exit(load_entry_point('docker-compose==1.29.2', 'console_scripts', 'docker-compose')())
  File "/usr/bin/docker-compose", line 22, in importlib_load_entry_point
    for entry_point in distribution(dist_name).entry_points
  File "/usr/lib/python3.9/importlib/metadata.py", line 524, in distribution
    return Distribution.from_name(distribution_name)
  File "/usr/lib/python3.9/importlib/metadata.py", line 187, in from_name
    raise PackageNotFoundError(name)
importlib.metadata.PackageNotFoundError: docker-compose
```

Retrying this with Alpine "Extended" image, resulted in the same broken installation.

Trying again w/ Debian as a base OS.

...

Debian worked as expected, I've since moved on to setting up the usual containers and upgrading my reverse proxy setup to Traefik 2.x.

Airsonic requires host network mode in order for UPnP/DLNA to work. In order for this to work w/ Traefik as a reverse proxy for external access, I had to jump through some hoops to configure traefik routing to the host port for Airsonic.
https://stackoverflow.com/questions/46245684/how-to-get-traefik-to-redirect-to-specific-non-docker-port-from-inside-docker
