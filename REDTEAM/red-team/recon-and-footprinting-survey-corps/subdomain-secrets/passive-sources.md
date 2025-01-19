# Passive Sources

## <mark style="color:green;">Passive Recon</mark>

#### What is passive subdomain enumeration? <a href="#what-is-passive-subdomain-enumeration" id="what-is-passive-subdomain-enumeration"></a>

> Passive subdomain enumeration is a method to search for domain data using databases from services like

{% hint style="info" %}
Don't trust the passive information Because it open to internet for some logical reasons.
{% endhint %}

### <mark style="color:blue;">Whois Lookup</mark>

**Purpose:** Find information about who owns a domain.\
**How it works:** Domain owners provide contact details upon registration, stored in a public database.\
**Usage:** `whois example.com`

**Its help to gather the information based on domain.**

**How the whois get the information of Domian because when the target Regester with domain vendors it must provide some information/details to authority. And they will available this information public as they use this method of advertisement unless and until buy the premium subscription**

**Register whois server is where the whois get the information of domain.**

{% code title="Syntax: whois" %}
```
whois <name><.in><.com><.etc>
```
{% endcode %}

| **The premium subscription: REDACTED FOR PRIVACY information marketing also: GoDaddy sell domain** | **The premium non-subscription gets the** |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------- |

![Different-bw-securitnonsecurit-plain](<../../../.gitbook/assets/3 (2).png>)

* &#x20;**Use various information from this Updated Date and try to buy before the original target did.**

| **This is Known as Security Plan.** | **This is not a Security Plan.** |
| ----------------------------------- | -------------------------------- |

![different-between-paid\&amp;unpaid](<../../../.gitbook/assets/4 (2).png>)

**Try to Find the information which can be reuse for further Gathering.**

### <mark style="color:blue;">Google Dorks</mark>

**Purpose:** Utilize specific queries for targeted Google searches.\
**Usage:** Use queries like `site:company.com` for precise information.

MY OPINION

> Google Dorking is where you use Google as a Vulnerability Scanner.
>
> What i mean is Google is a search Engine but in order for it to seach engine it need to go out and scan and spider its ways to the internet. where its scooping data along the way.

> Google not specifically looking vulnerabilities its just grab whatever out there and put it into a database so that when you search it can present with information about what you searched for. So you can search vulnerabilities in websites.&#x20;
>
> Like if Google Search for the term intitle:index.html id\_rsa - id\_rsa.pub
>
> This is asking Google if they found on internet with this name.



![google-dork-map](<../../../.gitbook/assets/Google dorking>)

Manully Entry.

```
site:company.com -www.company.com
site:company.com -www.company.com -example.company.com
site:company.com -www.company.com -example.company.com -eg.example.company.com
....
```

### [Shodan](https://shodan.io/)

> Shodan is A search engine Databases >> Databases IOT

**Purpose:** Search engine for discovering internet-connected devices.\
**Usage:** Explore on [Shodan](https://shodan.io) or use the command line (`shodan`).

* Its can other search engine which has information of a device that connected in internet.
* Shodan is a tool that lets you explore the internet; discovering connected devices or network services, monitoring network security, making global statistics and so on.
* Shodan give the gather some information which is, **sometime information can be false**
* **What is shodan ? : - Shodan is a database Which database ? : - IOT database**
  * **Shodan is a database of IOT and it host it over http/https and communicate over that and if we need to access the shodan need authentication which is token based**
  * **API will proved an interface which delivery this type of services and interact**
  * **And the API is the authentication Token. Which help to interact which shodan**
  * **Shodan is a search engine used to search for any device that is connected to the internet. Commonly used to search for IoT devices like cameras, raspberry-pi's, etc.**
  * **Shodan: It has GUI (**[**https://shodan.io**](https://shodan.io/)**) as well as CLI, shodan says that it has information but it can be wrong or have very less information.**
  * **It collects information on backend to make the world secure and cybersecurity. So, kind of vulnerability assessment**&#x20;

<figure><img src="../../../.gitbook/assets/shodan search example 1 (1)" alt=""><figcaption></figcaption></figure>

* And it identifies the vulnerabilities of the affected servers

<figure><img src="../../../.gitbook/assets/shodan search example 2 (1)" alt=""><figcaption></figcaption></figure>

* What if got the publicly exposed Ip –add and Vulnerability now Shadon gathers and give the information must validate and perform the attack.



<figure><img src="../../../.gitbook/assets/shodan search example 3 (1)" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
**Shodan Information can be False Positive**
{% endhint %}

<figure><img src="../../../.gitbook/assets/shodan enumeration" alt=""><figcaption><p>shodan.io</p></figcaption></figure>

#### Cli Commands Example

* **Add the API to Shodan from the account**

<figure><img src="../../../.gitbook/assets/shodan CLI (1)" alt=""><figcaption><p>Shodan CLI</p></figcaption></figure>

| **`shodan init <api-key>`** |
| --------------------------- |

<figure><img src="../../../.gitbook/assets/shodan init API KEY (1)" alt=""><figcaption><p>Add API</p></figcaption></figure>

**`shodan scan`**

<details>

<summary>Why this website charges to get extra or main information ?</summary>

well because they show to the company which has been open to internet and let the attacker used to get the Bug in the application after that they ask the company to pay to hide there information.

</details>

[**Automated shodan (shosubgo)**](https://github.com/incogbyte/shosubgo)

* for sticky subdomain discovery using subdomain &#x20;
* A smart hacker might wonder why to use this tool when Amass already has similar features. They might notice that specialized tools for Shodan and GitHub searches often produce more results by 3-4% because they focus on those areas.
* After getting the domains and karma output it can be flirted out by CHATGTP cut script

> get the results form Crt.sh and query here on shodan
>
> > ssl "company inc" 200
> >
> > > 200 is http 200 response.

1.  Retrieve results from Crt.sh and query them on Shodan:

    ```bash
    crtsh "your_domain_here" | shodan search
    ```
2.  Search for SSL-certified websites belonging to "Company Inc" with HTTP 200 response:

    ```bash
    shodan ssl "Company Inc" port:443,80 http.status:200
    ```
3.  Look for login functionality in Shodan:

    ```bash
    shodan search "login" 
    ```
4.  Perform a new search for SSL certificates with a specific Common Name (CN) and HTTP 200 response:

    ```bash
    shodan ssl.cert.subject.CN:"example.com" port:443,80 http.status:200
    ```

    Note: Place the domain within quotation marks, not the organization name.
5.  Filter results in Shodan with HTTP and explore every prompt provided:

    ```bash
    shodan search "your_filter_here" --expand
    ```
6.  In GitHub, utilize the domain name and additional filters like "example.com" for sensitive information such as passwords, secrets, tokens, and more:

    ```bash
    github-dork -u "example.com" -s "passwd|pwd|pw|secret|token" 
    ```

    Note: Ensure you have the necessary tools like `github-dork` installed for GitHub dorking.

### [Karma](https://github.com/Dheerajmadhukar/karma_v2)

**Purpose:** Automation tool using Shodan for passive data gathering.\
**Usage:** Identify potential vulnerabilities and exhaustively mine data.

Karma is an advanced automation tool that leverages search queries to exhaustively mine data from Shodan. It excels in gathering passive reconnaissance data and identifying potential vulnerabilities in a target system.



### [WTFIS](https://github.com/pirxthepilot/wtfis)

* Its the same as KarmaV2.

### Fullhunt

**Purpose:** Similar to Shodan, providing information on internet-connected devices.\
**Usage:** Access at [Fullhunt](https://fullhunt.io).

### [**Censys**](https://censys.io/)

**Purpose:** Search engine for discovering devices and networks connected to the internet.\
**Usage:** Explore data on [Censys](https://search.censys.io).

**Censys Search is a search engine that helps you find and understand information about devices and networks connected to the internet, revealing security issues and other important details.**

**Home page:** [**https://search.censys.io/**](https://search.censys.io/)

![Census-home-page](<../../../.gitbook/assets/5 (2).png>)

{% hint style="info" %}
**sometimes censys found and sometimes it's doesn't**
{% endhint %}

&#x20;

* **This indicate that the target use VPN for palo alto Vendous  which is global protect. Got the Algorithum Details and try to decrepted.**

<figure><img src="../../../.gitbook/assets/7 (2).png" alt=""><figcaption><p>Censys search deep check</p></figcaption></figure>

### [Whoisxmlapi](https://main.whoisxmlapi.com/)

We use various methods to find the subdomains of a target. In this approach, we don't actively send messages to the target. Instead, we quietly gather available information from the internet.

### Other Resources

1. **360PassiveDNS**
   * Home: [360PassiveDNS](https://www.360passive.com/)
   * Description: A platform providing passive DNS data, allowing users to investigate historical DNS records for a given domain.
2. **AbuseIPDB**
   * Home: [AbuseIPDB](https://www.abuseipdb.com/)
   * Description: A public database of IP addresses reported for malicious activity, providing a resource for threat intelligence.
3. **Ahrefs**
   * Home: [Ahrefs](https://ahrefs.com/)
   * Description: A comprehensive SEO toolset offering backlink analysis, keyword research, competitor analysis, and more to improve website performance.
4. **AlienVault**
   * Home: [AlienVault](https://www.alienvault.com/)
   * Description: A provider of threat intelligence and security management solutions, including Open Threat Exchange (OTX).
5. **AnubisDB**
   * Home: [AnubisDB](https://anubisdb.com/)
   * Description: A platform for threat intelligence, offering information on malicious domains, IP addresses, and other indicators of compromise.
6. **Arquivo**
   * Home: [Arquivo](http://arquivo.pt/)
   * Description: A web archive service allowing users to access and explore historical snapshots of websites.
7. **Ask**
   * Home: [Ask](https://www.ask.com/)
   * Description: A search engine where users can ask questions and receive answers, providing a different approach to information retrieval.
8. **AskDNS**
   * Description: A tool for querying DNS records, helping users gather information about domain names.
9. **Baidu**
   * Home: [Baidu](https://www.baidu.com/)
   * Description: A Chinese search engine that can be utilized for web searches and information retrieval.
10. **BeVigil**
    * Home: [BeVigil](https://bevigil.com/)
    * Description: A platform for cybersecurity and threat intelligence, offering services like domain and IP monitoring.
11. **BinaryEdge**
    * Home: [BinaryEdge](https://www.binaryedge.io/)
    * Description: A cybersecurity platform providing insights into internet-wide exposures, vulnerabilities, and digital risks.
12. **Bing**
    * Home: [Bing](https://www.bing.com/)
    * Description: A search engine by Microsoft that can be used for web searches and indexing.
13. **BufferOver**
    * Description: A platform that provides various DNS-related tools for domain enumeration and information gathering.
14. **BuiltWith**
    * Home: [BuiltWith](https://builtwith.com/)
    * Description: A technology profiler that allows users to discover the technologies used on websites.
15. **C99**
    * Description: C99 is a webshell script that may be used for various web-related activities.
16. **Censys**
    * Home: [Censys](https://censys.io/)
    * Description: A platform for internet-wide scanning, offering insights into networks, domains, and certificates.
17. **CertCentral**
    * Home: [CertCentral](https://www.digicert.com/)
    * Description: A certificate management platform providing tools for SSL/TLS certificate administration.
18. **CertSpotter**
    * Home: [CertSpotter](https://sslmate.com/certspotter/)
    * Description: A tool for monitoring and detecting SSL/TLS certificates issued for domains.
19. **Chaos**
    * Description: Chaos is a DNS reconnaissance tool for enumerating DNS subdomains.
20. **Chinaz**
    * Home: [Chinaz](http://chinaz.com/)
    * Description: A Chinese website that provides various web services, including domain-related information.
21. **CIRCL**
    * Home: [CIRCL](https://www.circl.lu/)
    * Description: Computer Incident Response Center Luxembourg, providing various cybersecurity services and tools.
22. **CommonCrawl**
    * Home: [CommonCrawl](https://commoncrawl.org/)
    * Description: A non-profit organization that crawls the web and freely provides its archives and datasets to the public.
23. **Crtsh**
    * Home: [Crt.sh](https://crt.sh/)
    * Description: A search engine for certificate transparency logs, helping users find information about SSL/TLS certificates.
24. **CSPHeader**
    * Description: A tool for checking Content Security Policy (CSP) headers on websites, providing insights into web security configurations.
25. **Deepinfo**
    * Home: [Deepinfo](https://www.deepinfo.com/)
    * Description: A platform for cybersecurity intelligence, offering services like domain analysis and threat detection.
26. **Detectify**
    * Home: [Detectify](https://detectify.com/)
    * Description: A web security scanner that helps users identify vulnerabilities and security issues in their web applications.
27. **Digitorus**
    * Home: [Digitorus](https://digitorus.com/)
    * Description: A platform offering digital forensics and cybersecurity services, including domain and IP investigations.
28. **DNSDB**
    * Home: [DNSDB](https://dnsdb.info/)
    * Description: A platform for exploring historical DNS data and conducting investigations on domain-related information.
29. **DnsDB**
    * Description: Another instance of a DNS database, allowing users to query and analyze DNS records.
30. **DNSDumpster**
    * Home: [DNSDumpster](https://dnsdumpster.com/)
    * Description: A web-based tool for DNS reconnaissance, providing information about domains, subdomains, and associated IP addresses.
31. **DNSHistory**
    * Home: [DNSHistory](https://www.dnshistory.org/)
    * Description: A tool for exploring historical DNS data, allowing users to track changes and gather information about domain history.
32. **DNSlytics**
    * Home: [DNSlytics](https://dnslytics.com/)
    * Description: A platform offering DNS-related tools and services for domain research and investigation.
33. **DNSRepo**
    * Home: [DNSRepo](https://dnsrepo.com/)
    * Description: A tool for querying DNS records and exploring information related to domains and IP addresses.
34. **dnsrepo**
    * Description: Another instance or tool for querying DNS records and gathering information about domains.
35. **DNSSpy**
    * Description: A tool or platform for conducting DNS reconnaissance and gathering information about domains and their infrastructure.
36. **DuckDuckGo**
    * Home: [DuckDuckGo](https://duckduckgo.com/)
    * Description: A privacy-focused search engine that can be used for web searches without tracking.
37. **FacebookCT**
    * Home: [FacebookCT](https://facebookct.com/)
    * Description: A tool or platform for exploring certificate transparency logs related to Facebook domains.
38. **FOFA**
    * Home: [FOFA](https://fofa.so/)
    * Description: A search engine for finding Internet of Things (IoT) devices and gathering information about them.
39. **Fofa**
    * Description: Another instance or tool related to FOFA, providing services for finding and analyzing IoT devices.
40. **FullHunt**
    * Home: [FullHunt](https://www.fullhunt.io/)
    * Description: A platform for threat intelligence and cybersecurity, offering services for domain and IP analysis.
41. **Gists**
    * Home: [Gists](https://gist.github.com/)
    * Description: A platform for sharing and discovering code snippets and Git repositories.
42. **GitHub**
    * Home: [GitHub](https://github.com/)
    * Description: A web-based platform for version control using Git, as well as a collaborative space for software development.
43. **GitLab**
    * Home: [GitLab](https://gitlab.com/)
    * Description: A web-based Git repository manager providing source code management (SCM) functionality and collaboration features.
44. **Google**
    * Home: [Google](https://www.google.com/)
    * Description: A widely used search engine for web searches and information retrieval.
45. **GrepApp**
    * Description: A tool for searching and analyzing web applications, providing insights into application-specific information.
46. **Greynoise**
    * Home: [Greynoise](https://greynoise.io/)
    * Description: A platform for threat intelligence, offering services for identifying and analyzing Internet-wide scan activity.
47. **HackerOne**
    * Home: [HackerOne](https://www.hackerone.com/)
    * Description: A platform for ethical hacking and bug bounty programs, connecting security researchers with organizations.
48. **HackerTarget**
    * Home: [HackerTarget](https://hackertarget.com/)
    * Description: A platform providing various online security tools, including DNS and domain-related information.
49. **HAW**
    * Description: HAW (Have I Been Pwned) is a platform for checking whether email addresses and passwords have been compromised in data breaches.
50. **Hunter**
    * Home: [Hunter](https://hunter.io/)
    * Description: A platform for email verification and discovery, helping users find email addresses associated with a domain.
51. **HyperStat**
    * Home: [HyperStat](https://hyperstat.com/)
    * Description: A platform for conducting statistical analyses on domains, including information about IP addresses, registrars, and more.
52. **IntelX**
    * Home: [IntelX](https://intelx.io/)
    * Description: A search engine for finding and analyzing data from the dark web, providing services for domain and IP investigation.
53. **Intelx**
    * Description: Another instance or tool related to IntelX, offering services for discovering and analyzing dark web data.
54. **LeakIX**
    * Home: [LeakIX](https://leakix.net/)
    * Description: A platform for collecting and analyzing Internet-wide scan data, including information about exposed services and vulnerabilities.
55. **Maltiverse**
    * Home: [Maltiverse](https://maltiverse.com/)
    * Description: A threat intelligence platform offering services for domain and IP analysis, including information about malware and threats.
56. **Mnemonic**
    * Home: [Mnemonic](https://www.mnemonic.no/)
    * Description: A cybersecurity company offering various services, including threat intelligence and digital forensics.
57. **Netlas**
    * Home: [Netlas](https://netlas.io/)
    * Description: A platform for Internet-wide scanning and reconnaissance, providing insights into domains, IPs, and SSL certificates.
58. **ONYPHE**
    * Home: [ONYPHE](https://www.onyphe.io/)
    * Description: A search engine for finding and analyzing Internet-exposed devices, providing services for cybersecurity and threat intelligence.
59. **PassiveTotal**
    * Home: [PassiveTotal](https://www.passivetotal.org/)
    * Description: A threat intelligence platform offering services for domain and IP analysis, including passive DNS data.
60. **Pastebin**
    * Home: [Pastebin](https://pastebin.com/)
    * Description: A platform for sharing and storing text online, often used for code snippets, configuration files, and other text-based content.
61. **PentestTools**
    * Home: [PentestTools](https://pentest-tools.com/)
    * Description: A platform providing various online penetration testing tools, including services for information gathering and reconnaissance.
62. **PKey**
    * Description: A tool or platform related to public keys (PKey), possibly used for cryptographic analysis and key-related information.
63. **PublicWWW**
    * Home: [PublicWWW](https://publicwww.com/)
    * Description: A search engine for finding websites based on the technologies used, providing insights into web technologies and code snippets.
64. **Pulsedive**
    * Home: [Pulsedive](https://pulsedive.com/)
    * Description: A threat intelligence platform offering services for domain, IP, and threat analysis.
65. **Quake**
    * Home: [Quake](https://quake.so/)
    * Description: A search engine for finding and analyzing Internet-exposed devices and services, providing insights into vulnerabilities and misconfigurations.
66. **quake**
    * Description: Another instance or tool related to Quake, offering services for Internet-wide scanning and reconnaissance.
67. **RapidDNS**
    * Home: [RapidDNS](https://rapiddns.io/)
    * Description: A platform for conducting DNS reconnaissance, providing information about domains, subdomains, and associated IP addresses.
68. **Riddler**
    * Home: [Riddler](https://riddler.io/)
    * Description: A platform for searching and analyzing Internet-exposed devices, providing insights into domains, IPs, and SSL certificates.
69. **Robtex**
    * Home: [Robtex](https://www.robtex.com/)
    * Description: A platform offering various network-related tools, including information about IP addresses, domain names, and network traffic.
70. **Searchcode**
    * Home: [Searchcode](https://searchcode.com/)
    * Description: A search engine for finding and exploring source code, providing services for code analysis and discovery.
71. **Searx**
    * Home: [Searx](https://searx.me/)
    * Description: An open-source metasearch engine that aggregates results from various search engines, allowing users to search without tracking.
72. **SecurityTrails**
    * Home: [SecurityTrails](https://securitytrails.com/)
    * Description: A cybersecurity platform offering services for DNS and domain intelligence, including historical DNS data and tracking.
73. **Shodan**
    * Home: [Shodan](https://www.shodan.io/)
    * Description: A search engine for finding Internet-connected devices, providing services for reconnaissance and analysis.
74. **SiteDossier**
    * Home: [SiteDossier](https://www.sitedossier.com/)
    * Description: A platform for gathering information about websites, including domain history, IP addresses, and related domains.
75. **SOCRadar**
    * Home: [SOCRadar](https://www.socradar.com/)
    * Description: A platform for cybersecurity and threat intelligence, offering services for monitoring and analyzing threats.
76. **Spamhaus**
    * Home: \[Spamhaus]\(https://www.spamhaus.org/) - Description: A project and organization providing real-time threat intelligence on spam and related cyber threats.
77. **SpyOnWeb**
    * Home: [SpyOnWeb](https://spyonweb.com/)
    * Description: A platform for exploring relationships between websites, domains, and IP addresses, providing insights into web presence.
78. **Sublist3rAPI**
    * Description: An API or tool for subdomain enumeration, allowing users to discover subdomains associated with a given domain.
79. **ThreatBook**
    * Home: [ThreatBook](https://www.threatbook.cn/)
    * Description: A cybersecurity platform offering services for threat intelligence and analysis, including information about threats and vulnerabilities.
80. **ThreatMiner**
    * Home: [ThreatMiner](https://www.threatminer.org/)
    * Description: A threat intelligence platform providing services for analyzing and visualizing data related to threats and cyber incidents.
81. **UKWebArchive**
    * Home: [UK Web Archive](https://www.ukwebarchive.org.uk/)
    * Description: A web archive service focused on archiving and preserving websites related to the UK.
82. **URLScan**
    * Home: [URLScan](https://urlscan.io/)
    * Description: A platform for analyzing and scanning websites, providing insights into their structure, content, and security.
83. **VirusTotal**
    * Home: [VirusTotal](https://www.virustotal.com/)
    * Description: A platform for analyzing files and URLs for malicious content, aggregating results from various antivirus engines and scanners.
84. **Wayback**
    * Home: [Wayback Machine](https://archive.org/web/)
    * Description: The Wayback Machine, part of the Internet Archive, allows users to access archived versions of websites over time.
85. **WhoisXMLAPI**
    * Home: [WhoisXMLAPI](https://www.whoisxmlapi.com/)
    * Description: A platform offering services for domain and WHOIS information, providing insights into domain ownership and history.
86. **Yahoo**
    * Home: [Yahoo](https://www.yahoo.com/)
    * Description: A search engine and web services provider offering various online products, including web searches and news.
87. **Yandex**
    * Home: [Yandex](https://yandex.com/)
    * Description: A Russian multinational IT company providing search and online services, similar to Google.
88. **ZETAlytics**
    * Description: A tool or platform for analyzing and gathering information about domains and IP addresses.
89. **ZoomEye**
    * Home: [ZoomEye](https://www.zoomeye.org/)
    * Description: A search engine for finding and analyzing Internet-connected devices, providing services for reconnaissance and cybersecurity.
90. **ZoomEyeAPI**
    * Description: An API or tool related to ZoomEye, allowing users to programmatically access and retrieve information about Internet-connected devices.
91. **Assetnote**
    * Home: [Assetnote](https://www.assetnote.io/)
    * Description: A platform for monitoring and securing internet-exposed assets, providing services for asset discovery and reconnaissance.
92. **Recon-ng**
    * Home: [Recon-ng](https://github.com/lanmaster53/recon-ng)
    * Description: An open-source reconnaissance framework that helps automate the discovery of information during the information gathering phase of penetration testing.
93. **Aquatone**
    * Home: [Aquatone](https://github.com/michenriksen/aquatone)
    * Description: A tool for visualizing and analyzing data collected during domain reconnaissance, providing insights into web infrastructure.
94. **Amass**
    * Home: [Amass](https://github.com/OWASP/Amass)
    * Description: An open-source tool for subdomain enumeration and network mapping, assisting in information gathering during security assessments.
95. **Fierce**
    * Home: [Fierce](https://github.com/mschwager/fierce)
    * Description: A DNS reconnaissance tool that helps discover non-contiguous IP space and enumerates DNS information to identify potential targets.
96. **Dnsmap**
    * Home: [Dnsmap](https://github.com/makefu/dnsmap)
    * Description: A tool for passive DNS discovery, mapping domains and subdomains associated with IP addresses.
97. **Subfinder**
    * Home: [Subfinder](https://github.com/projectdiscovery/subfinder)
    * Description: An open-source subdomain discovery tool that helps enumerate subdomains for a given domain.
98. **OWASP Amass**
    * Home: [OWASP Amass](https://github.com/OWASP/Amass)
    * Description: An open-source tool for network mapping and external asset discovery, aiding in DNS reconnaissance and subdomain enumeration.
99. **AltDNS**
    * Home: [AltDNS](https://github.com/infosec-au/altdns)
    * Description: A tool for generating permutations of domain names to discover new subdomains.
100. **Subjack** - Home: [Subjack](https://github.com/haccer/subjack) - Description: A tool designed to check if a subdomain can be taken over by exploiting various vulnerabilities.
101. **AlienVault**
     * [AlienVault](https://www.alienvault.com/)
102. **BinaryEdge**
     * [BinaryEdge](https://www.binaryedge.io/)
103. **VirusTotal**
     * [VirusTotal](https://www.virustotal.com/)
104. **Shodan Crawls**
     * [Shodan](https://www.shodan.io/)
105. **Shodan Filters**
     * [Shodan Filters](https://help.shodan.io/the-basics/filters)
106. **Penetration Testing Shodan from StationX**
     * [penetration testing shodan from stationx](https://www.stationx.net/how-to-use-shodan/)
107. **Penetration Testing Shodan from Turgensec**
     * [penetration testing shodan from turgensec](https://community.turgensec.com/shodan-pentesting-guide/)
108. **GodFatherorwa**
     * [GodFatherorwa](https://www.youtube.com/playlist?list=PLiLvsecrejRhQ7lOGgZSga47Jwhf5YXwD)
109. **SecurityTrails**
     * [SecurityTrails](https://securitytrails.com/)
110. **SpiderFootHX (2nd Best Paid AP)**
     * [SpiderFoot HX](https://www.spiderfoot.net/)

### [**Amass**](https://github.com/owasp-amass/amass)&#x20;

**Installation:**

```bash
# Set up Go environment (if not done already)
# Instructions: https://golang.org/doc/install
go install -v github.com/owasp-amass/amass/v3/...@master
```

**Configuration:**

* Amass uses a configuration file located at `$HOME/.config/amass/config.ini`.
* Configure API keys in the file (e.g., AlienVault, BinaryEdge) for passive DNS data.
* \[Example Config File]\(link to your config file)

**Running Amass:**

```bash
# Example command
amass enum -passive -d example.com  -o output.txt

# Explanation:
# - `enum`: Perform DNS enumeration
# - `passive`: Collect information passively through configured data sources
# - `active` : Collect information actively through transfers and certificate name grabs
# - `config`: Specify the location of the config file (default: $HOME/.config/amass/config.ini)
```

**Tip:** To verify API key setup, use the command: `amass enum -list -config config.ini`

#### Amass Enumeration <a href="#toc142346656" id="toc142346656"></a>

<figure><img src="../../../.gitbook/assets/amass enum example 2" alt=""><figcaption><p>Amass </p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/amass enum exmaple 0" alt=""><figcaption><p>Amass -d</p></figcaption></figure>

**What to do with this subnet?**

* _More subdomains mean more IP\_ADDR. More probability increased, more computer more attack chances it will give the attack successful chances to increase,_
* _Target it using service from different company, like the above example netflix is using services from Cloudflare_
* _So, these are in Public IP-Range It can be assets._

![Amass -d example.com -src](<../../../.gitbook/assets/amass enum example 1>)

### **Sublist3r**

```bash
# Install Sublist3r
sudo apt install sublist3r

# Example command
sublist3r -d example.com

#go installation
subfinder -d example.com -all -config config.yaml -o output.txt

```

### **Subfinder**

```bash
# Install Subfinder
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest

# Example command
subfinder -d example.com -all -config config.yaml -o output.txt
# - `d`: Specify the target domain
# - `all`: Use all passive sources (slower but more results)
# - `config`: Config file location

# Tip: To view sources requiring API keys, use: subfinder -ls
```

![subfinder-results](<../../../.gitbook/assets/subfinder (1)>)

### **Assetfinder (by Tomnomnom)**

```bash
# Install Assetfinder
go install github.com/tomnomnom/assetfinder@latest

# Example command
assetfinder --subs-only example.com > output.txt
```

### **BBOT**&#x20;

```bash
# Install BBOT
docker run -it blacklanternsecurity/bbot:stable --help
```

BBOT wraps around various tools and adds new sources. It supports API keys and offers additional features like email enumeration, cloud enumeration, and more. Example command:

```bash
bbot -t evilcorp.com -f subdomain-enum email-enum cloud-enum web-basic -m nmap gowitness nuclei --allow-deadly
```

```
docker run -it blacklanternsecurity/bbot:stable  -t evilcorp.com -f subdomain-enum email-enum cloud-enum web-basic -m  gowitness nuclei --allow-deadly
 > bbotoutput.txt
```



### [Subdomainer](https://github.com/Cyber-Guy1/Subdomainer)

* its an automated tool for domain and subdmain gathering&#x20;
* Its uses multiple repo like Amass,subfinder,gobuster and more.

## Recursive Enumeration



This technique involves further exploration of subdomains using tools like Amass, Subfinder, Assetfinder on the already discovered subdomains.&#x20;

1. **Prerequisites:**
   * You should have a list of subdomains stored in a file called "subdomains.txt."
   * API keys should be set up, but be cautious as this technique may exhaust your API querying quota.
2. **Execution Steps:** a) **Identify Frequent Second-Level Domains:**
   * Read the subdomains from the file.
   * Find the top 10 most frequently occurring Second-Level Domain names using tools like cut, sort, rev, uniq. b) **Identify Frequent Third-Level Domains:**
   * Find the top 10 most frequently occurring Third-Level domains.
   * This step uses similar tools to identify and list the most common Third-Level domains.
3. **Run Passive Subdomain Enumeration:**
   * Execute passive subdomain enumeration on the identified Second-Level and Third-Level domain names using tools like Amass, Subfinder, Assetfinder, Findomain.
   * Append the results to a file called "passive\_recursive.txt."
4. **Use Puredns to DNS Resolve:**
   * After obtaining a list of domain names, run Puredns to DNS resolve them and find the alive subdomains.
5. **Execution Script:**
   * Replace "subdomains.txt" with the actual filename of your subdomains list.
   * The provided script uses various command-line tools and scripts like subfinder, assetfinder, amass, and findomain.

```bash
go install -v github.com/tomnomnom/anew@latest

subdomain_list="subdomains.txt"

for sub in $(
  ( cat $subdomain_list | rev | cut -d '.' -f 3,2,1 | rev | sort | uniq -c | sort -nr | grep -v '1 ' | head -n 10 &&
    cat subdomains.txt | rev | cut -d '.' -f 4,3,2,1 | rev | sort | uniq -c | sort -nr | grep -v '1 ' | head -n 10 ) |
    sed -e 's/^[[:space:]]*//' | cut -d ' ' -f 2
); do
  subfinder -d $sub -silent -max-time 2 | anew -q passive_recursive.txt
  assetfinder --subs-only $sub | anew -q passive_recursive.txt
  amass enum -timeout 2 -passive -d $sub | anew -q passive_recursive.txt
  findomain --quiet -t $sub | anew -q passive_recursive.txt
  puredns -i passive_recursive.txt -r results.txt

done
```

### [**Findomain**](https://github.com/Findomain/Findomain)**:**

* **Purpose:** Finds subdomains for a website.
*   **Command:**

    ```bash
    # Finds subdomains for example.com and saves the output to output.txt
    findomain -t example.com -u output.txt
    ```

### **Gau (GitHub All URLs):**

* **Purpose:** Collects URLs, including GitHub.
*   **Command:**

    ```bash
    # Collects URLs from various sources including GitHub and saves unique results to output_unfurl.txt
    gau --threads 5 --subs example.com | sort -u -o output_unfurl.txt
    ```

### **Waybackurls:**

* **Purpose:** Gets URLs from the Wayback Machine.
*   **Command:**

    ```bash
    # Retrieves URLs from the Wayback Machine for example.com and saves unique results to output.txt
    waybackurls example.com | sort -u -o output.txt
    ```

### **Github-subdomains:**

* **Purpose:** Finds subdomains on GitHub.
*   **Command:**

    ```bash
    # Finds GitHub subdomains for example.com using GitHub access tokens and saves results to output.txt
    github-subdomains -d example.com -t tokens.txt -o output.txt
    ```

### **Crobat (Using Rapid7 Project Sonar dataset):**

* **Purpose:** Finds subdomains using an extensive dataset.
*   **Command:**

    ```bash
    # Uses the Rapid7 Sonar dataset to find subdomains for example.com and saves results to output.txt
    crobat -s example.com > output.txt
    ```



### **Crobat API for Rapid7 Sonar Dataset**:

* **What is it?** Crobat is a tool built on the Rapid7 Sonar dataset. It's like a search engine for subdomains.
*   **How to use it?**

    {% code overflow="wrap" %}
    ```bash
    # Install Crobat tool using Go
    go get github.com/cgboal/sonarsearch/cmd/crobat
    # Query the Crobat API for subdomains of example.com and save the results to output.txt
    crobat -s example.com > output.txt
    ```
    {% endcode %}

#### Subdomain Extraction from Crobat Output:

* **What is it?** After using Crobat, this command helps filter and organize the results.
*   **How to use it?**

    {% code overflow="wrap" %}
    ```bash
    # Extracts subdomains from files with the ".apexdomain.com" pattern, removes duplicates, and saves to output.txt
    cat *.txt | grep ".apexdomain.com" | grep -oP "(?<=[).*(?=\])" | tr ' ' '\n' | grep -v "*" | sort -u

    Examplation
    cat *.txt: Reads content from all text files.
    grep ".apexdomain.com": Filters lines containing ".apexdomain.com".
    grep -oP "(?<=[).*(?=\])": Extracts content between square brackets.
    tr ' ' '\n': Transforms spaces into newlines.
    grep -v "*": Excludes lines with asterisks.
    sort -u: Sorts and removes duplicates.
    ```
    {% endcode %}

### **Intelligence X:**

* **Purpose:** A search engine for online data.
* **Usage:** [Intelligence X](https://intelx.io/)
  * Search by email, domain, or IP for information.

### **RapidDNS:**

* **Purpose:** Provides information about DNS records.
* **Usage:** [RapidDNS](https://rapiddns.io/)
  * Enter the target domain and explore DNS records.



### **Project Sonar by Rapid7:**

* **What is it?** Project Sonar is a research project by Rapid7 that scans the entire internet. They share valuable datasets for free, containing lots of information about domains.
* **How to use it?** You can follow their guide here to explore these datasets.

### **Exif Tool:**

* **Purpose:** Extracts hidden information from files.
*   **Command:**

    ```bash
    # Displays metadata information for the specified PDF file
    exiftool /path/to/filename.pdf
    ```

    * `/path/to/filename.pdf`: Path to the file you want to inspect.

&#x20;it can adapt them to your specific needs by replacing example domains, file paths, etc.





## DNS Brute Forcing

> Finding the New Subdomain Using the Wordlist by Resolving Through DNS
>
>
>
> wordlist has admin, internal.dev, secert, backup101
>
> * admin >> admin.example.com
> * internal.dev.example.com
> * secert.example.com
> * backup101.example.com
>
> if it resolves that means the domain exists somewhere.

Nuclei

* Its it has template, like Metasploit has Auxiliary for scanning script, those script identifies another information against the target. It a template base tasks execution.

Installation : Sudo apt install nuclei

\#nudlie

When the nuclei start its first download default-nuclei template which is YAM base.

Argument –u

\#nuclie –u \[target-ipaddr]

-t to define the templates

-ss will scan auto scanning

-sandbox for safe execution

-nt for new templates

Download the custom templates from github or create one using yml and more.

{% embed url="https://github.com/emadshanab/Nuclei-Templates-Collection/blob/main/README.md" %}

From this download in this case : [https://github.com/pikpikcu/nuclei-templates/blob/master/README.md](https://github.com/pikpikcu/nuclei-templates/blob/master/README.md)

Basic Nuclei Scan

| <p>Beebox:</p><p>┌──(kali㉿kali)-[~]</p><p>└─$ nuclei -u 192.168.100.130</p><p>__ _</p><p>____ __ _______/ /__ (_)</p><p>/ __ \/ / / / ___/ / _ \/ /</p><p>/ / / / /_/ / /__/ / __/ /</p><p>/_/ /_/\__,_/\___/_/\___/_/ v2.9.7</p><p>projectdiscovery.io</p><p>[INF] Current nuclei version: v2.9.7 (latest)</p><p>[INF] Current nuclei-templates version: v9.5.3 (latest)</p><p>[INF] New templates added in latest release: 82</p><p>[INF] Templates loaded for current scan: 6146</p><p>[INF] Targets loaded for current scan: 1</p><p>[INF] Running httpx on input host</p><p>[INF] Found 1 URL from httpx</p><p>[INF] Templates clustered: 1110 (Reduced 1050 Requests)</p><p>[apache-detect] [http] [info] https://192.168.100.130 [Apache/2.2.8 (Ubuntu) DAV/2 mod_fastcgi/2.4.6 PHP/5.2.4-2ubuntu5 with Suhosin-Patch mod_ssl/2.2.8 OpenSSL/0.9.8g]</p><p>[openssl-detect] [http] [info] https://192.168.100.130 [OpenSSL/0.9.8g]</p><p>[php-detect] [http] [info] https://192.168.100.130</p><p>[expired-ssl] [ssl] [low] 192.168.100.130:443 [2018-04-13 18:11:32 +0000 UTC]</p><p>[self-signed-ssl] [ssl] [low] 192.168.100.130:443</p><p>[ssl-issuer] [ssl] [info] 192.168.100.130:443 [MME]</p><p>[revoked-ssl-certificate] [ssl] [low] 192.168.100.130:443</p><p>[http-missing-security-headers:cross-origin-opener-policy] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:cross-origin-resource-policy] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:referrer-policy] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:clear-site-data] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:x-frame-options] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:x-content-type-options] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:strict-transport-security] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:content-security-policy] [http] [info] https://192.168.100.130</p><p>[http-missing-security-headers:permissions-policy] [http] [info] https://192.168.100.130</p><p>[INF] Using Interactsh Server: oast.me</p><p>[tls-version] [ssl] [info] 192.168.100.130:443 [tls10]</p><p>[smtp-service-detect] [tcp] [info] 192.168.100.130:25</p><p>[options-method] [http] [info] https://192.168.100.130 [GET,HEAD,POST,OPTIONS,TRACE]</p><p>[weak-cipher-suites] [ssl] [medium] 192.168.100.130:443 [[tls10 TLS_RSA_WITH_AES_128_CBC_SHA]]</p><p>[deprecated-tls] [ssl] [info] 192.168.100.130:443 [ssl30]</p><p>[deprecated-tls] [ssl] [info] 192.168.100.130:443 [tls10]</p><p>[samba-detect] [tcp] [info] 192.168.100.130:139</p><p>[phpmyadmin-panel] [http] [info] https://192.168.100.130/phpmyadmin/</p><p>[server-status-localhost] [http] [low] https://192.168.100.130/server-status</p><p>[esmtp-detect] [tcp] [info] 192.168.100.130:25</p><p>[exposed-sqlite-manager] [http] [medium] https://192.168.100.130/sqlite/</p><p>[http-trace:trace-request] [http] [info] https://192.168.100.130</p><p>[waf-detect:apachegeneric] [http] [info] https://192.168.100.130/</p><p>[http-trace:options-request] [http] [info] https://192.168.100.130</p><p>[openssh-detect] [tcp] [info] 192.168.100.130:22 [SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1</p><p>]</p><p>[ftp-anonymous-login] [tcp] [medium] 192.168.100.130:21</p> | <p>Windows:</p><p>┌──(kali㉿kali)-[~]</p><p>└─$ nuclei -u 192.168.100.131</p><p>__ _</p><p>____ __ _______/ /__ (_)</p><p>/ __ \/ / / / ___/ / _ \/ /</p><p>/ / / / /_/ / /__/ / __/ /</p><p>/_/ /_/\__,_/\___/_/\___/_/ v2.9.7</p><p>projectdiscovery.io</p><p>[INF] Current nuclei version: v2.9.7 (latest)</p><p>[INF] Current nuclei-templates version: v9.5.3 (latest)</p><p>[INF] New templates added in latest release: 82</p><p>[INF] Templates loaded for current scan: 6146</p><p>[INF] Targets loaded for current scan: 1</p><p>[INF] Running httpx on input host</p><p>[INF] Found 1 URL from httpx</p><p>[INF] Templates clustered: 1110 (Reduced 1050 Requests)</p><p>[http-missing-security-headers:content-security-policy] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:permissions-policy] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:x-frame-options] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:x-permitted-cross-domain-policies] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:referrer-policy] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:cross-origin-opener-policy] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:cross-origin-resource-policy] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:strict-transport-security] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:clear-site-data] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:cross-origin-embedder-policy] [http] [info] http://192.168.100.131</p><p>[http-missing-security-headers:x-content-type-options] [http] [info] http://192.168.100.131</p><p>[INF] Using Interactsh Server: oast.site</p><p>[openssh-detect] [tcp] [info] 192.168.100.131:22 [SSH-2.0-OpenSSH_for_Windows_8.1]</p><p>[microsoft-iis-version] [http] [info] http://192.168.100.131 [Microsoft-IIS/10.0]</p><p>[tech-detect:ms-iis] [http] [info] http://192.168.100.131</p><p>[rdp-detect:win2016] [tcp] [info] 192.168.100.131:3389</p><p>[waf-detect:modsecurity] [http] [info] http://192.168.100.131/</p><p>[ftp-anonymous-login] [tcp] [medium] 192.168.100.131:21</p><p>[options-method] [http] [info] http://192.168.100.131 [OPTIONS, TRACE, GET, HEAD, POST]</p> |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Nuclei Auto scan which include Host-spray and template spray.

Custom Template Scan

Download the Template or Create one.

Note sometime the template can be an issue so make sure to validate before

| <p>┌──(root㉿kali)-[/home/hasanrehni/nuclei-custom-template/Content-Injection-Nuclei-Script]</p><p>└─# nuclei -t content_injection.yaml -u 192.168.100.130</p><p>__ _</p><p>____ __ _______/ /__ (_)</p><p>/ __ \/ / / / ___/ / _ \/ /</p><p>/ / / / /_/ / /__/ / __/ /</p><p>/_/ /_/\__,_/\___/_/\___/_/ v2.9.7</p><p>projectdiscovery.io</p><p>[WRN] Found 1 templates loaded with deprecated protocol syntax, update before v3 for continued support.</p><p>[WRN] Found 1 templates with syntax error (use -validate flag for further examination)</p><p>[INF] Current nuclei version: v2.9.7 (latest)</p><p>[INF] Current nuclei-templates version: v9.5.3 (latest)</p><p>[INF] Targets loaded for current scan: 1</p><p>[INF] No results found. Better luck next time!</p><p>[FTL] Could not run nuclei: no valid templates were found</p><p>┌──(root㉿kali)-[/home/hasanrehni/nuclei-custom-template/Content-Injection-Nuclei-Script]</p><p>└─# nuclei -t content_injection.yaml -validate</p><p>__ _</p><p>____ __ _______/ /__ (_)</p><p>/ __ \/ / / / ___/ / _ \/ /</p><p>/ / / / /_/ / /__/ / __/ /</p><p>/_/ /_/\__,_/\___/_/\___/_/ v2.9.7</p><p>projectdiscovery.io</p><p>[ERR] Error occurred loading template /home/hasanrehni/nuclei-custom-template/Content-Injection-Nuclei-Script/content_injection.yaml: Could not load template /home/hasanrehni/nuclei-custom-template/Content-Injection-Nuclei-Script/content_injection.yaml: invalid field format for 'id' (allowed format is ^([a-zA-Z0-9]+[-_])*[a-zA-Z0-9]+$)</p><p>[FTL] Could not validate templates: errors occured during template validation</p><p>Basic Detection using templates:</p><p>>>#nuclei –t &#x3C;template-id-1 template-id-2> -u &#x3C;target></p><p>┌──(root㉿kali)-[/home/hasanrehni/nuclei-templates/basic-detections]</p><p>└─# ls</p><p>basic-xss-prober.yaml general-tokens.yaml</p><p>┌──(root㉿kali)-[/home/hasanrehni/nuclei-templates/basic-detections]</p><p>└─# nuclei -t basic-xss-prober.yaml general-tokens.yaml -u 192.168.100.131</p><p>__ _</p><p>____ __ _______/ /__ (_)</p><p>/ __ \/ / / / ___/ / _ \/ /</p><p>/ / / / /_/ / /__/ / __/ /</p><p>/_/ /_/\__,_/\___/_/\___/_/ v2.9.7</p><p>projectdiscovery.io</p><p>[WRN] Found 1 templates loaded with deprecated protocol syntax, update before v3 for continued support.</p><p>[INF] Current nuclei version: v2.9.7 (latest)</p><p>[INF] Current nuclei-templates version: v9.5.3 (latest)</p><p>[INF] New templates added in latest release: 82</p><p>[INF] Templates loaded for current scan: 1</p><p>[INF] No results found. Better luck next time!</p><p>┌──(root㉿kali)-[/home/hasanrehni/nuclei-templates/basic-detections]</p><p>└─# nuclei -t basic-xss-prober.yaml general-tokens.yaml -u 192.168.100.130</p><p>__ _</p><p>____ __ _______/ /__ (_)</p><p>/ __ \/ / / / ___/ / _ \/ /</p><p>/ / / / /_/ / /__/ / __/ /</p><p>/_/ /_/\__,_/\___/_/\___/_/ v2.9.7</p><p>projectdiscovery.io</p><p>[WRN] Found 1 templates loaded with deprecated protocol syntax, update before v3 for continued support.</p><p>[INF] Current nuclei version: v2.9.7 (latest)</p><p>[INF] Current nuclei-templates version: v9.5.3 (latest)</p><p>[INF] New templates added in latest release: 82</p><p>[INF] Templates loaded for current scan: 1</p><p>[INF] No results found. Better luck next time!</p> |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### **That's it !!! Done with passive things** <a href="#thats-it-done-with-passive-things" id="thats-it-done-with-passive-things"></a>

**Liked my work? Don't hesitate to buy me a coffee XDD**
