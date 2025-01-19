---
description: In this Secure Shell Service is being Enumerated.
---

# Secure Shell Enumeratrix

## Secure Shell&#x20;

> SSH is a CLI (Commands line interface )  it provide same serves as talent but it secure and telnet is not secure.
>
> SSH has a feature of Public key & Private Key both keys are created with the help of ssh cmd to machine or server etc
>
> Both entities share they public key to each other & encrypt packet using private key and Decrypt packet using each others public keys.
>
> its works on Port Number 22

### Network Mapper

```
nmap -n -Pn -p 22 #TARGETIP
nmap -n -Pn -p 22 --script=ssh-*.nse #TARGETIP
```

### BruteForce

```
ncrack -v -U username.txt -P password.txt 192.168.50.124:22
```

