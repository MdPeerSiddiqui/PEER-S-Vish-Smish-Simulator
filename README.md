# PEER'S Vish & Smish Simulator 📞💬

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux%20%7C%20Windows%20%7C%20macOS-0078D4?style=for-the-badge&logo=linux&logoColor=white)](https://kali.org)
[![Security](https://img.shields.io/badge/Security-Social%20Engineering%20%26%20VoIP-red?style=for-the-badge&logo=shield)](https://sqrock.com)
[![Tests](https://img.shields.io/badge/Tests-9%2F9%20Passing-brightgreen?style=for-the-badge&logo=checkmarx)](https://github.com/MdPeerSiddiqui/PEER-S-Vish-Smish-Simulator)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

> **Enterprise Voice (Vishing) & SMS (Smishing) Attack Progression and Countermeasure Simulator**  
> Developed by **Md Peer Siddiqui** for the **Sqrock IT Solution Cybersecurity Internship (Day 04: Social Engineering Attack Simulations)**.

---

## 🎯 Executive Overview

Modern social engineering attacks have moved beyond conventional email phishing into multi-channel telephony manipulation:
1. **Voice Phishing (Vishing):** Exploits Session Initiation Protocol (SIP) spoofing, audio urgency, and psychological compliance to bypass traditional perimeter security.
2. **SMS Phishing (Smishing):** Leverages rogue SMS gateway aggregators, alphanumeric Sender IDs, and link shortening to execute mobile credential theft.

**PEER'S Vish & Smish Simulator** is a rock-solid, production-grade CLI suite designed to demonstrate, dissect, and defend against targeted social engineering tactics across **10 real-world industry sectors**.

---

## 🚀 Key Features

* **🎭 Interactive Live Call Roleplay Engine:** Conduct realistic, branching voice attack simulations with 5 conversation phases (Introduction, Hook, The Exploitation Ask, Dynamic Objection Handling, Exit Strategy). Users can test their operational resilience against adversarial counters.
* **📱 GSM-7 Mobile Payload Inspector:** Analyzes SMS lures, calculating raw character length, GSM-7 160-character thresholds, multi-part Concatenated SMS (UDH) segment splits, and domain destination extraction.
* **📊 Quantitative Psychological Trigger Radar:** Evaluates attack intensity across 5 psychological levers: **Urgency**, **Authority**, **Fear**, **Scarcity**, and **Sympathy** (Total Score out of 100).
* **🛡️ Telephony Defense & Authentication Matrix:** In-depth technical breakdown of carrier-level mitigations including **STIR/SHAKEN** (RFC 8588) attestation levels (A, B, C), FIDO2/WebAuthn hardware tokens, and Out-of-Band (OOB) authentication workflows.
* **⚡ 10-Sector Automated Benchmark Audit:** Instantly validates and stress-tests all attack personas, payload lengths, and psychological triggers in under **0.005 seconds**.
* **🛡️ Bulletproof CLI Architecture:** Zero GUI bloat, strict input validation, graceful exception handling (`Ctrl+C` interrupt safety), and complete cross-platform compatibility across Kali Linux, Ubuntu, macOS, and Windows.

---

## 🏢 10 Comprehensive Industry Attack Sectors

The simulator implements 10 distinct threat scenarios modeling modern cyber-adversary tactics:

| Sector ID | Industry Sector | Spoofed Caller ID / Sender ID | Primary Objective | Psychological Dominance |
| :--- | :--- | :--- | :--- | :--- |
| `it_support` | **Enterprise IT** | Internal Helpdesk (`+1-800-555-0199`) | MFA Bypass / Session Token Harvest | Authority (90) & Urgency (85) |
| `banking_fraud` | **Banking & Finance** | Apex Global Fraud (`+1-888-555-0144`) | Wire Transfer to "Safe Holding Account" | Fear (95) & Urgency (90) |
| `gov_tax` | **Government & Tax** | Federal Revenue Agency (`+1-800-829-1040`) | Immediate Tax Penalty Payment | Authority (95) & Fear (90) |
| `parcel_delivery`| **Logistics & Courier** | SwiftTrack Global (`SWIFT-PKG`) | Redelivery Fee / Phishing Portal Capture | Scarcity (85) & Urgency (75) |
| `hr_payroll` | **Corporate HR** | People Operations (`+1-800-555-0177`) | Banking Routing Number Interception | Authority (85) & Fear (80) |
| `healthcare_copay`| **Healthcare & Rx** | MediCare Claims (`MED-RX`) | Insurance ID & Medical Portal Credential | Fear (85) & Urgency (80) |
| `executive_ceo` | **Executive Whaling** | CEO Mobile Line (`+1-415-555-0122`) | Urgent Gift Cards / Wire Transfer | Authority (95) & Urgency (90) |
| `telecom_carrier`| **Telecom / Carrier** | Cellular Security Desk (`CARRIER-SEC`) | One-Time Verification Passcode (SIM Swap)| Urgency (95) & Authority (85) |
| `ecommerce_retail`| **E-Commerce Retail** | Order Security Alert (`ORDER-ALERT`) | High-Value Unauthorized Charge Cancellation| Fear (85) & Urgency (80) |
| `utility_services`| **Public Utilities** | City Grid Operations (`+1-800-555-0111`) | Immediate Power Disconnection Aversion | Fear (95) & Urgency (90) |

---

## 📦 Installation & Setup

### For Kali Linux / Debian / Ubuntu:
```bash
# 1. Clone the repository
git clone https://github.com/MdPeerSiddiqui/PEER-S-Vish-Smish-Simulator.git
cd PEER-S-Vish-Smish-Simulator

# 2. Set up a Python virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the simulator
python3 vish_smish.py
```

### For Windows (PowerShell / Command Prompt):
```powershell
# 1. Clone the repository
git clone https://github.com/MdPeerSiddiqui/PEER-S-Vish-Smish-Simulator.git
cd PEER-S-Vish-Smish-Simulator

# 2. Set up virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the simulator
python vish_smish.py
```

---

## 🎮 CLI Usage Guide

When you launch `vish_smish.py`, the interactive master console appears:

```
======================================================================
  PEER'S VISH & SMISH SIMULATOR v1.0
  Social Engineering Attack Vector & Countermeasure Suite
  Author: Md Peer Siddiqui | Sqrock IT Solution Internship (Day 04)
======================================================================

 [1] Interactive Voice Call Simulation (Roleplay Mode)
 [2] Mobile Smishing Payload & GSM-7 Inspector
 [3] Scenario Psychological Trigger Radar
 [4] Telephony Security & Carrier Defense Matrix
 [5] Run Comprehensive 10-Sector Audit Benchmark
 [6] Inspect Specific Scenario (Deep Forensic View)
 [7] Exit Simulator
```

### Menu Options Explained:
1. **Option 1 (Interactive Roleplay):** Simulates an inbound adversarial phone call. Step through the attacker's script and choose whether to `[A]` Resist / Challenge using Out-of-Band verification or `[B]` Comply / Yield, dynamically observing how attackers overcome resistance.
2. **Option 2 (Smishing Inspector):** Analyzes SMS character limits, GSM-7 single vs concatenated multi-part message boundaries, and malicious links.
3. **Option 3 (Psychological Radar):** Renders a quantitative ASCII bar chart depicting psychological levers utilized in the attack.
4. **Option 4 (Defense Matrix):** Detailed briefing on STIR/SHAKEN digital certificates, FIDO2 authentication, and strict callback protocols.
5. **Option 5 (Audit Benchmark):** Automated verification test testing all 10 scenarios with zero errors.

---

## 🧪 Automated Testing

The suite includes 9 automated unit tests verifying scenario schema validity, dialogue stages, GSM-7 threshold calculations, psychological scores, and objection handling.

Run tests via:
```bash
python -m unittest tests/test_vish_smish.py -v
```

**Test Output:**
```
test_all_scenarios_have_required_fields (tests.test_vish_smish.TestVishSmishSimulator) ... ok
test_gsm7_character_counter (tests.test_vish_smish.TestVishSmishSimulator) ... ok
test_json_scenarios_file_exists (tests.test_vish_smish.TestVishSmishSimulator) ... ok
test_objection_handling_structure (tests.test_vish_smish.TestVishSmishSimulator) ... ok
test_psychological_scores_valid (tests.test_vish_smish.TestVishSmishSimulator) ... ok
test_scenario_count (tests.test_vish_smish.TestVishSmishSimulator) ... ok
test_smishing_has_payload_and_link (tests.test_vish_smish.TestVishSmishSimulator) ... ok
test_telephony_defenses_present (tests.test_vish_smish.TestVishSmishSimulator) ... ok
test_vishing_dialogue_phases (tests.test_vish_smish.TestVishSmishSimulator) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.003s

OK
```

---

## 📁 Repository Structure

```
PEER-S-Vish-Smish-Simulator/
├── vish_smish.py             # Core production CLI engine & interactive roleplay
├── scenarios.json            # 10-sector attack scenario database
├── requirements.txt          # Python dependencies (colorama, reportlab)
├── LICENSE                   # MIT License
├── README.md                 # Complete documentation & usage guide
├── .gitignore                # Python and IDE exclusions
├── tests/
│   └── test_vish_smish.py    # 9-point automated test suite
├── scripts/
│   └── generate_day04_pdf.py # Executive 4-page PDF lab report compiler
└── reports/
    └── Day04_Vishing_Smishing_Report_Sqrock_MdPeerSiddiqui.pdf  # Generated executive report
```

---

## 🛡️ Ethical Compliance & Disclaimer

> **NOTICE:** This tool and its associated simulation scenarios are developed strictly for **authorized educational, awareness training, and academic research purposes** under the **Sqrock IT Solution Cybersecurity Internship Program**.  
> The scripts and dialogue models are designed solely for defensive awareness to train employees and students to recognize, challenge, and report social engineering attacks. Unauthorized execution of vishing, caller ID spoofing, or smishing against real individuals or networks without explicit consent is illegal under international telecommunications and computer fraud regulations.

---

## 👤 Author

* **Md Peer Siddiqui**
* **Cybersecurity Intern at Sqrock IT Solution**
* **GitHub:** [@MdPeerSiddiqui](https://github.com/MdPeerSiddiqui)
* **LinkedIn:** [Md Peer Siddiqui](https://linkedin.com)
