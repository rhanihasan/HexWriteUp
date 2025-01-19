# WEB SECURITY (WEB INVENTORY)

## WEB

> 1. is Hacking a system from Trojan.
> 2. A Vulnerable Services.
> 3. A Vulnerable Web Application of the system.

> A Software service publicly hosted over WAN.
>
> Client browsers communicate via frontend language HTML, CSS, JavaScript.
>
> The frontend Language will communicate with the backend language like JAVA, REACT, PHP, SQL, and more.
>
> Then it goes so server operating system which are Linux & Windows based.
>
> The server will response to the request and from backend to frontend then the frontend response to client browser.

## &#x20;OWASP (Open Web Application Security Project)

> * It a non-profit organization which realize the TOP 10 most targeted web application Vulnerability Tree (Umerabla) over the world during the 4-year tenure.&#x20;
> * its spread awareness and contribute to the security community

{% hint style="info" %}
* OWASP updates after 4 years as pre technology and security evolve, and Ranking are based on impact.
* Auditors also used OWASP as a prerequisetes.


{% endhint %}

* Github Cheatsheet
  * link: [https://cheatsheetseries.owasp.org/](https://cheatsheetseries.owasp.org/)

### OWASP TOP 10 2017

<table data-header-hidden><thead><tr><th width="89"></th><th width="495"></th><th></th></tr></thead><tbody><tr><td>Tops</td><td>Details</td><td>Roles</td></tr><tr><td>1.</td><td>Injection<br>(The software code is injected and execute.)</td><td>Types</td></tr><tr><td>2.</td><td>Broken Authentication<br>(Broken the confidentiality)</td><td>Types</td></tr><tr><td>3.</td><td>Sensitive data exposure<br>(the valuable data exposed to internet)</td><td>Types</td></tr><tr><td>4.</td><td>XML External Entities<br>(XML used in HTTP Header)</td><td>Vulnerabilities</td></tr><tr><td>5.</td><td>Broken Access Control<br>(A User is authenticated and has unnecessary access.)</td><td>Types</td></tr><tr><td>6.</td><td>Security Misconfiguration<br>(As a security engineer I have made a lot of mistakes like configure the policy without testing the policy.)</td><td>Types</td></tr><tr><td>7.</td><td>Cross Site Scripting <br>(Input malicious JavaScript code which results in comprised the system.)</td><td>Types</td></tr><tr><td>8.</td><td>Insecure Deserialization <br>(The data packet is tamper from the client side and the server didn't validate.)</td><td>Types.</td></tr><tr><td>9.</td><td>Using Component with known Vulnerabilities<br>(All the common vulnerability comes under this.)<br></td><td>Types.</td></tr><tr><td>10.</td><td>Insufficient Logging and monitoring<br>(The logs and monitoring resources are unavailable)</td><td>Types</td></tr></tbody></table>

{% hint style="info" %}
**Ice Breaks Security, X-ray Breaks Security, Cats Ignore Useful Information.**
{% endhint %}

### OWASP Top 10 2021

<table data-header-hidden><thead><tr><th width="89"></th><th width="288"></th><th width="271"></th><th></th></tr></thead><tbody><tr><td><strong>Tops</strong></td><td><strong>Details</strong></td><td><strong>Roles &#x26; Referred by OWASP Top 2017</strong></td><td><strong>Current</strong></td></tr><tr><td>1.</td><td>Broken Access Control<br>(A user is authenticated, and unnecessary privilege is given)</td><td>It's a type Referred by 2017 top 5</td><td></td></tr><tr><td>2.</td><td>Cryptographical Failover<br>(Weak Encryption is used)</td><td>It's a type Referred by 2017 top 3</td><td></td></tr><tr><td>3.</td><td>Injection<br>(Inject the software code and used the command an unintended way to comprise the system)</td><td>It's a type Referred by 2017 top 1</td><td></td></tr><tr><td>4.</td><td>Insecure Design<br>(Cost cutting design which increase the risk factor)</td><td>It's a type Referred by 2017 top 5</td><td>New</td></tr><tr><td>5.</td><td>Security Misconfiguration<br>(I have an this mistake a lot like create a policy and forget to test)</td><td>It's a type Referred by 2017 top 6</td><td></td></tr><tr><td>6.</td><td>Vulnerability &#x26; Outdated Components<br>(all the Common vulnerability used in this)</td><td>It's a type Referred by 2017 top 9</td><td></td></tr><tr><td>7.</td><td>Identification &#x26; Authentication Failure<br>(A user is authenticated and have unnecessary privileges)</td><td>It's a type Referred by Broken Access Control, 2017 top 5</td><td></td></tr><tr><td>8.</td><td>Software &#x26; Data Integrity Failure<br>The data is tamper form the client side and the server didn't validate)</td><td>It's a type Referred by 2017 top 8</td><td>New</td></tr><tr><td>9.</td><td>Security Logging &#x26; Monitor Failure<br>(less resources for logging and monitoring)</td><td>It's a type Referred by 2017 top 10</td><td></td></tr><tr><td>10.</td><td>Service-Side Request Forgery<br>(the server will be the mediatory for the vulnerably server)</td><td>[The Server will be the middleman between External server through Attacker] it's a Vulnerability</td><td>New</td></tr></tbody></table>

{% hint style="info" %}
Broken Cat Ignore Insecure Security Vulnerability Its Secure Seriously Secure
{% endhint %}

## Web Based Exploit

> Web based exploit means finding loopholes in the web application and compromised the system.
>
> * There are two types of Vulnerabilities
>   * Client-side Vulnerability.
>     * A Clinet browser is exploited with malicious code&#x20;
>   * Server-side Vulnerability.
>     * Vulnerably server is exploited.
>     *



