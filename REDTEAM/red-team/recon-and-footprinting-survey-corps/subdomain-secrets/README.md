---
description: Subdomain Enumeration is also known as Vertical domain.
---

# Subdomain Secrets

### <mark style="color:purple;">Vertical Enumeration.</mark>

Vertical Enumeration, also known as Vertical Domain Correlation, involves discovering hosts located on the same root domain by exploring various levels of subdomains. This process can be automated and utilizes several techniques:

<figure><img src="../../../.gitbook/assets/Subdomains" alt=""><figcaption><p>Subdomains.</p></figcaption></figure>

### <mark style="color:purple;">What are we after ?</mark>

1. Passive Techniques:
   * Utilizing passive sources like Certificate Logs.
2. Active Techniques:
   * DNS brute forcing: Systematically guessing subdomains to find valid ones.
   * Generating permutations or alterations of known subdomains.
   * Scraping JavaScript or source code to uncover subdomains.
   * Discovering Virtual Hosts (VHOST) configurations.
   * Analyzing Google Analytics data for subdomain information.
   * Performing recursive enumeration to delve deeper into subdomains.
   * Probing for TLS, CSP, and CNAME records to gather subdomain data.
   * Employing regular expression (Regex) permutations to identify subdomains.
3. Web Probing:
   * Scanning for default and common ports associated with subdomains.

Using these methods, vertical enumeration can map out all the smaller areas within a main website domain, helping in gathering information and checking for possible security issues.



## <mark style="color:green;">PREREQUISITIES</mark>

1. **API Keys for Passive DNS Data:**
   * Passive DNS data involves recording DNS queries made to DNS resolvers, revealing associations between domains and specific DNS records.
   * Various services and companies maintain databases of this historical DNS data, helping us identify subdomains of a particular root domain.
   * Two types of services: those allowing free queries and others requiring API keys for authorization.
   * Obtaining API keys can be challenging due to limitations like short validity periods, query quotas, and limited results.
2. **100% Accurate Open Public DNS Resolvers:**
   * DNS resolvers translate domain names into IP addresses.
   * Tools like MassDNS require a list of public DNS resolvers to check the validity of domains during enumeration.
   * Dnsvalidator is a tool that verifies and generates a valid list of open public DNS resolvers.
   * There are around 28.7K public resolvers, but not all may work; hence, dnsvalidator helps filter out the valid ones.
   * Alternatively, one can rely on periodically verified lists of DNS resolvers provided by security researchers.
3. **A VPS (Virtual Private Server):**
   * A VPS is a dedicated virtual machine in the cloud, offering higher bandwidth and better DNS resolution capabilities compared to a local router.
   * Essential for bandwidth-intensive tasks like DNS resolution and brute-forcing, which might disrupt a local Wi-Fi network.
   * Enables 24/7 operations, unlike a local system, and various cloud providers offer free credits for signing up.
     * [Digital Ocean](https://www.digitalocean.com/)
     * [Linode](https://www.linode.com/)
     * [Vultr](https://www.vultr.com/)

## <mark style="color:green;">Certificate Logs</mark>

**SSL/TLS Certificates:** SSL/TLS certificates are security measures that websites use to transition from "HTTP" to the more secure "HTTPS." These certificates, trusted by both the domain and its clients, encrypt communications. To obtain an SSL/TLS certificate, one needs to request it from a Certificate Authority (CA).

[**Certificate Transparency logs**](https://certificate.transparency.dev/) **:** Before 2013, CAs faced breaches that allowed malicious creation of forged certificates. Google's solution was Certificate Transparency logs, a central repository for all issued certificates. This transparency helps prevent fraudulent certificate issuance, ensuring domain owners can spot unauthorized certificates.

**Abusing CT Logs:** CT logs can be abused to enumerate subdomains with associated TLS certificates. Tools like CTFR leverage Certificate Transparency logs to query and retrieve subdomains for a target domain.

### [**CTFR**](https://github.com/UnaPibaGeek/ctfr) **Tool:**

* A Python-based tool, CTFR queries crt.sh and retrieves subdomains.
*   Example:

    ```bash
    git clone https://github.com/UnaPibaGeek/ctfr.git
    pip3 install -r requirements.txt
    python3 ctfr.py -d target.com -o output.txt
    ```

### [**Crt sh**](https://crt.sh/)[​](https://rhanihasan.github.io/cybersecurity/docs/CyberSecurity/CyberrSecurity360/Basic%20Enum,%20Info%20Gathering%20&%20Vulnerability%20Assessment#crt-sh) <a href="#toc142346654" id="toc142346654"></a>

* **It searches through the certificate fingerprint and domain name**

![cet-sh-results](<../../../.gitbook/assets/crt (1).sh>)

* **These three certs might be belonged to netplace**
* **The operator of the certificate is google and Cloudflare**
* [**tls.bufferover.run**](https://tls.bufferover.run/) **Service:**
  * Scans the IPv4 address space and extracts data from TLS certificates, including the "Subject" field.
  * The "CommonName (CN)" component in the Subject field indicates the Fully Qualified Domain Name (FQDN) of the host, helping identify subdomains.
  * An API key is required to query this service.
  *   Example:

      ```bash
      curl 'https://tls.bufferover.run/dns?q=.dell.com' -H 'x-api-key: YOUR_API_KEY' | jq -r .Results[] | cut -d ',' -f5 | grep -F ".dell.com" | sort -u > output.txt
      ```

### [Domain Collector](https://github.com/Cyber-Guy1/domainCollector)

* A simple tool to gather domain using Crh.sh.

### <mark style="color:blue;">TLS, CSP,CNAME,Finding</mark>

> **Understanding Website Security and Subdomain Discovery:**

Nowadays, most websites use HTTPS (HyperText Transfer Protocol Secure) for secure communication. To enable HTTPS, website owners issue SSL (Secure Socket Layer) or TLS (Transport Layer Security) certificates. These certificates contain hostnames belonging to the same organization. You can view the TLS/SSL certificate of a website by clicking on the "Lock🔒" button in the address bar.

<figure><img src="../../../.gitbook/assets/SSL certification dns check" alt=""><figcaption></figcaption></figure>

#### 1. Discovering Subdomains with Cero:

*   To find subdomains listed in a TLS certificate, use the tool Cero:

    ```bash
    go install github.com/glebarez/cero@latest
    cero sni.cloudflaressl.com | sed 's/^*.//' | grep -e "\." | sort -u
    ```

#### 2. Extracting Subdomains from CSP Headers:

*   To discover subdomains from CSP headers, follow these steps:

    ```bash
    cat subdomains.txt | httpx -csp-probe -status-code -retries 2 -no-color | anew csp_probed.txt | cut -d ' ' -f1 | unfurl -u domains | anew -q csp_subdomains.txt
    ```

    * This extracts domains/subdomains from the CSP headers of websites, which can be useful for security.

#### 3. Probing CNAMEs of Subdomains:

*   In some cases, visiting the CNAME of a website may bypass the firewall. To probe CNAMEs of discovered subdomains, use dnsx:

    ```bash
    dnsx -retry 3 -cname -l subdomains.txt
    ```

    * This step helps ensure a comprehensive understanding of the website's infrastructure.

