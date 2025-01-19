---
description: Understanding the Web application
---

# WEB TECHNOLOGIES

## <mark style="color:green;">Tech Profiling</mark>

one of the first tasks is need to do when dealing with application is to understand what web application server its running on , what programming language its written in and what framework its using

1. **Browser Extensions:**
   * **WhatRun:**
     * **Link:** [WhatRun](https://www.whatruns.com/)
     * **Overview:** WhatRun is a browser extension that automatically detects and displays the technologies used by a website. It covers a wide range of information, including the web server, programming language, CMS, analytics tools, and more.
   * **Wappalyzer:**
     * **Link:** [Wappalyzer](https://www.wappalyzer.com/)
     * **Overview:** Wappalyzer is a browser extension that identifies technologies employed by websites, offering details on web servers, programming languages, frameworks, CMS, and various other technologies.
   * **BuiltWith:**
     * **Link:** [BuiltWith](https://builtwith.com/)
     * **Overview:** BuiltWith is a web service that reveals the technologies powering a given website. It provides insights into web servers, programming languages, frameworks, JavaScript libraries, advertising networks, and more.
2. **Command-Line Tool:**
   * **Webanalyze:**
     * **Link:** [Webanalyze](https://github.com/rverton/webanalyze)
     * **Overview:** Webanalyze is a command-line tool that automates the functionality of Wappalyzer. It allows you to obtain technology information about a web application directly from the command line, making it suitable for automation and integration into custom recon frameworks.
   *   **Usage Example:**

       ```bash
       webanalyze -url https://example.com
       ```
   * **Note:** This is particularly useful when building custom reconnaissance frameworks or enriching existing datasets with technology stack information.

## <mark style="color:green;">BIG QUESTIONS</mark>

* **How does the application operate?**
  * **Details:** Can you provide a breakdown of the primary functions and features of the application? What are the specific user interactions, and how do they align with the overall purpose of the application?
* **How does the application pass the data?**
  * **Details:** Delve deeper into data transmission. Are there specific protocols in place for secure data transfer? How is sensitive information handled during transit, and what encryption standards are implemented?
* **How/where does the application store data about users?**
  * **Details:** For user data storage, specify the types of databases used and their configurations. How is encryption applied to safeguard user information, and are there any specific measures for maintaining data confidentiality?
* **Does the application have multi-tenancy or user levels?**
  * **Details:** Provide insights into the intricacies of user levels. What roles exist, and how are access controls implemented? Detail the permissions assigned to different user roles for a thorough understanding.
* **Does the application have a unique threat model?**
  * **Details:** Explore specific threats the application faces. Are there peculiar challenges due to its features? Unravel the nuances of the threat landscape, guiding the tailoring of security measures.
* **Has there been past security research and vulnerability disclosure?**
  * **Details:** If there's a history, spill the beans. Share details on any reported vulnerabilities from past security research, public databases, advisories, or bug bounty platforms.
* **How does the application and framework handle specific vulnerability classes?**
  * **Details:** For common vulnerabilities, such as SQL injection or cross-site scripting, elucidate on the defense mechanisms. What measures are in place to prevent or mitigate these risks?
* **What are the business-critical functions of the application?**
  * **Details:** Specify critical functions crucial to the business. Understanding these helps in prioritizing security assessments and fortifying vital components.
* **Does the application integrate with third-party services or APIs?**
  * **Details:** Detail the external integrations. What services or APIs are involved? Assess the potential vulnerabilities introduced by these external connections.
* **Is sensitive data hashed or encrypted at rest?**
  * **Details:** Dive into data at rest. How is sensitive information protected when stored? Provide insights into encryption or hashing methods employed for added security.
* **How does the application handle authentication and session management?**
  * **Details:** Explore authentication methods and session management. How is user access controlled, and what measures are in place to thwart unauthorized access or session hijacking?
* **What technologies and frameworks power the application?**
  * **Details:** Dive into the tech stack. What languages, frameworks, and libraries are in play? Understanding the underlying technologies helps identify potential vulnerabilities and stay ahead of security risks.
* **Are there any known open-source vulnerabilities in the application's dependencies?**
  * **Details:** Look into the dependencies. Are there any open-source components, and have there been vulnerabilities reported in these libraries? Keeping tabs on potential weaknesses in third-party code is crucial.
* **How frequently does the application undergo security assessments and testing?**
  * **Details:** Uncover the testing cadence. How often is the application subjected to security assessments, penetration testing, or vulnerability scans? Regular testing is key to maintaining a robust security posture.
* **What logging and monitoring mechanisms are in place for security events?**
  * **Details:** Examine the logging and monitoring setup. What security events are logged, and how is anomalous behavior detected? Establishing effective monitoring ensures swift responses to potential security incidents.
* **Is there a formal incident response plan in case of a security breach?**
  * **Details:** Delve into the incident response strategy. Is there a documented plan outlining steps to take in the event of a security breach? Preparedness is key to minimizing damage in the face of an attack.
* **How is user input validated and sanitized in the application?**
  * **Details:** Focus on input validation. How does the application handle user inputs? Ensuring proper validation and sanitization mitigates the risk of injection attacks and other vulnerabilities.
* **What encryption algorithms are used for sensitive data, and are they up-to-date?**
  * **Details:** Explore encryption further. Which encryption algorithms protect sensitive data, and are they using the latest standards? Regularly updating encryption methods is crucial for staying ahead of evolving threats.
* **Does the application utilize any Content Delivery Network (CDN), and if so, how is it secured?**
  * **Details:** Look into CDN usage. If the application relies on a CDN, ensure it's secured. CDNs can introduce security challenges, and understanding how they're managed is essential.\\



## <mark style="color:green;">AUTOMATED VULNERABILITY DISCOVERY</mark>



{% hint style="info" %}
Bug bounty hunters often clash over whether to scan for known vulnerabilities using automated tools.&#x20;
{% endhint %}

### <mark style="color:blue;">Nuclie</mark>

1. **First Pass Discovery:**
   * Imagine you've scouted a field during recon, and you stumble upon potential vulnerabilities. Using automated tools as your first sweep helps unearth these hidden gems before anyone else catches wind of them. It's like getting a head start on finding those valuable digital treasures. 🕵️‍♂️💻💰
2. **Swiss Army Toolkit:**
   * These tools, like the [Nuclei Scanner](https://github.com/projectdiscovery/nuclei), are not just one-trick ponies for CVEs. They're like digital detectives, helping you figure out what's going on in a web application. They sniff out login panels, test default credentials, and more. It's your versatile sidekick in the bug-hunting realm. 🔍🔐🚀
3. **Scaling Your Findings:**
   * If your own research uncovers a vulnerability that could be widespread, these tools let you automate and scan your discovery across multiple websites. It's like spreading your influence across the digital landscape, turning your findings into a powerful force. 🔄💡💻

* **Nuclei Scanner Details:**
  * Developed by the [Project Discovery team](https://github.com/projectdiscovery), it's a powerhouse tool with:
    * 1000+ CVE checks
    * 100+ information detections
    * 500+ admin panel detections
    * 1500+ other checks including credentials and keys
    * 67 subdomain takeover checks
    * HTTP form brute force capabilities
    * A whopping 3420+ templates for diverse testing scenarios. 🚀🛠️💼
* **Extensions:**
  * Nuclei can be supercharged with additional projects like [AllForOne](https://github.com/projectdiscovery/all-for-one) and [Cent](https://github.com/projectdiscovery/cent). But here's the catch: more templates don't always mean more value. Some may be duplicates, and others might not be useful at all. It's like having a bag of tricks; you need to pick the right ones. 🧰🤔

### <mark style="color:blue;">RetireJS: The Vigilant Guardian</mark>

* **Standalone Mastery:**
  * RetireJS, in its standalone brilliance, excels at the noble task of identifying outdated JavaScript libraries, ensuring your web applications stand resilient against potential vulnerabilities.
* **BurpSuite Integration:**
  * Now, picture this guardian extending its protective wings into the realm of BurpSuite. It transforms into a powerful extension, harmonizing with various tools and enhancing your cybersecurity arsenal.

#### Why Choose RetireJS in BurpSuite?

* **Comprehensive JavaScript Security:**
  * By integrating RetireJS into BurpSuite, you ensure a comprehensive approach to JavaScript-related security. It becomes an ever-watchful companion, guarding against vulnerabilities stemming from outdated libraries.
* **Adaptability Across Tools:**
  * The beauty of RetireJS lies not just in its standalone capabilities but in its adaptability as a BurpSuite extension. It seamlessly integrates into various tools, becoming a versatile asset in your cybersecurity toolkit.

#### How to Harness RetireJS in BurpSuite?

* **Explore the Extension:**
  * Head to the BurpSuite BApp Store and unveil the RetireJS extension [here](https://portswigger.net/bappstore/ShowBappDetails.aspx?uuid=3bfe33d0d6c24cbca9ed5b29c7c368c3).
* **Installation Guide:**
  * Follow the installation steps provided in the BApp Store, effortlessly incorporating RetireJS into your BurpSuite environment.

### [Naabu](https://github.com/projectdiscovery/naabu)

* Naabu is a port scanning tool written in Go that allows you to enumerate valid ports for hosts in a fast and reliable manner. It is a really simple tool that does fast SYN/CONNECT/UDP scans on the host/list of hosts and lists all ports that return a reply.



## <mark style="color:green;">CONTENT DISCOVERY</mark>

> **Content discovery** content discovery is the part of web application testing where trying to discover all the routes path, parameters, function and files of application sometime content discovery can also be known as a directory brute forcing.

### <mark style="color:purple;">Types of Content Discovery:</mark>

#### 1. Tech-Based Discovery:

Identify content based on the technologies utilized by the application. Tools like [BuiltWith](https://builtwith.com/) and [Wappalyzer](https://www.wappalyzer.com/) can provide insights into the technologies used.

#### 2. Known Pathing (Install, Demo, Leaked):

Utilize known paths, installations, or leaked information for content discovery, categorized into:

* **Local Install:**
  * Download open-source projects locally, install them, and point them at BurpSuite.
  * Use tools like [Daniel Miessler's Source2URL](https://danielmiessler.com/study/url_hacking/#tool-source2url) to map application routes.
* **Demo Instances:**
  * Access demo instances of paid software through BurpSuite, capturing admin functionality paths.
  * Check for vulnerabilities like IDOR during this process.
* **Installed and Leaked:**
  * Search DockerHub or GitHub for installed instances or accidentally leaked source code.
  * Gain insights into complete source code or modifications posted on GitHub.

#### 3. Custom Discovery:

Use custom wordlists for context-specific content discovery:

* **Custom Wordlists:**
  * Create wordlists based on contextual words related to the application.
  * Tools like [WordlistGen](https://github.com/txthinking/wordlistgen) can assist in generating custom wordlists.

#### 4. Historical Discovery:

Explore archived URL data from sources such as the Wayback Machine, AlienVault, Common Crawl, and URLScan:

* **Historical Discovery (Tip: Recursion):**
  * Investigate 401 unauthorized responses recursively, exploring resources beyond that path.
  * Use the Wayback Machine to check historical authentication configurations.
  *   Example:

      ```
      https://someapp.com/admin/  401
      https://someapp.com/admin/dashboard/    401
      https://someapp.com/admin/dashboard/member  200
      ```

#### 5. Spidering:

Employ tools like Turbo Intruder, Gobuster, FFuF, Dirsearch, Wfuzz, Feroxbuster for systematic content discovery:

#### 6. Mobile Discovery:

Extract additional routes and API endpoints from mobile application binaries using tools like APILeaks and [MobSF](https://mobsf.live/):

* **Mobile Discovery (Tip: Mobile):**
  * Include mobile API testing within the scope for comprehensive coverage.

### <mark style="color:purple;">Content Discovery (Tech-Based)</mark>

#### Content Discovery Tools: Your Cyber Sherpas

&#x20;**Turbo Intruder:**

* A powerhouse in the content discovery expedition, Turbo Intruder excels in propelling requests with speed and precision, unraveling hidden routes.

&#x20;**Gobuster:**

* The vigilant wanderer, Gobuster, embarks on a journey of directory brute-forcing, meticulously scanning for concealed paths and files.

&#x20;**Ffuf:**

* Armed with flexibility, Ffuf becomes the versatile explorer, allowing customizable fuzzing to uncover what traditional methods might miss.

&#x20;**Dirsearch:**

* In the quest for discovery, Dirsearch traverses directories, revealing the subtle nuances and uncharted territories within web applications.

&#x20;**Wfuzz:**

* Wfuzz, a multifaceted companion, adapts to varied discovery scenarios, efficiently probing for hidden parameters, paths, and functions.

&#x20;**Feroxbuster:**

* A dynamic force in the arsenal, Feroxbuster tirelessly scans for hidden gems, complementing the seeker's quest for uncharted territories.

## <mark style="color:purple;">Content Discovery (Known Path)</mark>

> Kown Path discovery involbes finds application routes paths and parameters of open sources projects demos versions and uninentionally leaded resources.

**1. Understanding the App's Roots: Open or Paid?**

* **Open-source:** Developed collaboratively and freely accessible.
* **Paid software:** Commercial product with restricted access.

**2. Your Toolkit: Local, Demo, Installed, Leaked**

**- Local Installations:**

* Dive into open-source projects. Install them locally, using BurpSuite to reveal secrets.
  * [Daniel Miessler's Source2URL Tool](https://danielmiessler.com/projects/source2url/)

**- Demo Adventures:**

* For paid apps, explore demo versions with BurpSuite. Grab admin insights - paths, routes, and parameters.
  * [BurpSuite](https://portswigger.net/burp)

**- Installed and Leaked Sagas:**

* Uncover paid software sans demo. DockerHub and GitHub may expose the entire code.
  * [DockerHub](https://hub.docker.com/)
  * [GitHub](https://github.com/)

**3. The Big Reveal: Full Path Discovery**

Combine the following methods for comprehensive discovery:

* **Local installs:** Uncover default paths and configurations.
* **Demo insights:** Identify hidden features and vulnerabilities.
* **Leaked resources:** Analyze exposed code for additional insights.

### <mark style="color:purple;">Local Content Discovery (known Path)</mark>&#x20;

**1. Download and Install:**

* Select an open-source project, download it, and install it on your local machine.

**2. Place in Web Root:**

* Position the installed project in the web root directory of your personal installation.

**3. Connect to Burp:**

* Direct the project to BurpSuite, activating its formidable capabilities.

**4. Run Shell Script:**

* Execute a purpose-built shell script to extract all existing directories.

**5. Proxy Through Burp:**

* Marvel as the script unveils directories, proxying them through Burp at your new target domain.

**6. Default Paths Revealed:**

* Explore a trove of default paths exposed during basic installations of open-source software.

**7. Open Source Mapping:**

* Harness Daniel Miessler's [Source2URL tool](https://github.com/danielmiessler/) to map application routes and endpoints.

**8. Proxy Back Through Burp:**

* Channel mapped routes and endpoints back through BurpSuite, concluding the local content discovery journey.

### Content Discovery (known Path): Demo Uncover

**1. Identify Paid Software:**

* Determine if the application is a paid software product.

**2. Seek Demo Instances:**

* Explore the availability of demo instances or check for a demo request process offered by the software vendor.

**3. Gain Demo Access:**

* Obtain access to the demo instance to freely navigate and explore the application.

**4. Route Through BurpSuite:**

* Direct the application through BurpSuite for detailed examination and analysis.

**5. Grasp Pathing Details:**

* Capture crucial information such as paths, routes, and parameters while proxying through BurpSuite.

**6. Admin Functionality Check:**

* Ensure access to admin functionality during the demo exploration to uncover hidden features.

**7. Uncover Vulnerabilities:**

* Actively search for vulnerabilities, with a focus on potential issues like Insecure Direct Object References (IDOR).

**8. Exploit Admin Routes:**

* Exploit admin routes and functionalities to expose any security flaws or vulnerabilities.

**9. Demo Insights for Security:**

* Leverage the demo experience to gain valuable insights into the security aspects of the application.



### Content Discovery (Known Path) : Installed and Leaked&#x20;

#### Navigating Installed and Leaked Software Instances

**1. Identify Paid Software:**

* Identify the application as paid software lacking a demo for exploration.

**2. DockerHub Exploration:**

* Delve into DockerHub, a common platform for software deployment and distribution.

**3. Unintentional Source Exposure:**

* Developers may unintentionally expose source code alongside the application on DockerHub.

**4. Complete Source Code Access:**

* Capitalize on DockerHub's nature, providing access to the entire source code of installed instances.

**5. GitHub Discoveries:**

* Search for modifications or sections of the software on GitHub, expanding the scope of source code exploration.

**6. Source Code Insights:**

* Gain valuable insights into the application's source code for a profound understanding of its architecture.

**7. Leverage DockerHub Features:**

* Utilize DockerHub features to access software instances and explore associated source repositories.

**8. Uncover Developer Oversights:**

* Exploit inadvertent developer oversights that lead to source exposure on platforms like DockerHub.

**9. Comprehensive Source Exploration:**

* Conduct a thorough exploration, unveiling potential vulnerabilities embedded within the source code.



## <mark style="color:green;">Content Discovery: Crafting Custom Wordlists</mark>



**1. Identify Contextual Words:**

* Look at the application's purpose or industry and list related words.
* **Example for a banking app**: Words like `transaction`, `account`, `login`, `security`, `investment`, `portfolio`

**2. Make a Wordlist**

* Write the words into a plain text file, one word per line.
* Save it as something like `banking_wordlist.txt`.

3\. **Use the Wordlist for Brute Force**

*   Use a tool like [Feroxbuster](https://github.com/epi052/feroxbuster) for brute force exploration.

    ```bash
    feroxbuster --url https://banking-app.com/ --wordlist banking_wordlist.txt
    ```

4\. **Add Specific Terms**



* Customize your wordlist with app-specific terms or features.
* **Example**: If the banking app has investment features, add terms like `dividend`, `stocks`, `portfolio`.

5\. **Automate Wordlist Creation**

* Use tools to generate the wordlist.
  *   **WordlistGen**:

      ```bash
      bwordlistgen -o custom_wordlist.txt -s "banking, account, transaction, login"
      ```
  *   **Cewl** (scrapes words from the website):

      ```bash
      cewl https://banking-app.com -w custom_wordlist.txt
      ```
  *   **GUA** (gets domain paths):

      ```bash
      gua https://banking-app.com | cut -d '/' -f 3 | sort -u > custom_wordlist.txt
      ```

**6. Test the Wordlist**

* Feed your wordlist into tools like **Feroxbuster** or others to find hidden files and directories

{% code overflow="wrap" %}
```bash
feroxbuster --url https://banking-app.com/ --wordlist custom_wordlist.txt
```
{% endcode %}

**7. Refine and Improve**

* Keep adding new words based on what you find during testing.
* Remove irrelevant or duplicate terms to make the list more effective.



### <mark style="color:purple;">Content Discovery (Historical )</mark>&#x20;

> Use Historical archives to find old or forgotten application paths, files and configuration.&#x20;

**1. Wayback Machine Expedition:**

* The [Wayback Machine](https://archive.org/web/).  stores snapshots of websites over time.

```bash
wget -r -nc -np https://web.archive.org/web/https://example.com/
```

**2. Alienvault Excursion:**

*   AlienVault shows historical DNS data for a domain

    ```bash
    curl -s "https://otx.alienvault.com/api/v1/indicators/domain/example.com/passive_dns" | jq '.passive_dns[].hostname' | sort -u
    ```



**3. Common Crawl Adventure:**

* The  [Common Crawl](https://commoncrawl.org/)'s Explore a vast archive of crawled web data using **Common Crawl**.

```bash
aws s3 ls s3://commoncrawl/crawl-data/CC-MAIN-2020-24/ | awk '{print $4}'
```

**4. URL Scan Exploration:**

* The  [URL Scan](https://urlscan.io/).io shows past scanned data for URLs.

```bash
urlscan.io -q "domain:example.com" | jq '.results[].page.url'
```

**5. Waymore by Xnl-h4ck3r:**

* &#x20;The [Waymore by Xnl-h4ck3r](https://github.com/XNLH4CK3R/WayMore). to automate historical exploration.

```
waymore -u https://example.com/
```

**6. Archival Downloads and Insights:**

* Download archived responses to search for additional links or files.

```
wget -r -nc -np https://web.archive.org/web/https://example.com/
```

**7. Forgotten Paths:**

*   Search for broken or hidden paths in archived data.

    ```bash
    grep -r "404 Not Found" . | cut -d ' ' -f 3
    ```

**8. Comprehensive Archive Analysis:**

*   Analyze downloaded archives for links, directories, or hidden details.

    ```bash
    cat index.html | grep "href=" | cut -d '/' -f 3 | sort -u
    ```

**9. Waymore's Expertise:**

*   Leverage Waymore's expertise to navigate the historical web:

    ```bash
    waymore -u https://example.com/
    ```

### <mark style="color:purple;">Content Discovery (Tips and Recursion )</mark> &#x20;

**Tip: The Unseen Paths**

> Content discovery is trying to guess sensitive paths and files that might in the application but are not linked anywhere.

**Recursion Revelation: Decoding 401 Responses**

Encountering 401 Unauthorized responses is common during web assessments. To unravel the secrets, engage in recursive brute-force attempts on such paths. Resources beyond the initial path may lack the same access control, offering a potential gateway.

**Insightful Investigation with Wayback Machine**

1.  When faced with 401 responses:

    * **Path 1:** [https://someapp.com/admin/](https://someapp.com/admin/) - Status 401
    * **Path 2:** [https://someapp.com/admin/dashboard/](https://someapp.com/admin/dashboard/) - Status 401
    * **Path 3:** [https://someapp.com/admin/dashboard/member](https://someapp.com/admin/dashboard/member/) - Status 200

    **Why This Works:**

    * Developers might forget to apply the same access controls to deeper resources, leaving them accessible.
2. **Access Control Oversight:**
   * Sometimes, access control is overlooked, leading to 401 errors.
3. **HTTP 401 Code Significance:**
   * The HTTP 401 Unauthorized status indicates a lack of valid authentication credentials for the requested resource.
4. **Strategic Brute Forcing:**
   * Identifying /admin with a 401 error suggests the existence of an admin area. Proceed with brute-forcing (/admin/member) to unveil deeper layers.
5. **Path Triumph:**
   * Successfully brute-forcing /admin/member/dashboard yields a 200 status, exposing an admin dashboard.
6. **Wayback Machine Exploration:**
   * Use the [Wayback Machine](https://archive.org/web/)  to check if the application had **weaker authentication** in the past.



### <mark style="color:purple;">Content Discovery (Mobile Marvels)</mark>

**Tip: Explore Mobile App Binaries**

* Mobile apps often contain hidden pathways and APIs linked to their web counterparts.
* These APIs may lead to valuable endpoints on the main domain.
* Use tools like **APILeaks** and **MobSF** to analyze mobile app binaries (APK files).

**Mobile API Secrets**

1.  Analyze the APK File with MobSF(Mobile Security Framework)

    * Use [MobSF](https://mobsf.live/) to dissect APK files:
    * ```bash
      mobsf -f your_app.apk
      ```

    Explore the MobSF interface to find:

    * API keys
    * Endpoints
    * Configuration related to app brackend.
2. Extract API Paths with APILeaks
   * Use the [APILeaks](https://apileaks.net/) to uncover hidden API routes and endpoints:

```
apileaks analyze -a your_app.apk
```

Review the output for:

* API paths
* HTTP methods (GET, POST)
* Sensitive information (tokens, credentials).

**3. Expand the Scope**

* Include the discovered API paths in your testing scope.
* Many of these endpoints may still be active and accessible, leading to more attack surfaces.



***



## <mark style="color:green;">DNS Subdomain Discovery</mark>

> Aiming to discover hidden subdomains associated with a target domain. This method involves appending a comprehensive list of common subdomain names to the target domain and attempting DNS resolution, with the objective of revealing valid subdomains. This process helps uncover paths and files within an application that might not be accessible through regular means.

#### Why Perform Subdomain Bruteforcing?

* **Incomplete Passive DNS Data:** Passive DNS data might not cover all subdomains associated with the target.
* **New Subdomains:** Newly created subdomains may not have been crawled by internet crawlers.
* **Hidden Paths:** Subdomain bruteforcing can unveil hidden paths not accessible through conventional means.

#### puredns Features:

* **Massdns Integration:** Leverages Massdns for high-speed DNS resolution.
* **Effective Wildcard Detection:** Reduces false positives by effectively detecting wildcards.
* **Validation with Trusted Resolvers:** Filters out false positives by validating results using trusted resolvers.
* **Handling SERVFAIL Errors:** Defaults to retry on SERVFAIL errors, improving result reliability.

#### Steps to Use puredns:

#### 1. Install puredns and Massdns:

```bash
git clone https://github.com/blechschmidt/massdns.git
go install github.com/d3mondev/puredns/v2@latest
```

#### 2. Generate Public DNS Resolvers List:

Use `dnsvalidator` to generate a list of open public DNS resolvers.

```bash
git clone https://github.com/vortexau/dnsvalidator.git
pip3 install -r dnsvalidator/requirements.txt
pip3 install setuptools==58.2.0
dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 100 -o resolvers.txt
```

#### 3. Perform Subdomain Bruteforcing:

Use puredns with the generated resolvers list.

```bash
puredns bruteforce wordlist.txt example.com -r resolvers.txt -w output.txt
```

### <mark style="color:purple;">Puredns : Subdomain Bruteforcing</mark>

Puredns stands out as a superior tool for DNS bruteforcing, excelling in speed and accuracy. It leverages mass DNS resolution using the Massdns tool, effectively detects wildcards, and ensures result reliability through validation with trusted resolvers. This guide will walk you through the steps to harness the power of Puredns for subdomain discovery.

#### Installation:

```bash
# Clone Massdns repository
git clone https://github.com/blechschmidt/massdns.git

# Install Puredns
go install github.com/d3mondev/puredns/v2@latest

# Clone dnsvalidator repository
git clone https://github.com/vortexau/dnsvalidator.git

# Install dnsvalidator dependencies
pip3 install -r dnsvalidator/requirements.txt
pip3 install setuptools==58.2.0
```

#### <mark style="color:purple;">Generating Public DNS Resolvers List</mark>:

#### Using dnsvalidator:

```bash
# Generate public DNS resolvers list
dnsvalidator -tL https://public-dns.info/nameservers.txt -threads 100 -o resolvers.txt
```

#### Downloading Pre-populated List:

Various contributors maintain a pre-populated list of valid DNS resolvers. Trickest has a consolidated repository called "resolvers."

```bash
wget https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt
```

**Note:** Periodically update your public DNS resolvers list to ensure optimal performance.

### Performing Subdomain Bruteforcing:

#### Using Puredns:

```bash
# Brute force subdomains using Puredns
puredns bruteforce wordlist.txt example.com -r resolvers.txt -w output.txt
```

* `bruteforce`: Specifies the bruteforcing mode.
* `-r resolvers.txt`: Specifies your public resolvers.

**Note:** Puredns retries on SERVFAIL errors, enhancing result reliability compared to most tools.

#### <mark style="color:purple;">Wordlists for Subdomain Bruteforcing</mark>:

1. [Assetnote best-dns-wordlist.txt](https://github.com/assetnote/commonspeak2-wordlists/blob/master/wordlists/best-dns-wordlist.txt): Comprehensive wordlist for effective subdomain discovery.
2. [n0kovo\_subdomains\_huge.txt](https://github.com/n0k0/certspotter-scans/blob/master/subdomains/n0kovo_subdomains_huge.txt): Large wordlist created by scanning the entire IPv4 range.
3. [Smaller wordlist](https://github.com/six2dez/OneListForAll/blob/master/SmallSubDomains.txt): A smaller wordlist suitable for personal use.
4. [orwagodfather wordlist](https://github.com/orwagodfather/WordList) . A wordlist by orwa.

#### <mark style="color:purple;">Subdomain Wordlists</mark>:

1. **SecLists by Daniel Miessler:**
   * [SecLists](https://github.com/danielmiessler/SecLists)
   * A collection of multiple lists, including subdomain wordlists, useful for diverse applications.
2. **FuzzDB by ethicalhack3r:**
   * [FuzzDB](https://github.com/fuzzdb-project/fuzzdb)
   * While primarily a fuzzing database, it includes valuable wordlists for subdomain discovery.

Puredns, with its robust features and integration with Massdns, is a powerhouse for DNS bruteforcing. Ensure a well-curated wordlist and stay updated with the latest public DNS resolvers for optimal results in subdomain discovery.

#### Additional Tools and Resources:

* [Massdns](https://github.com/blechschmidt/massdns): High-performance DNS stub resolver.
* [altdns](https://github.com/infosec-au/altdns): Generates permutations, alterations, and mutations of subdomains.
* [dnsgen](https://github.com/ProjectAnte/dnsgen): Generates domain permutations based on seed words.

#### <mark style="color:purple;">Wildcard Detection Techniques</mark>:

1. **Commonspeak Wildcard Tester:**
   * [Commonspeak Wildcard Tester](https://github.com/assetnote/commonspeak2-wordlists/blob/master/files/wildcard-detection/commonspk_wildcard_tester.py)
   * A Python script to test wildcard detection.
2. **Wildcard Security Implications:**
   * [Understanding Wildcard Security Implications](https://0xpatrik.com/wildcard-security-implications/)
   * An insightful article discussing the security implications of wildcard DNS records.

#### <mark style="color:purple;">Permutation and Alternative Scanning Tools:</mark>

1. **Altdns by Infosec-au:**
   * [Altdns](https://github.com/infosec-au/altdns)
   * GitHub repository for altdns, a tool to discover permutations in subdomains.

* Use tools like `altdns` and `dnsgen` for permutation/alternative scanning.
* Identify patterns in subdomains (e.g., dev, dev1) and generate alternative subdomain names.
* Combine with puredns for DNS resolution.

```bash
cat subdomains.txt | dnsgen - | puredns resolve --resolvers resolvers.txt
```

#### Generating Subdomain Permutations:

[Dnsgen](https://github.com/projectdiscovery/dnsprobe), a tool from the Project Discovery toolkit, facilitates the generation of subdomain permutations. It doesn't resolve them but creates a list of possible subdomains based on permutations and alternations.

```bash
# Generate subdomain permutations with dnsgen
cat subdomain.txt | dnsgen - > permutations.txt
```

#### Resolving Permutations with Puredns:

[Puredns](https://github.com/d3mondev/puredns), being an efficient DNS resolution tool, can be used to resolve the generated subdomain permutations.

{% code overflow="wrap" %}
```bash
# Resolve subdomain permutations with puredns
cat permutations.txt | puredns resolve --resolvers resolvers.txt -w resolved_permutations.txt
```
{% endcode %}

1. **Dnsgen by ProjectDiscovery:**
   * [Dnsgen](https://github.com/projectdiscovery/dnsprobe)
   * Part of the dnsprobe toolset, dnsgen generates permutations of subdomains.

#### <mark style="color:purple;">DNS Resolution Tools</mark>:

1. **Massdns by Blechschmidt:**
   * [Massdns](https://github.com/blechschmidt/massdns)
   * GitHub repository for massdns, used as the base tool for DNS querying in puredns.
2. **Puredns by D3mondev:**
   * [Puredns](https://github.com/d3mondev/puredns)
   * GitHub repository for puredns, a wrapper and feature-enhanced version of massdns.

#### <mark style="color:purple;">Public DNS Resolvers</mark>:

1. **DNSValidator by Vortexau:**
   * [DNSValidator](https://github.com/vortexau/dnsvalidator)
   * GitHub repository for DNSValidator, a tool to generate a list of open public DNS resolvers.
2. **Trickest Resolvers Repository:**
   * [Trickest Resolvers](https://github.com/trickest/resolvers)
   * A merged list of DNS resolvers validated every 24 hours, aggregating contributions from various sources.

#### Post-Recon Image Analysis with Exif Tools:

After reconnaissance, consider using [ExifTool](https://exiftool.org/) for image analysis. It extracts metadata from images, potentially revealing additional information.

```bash
# Install exiftool
# On Linux: sudo apt-get install libimage-exiftool-perl
# On macOS: brew install exiftool

# Analyze images with exiftool
exiftool image.jpg
```

### Issues and Solutions:

1. **Crashes on Low Specs:**
   * Use the `--wildcard-batch` flag in puredns to process subdomains in batches during wildcard filtering.
2. **Performance Impact on Home Router:**
   * Utilize the `-l` flag to limit the rate of DNS queries to public resolvers, preventing excessive traffic.

#### Overcoming Common Issues:

**1. Crashes on Low Specs (1 CPU/1GB VPS):**

If running on a low-spec VPS, memory issues may arise with large wordlists. Use the `--wildcard-batch` flag in puredns to process subdomains in batches.

```bash
# Overcome memory issues with --wildcard-batch flag
puredns bruteforce wordlist.txt example.com -r resolvers.txt -w output.txt --wildcard-batch 1000000
```

**2. Puredns Consuming Excessive Bandwidth:**

Puredns, leveraging massdns, might lead to bandwidth consumption. Mitigate this by using the `-l` flag to rate limit DNS queries to public resolvers.

```bash
# Rate limit DNS queries to avoid excessive bandwidth usage
puredns bruteforce wordlist.txt example.com -r resolvers.txt -w output.txt -l 5000
```

Adjust the values for `--wildcard-batch` and `-l` based on the available resources and network conditions to ensure efficient and reliable subdomain bruteforcing.



### <mark style="color:purple;">Validating We</mark>b

```bash
cat subdomains.txt | httpx -random-agent -retries 2 -threads 150 -no-color -ports 81,300,591,593,832,981,1010,1311,1099,2082,2095,2096,2480,3000,3128,3333,4243,4567,4711,4712,4993,5000,5104,5108,5280,5281,5601,5800,6543,7000,7001,7396,7474,8000,8001,8008,8014,8042,8060,8069,8080,8081,8083,8088,8090,8091,8095,8118,8123,8172,8181,8222,8243,8280,8281,8333,8337,8443,8500,8834,8880,8888,8983,9000,9001,9043,9060,9080,9090,9091,9200,9443,9502,9800,9981,10000,10250,11371,12443,15672,16080,17778,18091,18092,20720,32000,55440,55672 -o output.txt
```

Explanation:

* `cat subdomains.txt`: Reads the list of subdomains from the file "subdomains.txt."
* `httpx`: The tool used for web probing.
* `-random-agent`: Sends random User-Agent headers to mimic different browsers, making it more challenging for the target to identify automated requests.
* `-retries 2`: Specifies the number of retries for failed requests. Useful for dealing with intermittent network issues.
* `-threads 150`: Sets the number of threads for concurrent probing. Higher thread count can increase the speed of the scanning process.
* `-no-color`: Disables colorized output. Useful when saving results to a file or for better readability in certain environments.
* `-ports`: Specifies a list of ports to check for each subdomain. This allows for a more extensive examination, as different services may run on different ports.
* `-o output.txt`: Saves the results to a file named "output.txt." It's good practice to save the output for later analysis and reporting.



## <mark style="color:green;">JavaScript Analytics</mark>

> Analyzing JavaScript files for paths and routes is crucial in

### <mark style="color:purple;">**JavaScript Analytics with GAP in Burp Suite**</mark>

**What is GAP?**

* GAP (GitHub Analysis Processor) is a Burp Suite extension by Xnl for analyzing JavaScript files.
* It helps find hidden paths, routes, and potential vulnerabilities in web applications.

**How to Use GAP:**

1. **Install GAP:**
   * Download and install GAP from its [GitHub repository](https://github.com/).
2. **Scope-Based Extraction:**
   *   Extract JavaScript file data within a specific scope:

       ```bash
       gap_cmd --scope https://example.com
       ```
3. **Analyze JavaScript:**
   * Extract data from:
     * Standalone JavaScript files.
     * Inline JavaScript embedded in HTML.
4. **Benefits:**
   * Seamlessly integrates with Burp Suite.
   * Finds security issues, hidden paths, and important parameters.

### <mark style="color:purple;">**JavaScript Audit with Metasec.js**</mark>

**What is Metasec.js?**

* A tool by @lewisarden for scanning and auditing JavaScript files.
* Uses static analysis tools like **npm-audit**, **yarn-audit**, and **semgrep** to identify:
  * Dependency vulnerabilities.
  * Secrets and security issues in the code.

**How to Use Metasec.js:**

1. **Download and Setup:**
   * Get Metasec.js from its [GitHub repository](https://github.com/).
   *   Install dependencies:

       ```bash
       npm install
       ```
2. **Run Metasec.js:**
   *   Analyze JavaScript files:

       ```bash
       node metasec.js your_file.js
       ```
3. **How it Works:**
   * **npm-audit** and **yarn-audit** check for vulnerabilities in dependencies.
   * **Semgrep** performs static code analysis to find secrets and bugs.

**Benefits of Metasec.js:**

* Combines dependency checks and static analysis.
* Easy to integrate into JavaScript security testing workflows.
* Helps uncover hidden security flaws in the code.





### <mark style="color:purple;">The Power of Gospider: Subdomain Discovery with JS Files</mark>

#### A Comprehensive Guide to Harnessing Gospider for Subdomain Enumeration

#### Step 1: Web Probing Subdomains

**1.1 Web Probe Subdomains:**

```bash
cat subdomains.txt | httpx -random-agent -retries 2 -no-color -o probed_tmp_scrap.txt
```

* `cat`: Concatenate and display the content of subdomains.txt.
* `httpx`: Web probe tool to check the availability of subdomains.
* `-random-agent`: Use a random user agent for each request.
* `-retries 2`: Retry failed requests up to 2 times.
* `-no-color`: Disable colorized output.
* `-o probed_tmp_scrap.txt`: Save the probed subdomains to a temporary file.

**1.2 Crawl with Gospider:**

```bash
gospider -S probed_tmp_scrap.txt --js -t 50 -d 3 --sitemap --robots -w -r > gospider.txt
```

_Options:_

* `-S`: Input from the web-probed subdomains.
* `--js`: Extract links from JavaScript files.
* `-t`: Number of threads (run sites in parallel).
* `-d`: Depth (scrape links from second-level JS files).
* `--sitemap`: Crawl sitemap.xml.
* `--robots`: Crawl robots.txt.
* `-w`: Save results to files.
* `-r`: Include the raw content of JS files in the output.

**1.3 Handling URL Length:**

```bash
sed -i '/^.\{2048\}./d' gospider.txt
```

* `sed`: Stream editor for filtering and transforming text.
* `'/^.\{2048\}./d'`: Delete lines exceeding 2048 characters in length.

#### Step 2: Extracting Subdomains

**2.1 Extract Subdomains:**

```bash
cat gospider.txt | grep -Eo 'https?://[^ ]+' | sed 's/]$//' | unfurl -u domains | grep ".example.com$" | sort -u > scrap_subs.txt
```

_Breakdown:_

* `grep`: Extract links starting with http/https.
* `sed`: Remove " ] " at the end of the line.
* `unfurl`: Extract domain/subdomain from the URLs.
* `grep`: Select subdomains of the target.
* `sort`: Avoid duplicates.

#### Step 3: Resolving Subdomains

**3.1 DNS Resolve and Check Valid Subdomains:**

```bash
puredns resolve scrap_subs.txt -w scrap_subs_resolved.txt -r resolvers.txt
```

* `puredns`: A tool for DNS resolution and subdomain discovery.
* `resolve`: Subcommand for resolving subdomains.
* `scrap_subs.txt`: Input file containing subdomains.
* `-w scrap_subs_resolved.txt`: Output file to save resolved subdomains.
* `-r resolvers.txt`: File containing DNS resolvers.

This technique not only discovers subdomains but also provides an opportunity to find hidden Amazon S3 buckets. Ensure to leverage the output by further examining with tools like secretfinder to uncover hidden secrets and exposed API tokens.&#x20;

JavaScript files are used by modern web applications to provide dynamic content that contains various functions & events. Each website includes JS files and is a great resource for finding those internal subdomains used by the organization.

[Gospider](https://github.com/jaeles-project/gospider) is a fast web spidering tool capable of crawling the whole website within a short amount of time. This means Gospider will visit/scrap each and every URL mentioned in the JS file and source code. Since source code & JS files make up a website, they may contain links to other subdomains too.

This process is divided into 3 Steps:

1.  **Web Probing Subdomains:**

    * Web probe all the subdomains gathered so far using [httpx](https://github.com/projectdiscovery/httpx).

    ```bash
    cat subdomains.txt | httpx -random-agent -retries 2 -no-color -o probed_tmp_scrap.txt
    ```

    * Send the probed URLs for crawling to Gospider.

    ```bash
    gospider -S probed_tmp_scrap.txt --js -t 50 -d 3 --sitemap --robots -w -r > gospider.txt
    ```

    * Remove lines with URLs exceeding 2048 characters.

    ```bash
    sed -i '/^.\{2048\}./d' gospider.txt
    ```
2.  **Extracting Subdomains:**

    * Extract subdomains from the Gospider output using [unfurl](https://github.com/tomnomnom/unfurl).

    ```bash
    cat gospider.txt | grep -Eo 'https?://[^ ]+' | sed 's/]$//' | unfurl -u domains | grep ".example.com$" | sort -u > scrap_subs.txt
    ```
3.  **Resolving Subdomains:**

    * DNS resolve and check for valid subdomains using [puredns](https://github.com/d3mondev/puredns).

    ```bash
    puredns resolve scrap_subs.txt -w scrap_subs_resolved.txt -r resolvers.txt
    ```

> This technique not only finds subdomains but also identifies hidden Amazon S3 buckets. The output can be further analyzed with tools like secretfinder to uncover hidden secrets and exposed API tokens.



