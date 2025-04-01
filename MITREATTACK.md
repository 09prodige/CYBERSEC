# T1592 - Gather Victim Host Information

## MITRE ATT&CK Tactic: Reconnaissance

**ID**: T1592  
**Tactic**: Reconnaissance  
**Platform**: All  
**Permissions Required**: None  
**Data Sources**: Web analytics, Network protocol analysis, File monitoring

---

## 🔎 Description

Adversaries may gather information about the victim's hosts that can be used during targeting. This technique typically occurs in the early phases of a cyber operation. Information about hosts may include:

- Assigned IP addresses
- Hostnames
- Operating systems (OS)
- System architecture
- Roles of the host (e.g., web server, mail server)
- Running services
- Network interfaces
- System configurations
- Installed software and firmware
- Hardware details (CPU, RAM, devices)

This data allows adversaries to identify potential targets for exploitation and determine how best to access them. This method is particularly valuable in long-term stealth operations such as those attributed to state-sponsored groups like **Volt Typhoon** ([CISA Report](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)).

---

## 🎯 Case Study: Attack Scenario on 192.168.45.63

### 🧾 Target Profile (Fictive)
- **IP Address**: 192.168.45.63
- **Hostname**: `internal-core-scan.local`
- **Role**: Core Network Device in ICS Segment
- **OS**: Ubuntu Server 20.04 LTS
- **Architecture**: x86_64
- **Interfaces**: eth0 (LAN), tun0 (VPN)
- **Services Exposed**:
  - Port 22 → OpenSSH_8.9p1
  - Port 80 → Apache/2.4.52 (Ubuntu)
- **MAC Address Prefix**: Cisco Systems, Inc.
- **Last Seen**: March 31, 2025
- **Firmware Hint**: Intel AMT Enabled on motherboard
- **DNS Name Resolution**: Reverse DNS shows "core-sensor.local"

### 📋 Attack Plan Based on T1592

#### Phase 1: Passive Reconnaissance (No Touch)
- WHOIS and DNS Enumeration from public sources
- Leaked configuration files found via `Google Dorking`
- Web analytics from Shodan/Censys → Identified ports 22 and 80
- OSINT social media reveal internal IT naming conventions (e.g., `core-`, `scan-`, `-local`)
- GitHub repo found with network map (in `.png` form) published by former employee

#### Phase 2: Infrastructure Profiling
- Used `nslookup` and `dig` for DNS leak validation
- Banner grabbing using Python-based tool → confirmed `OpenSSH` and `Apache`
- Extracted Apache version → matched to CVE-2022-23943 (vulnerable module enabled)
- Discovered Intel AMT hint using MAC prefix enumeration
- SNMPwalk test (UDP 161) showed system uptime, contact, and host description (SNMP v2c - default community string)

#### Phase 3: Active Scanning *(last phase to avoid early detection)*
- Performed Nmap stealth scan (`-sS -sV -O -Pn`) on 192.168.45.63
- Used custom **banner_grabber.py** script to confirm services and test responsiveness
- Confirmed Apache version mismatch with patch baseline
- Determined system Uptime > 180 days → likely unpatched

#### Phase 4: Host Information Exploitation
- Attempted default credential login via SSH (blocked)
- Leveraged HTTP for basic directory enumeration
- Discovered `/status` endpoint with exposed internal config metadata
- Indexed possible open SMB share on adjacent host 192.168.45.62 (target laterally reachable)

---

## 🔗 Resources & References

- [MITRE ATT&CK T1592 Technique Page](https://attack.mitre.org/techniques/T1592/)
- [Sub-techniques of T1592](https://attack.mitre.org/techniques/T1592/)
  - [T1592.001 - Hardware](https://attack.mitre.org/techniques/T1592/001/)
  - [T1592.002 - Software](https://attack.mitre.org/techniques/T1592/002/)
  - [T1592.003 - Firmware](https://attack.mitre.org/techniques/T1592/003/)
  - [T1592.004 - Client Configurations](https://attack.mitre.org/techniques/T1592/004/)
- [Group G1017](https://attack.mitre.org/groups/G1017/)
- [Data Source: DS0035 - Application Log](https://attack.mitre.org/datasources/DS0035/)
- [Volt Typhoon Threat Actor - CISA Advisory](https://www.cisa.gov/sites/default/files/2024-03/aa24-038a_csa_prc_state_sponsored_actors_compromise_us_critical_infrastructure_3.pdf)

---

## ⚖️ Example Tools & Techniques

| Tool/Method                | Description                                           |
|---------------------------|-------------------------------------------------------|
| WHOIS                     | Retrieves domain registration details                |
| nslookup / dig            | Gathers DNS records and server info                  |
| Shodan / Censys           | Provides data on exposed devices and services        |
| Banner Grabbing           | Identifies services running on open ports            |
| Port Scanning (e.g., Nmap)| Detects live hosts and open ports                    |
| SMB Enum Tools            | Extracts OS and host info from Windows shares        |
| SNMPwalk                  | Dumps system info from SNMP-enabled hosts            |
| Netcat / Telnet           | Manual banner grabbing and service testing           |

---

## 🔐 Defensive Measures

- Monitor DNS, WHOIS, and web traffic for anomalies  
- Block suspicious external recon attempts  
- Enforce strict access control on internal host data  
- Monitor logs for enumeration patterns  
- Disable unnecessary services and ports  
- Harden SNMP, NetBIOS, and RPC endpoints

---

## ⚒️ Usage in Red Team / Pentest

During red team operations or penetration tests, this technique is commonly used to:

- Enumerate exposed infrastructure
- Identify running services and versions
- Extract system-level metadata
- Prioritize targets based on their roles or vulnerabilities

Example:
```bash
nmap -sV -O 192.168.45.63
