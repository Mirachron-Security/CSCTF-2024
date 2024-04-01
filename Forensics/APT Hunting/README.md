# APT Hunting
Author: [Roșu Darius](https://www.linkedin.com/in/darius-rosu-922961233/)

<br>

## Description
```
Uncover the details of a malware binary: its APT number, type, C2 server IP, origin country, and the year the associated cybercriminal group became active.
```

<br>

## Requirements
- Binary analysis
- Malware research

<br>

## Solve
The solution involved:
1. **VirusTotal Analysis:** Uploaded the binary to VirusTotal to identify its nature and C2 server IP.
2. **Malware Type:** Detected as a backdoor, specifically.
3. **C2 Server IP:** Found within the details on VirusTotal (`210.48.231.182`).
4. **Cybergang Group:** Research on Turla (linked on VirusTotal) led to identifying [APT28](https://malpedia.caad.fkie.fraunhofer.de/actor/turla), Russia as the country of origin, and 2004 as the year they first became active.

Virustotal link: [link](https://www.virustotal.com/gui/file/3f94b20cb7f4ff55207660649ebbb02679c991fe03efbcb0bd3840fc7f0bd527/community)

<br>

> Flag: `CSCTF{APT28_Backdoor_210.48.231.182_Russia_2004}`
