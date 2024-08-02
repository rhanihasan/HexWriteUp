---
description: its help and used for remote management system.
---

# RPC Client

## rpcclient

* Null session using rpc client

```bash
rpcclient -U "" -N #Target-IP
```

* User session using rpc client

```bash
rpcclient -U "username" -N #Target-IP
```

## Impacket

* there are many tools in <mark style="color:orange;">impacket rpd dump</mark> and <mark style="color:orange;">rpc map</mark>.

#### Impacket-rpcmap

```bash
impacket-rpcmap ncacn_ip_tcp:(target-ip)[135]
impacket-rpcmap ncacn_http:(target-ip)[593]
impacket-rpcmap ncacn_np:(target-ip)[\pipe\spoolss]
```

#### Impacket-rpcdump

* Null Session

```
impacket-rpcdump (username) ""@(target-ip)
```

* Guest Sessions

```bash
impacket-rpc "username"@(target-ip)
```

