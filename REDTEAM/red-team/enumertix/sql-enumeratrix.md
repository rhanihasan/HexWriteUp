---
description: its a Language used for Database management being Enumerated.
---

# SQL Enumeratrix

## Microsoft SQL

> * &#x20;Microsoft SQL Server is a database management system developed by Microsoft&#x20;
> * &#x20;As a database server  it is a software product with the primary function of storing and retrieving data as requested by other software applications which may run either on the same computer or on another computer across a network (including the Internet).
> * MSSQL is backend language that solve queres it is from Microsoft paid version.
>   * 1433 - Used by clients to interact with the database
>   * 1434 - Used to list available instances (a Server can run multiple instances on high ports)
> * Default credentials are often set to sa:sa, which sa is Sysadmin/system admin.





### Network Mapper

> Nmap

```
nmap -Pn -n -sV -p 1433,1434 #TARGETIP
nmap -Pn -n -sV -p 1433,1434 -sC=mssql-* #TARGETIP
```

### BruteForce

```
medusa -h #TARGETIP -u 'username' -p 'password' -M mysql
```

### Accessing SQL

```
mysql -h #TARGETIP -u root -p
```

## MYSQL

> Its an open sources SQL Database management system deveploed and supported by Oracle.
>
> There are multilpy database to stored data mostly SQL is used becuase of it interreat with those databases&#x20;
>
> It a mode of Communication data \[unne dena / dekha yeh sab handle karte hai]
>
> &#x20;MSSQL >> open source >> if you are performing an attack in a small org, or someone who have limited scope . Can assume that the application could be MSQL Because they are already tired with the budget
>
> It used port Number 3306.

### Network Mapper

```
nmap -sV -Pn -n -p 3306 #TARGETIP
```

> Wireshark Packet

<figure><img src="../../.gitbook/assets/image (7).png" alt=""><figcaption></figcaption></figure>

```
nmap -Pn -n -p 3306 --script=mysql-*.nse #targetip
```

> Wireshark Packet

<figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>

### BruteForce

```
hydra -l username-p password mysql://TARGETIP
medusa -h TARGETIP -u username -P password.list  -M mysql 
```

### Discovery

<table data-header-hidden><thead><tr><th valign="top"></th><th valign="top"></th></tr></thead><tbody><tr><td valign="top"><p># Try connection from outside</p><p>-u for username -p for database name.</p><p>mysql --host &#x3C;IP> -u root -p root</p><p>       </p><p># Connection from the target machine</p><p>mysql -u root -p root database</p><p> </p><p> </p><h4 id="toc142939263">Classical commands </h4><p>show databases;</p><p>use database_name;</p><p>show tables;</p><p>describe table_name;</p><p>select host, user, password from mysql.user;</p><p> </p></td><td valign="top"><h3 id="toc142939264">Local Access / Remote Access</h3><p>if you gain access to target box and see mysql running , you can try to connect with it from target locally</p><p>mysql -u root</p><p># Connect to root without password</p><p>mysql -u root -p</p><p># A password will be asked</p><p># Always test root:root credential</p><p> </p></td></tr><tr><td valign="top"><p>┌──(root㉿Kali-Linux-full)-[/home/hasanrehni/credentails]</p><p>└─# mysql -h 192.168.100.130 -u root -p</p><p>Enter password:</p><p>Welcome to the MariaDB monitor.  Commands end with ; or \g.</p><p>Your MySQL connection id is 90</p><p>Server version: 5.0.96-0ubuntu3 (Ubuntu)</p><p> </p><p>Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.</p><p> </p><p>Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.</p><p> </p><p>MySQL [(none)]> show databases;</p><p>+--------------------+</p><p>| Database           |</p><p>+--------------------+</p><p>| information_schema |</p><p>| bWAPP              |</p><p>| drupageddon        |</p><p>| mysql              |</p><p>+--------------------+</p><p>4 rows in set (0.001 sec)</p><p> </p><p>MySQL [(none)]> use mysql;</p><p>Reading table information for completion of table and column names</p><p>You can turn off this feature to get a quicker startup with -A</p><p> </p><p>Database changed</p><p>MySQL [mysql]> show tables;</p><p>+---------------------------+</p><p>| Tables_in_mysql           |</p><p>+---------------------------+</p><p>| columns_priv              |</p><p>| db                        |</p><p>| func                      |</p><p>| help_category             |</p><p>| help_keyword              |</p><p>| help_relation             |</p><p>| help_topic                |</p><p>| host                      |</p><p>| proc                      |</p><p>| procs_priv                |</p><p>| tables_priv               |</p><p>| time_zone                 |</p><p>| time_zone_leap_second     |</p><p>| time_zone_name            |</p><p>| time_zone_transition      |</p><p>| time_zone_transition_type |</p><p>| user                      |</p><p>+---------------------------+</p><p>17 rows in set (0.001 sec)</p><p> </p><p>MySQL [mysql]></p></td><td valign="top"></td></tr></tbody></table>
