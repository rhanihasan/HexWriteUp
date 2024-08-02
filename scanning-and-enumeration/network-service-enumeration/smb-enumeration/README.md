---
description: >-
  smb windows share that can help windows to share files to eachother. Both 139
  and 445 are used for smb.
---

# SMB Enumeration

## Obtaining Information

```bash
nmap -Pn -p 139,443 -A #target-ip
nmap --script smb-enum-* -p 139,445 #Target-IP
nmap --script smb-* -p 139,445 #Target-IP
```

### smbclient

#### Null Session using smbclient

```bash
smbclient -N -L #target-ip
```

* Access using smbclinet

```
smbclient //IP-Address/sharelist/ -U ''
```

### smbmap

* Null Session using smbmap

```bash
smbmap -u '' -p -H #target-ip
smbmap -H #Target-IP
```

* anonymous login / Guest session using smbmap

```
smbmap -u 'anonymous' -p 'anonymous' -H #target-ip
```

### enum4linux

```bash
#Dump interesting information
enum4linux -a [-u "<username>" -p "<passwd>"] <IP>
enum4linux-ng -A [-u "<username>" -p "<passwd>"] <IP>
```



### Crackmap exec

* Baisc Information useing crackmapexec

```bash
crackmapexec smb #Target-IP
```

* For Shares.

```bash
crackmapexec smb #Target-IP --shares
```



### impacket-smbclient

* For Guest Sessions

```bash
impacket-smbclient #username@Target-IP
```

