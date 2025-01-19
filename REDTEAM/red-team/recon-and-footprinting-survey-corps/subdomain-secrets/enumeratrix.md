---
description: >-
  It combines the concept of enumeration with a touch of adventure. Dive into
  the Enumeratrix Odyssey and chart the uncharted territories of information!
  🌐🚀😈
---

# Enumeratrix

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

