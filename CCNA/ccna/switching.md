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
| Enable Mode                       | Enter enable mode (user/enable mode) using the "enable" command to gain elevated privileges.                                                                                       |
| Interface Information             | - To view all interfaces and their status: use the "show ip interface brief" command. - To view details of a specific interface: use `show ip interface <interface>`               |
| Configuration Mode                | Enter global configuration mode using commands like "configure terminal" or "conf t." This mode provides full access with privilege level 15.                                      |
| Using "do" with Commands          | While in configuration mode, you can use show commands by prefixing them with "do," such as "do show ip int brief."                                                                |
| Interface Configuration           | Configure interface settings (e.g., speed, duplex, description) using commands like: - `interface <interface>` - `speed <speed>` - `duplex <duplex>` - `description <description>` |
| Selecting Multiple Interfaces     | Use the "interface range" command to select and configure multiple interfaces simultaneously.                                                                                      |
| Set Switch Hostname               | Assign a name to the switch using the `hostname <name>` command.                                                                                                                   |
| Banner Message                    | Create a banner message that users see when they log in.                                                                                                                           |
| Console Password                  | Set a password for console access using the "line console 0" command.                                                                                                              |
| Enable Telnet                     | Configure virtual lines (vty) for Telnet access.                                                                                                                                   |
| Management IP Address             | Assign an IP address to the management interface (usually VLAN 1).                                                                                                                 |
| Set Passwords                     | Set an enable secret password for privileged mode.                                                                                                                                 |
| Set Default Gateway               | Configure the default gateway.                                                                                                                                                     |
| Clear Configurations              | To delete all configurations, use the "write erase" command.                                                                                                                       |
| Disable DNS Lookup                | Use "no ip domain lookup" to disable DNS lookups.                                                                                                                                  |
| Enable IP Routing (L3 Switch)     | Configure IP routing on Layer 3 switches.                                                                                                                                          |
| Save Configurations               | Save configurations to memory or copy them to a TFTP server.                                                                                                                       |
| Check Interface Configurations    | Use "show run" to view running configurations.                                                                                                                                     |
| Check Time                        | View the switch's current time with "show clock."                                                                                                                                  |
| Change Time                       | Set the time with the "clock set" command.                                                                                                                                         |
| Change Timezone                   | Configure the timezone using "clock timezone."                                                                                                                                     |
| Interface Shutdown/No Shutdown    | Use "`shutdown`" and "`no shutdown`" to disable/enable an interface.                                                                                                               |
| Interface Access Mode             | Set an interface to access mode with "switchport mode access."                                                                                                                     |
| Interface Trunk Mode              | Set an interface to trunk mode with "switchport mode trunk."                                                                                                                       |
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
