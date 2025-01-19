---
description: Enumearation on SMTP Protocol which mostly used in EMAILs.
---

# SMTP Enumeratrix

## SMTP

> **SMTP (Simple Mail Transfer Protocol)** is a TCP/IP protocol used in **sending** and receiving **e-mail**.
>
> However, since it has limitations of queue/waiting  messages at the receiving end, it is usually used with  other protocols, POP3 or IMAP, These protocols allow users to save messages in a server mailbox and download them according . This combination of protocols is commonly referred to as a "draft."
>
> &#x20;
>
> More Details in website….
>
> &#x20;
>
> SMTP functions as a client-server-based protocol, enabling it to fetch and send emails. In other words, users typically utilize a program that employs SMTP for sending emails and either POP3 or IMAP for receiving emails.
>
> SMTP servers usually operate on ports 25, 465, or 587.
>
> The primary functions of an SMTP server include preventing spam through authentication and allowing authorized users to send emails.
>
> Most SMTP servers also support the protocol extension known as ESMTP with SMTP-Auth.
>
> &#x20;
>
> When a user sends an email, the SMTP client (also known as the Mail User Agent or MUA) converts the email into a header and a body and uploads both to the SMTP server. The server, acting as a Mail Transfer Agent (MTA), checks the email for size and spam and then stores it. Sometimes, a Mail Submission Agent (MSA) is employed before the MTA to validate the content of the email, (Example: that the mail is genuine form client, the origin of the e-mail). ensuring its authenticity and origin. The MSA is also known as a Relay server. Correct configuration of these servers is crucial as many SMTP servers are vulnerable to Open Relay Attacks if improperly configured. This process works the same way for both the sender and the receiver.
>
> The MSA and MTA can be likened to a post office and are hosted on vendor servers, similar to how applications and software are hosted.
>
> On the receiver's server end, once the MSA and MTA processes are validated, the email is pushed or sent to the receiver's Mail User Agent (MUA) via POP3 or IMAP.
>
> When the client's mailbox receives the email, POP3 deletes the email from the server end. On the other hand, IMAP stores the original email on the server and sends a copy of the email to the client's mailbox

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">SMTP</td><td valign="top">POP</td><td valign="top">IMAP</td></tr><tr><td valign="top">Simple Mail Transfer Protocol</td><td valign="top">Post Office Protocol</td><td valign="top">Internet Message Access Protocol</td></tr><tr><td valign="top">Send Mail /(Push Mail)</td><td valign="top">Retrieve mail (POP mail)</td><td valign="top">Retrieve Mail (POP Mail)</td></tr><tr><td valign="top">Port No 25</td><td valign="top">Default Port No is 110 &#x26; SSL 995</td><td valign="top">Default Port No is 143 &#x26; SSL 993</td></tr><tr><td valign="top">Default is TCP Or UDP</td><td valign="top">Default is TCP Or UDP</td><td valign="top">Default is TCP Or UDP</td></tr></tbody></table>



> Client (MUA) A Submissions Agent (MSA) A Open Relay (MTA) A Mail Delivery Agent (MDA) A Mail Box (POP3/IMAP)

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top">Command</td><td valign="top">Description</td></tr><tr><td valign="top">AUTH PLAIN</td><td valign="top">AUTH is a service extension used to authenticate the client.</td></tr><tr><td valign="top">HELO</td><td valign="top">The client logs in with its computer name and thus starts the session.</td></tr><tr><td valign="top">MAIL FROM</td><td valign="top">The client names the email sender.</td></tr><tr><td valign="top">RCPT TO</td><td valign="top">The client names the email recipient.</td></tr><tr><td valign="top">DATA</td><td valign="top">The client initiates the transmission of the email.</td></tr><tr><td valign="top">RSET</td><td valign="top">The client aborts the initiated transmission but keeps the connection between client and server.</td></tr><tr><td valign="top">VRFY</td><td valign="top">The client checks if a mailbox is available for message transfer.</td></tr><tr><td valign="top">EXPN</td><td valign="top">The client also checks if a mailbox is available for messaging with this command.</td></tr><tr><td valign="top">NOOP</td><td valign="top">The client requests a response from the server to prevent disconnection due to time-out.</td></tr><tr><td valign="top">QUIT</td><td valign="top">The client terminates the session.</td></tr></tbody></table>



### Network Mapper

> DIG

```
dig +short mx google.com
nmap -Pn -n -sV -sC -p 35 #targetip
```

<figure><img src="../../.gitbook/assets/image (20).png" alt=""><figcaption></figcaption></figure>

> NSE

```
nmap -Pn -n -sV -sC=smtp*.nse -p 35 #targetip
```

<figure><img src="../../.gitbook/assets/image (21).png" alt=""><figcaption></figcaption></figure>

### BruteForce

> Hydra

```
hydra -L username.txt -P password.txt smtp-enum://#TARGETIP
```

