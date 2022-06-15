---
title: Go Rewrite - Load
date: 2020-01-30 01:00:38
updated: 2020-01-29 22:16:55
categories: ["Archive"]
draft: true
---

# GOMAXPROCS=2

```bash
meder@devb0x:wrk$ wrk http://localhost:3000 -c 100 -d 15s -t 4
Running 15s test @ http://localhost:3000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    37.13ms   45.17ms 398.89ms   84.51%
    Req/Sec     1.13k   226.65     1.99k    71.67%
  67708 requests in 15.01s, 289.02MB read
Requests/sec:   4511.45
Transfer/sec:     19.26MB
```

# GOMAXPROX=4

```bash
meder@devb0x:wrk$ wrk http://localhost:3000 -c 100 -d 15s -t 4
Running 15s test @ http://localhost:3000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    24.82ms   30.69ms 280.80ms   85.86%
    Req/Sec     1.68k   253.46     2.62k    68.50%
  100112 requests in 15.01s, 427.07MB read
Requests/sec:   6669.38
Transfer/sec:     28.45MB
```

# GOMAXPROCS=8


```bash
meder@devb0x:wrk$ wrk http://localhost:3000 -c 100 -d 15s -t 4
Running 15s test @ http://localhost:3000
  4 threads and 100 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    27.39ms   32.98ms 378.54ms   86.09%
    Req/Sec     1.41k   203.20     2.14k    68.00%
  84139 requests in 15.02s, 358.94MB read
Requests/sec:   5600.43
Transfer/sec:     23.89MB
```

# GOMAXPROCS=4 == Max RPS

```bash
meder@devb0x:wrk$ wrk http://localhost:3000 -c 150 -d 15s -t 4                                                      
Running 15s test @ http://localhost:3000
  4 threads and 150 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    36.57ms   45.55ms 492.70ms   85.83%
    Req/Sec     1.68k   282.89     2.67k    66.00%
  100559 requests in 15.02s, 428.98MB read
Requests/sec:   6695.12
Transfer/sec:     28.56MB
```

# ways 2 fail

1. Too many open connections to the database.

```log
2020/01/29 20:11:56 getting posts from database: Error 1129: Host `'devb0x.tsnet' is blocked` because of many connection errors; unblock with 'mysqladmin flush-hosts'
```

```bash
mysql> FLUSH HOSTS;
Query OK, 0 rows affected (0.00 sec)
```

```log
2020/01/29 20:13:17 getting posts from database: dial tcp 192.168.2.109:3306: socket: `too many open files`           
2020/01/29 20:13:17 open ./templates: too many open files
```

```go
db.SetMaxOpenConns(10)
db.SetMaxIdleConns(2)
```

# GOMAXPROCS=4 + 50 clients 4 threads with db hits

Hitting the `/blog` endpoint, which loads 40 posts from the database.

```bash
meder@devb0x:globber$ wrk http://localhost:3000/blog -c 50 -d 15s -t 4                                              
Running 15s test @ http://localhost:3000/blog
  4 threads and 50 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    79.80ms   78.68ms 683.00ms   87.42%
    Req/Sec   184.35     36.49   320.00     70.17%
  11029 requests in 15.02s, 0.98GB read
Requests/sec:    734.41
Transfer/sec:     66.82MB
```

A slew of mostly harmless errors...

```log
2020/01/29 21:46:50 getting posts from database: context canceled
2020/01/29 21:46:50 [devb0x/ReRgRtMjxy-066573] "GET http://localhost:3000/blog HTTP/1.1" from [::1]:33706 - 200 8192B in 31.62011ms
2020/01/29 21:46:50 http: superfluous response.WriteHeader call from github.com/go-chi/chi/middleware.(*basicWriter).WriteHeader (wrap_writer.go:74)
2020/01/29 21:46:50 [devb0x/ReRgRtMjxy-066580] "GET http://localhost:3000/blog HTTP/1.1" from [::1]:33704 - 200 8192B in 18.819665ms
2020/01/29 21:46:50 getting posts from database: driver: bad connection                                             
2020/01/29 21:46:50 [devb0x/ReRgRtMjxy-066577] "GET http://localhost:3000/blog HTTP/1.1" from [::1]:33742 - 200 2889B in 26.299548ms
2020/01/29 21:46:50 write tcp [::1]:3000->[::1]:33696: write: broken pipe                                           
2020/01/29 21:46:50 http: superfluous response.WriteHeader call from github.com/go-chi/chi/middleware.(*basicWriter).WriteHeader (wrap_writer.go:74)
2020/01/29 21:46:50 [devb0x/ReRgRtMjxy-066580] "GET http://localhost:3000/blog HTTP/1.1" from [::1]:33704 - 200 8192B in 18.819665ms
```

After adding some pagination and post/page limit:

```bash
meder@devb0x:globber$ wrk http://localhost:3000/blog -c 30 -d 15s -t 4
Running 15s test @ http://localhost:3000/blog
  4 threads and 30 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency     9.60ms   10.39ms 157.32ms   92.23%
    Req/Sec     0.88k    84.10     1.09k    68.83%
  52861 requests in 15.01s, 695.23MB read
Requests/sec:   3521.95
Transfer/sec:     46.32MB
```
