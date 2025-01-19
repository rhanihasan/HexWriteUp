---
description: In this HTTP/S Service is being Enumerated
---

# HTTP/S Enumeratrix

## HTTP/s

> Mostly Website used the HTTP/S Services so the identification & Scanning is common.

### Network Mapper

```
nmap -n -Pn -p 80,443 
nikto -host 
```

### Directory Enumeration

{% code overflow="wrap" %}
```
gobuster dir -u https://netplace.in -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt

gobuster fuzz -u https://netplace.in/FUZZ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt

gobuster fuzz -u https://FUZZ.bcg.com -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt

ferobuster 

```
{% endcode %}

DNS Enumeration

> Its will NSLOOKUP on MASS amount.

{% code overflow="wrap" %}
```
gobuster dns -d netplace.in -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt  
```
{% endcode %}

### Vhost Enumeration

> Vhost as the name say it will brute on http host hearder  the website or url of http does not change however the host hearder changes to or toughly whatever to wordlist
>
> VHOST(Virtual Host) refers to the practice of running more than one website (such as company1.example.com and company2.example.com) on a single machine.
>
> There are mainly 2 types of Virtual hosts:
>
> * &#x20;**IP-based Virtual Host:**
>   * In IP-based Virtual Host, we have different IP addresses for every website.
> * **Name-based Virtual Host:**
>   * In named-based Virtual Host, several websites are hosted on the same IP. Mostly this type is widely and preferred in order to preserve IP space.
>
> But when talking about VHOST we are generally talking about **Named-based Virtual hosts.**
>
> How does this actually work?
>
> Now, you would be confused about how will the webserver differentiate to which website it has to send my requests since many websites are being hosted on the same server with the same IP.
>
> It's through the "**Host header**". The web server identifies which content to serve up once it receives the Host header from the client.

{% code overflow="wrap" %}
```
gobuster vhost -u http://192.168.50.124 -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-small.txt  
```
{% endcode %}

<figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>

**Author**: [SpiderLabs](https://github.com/SpiderLabs)

**Language**: Python

Installation:

```
git clone https://github.com/SpiderLabs/HostHunter.git
pip3 install -r requirements.txt
Running:
python3 hosthunter.py ip_addresses.txt

```

### Nuclie

> Its a great tools from Project Discovery

```
nuclei -ntv -u 
```

