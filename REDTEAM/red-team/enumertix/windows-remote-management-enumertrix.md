---
description: Enumerataion of WINRM.
---

# Windows Remote Management Enumertrix

## WIN RM

> Its a windows remote management service which used to access the endpoints.  its used port 5985 for NON ENCRYPTION and port 5986 for ENCRYPTION.
>
> To rnable this service using the powershell&#x20;
>
> `Enable-Psremoting-Force`

### Network Mapper

> Nmap

```
nmap -Pn -p 5985,5987 #TARGETIP
```



### Evil WINRM

```
gem install evil-winrm
evil-rm -i #TARGETIP -u 'username'-p 'password'
```

### BruteForce

### Netexec/CrackMapexec

```
crackmapexec #TARGETIP -u "username.txt" -p "password.txt" -X whoami
```

