# Automations



## Automation

### ReconFTW for Subdomain Enumeration

#### Overview:

ReconFTW is a powerful tool for subdomain enumeration that incorporates six unique techniques. It automates the intensive steps involved in subdomain discovery, making it a comprehensive solution.

#### Installation:

Use the following commands to install ReconFTW:

```bash
git clone https://github.com/six2dez/reconftw
cd reconftw
./install.sh
```

#### Usage:

Perform subdomain enumeration using the `-s` flag:

```bash
./reconftw.sh -d example.com -s
```

Additional Tips:

* The tool can be configured through its config file to skip specific techniques.
* Provide your custom wordlist for subdomain bruteforcing in the config file.

#### Deep Mode:

Consider using `--deep` mode for a more thorough but time-consuming subdomain enumeration.

### Axiom for Distributed Workload

#### Overview:

Axiom is a dynamic infrastructure tool designed to distribute the workload of a single task among multiple cloud instances. It's particularly useful to avoid bans and reduce execution time during mass recon.

#### Supported Cloud Providers:

Digital Ocean, Linode, Azure, GCP, IBM

#### Installation:

Use the following commands to install Axiom:

```bash
git clone https://github.com/pry0cc/axiom ~/.axiom/
$HOME/.axiom/interact/axiom-configure
```

#### Initializing Fleet:

1. Divide the bruteforce wordlist into equal parts.
2. Transfer each part to respective instances.
3. Perform standalone execution on separate instances.
4. Merge the output results from all instances.

#### Integration with ReconFTW:

It's possible to integrate Axiom into ReconFTW for distributed subdomain enumeration. Use the `reconftw_axiom.sh` script:

```bash
./reconftw_axiom.sh -d example.com -s
```

#### GitHub Repositories:

* ReconFTW: [GitHub Repository](https://github.com/six2dez/reconftw)
* Axiom: [GitHub Repository](https://github.com/pry0cc/axiom)

Certainly! Let's delve into Osmedeus:

### Osmedeus: Automated Reconnaissance and Scanning

#### Overview:

Osmedeus is an open-source automated reconnaissance and scanning tool designed for offensive security professionals and penetration testers. It streamlines the process of information gathering, subdomain enumeration, and various scanning tasks, making it a comprehensive tool for reconnaissance.

#### Key Features:

1. **Subdomain Enumeration:**
   * Osmedeus performs subdomain enumeration using various techniques to discover potential targets and expand the scope of reconnaissance.
2. **Web Application Scanning:**
   * The tool incorporates multiple scanning modules for web applications, including vulnerability scanning, enumeration, and data extraction.
3. **Port Scanning:**
   * Osmedeus conducts port scanning to identify open ports on target systems, providing valuable information about potential attack vectors.
4. **Directory Brute-Forcing:**
   * The tool includes directory brute-forcing capabilities to identify hidden paths and files within web applications.
5. **Integration with Other Tools:**
   * Osmedeus integrates with popular reconnaissance tools such as Subfinder, Amass, Aquatone, and more, enhancing its capabilities.

#### Installation:

Clone the Osmedeus repository from GitHub:

```bash
git clone https://github.com/j3ssie/Osmedeus
cd Osmedeus
./install.sh
```

#### Basic Usage:

Run Osmedeus with the following command:

```bash
./osmedeus.py -t example.com
```



**1. Custom Configuration File:**

* Use a custom configuration file to define scanning modules, parameters, and other settings. Create a configuration file (e.g., `custom.conf`) and run Osmedeus with the `-C` flag:

```bash
./osmedeus.py -t example.com -C custom.conf
```

**2. Specify Modules:**

* Choose specific modules to run during the scanning process. For example, to run only subdomain enumeration and web scanning modules:

```bash
./osmedeus.py -t example.com -m subdomain,scan
```

**3. Exclude Modules:**

* Exclude specific modules from the scanning process. The following command excludes the directory brute-forcing module:

```bash
./osmedeus.py -t example.com -x dir
```

**4. Custom Wordlists:**

* Provide custom wordlists for subdomain enumeration, directory brute-forcing, and other tasks. Use the `-w` flag followed by the path to your wordlist:

```bash
./osmedeus.py -t example.com -m subdomain -w custom_wordlist.txt
```

**5. Report Generation:**

* Generate a detailed HTML report summarizing the results of the reconnaissance and scanning activities. Use the `-R` flag:

```bash
./osmedeus.py -t example.com -R
```

**6. Continuous Scanning:**

* Set up continuous scanning by specifying the interval (in seconds) between scans. The following command runs Osmedeus every 3600 seconds (1 hour):

```bash
./osmedeus.py -t example.com -i 3600
```

**7. Verbose Output:**

* Enable verbose output to see detailed information about each step of the scanning process. Use the `-v` flag:

```bash
./osmedeus.py -t example.com -v
```

**8. Integration with Axiom:**

* Osmedeus can be integrated with Axiom for distributed scanning. After setting up Axiom, run Osmedeus with the `-a` flag:

```bash
./osmedeus.py -t example.com -a
```

**9. Run Specific Recon Module:**

* Run a specific reconnaissance module individually. For example, run only the `subdomain` module:

```bash
./osmedeus.py -t example.com -M subdomain
```

**10. Custom API Keys:**

* For modules requiring API keys, use the `-K` flag to provide custom API keys (replace `your_api_key` with the actual key):

```bash
./osmedeus.py -t example.com -K shodan:your_api_key
```



### [Frogy](https://github.com/iamthefrogy/frogy)

* its an open source tool which is capably to find IPs,domains,subdomains,live website,login portals and more.
