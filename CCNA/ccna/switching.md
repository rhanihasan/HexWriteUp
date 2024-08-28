---
description: >-
  Switching is process to forward packets coming in from one port to a port
  leading towards the destination.
cover: ../.gitbook/assets/SWITCHING_LOGO.png
coverY: 0
layout:
  cover:
    visible: true
    size: hero
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Switching

### <mark style="color:purple;">Switch</mark>

> A switch is a Network Device operate under Layer 2 (Data Link Layer) of the OSI Model. Nowadays the Switches are evolve to L3 Switches.

> Its design to connect devices within the same local Network, Such as computer, Printers, And other Networked Devices.

> Switches use MAC Address and ARP to Forwarded data.

### <mark style="color:purple;">Ethernet Frame</mark>

> Ethernet frame is a packet that include ethernet headers.
>
> The minimum frame size is 64 bytes including the header packets in that there is desitnation MAC address, source MAC Address and Types etc. And to detect error Frame Check Sequence(FCS) is used.

### <mark style="color:purple;">**Switch Functions**</mark>

1. **Address Learning:** Switches learn MAC addresses by observing the source MAC address of incoming frames. They build and maintain a MAC address table.
2. **Forwarding Messages:** Switches use the MAC address table to make forwarding decisions. They forward frames only to the appropriate destination port.
3. **Loop Avoidance:** Switches use the Spanning Tree Protocol (STP) to prevent network loops, which can cause broadcast storms and network instability.

### <mark style="color:purple;">**Why Switches Are Essential**</mark>

* Switches provide efficient and fast data forwarding within LANs, reducing network congestion and improving performance.
* They enable devices to communicate directly with each other, minimizing unnecessary network traffic.
* Switches allow the segmentation of LANs into VLANs (Virtual LANs), improving network security and management.
* By learning MAC addresses, switches create efficient paths for data transmission, reducing broadcast domains.
* STP ensures network reliability by preventing loops and redundant paths.

### <mark style="color:purple;">**Initials Configurations**</mark>

| Step                              | Description                                                                                                                                                                        |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power Up the Devices              | Ensure all network devices are powered on and operational.                                                                                                                         |
| Connect to the Device via Console | Use terminal emulation software (e.g., PuTTY or SecureCRT) to establish a console connection to the network switch through the COM port.                                           |
| Privilege Levels                  | By default, users may have privilege level 0, requiring a username and password for access.                                                                                        |
| Enable Mode                       | Enter enable mode (user/enable mode) using the "`enable`" command to gain elevated privileges.                                                                                     |
| Interface Information             | - To view all interfaces and their status: use the "show ip interface brief" command. - To view details of a specific interface: use `show ip interface <interface>`               |
| Configuration Mode                | Enter global configuration mode using commands like "`configure terminal`" or "`conf t`." This mode provides full access with privilege level 15.                                  |
| Using "do" with Commands          | While in configuration mode, you can use show commands by prefixing them with "`do`," such as "`do show ip int brief.`"                                                            |
| Interface Configuration           | Configure interface settings (e.g., speed, duplex, description) using commands like: - `interface <interface>` - `speed <speed>` - `duplex <duplex>` - `description <description>` |
| Selecting Multiple Interfaces     | Use the "`interface range`" command to select and configure multiple interfaces simultaneously.                                                                                    |
| Set Switch Hostname               | Assign a name to the switch using the `hostname <name>` command.                                                                                                                   |
| Banner Message                    | Create a banner message that users see when they log in.                                                                                                                           |
| Console Password                  | Set a password for console access using the "`line console 0`" command.                                                                                                            |
| Enable Telnet                     | Configure virtual lines (vty) for Telnet access.                                                                                                                                   |
| Management IP Address             | Assign an IP address to the management interface (usually VLAN 1).                                                                                                                 |
| Set Passwords                     | Set an enable secret password for privileged mode.                                                                                                                                 |
| Set Default Gateway               | Configure the default gateway.                                                                                                                                                     |
| Clear Configurations              | To delete all configurations, use the "`write erase`" command.                                                                                                                     |
| Disable DNS Lookup                | Use "`no ip domain lookup`" to disable DNS lookups.                                                                                                                                |
| Enable IP Routing (L3 Switch)     | Configure IP routing on Layer 3 switches.                                                                                                                                          |
| Save Configurations               | Save configurations to memory or copy them to a TFTP server.                                                                                                                       |
| Check Interface Configurations    | Use "show run" to view running configurations.                                                                                                                                     |
| Check Time                        | View the switch's current time with `"show clock`."                                                                                                                                |
| Change Time                       | Set the time with the "`clock set`" command.                                                                                                                                       |
| Change Timezone                   | Configure the timezone using "`clock timezone`"                                                                                                                                    |
| Interface Shutdown/No Shutdown    | Use "`shutdown`" and "`no shutdown`" to disable/enable an interface.                                                                                                               |
| Interface Access Mode             | Set an interface to access mode with "`switchport mode access`."                                                                                                                   |
| Interface Trunk Mode              | Set an interface to trunk mode with "`switchport mode trunk`."                                                                                                                     |
| DTP Modes                         | Configure Dynamic Trunking Protocol (DTP) modes.                                                                                                                                   |
| Check ARP Table                   | View the Address Resolution Protocol (ARP) table with "show ip arp."                                                                                                               |
| Encapsulation                     | Configure encapsulation for interfaces using "switchport trunk encapsulation dot1q."                                                                                               |

## <mark style="color:purple;">**Virtual Local Area Network**</mark>



| Topic                                          | Description                                                                                                                                                                                                                                                                                        |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is VLAN (Virtual Local Area Network)?** | <p>VLAN, or Virtual Local Area Network, enhances network security by creating virtual partitions within a network. It isolates and segregates network traffic, making it act as a virtual wall between different parts of a network.<br>There are 4094 Vlan and VLAN 1 is default in switches.</p> |
| **Why Use VLANs?**                             | VLANs are used to improve network security and organization. They help segment a network into isolated parts, allowing different departments or groups to share the same network infrastructure while keeping their data separate and secure.                                                      |
| **Inter-Switch Link (ISL)**                    | **IEEE 802.1Q (Dot1q)**                                                                                                                                                                                                                                                                            |
| **Protocol Type**                              | Cisco Proprietary                                                                                                                                                                                                                                                                                  |
| **Header Modification**                        | Adds a proprietary 26-byte header to Ethernet frames, containing VLAN information.                                                                                                                                                                                                                 |
| **Compatibility**                              | Primarily used within Cisco environments; not compatible with non-Cisco devices.                                                                                                                                                                                                                   |
| **Supported VLANs**                            | Supports up to 1000 VLANs, suitable for large-scale networks.                                                                                                                                                                                                                                      |
| **Native VLAN**                                | Does not include Vlan Tags Used for managments purpose.                                                                                                                                                                                                                                            |
| **Tagging Process**                            | VLAN tagging occurs with the addition of a proprietary header at Layer 2.                                                                                                                                                                                                                          |
| **Dynamic Trunking Protocol (DTP)**            | **Three DTP modes**: Auto, Desirable, No Negotiate. Auto waits for commands from the other switch, Desirable initiates trunking, No Negotiate disables DTP.                                                                                                                                        |

### <mark style="color:blue;">Configuration of Vlans on Cisco Switch</mark>

#### <mark style="color:blue;">Access Port</mark>

> An Access port is switch port that can be a member of one VLAN.
>
> 1. Create a VLAN in the switch.
> 2. Add the VLAN into switch Ports.

{% code title="Create a Vlan" %}
```
SwitchX(config)# vlan 10
```
{% endcode %}

{% code title="Name the VLAN" %}
```
SwitchX(config-vlan)# name MGMT
```
{% endcode %}

> Now the VLAN is configured in switch, Assign the VLAN to port.

{% code title="Assiging the VLAN" %}
```
Switch(config)# interface Ethernet 0/0
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10
```
{% endcode %}

> Some versions of Cisco switches automatically create the VLAN in the VLAN Database when you assign an access port to a VLAN

```
Switch(config)# interface Ethernet 0/1
Switch(config-if)# switchport mode access	
Switch(config-if)# switchport access vlan 30
% Access VLAN does not exist. Creating vlan 30
```

#### <mark style="color:blue;">Trunk Ports</mark>

> A trunk port that carry more then one VLAN.

```
Switch(config)# interface Ethernet1/1
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk encapsulation dot1q
```

#### <mark style="color:blue;">Native VLAN</mark>

> Its a VLAN which is not tagged or untagged in the TRUNK Port.

{% code title="Native Vlan" %}
```
Switch(config)# interface Ethernet 1/1
Switch(config-if)# switchport trunk native vlan 2
```
{% endcode %}

#### <mark style="color:blue;">Allowed VLAN</mark>

> Particular VLAN is allowed on the interface.

```
Switch(config)# interface Ethernet 2/1
Switch(config-if)# switchport trunk allowed vlan 10,20
Switch(config-if)# switchport trunk allowed vlan all
```

#### <mark style="color:blue;">Show command</mark>

> View the VLAN and interface configuration.

```
Switch# show vlan brief
Switch# show interfaces trunk
Switch# show interfaces Ethernet 0/1 switchport
Switch# show running-config interface Ethernet 1/1

Switch#show interfaces status
interface Ethernet1/1
 switchport trunk encapsulation dot1q
 switchport trunk native vlan 2
 switchport trunk allowed vlan 1-10,20-4094
 switchport mode trunk
end 
```



{% hint style="info" %}
In Cisco and Fitpipe Vlan 0 is used for QOS Configuration and VLAN 1 is used as default with untagged VLAN.\
But in Juniper VLAN 0 is used a default VLAN and VLAN 1 is used as a custom VLAN.
{% endhint %}

## <mark style="color:purple;">**VLAN Trunking Protocol**</mark>

| **VTP (VLAN Trunking Protocol)** | **Description**                                                                                                                                      |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**                      | Simplifies VLAN configuration in networks with multiple switches by allowing one switch to configure VLANs and share that configuration with others. |
| **VTP Server Mode**              |  Default mode for all switches. - Can create, modify, and delete VLANs.                                                                              |
| **VTP Client Mode**              |  Cannot create or modify VLANs. - Receives VLAN information from VTP Servers.                                                                        |
| **VTP Transparent Mode**         |  Does not store VLAN information locally. - Passes VTP Server's VLAN configurations to connected switches.                                           |
| **Configuration (Server Mode)**  |  Set switch as a VTP Server: `vtp mode server` - Define VTP domain: `vtp domain Shadow` - Set VTP password: `vtp password ShadowGuardain`            |
| **Configuration (Client Mode)**  |  Set switch as a VTP Client: `vtp mode client` - Specify VTP domain: `vtp domain Shadow` - Set VTP password: `vtp password ShadowGuardain`           |

### <mark style="color:blue;">Configuration Of VTP on Cisco Switch</mark>

{% code title="Server Configuration" %}
```
Switch(config)#vtp domain CCNA
Changing VTP domain name from NULL to CCNA

SW1(config)#vtp password cisco
Setting device VLAN database password to cisco
```
{% endcode %}

{% hint style="info" %}
{% code overflow="wrap" %}
```
The default VTP mode on Cisco switches is the server mode, so the command vtp mode server wasn’t necessary in the SW1 configuration.
Now need to configure SW2 and SW3 as VTP clients.
```
{% endcode %}
{% endhint %}

{% code title="Client Configuration" %}
```
Switch(config)#vtp mode client 
Setting device to VTP CLIENT mode.

Switch(config)#vtp domain CCNA 
Changing VTP domain name from NULL to CCNA
```
{% endcode %}

## <mark style="color:purple;">Etherchannel</mark>

Etherchannel is a method used for link aggregation and redundancy in the network configuration.

Its operates under **IEEE 802.3ad**, which defines link aggregation

EtherChannel bundles multiple physical Ethernet links into a single logical link. This allows for increased bandwidth and provides redundancy, but the balancing depends on the hashing algorithm based on MAC, IP, or layer 4 headers, and not all traffic will equally use the bandwidth.

### <mark style="color:blue;">**Conditions**</mark>

* The switch must support IEEE 802.1 AD Standard.
* All cables in the EtherChannel bundle must have the same speed; mixing different cable speeds is not supported.

### <mark style="color:blue;">**TYPES**</mark>

#### <mark style="color:blue;">**LACP (Link Aggregation Control Protocol):**</mark>

* LACP stands for Link Aggregation Control Protocol it is an **open standard** defined by **IEEE 802.3ad (**vendor-neutral**),** which is used to establish and manage EtherChannels .
* LACP enables the combination of multiple network connections in parallel, improving performance and redundancy.

#### <mark style="color:blue;">MODE</mark>

* **Active Mode:** The device actively tries to make a connection by sending "hello" messages (LACP packets) to other devices on the network. If the other side responds, they create a connection.
* **Passive Mode:** The device waits for the other side to say "hello" first. It will connect if it receives the right message. But, if both sides are waiting (both in passive mode), nothing will happen because neither is sending the first message.
* **ON Mode**: Both devices connect without sending any "hello" messages or checks. This is a static EtherChannel configuration, meaning no protocols like LACP or PAgP are used to negotiate the connection. Both sides must be manually configured to use ON mode for the EtherChannel to work.

Configure EtherChannel on both switches

```
# On Switch 1
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode active
exit

# On Switch 2
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode passive
exit

Static (ON) Mode (No negotiation protocol)
# On both switches
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode on
exit

#On Port-Channel Interface as trunk Interface
interface port-channel 1
switchport mode trunk
switchport mode trunk encapsulation dot1q
no shutdown
exit

#On Port-Channel Interface as Access Interface
interface port-channel 1
no shutdown
switchport mode access
switchport access vlan 1
exit
```

* Switch 1 is configured in `active` mode (it actively sends LACP packets). Switch 2 is in `passive` mode (it waits for LACP packets from Switch 1).
* Both sides are manually configured to establish the EtherChannel without using any negotiation protocols.

#### <mark style="color:blue;">PAgP (Cisco Proprietary)</mark>

Its same as LACP but only works on Cisco devices.

#### <mark style="color:blue;">Mode</mark>

* **Desirable Mode**: Actively tries to negotiate the EtherChannel.
* **Auto Mode**: Passively waits for the other device to negotiate the EtherChannel.
* **ON Mode** : Statically bundles the interfaces into an EtherChannel. This is a manual configuration and should be consistent on both ends of the link.

#### <mark style="color:blue;">**PAgP Configuration**</mark> <mark style="color:blue;"></mark><mark style="color:blue;">(Cisco-only environments)</mark>

```
# On Switch 1
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode desirable
exit

# On Switch 2
interface range gigabitEthernet 0/1 - 2
no shudown
channel-group 1 mode auto
exit

Static (ON) Mode (No negotiation protocol)
# On both switches
interface range gigabitEthernet 0/1 - 2
no shutdown
channel-group 1 mode on
exit

#On Port-Channel Interface as trunk Interface
interface port-channel 1
switchport mode trunk
switchport mode trunk encapsulation dot1q
no shutdown
exit

#On Port-Channel Interface as Access Interface
interface port-channel 1
no shutdown
switchport mode access
switchport access vlan 1
exit

```

* Switch 1 is set to `desirable` mode, actively negotiating the EtherChannel. Switch 2 is in `auto` mode, waiting for Switch 1 to initiate the channel.
* Both sides are manually configured to establish the EtherChannel without using any negotiation protocols.

#### <mark style="color:blue;">Show Commands</mark>

```
show etherchannel summary
show interfaces port-channel
show lacp neighbor



```

## <mark style="color:purple;">CDP (Cisco Discovery Protocol) and LLDP (Link Layer Discovery Protocol)</mark>

**CDP (Cisco Discovery Protocol)** and **LLDP (Link Layer Discovery Protocol)** are Layer 2 protocols used for discovering neighboring devices and gathering important device information within a network.

* **CDP**: Cisco proprietary, typically used in Cisco environments but may work with some non-Cisco devices.
* **LLDP**: An open standard defined by IEEE 802.1AB, supported by various network vendors, making it useful in multi-vendor environments.

### <mark style="color:blue;">Cisco Discovery Protocol</mark>

* **Developed by**: Cisco Systems.
* **Functionality**: Discovers Cisco and, in some cases, non-Cisco devices. CDP shares information such as device type, hostname, IP address, interface details, and even VLAN and PoE capabilities.
* **Layer**: Operates at Layer 2 (Data Link Layer) of the OSI model.
* **Common Uses**: Gathering details about neighboring Cisco devices, IP phones, and managing VoIP deployments.

### <mark style="color:blue;">Link Layer Discovery Protocol</mark>

* **Defined by**: IEEE 802.1AB.
* **Functionality**: Allows devices from different vendors to exchange information. LLDP provides details such as system name, description, port information, VLAN, PoE capabilities, and more.
* **Layer**: Operates at Layer 2 (Data Link Layer).
* **Common Uses**: Managing multi-vendor environments, VoIP deployments, and identifying network topology.

{% hint style="info" %}
These protocols help network administrators discover and understand the topology of their networks by providing information about directly connected devices.&#x20;
{% endhint %}

### <mark style="color:blue;">Configure CDP</mark>

**Enable CDP**

```
Switch# configure terminal
Switch(config)# cdp run

```

**Enable or Disbale CDP in Interface.**

```
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# no cdp enable  # Disable CDP on this interface

```

**Adjusting Timers and Hold Time**

```
Switch(config)# cdp timer 60        # Send CDP updates every 60 seconds
Switch(config)# cdp holdtime 180    # Retain CDP information for 180 seconds
```

**Show command**

```
Switch# show cdp neighbors
Switch# show cdp neighbors detail
```

### <mark style="color:blue;">Configure LLDP</mark>

**Enable LLDP Globally**

```
Switch# configure terminal
Switch(config)# lldp run

```

**LLDP Interface Configuration:**

```
Switch(config)# interface GigabitEthernet0/1
Switch(config-if)# no lldp transmit   # Disable LLDP transmit on this interface
Switch(config-if)# no lldp receive    # Disable LLDP receive on this interface

```

**Show command**

```
Switch# show lldp neighbors
Switch# show lldp neighbors detail
```

## <mark style="color:purple;">**Spanning Tree Protocol (STP):**</mark>

Spanning Tree Protocol (STP) is a network protocol used to prevent loops in Ethernet networks, particularly in bridged or switched networks. STP ensures that there is only one logical path between all destinations on the network, preventing broadcast storms and other issues that can arise from network loops.

<mark style="color:blue;">**Phases of STP:**</mark>

1. **Election of Root and Bridge ID:**
   * In the initial phase, switches elect a Root Bridge. The Root Bridge serves as the central reference point for the entire STP network.
   * Each switch has a Bridge ID, which includes a priority value and a MAC address.
   * By default, the Bridge ID priority on Cisco switches is 32768 for all VLANs. This priority remains the same for every VLAN unless explicitly configured otherwise. The value 32769 is incorrect and can lead to misunderstanding.
   * The switch with the lowest Bridge ID becomes the Root Bridge.
   * If multiple switches have the same Bridge ID, the switch with the lowest MAC address is elected as the Root Bridge.
   * Bridge Protocol Data Units (BPDU) packets are used for Root Bridge election.

{% hint style="info" %}
32768 if SYN Count then 32769 +  1 increase with Vlan Counts Becasue Best Devices has the Lowest Bridge ID
{% endhint %}

2. **Election of Root Port:**
   * Each switch determines its best path (Root Port) to reach the Root Bridge.
   * The best path is determined based on the lowest cumulative cost (port cost) to reach the Root Bridge.
   * Port costs are assigned based on link speeds. For example, FastEthernet has a lower cost than Ethernet.
   * The switch with the lowest cumulative cost to reach the Root Bridge becomes the Root Port.

| Linkspeed         | Speed    | Post Cost |
| ----------------- | -------- | --------- |
| Ethernet          | 10 MBPS  | 100       |
| FastEthernet      | 100 MBPS | 19        |
| GigabitEthernet   | 1 GBPS   | 4         |
| 10GigabitEthernet | 10 GBPS  | 2         |

3. **Blocking Ports:**
   * After determining the Root Bridge and Root Port, STP identifies and blocks certain ports to prevent loops.
   * Ports on non-Root Bridges that are not part of the best path to the Root Bridge are blocked.
   * Blocked ports do not forward traffic but are in a "listening and learning" state.

**STP Process:**

* STP has multiple phases, but the time it takes is based on timers. Specifically, **15 seconds for Listening** and **15 seconds for Learning**, but the total convergence time could be more depending on the network size and spanning tree configuration. 30 seconds is the default time, but this can be changed.
* The first 15 seconds are in the "listening" mode, where switches receive BPDU packets and exchange information.
* The next 15 seconds are in the "learning" mode, during which switches determine the Root Bridge and Root Port.
* Once the Root Bridge and Root Port are identified, the remaining ports are blocked to prevent loops.

STP is crucial for network stability and redundancy in Ethernet networks. It ensures that even in complex network topologies, there is a single logical path to reach each destination, preventing data collisions and broadcast storms.

### <mark style="color:blue;">Configuration</mark>

**Root Bridge Election Configuration**

```
Switch(config)# spanning-tree vlan <vlan-id> priority 4096
```

**Root Port Election**

```
Switch(config-if)# spanning-tree vlan <vlan-id> cost <value>
```

**Blocking And Listening States**

```
Switch(config)# spanning-tree vlan <vlan-id> forward-time <time>
```

## <mark style="color:purple;">**Aruba HPE Networking and Cisco CLI Reference**</mark>

{% hint style="info" %}
The commands and options may vary based on the specific features and versions of the devices. Please refer to the respective documentation for accurate and up-to-date information
{% endhint %}

```bash
[Comware7] dhcp snooping enable
[Comware7]interface GigabitEthernet1/0/6
[Comware7-GigabitEthernet1/0/6]arp detection trust
[Comware7]vlan 220
[Comware7-vlan220]arp detection enable
[Comware7]display arp detection
[Comware7]display arp detection statistics
```

Certainly! Here's the information without line breaks:

**Web or Portal Authentication**

**ProVision:**

```bash
ProVision(config)# radius-server host 10.0.100.111 key password
[Comware5]radius scheme <radius-auth>
[Comware5-radius-radius-auth]primary authentication 10.0.100.111 1812
[Comware5-radius-radius-auth]primary accounting 10.0.100.111 1813
[Comware5-radius-radius-auth]key authentication password
[Comware5-radius-radius-auth]user-name-format without-domain
[Comware5-radius-radius-auth]server-type extended
ProVision(config)# aaa port-access web-based 18
[Comware5]domain web-auth
[Comware5-isp-web-auth]authentication portal radius-scheme radius-auth
[Comware5-isp-web-auth]authorization portal radius-scheme radius-auth
[Comware5-isp-web-auth]accounting portal radius-scheme radius-auth
[Comware5-isp-web-auth]authorization portal radius-scheme radius-auth
ProVision(config)# aaa port-access web-based 18 unauth-vid 99
ProVision(config)# aaa port-access web-based 18 client-limit 5
ProVision(config)# ip device tracking
ProVision(config)# ip admission name web-auth-rule1 proxy http
ProVision(config)# ip admission auth-proxy-banner http
[Comware5] interface LoopBack12
[Comware5-LoopBack12]ip address 1.1.1.1 255.255.255.255
ProVision(config)#fallback profile fallback1
[Comware5]interface g1/0/18
[Comware5-GigabitEthernet1/0/18]port link-type hybrid
[Comware5-GigabitEthernet1/0/18]mac-vlan enable
[Comware5-GigabitEthernet1/0/18]portal local-server enable
[Comware5-GigabitEthernet1/0/18]portal domain web-auth
[Comware5-GigabitEthernet1/0/18]stp edged-port enable
ProVision(config-if)#dot1x pae authenticator
ProVision(config-if)#authentication fallback fallback1
ProVision(config-if)#authentication order webauth
ProVision(config-if)#authentication port-control auto
ProVision(config-if)#ip access-group web-auth-policy1 in
ProVision(config-if)#ip admission web-auth-rule1
ProVision(config-if)#switchport mode access
ProVision(config-if)#switchport access vlan 220
ProVision(config-if)#authentication auth-fail vlan 99
ProVision# show port-access web-based
[Comware5]display portal user all
ProVision# show port-access web-based clients
[Comware5]display connection access-type portal
[Comware5]display connection ucibindex 3
ProVision# show port-access web-based config 18
[Comware5]display portal connection statistics all
```

**Cisco:**

```bash
Cisco(config)#radius-server host 10.0.100.111 auth-port 1812 acct-port 1813 key password
Cisco(config)#radius-server attribute 8 include-in-access-req
Cisco(config)#radius-server vsa send authentication
Cisco(config)#aaa new-model
Cisco(config)#aaa authentication login default group radius
Cisco(config)#aaa authorization auth-proxy default group radius
Cisco(config)#ip arp inspection vlan 220
Cisco(config)#ip arp inspection trust
Cisco(config)#ip dhcp snooping
Cisco(config)#ip dhcp snooping authorized-server 10.0.100.251
Cisco(config)#ip dhcp snooping database file tftp://10.0.100.111/Cisco_dhcp.txt
Cisco(config)#ip dhcp snooping vlan 220
Cisco(config)#ip dhcp snooping trust
Cisco(config)#interface g1/0/6
Cisco(config-if)#ip dhcp snooping trust
Cisco(config)#ip device tracking
Cisco(config)#ip access-list extended web-auth-policy1
Cisco(config-ext-nacl)#permit udp any any
Cisco(config-ext-nacl)#permit tcp any any eq www
Cisco(config-ext-nacl)#deny ip any any
Cisco(config)#fallback profile fallback1
Cisco(config-fallback-profile)#ip access-group web-auth-policy1 in
Cisco(config-if)#ip admission web-auth-rule1
Cisco(config-if)#switchport mode access
Cisco(config-if)#switchport access vlan 220
Cisco(config-if)#portal local-server enable
Cisco(config-if)#dot1x pae authenticator
Cisco(config-if)#portal auth-fail vlan 99
Cisco(config-if)#authentication fallback fallback1
Cisco(config-if)#authentication order webauth
Cisco(config-if)#authentication port-control auto
Cisco(config-if)#stp edged-port enable
Cisco(config)#ip access-group web-auth-policy1 in
Cisco#show ip admission cache
Cisco#show authentication interface g1/0/18
```

Certainly! Here's the information without line breaks:

**Local Mirror or SPAN**

**ProVision:**

```bash
ProVision(config)# mirror 1 port 4
ProVision(config)# interface 11 monitor all both mirror 1
ProVision# show monitor
ProVision# show monitor 1
```

**Comware:**

```bash
[Comware]mirroring-group 1 local
[Comware]mirroring-group 1 mirroring-port g1/0/6 both
[Comware]mirroring-group 1 monitor-port g1/0/4
[Comware]display mirroring-group all
[Comware]display mirroring-group 1
```

**Cisco:**

```bash
Cisco(config)#monitor session 1 source interface g1/0/6 both
Cisco(config)#monitor session 1 destination interface g1/0/4 encapsulation replicate
Cisco#show monitor
Cisco#show monitor session 1
Cisco#show monitor session 1 detail
```

#### **Display Commands**

**ProVision commands**

```bash
show arp
show arp-protection
show arp-protection statistics
show arp ip-address
show flash
show time
show system information
show alias
show interface <port>
show interface <interface> rate
show cpu
No equivalent ProVision software command
show running-configuration
show running-configuration by-linenum
No equivalent ProVision software command
show current-configuration interface
show debug
No equivalent ProVision software command
No equivalent ProVision software command
No equivalent ProVision software command
display dhcp relay information all
display dhcp relay information interface Vlan-interface <vlan-id>
show dhcp-relay
show dhcp-snooping binding database
show dhcp-snooping information
show dhcp-snooping [ip ip_address]
show dhcp-snooping packet statistics
show dhcp-snooping trust
show tech
show ip dns domain
display dns domain dynamic
show ip dns < domain | server >
show port-access authenticator config
show port-access authenticator config [interface]
show port-access authenticator session counters [interface interface-list]
show port-access authenticator statistics [interface interface-list]
show system temperature
show system fans
show secure-mode
show gvrp statistics interface <port_list>
show gvrp timer interface <port_list>
show gvrp state interface <port_list> vlan <vlan-id>
show gvrp statistics
show gvrp status
display gvrp vlan-operation interface interface-type interfacenumber
show history-command
show tacacs
show accounting
display radius scheme
show rip
show rip interface
show rip process-id ip-address mask/mask-length
show rip process-id route
show rip process-id route peer ip-address
show rmon statistics
show route-policy
show saved-configuration
show saved-configuration by-linenum
show schedule reboot <after|at>
show sflow
show sflow sampling-polling <receiver table number>
show sflow slot <slot-number>
show snmp-agent host-public-key
show snmp-agent public-key local rsa public
show snmp-agent public-key peer
show radius
show radius host
show accoutning
show radius scheme
show ip check source
show ip community-list
display ip http
display ip https
show ip prefix-list
show lacp local
display link-aggregation load-sharing mode
display link-aggregation member-port
display link-aggregation summary
display link-aggregation verbose
display lldp local-information
display lldp local-information global
display lldp local-information interface interface-type interfacenumber
show lldp neighbor-information brief
show lldp neighbor-information list
show lldp neighbor-information list system-name <string>
show lldp stats
show lldp stats global
show lldp stats interface interface-type interface-number
show lldp status
show lldp status interface interface-type interface-number
show lldp tlv-config interface interface-type interface-number
show logging
display logfile buffer
display loopback-detection
show mac-address
display mac-address
show mac-address aging-time
display mac-address multicast
show port-access mac-based
show port-access mac-authentication
show port-access mac-authentication [interface …]
show system information
display memory
show uplink-failure-detection
display multicast forwarding-table
show ip mroute
display multicast routing-table
show ip pim rpf-override
display multicast routing-table static
display multicast rpf-info
show ip pim interface
display pim interface
show ip pim interface verbose
display pim join-prune
show ip pim neighbor
display pim neighbor
show ip pim neighbor <ip> verbose
display pim routing-table
display pim rp-info
show power-over-ethernet device
show power-over-ethernet interface
show power-over-ethernet interface power
show power-over-ethernet power-usage
show power-over-ethernet alarm
display poe-power switch state
display poe-power switch state
show port trunk
display power
display protocol-vlan
display protocol-vlan interface
show crypto host-public-key
show ip host-public-key
display public-key local rsa public
show ip client-public-key
display public-key peer
show radius
show radius host
show accoutning
display radius scheme
display rip
display rip interface
display rip process-id ip-address mask/mask-length
display rip process-id route
display rip process-id route peer ip-address
show rmon statistics
display rmon statistics
show route-policy
display route-policy
show saved-configuration
display saved-configuration
display saved-configuration by-linenum
display current-configuration
display current-configuration by-linenum
display current-configuration interface
display current-configuration
show ip source-lockdown bindings
display user-bind
show vlan
display vlan
show vrrp
display vrrp
show vrrp <interface-type> vrid <virtual routerid>
display vrrp interface <interface-type> vrid <virtual routerid>
show vrrp statistics
display vrrp statistics
show vrrp statistics global
display vrrp statistics interface <interface-type> vrid <virtual routerid>
show vrrp verbose
display vrrp vlan-operation interface interface-type interfacenumber
```
