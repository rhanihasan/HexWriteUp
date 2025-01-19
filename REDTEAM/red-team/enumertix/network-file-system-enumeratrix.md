---
description: In this NFS Service is being Enumerated
---

# Network File System Enumeratrix

## Network File System

> Its allow files to share over the network. Its kindla similar to SMB.
>
> Its developed by Sun Mircosystem in 1984.
>
> Its also have guest session.
>
> Its used the port number 111 and 2049  on BOTH TCP/UDP for data Transfering and Validateing.  It used PPC protocol to Communicated.

### Version

| Version | Features                                                                                                                                                                                                                                                             |
| ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NFSv2   | It is older but is supported by many systems and was initially operated entirely over UDP.                                                                                                                                                                           |
| NFSv3   | It has more features, including variable file size and better error reporting, but is not fully compatible with NFSv2 clients.                                                                                                                                       |
| NFSv4   | It includes Kerberos, works through firewalls and on the Internet, no longer requires portmappers, supports ACLs, applies state-based operations, and provides performance improvements and high security. It is also the first version to have a stateful protocol. |

### Network Mapper

```
Nmap –n -Pn -v -p 111,2049 Target-IP
rpcinfo -p TARGETIP
nmap -sV -p 111 --script=rpcinfo #TAREGETIP
nmap -p 111 --script nfs* TARGETIP

```

### MOUNTS

> the NFS mounts the directory.

```
showmount -e #TARGETIP
```

> Wiresharks

<figure><img src="../../.gitbook/assets/image (9).png" alt=""><figcaption></figcaption></figure>

#### MOUNTING THE SHARES.

> Now the directory is seems & knowns which can be  Mount & linked the Directorys for future Enumerations.
>
> Mount will link the shared directory.
>
> Mount will be a link the source folder to the target nfs shares. Its require sudo permissions to mount , the folder should be empty before mounting.
>
> Both have the common which is id called :1000

<table data-header-hidden><thead><tr><th valign="top"></th><th></th></tr></thead><tbody><tr><td valign="top"><h4>Syntax &#x26; Commands</h4></td><td></td></tr><tr><td valign="top"><p>mount -t nfs [-o vers=2] &#x3C;ip>:&#x3C;remote_folder> &#x3C;local_folder> -o nolock</p><p>You should specify to use version 2 because it doesn't have any authentication or authorization.</p><p>Example:</p><p>mkdir /mnt/new_back</p><p>mount -t nfs [-o vers=2] 10.12.0.150:/backup /mnt/new_back -o nolock</p><p> </p></td><td><p>first create the directory for mounting -</p><p>mkdir /mnt/nfs</p><p>mount -t nfs $ip:/share /mnt/nfs</p><p> </p></td></tr><tr><td valign="top"><p>                                                                                                                                                                                                                 </p><p>┌──(root㉿Kali-Linux-full)-[/home/hasanrehni]</p><p>└─# mount -t nfs 192.168.100.130:/mnt/nfs_share /home/hasanrehni/mntdir</p><p> </p><p>Created symlink /run/systemd/system/remote-fs.target.wants/rpc-statd.service → /lib/systemd/system/rpc-statd.service.</p><p> </p></td><td></td></tr></tbody></table>

#### UNMOUTING THE SHARES

> For unmounting #umount foldername of kali. (which is mounted)

```
umount -f -l /mnt/nfs
umount -f -l /home/hasanrehni/mntdir
```

