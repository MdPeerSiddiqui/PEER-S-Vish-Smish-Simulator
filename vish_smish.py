#!/usr/bin/env python3
r"""
================================================================================
  _____  ______ ______ _____  _  _____ 
 |  __ \|  ____|  ____|  __ \(_)/ ____|
 | |__) | |__  | |__  | |__) |_| (___  
 |  ___/|  __| |  __| |  _  /   \___ \ 
 | |    | |____| |____| | \ \   ____) |
 |_|    |______|______|_|  \_\ |_____/ 
  __     ___     _     _             _____           _     _     
  \ \   / (_)   | |   (_)           / ____|         (_)   | |    
   \ \_/ / _ ___| |__  _ _ __   __ | (___  _ __ ___  _ ___| |__  
    \   / | / __| '_ \| | '_ \ / _` \___ \| '_ ` _ \| / __| '_ \ 
     | |  | \__ \ | | | | | | | (_| |___) | | | | | | \__ \ | | |
     |_|  |_|___/_| |_|_|_| |_|\__, |_____/|_| |_| |_|_|___/_| |_|
                                __/ |                             
                               |___/                              
 ⚡ PEER'S VISH & SMISH SIMULATOR v1.0 — CLI ENGINE ⚡
 Developed for Sqrock IT Solution | Alpha 2 Cybersecurity Internship (Day 04)
 Author: Md Peer Siddiqui
 Repository: https://github.com/MdPeerSiddiqui/PEER-S-Vish-Smish-Simulator
================================================================================
"""

import os
import sys
import json
import argparse
from typing import Dict, List, Optional, Tuple

# Safe Colorama Import
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
    C_CYAN = Fore.CYAN
    C_BLUE = Fore.BLUE
    C_GREEN = Fore.GREEN
    C_YELLOW = Fore.YELLOW
    C_RED = Fore.RED
    C_MAGENTA = Fore.MAGENTA
    C_WHITE = Fore.WHITE
    C_BRIGHT = Style.BRIGHT
    C_DIM = Style.DIM
    C_RESET = Style.RESET_ALL
except ImportError:
    C_CYAN = "\033[36m"
    C_BLUE = "\033[34m"
    C_GREEN = "\033[32m"
    C_YELLOW = "\033[33m"
    C_RED = "\033[31m"
    C_MAGENTA = "\033[35m"
    C_WHITE = "\033[37m"
    C_BRIGHT = "\033[1m"
    C_DIM = "\033[2m"
    C_RESET = "\033[0m"

# Ensure UTF-8 printing in Windows terminal
if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except AttributeError:
        pass

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SCENARIOS_FILE = os.path.join(CURRENT_DIR, "scenarios.json")

BANNER = rf"""{C_CYAN}{C_BRIGHT}
  _____  ______ ______ _____  _  _____ 
 |  __ \|  ____|  ____|  __ \(_)/ ____|
 | |__) | |__  | |__  | |__) |_| (___  
 |  ___/|  __| |  __| |  _  /   \___ \ 
 | |    | |____| |____| | \ \   ____) |
 |_|    |______|______|_|  \_\ |_____/ 
  __     ___     _     _             _____           _     _     
  \ \   / (_)   | |   (_)           / ____|         (_)   | |    
   \ \_/ / _ ___| |__  _ _ __   __ | (___  _ __ ___  _ ___| |__  
    \   / | / __| '_ \| | '_ \ / _` \___ \| '_ ` _ \| / __| '_ \ 
     | |  | \__ \ | | | | | | | (_| |___) | | | | | | \__ \ | | |
     |_|  |_|___/_| |_|_|_| |_|\__, |_____/|_| |_| |_|_|___/_| |_|
                                __/ |                             
                               |___/                              
{C_RESET}
{C_YELLOW}{C_BRIGHT} ⚡ PEER'S VISH & SMISH SIMULATOR v1.0 — PRODUCTION CLI SUITE ⚡{C_RESET}
{C_WHITE}{C_DIM} [★] Developed for Sqrock IT Solution | Alpha 2 Cybersecurity Track (Day 04){C_RESET}
{C_CYAN}{"=" * 82}{C_RESET}
"""


# =============================================================================
# DATA LAYER & SCENARIO LOADER
# =============================================================================

def load_scenarios() -> List[Dict]:
    """Load the master database of social engineering simulation scenarios."""
    if not os.path.exists(SCENARIOS_FILE):
        print(f"{C_RED}[!] Critical Error: Scenarios database '{SCENARIOS_FILE}' not found.{C_RESET}")
        sys.exit(1)

    try:
        with open(SCENARIOS_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        print(f"{C_RED}[!] Error parsing scenarios database: {e}{C_RESET}")
        sys.exit(1)


def get_scenario_by_id(scenarios: List[Dict], scenario_id: str) -> Optional[Dict]:
    """Retrieve a specific scenario by its unique identifier."""
    clean_id = scenario_id.strip().lower()
    for sc in scenarios:
        if sc.get("id", "").lower() == clean_id:
            return sc
    return None


# =============================================================================
# HEURISTIC ANALYSIS & PSYCHOLOGICAL TRIGGER RADAR
# =============================================================================

def calculate_trigger_composite_score(triggers: Dict[str, int]) -> Tuple[int, str]:
    """
    Calculate an overall psychological attack intensity index (0 to 100)
    weighted across Urgency, Authority, Fear, Scarcity, and Sympathy.
    """
    weights = {
        "urgency": 0.25,
        "fear_intimidation": 0.25,
        "authority": 0.20,
        "scarcity": 0.15,
        "sympathy_helpfulness": 0.15
    }

    weighted_sum = sum(triggers.get(k, 50) * weights[k] for k in weights)
    final_score = int(min(max(weighted_sum, 0), 100))

    if final_score >= 85:
        tier = "Critical Manipulation"
    elif final_score >= 70:
        tier = "High Psychological Pressure"
    elif final_score >= 50:
        tier = "Moderate Psychological Coercion"
    else:
        tier = "Low / Subtle Elicitation"

    return final_score, tier


def render_ascii_trigger_bar(name: str, value: int, width: int = 24) -> str:
    """Render a clean visual progress bar representing trigger intensity."""
    filled = int((value / 100.0) * width)
    unfilled = width - filled
    
    if value >= 80:
        bar_color = C_RED
    elif value >= 60:
        bar_color = C_YELLOW
    else:
        bar_color = C_GREEN

    bar = f"{bar_color}[{'█' * filled}{'░' * unfilled}]{C_RESET} {C_BRIGHT}{value:>3}%{C_RESET}"
    return f"  {C_WHITE}{name:<22}{C_RESET} : {bar}"


def calculate_sms_segments(message: str) -> Tuple[int, int, bool]:
    """
    Analyze SMS character count against standard GSM-7 (160 characters)
    and multi-part concatenated SMS segmentation limits.
    """
    char_len = len(message)
    if char_len <= 160:
        segments = 1
        fits_single_sms = True
    else:
        # Concatenated SMS uses 153 chars per segment due to UDH header
        segments = (char_len + 152) // 153
        fits_single_sms = False

    return char_len, segments, fits_single_sms


# =============================================================================
# FORMATTED PRINTERS & SIMULATION CARDS
# =============================================================================

def print_scenario_card(scenario: Dict, victim_name: str = "[Target Employee]"):
    """Render a comprehensive forensic overview of a social engineering attack scenario."""
    sc_id = scenario.get("id", "N/A")
    title = scenario.get("title", "Untitled Scenario")
    category = scenario.get("category", "General Social Engineering")
    caller = scenario.get("caller_persona", "Unknown Caller")
    spoofed_num = scenario.get("spoofed_caller_id", "Unknown Number")
    target = scenario.get("target_persona", "General User")
    triggers = scenario.get("psychological_triggers", {})
    score, tier = calculate_trigger_composite_score(triggers)

    print(f"\n{C_CYAN}{'=' * 82}{C_RESET}")
    print(f"{C_WHITE}{C_BRIGHT}SCENARIO IDENTIFIER :{C_RESET} {C_YELLOW}{sc_id}{C_RESET}")
    print(f"{C_WHITE}{C_BRIGHT}ATTACK TITLE        :{C_RESET} {C_WHITE}{C_BRIGHT}{title}{C_RESET}")
    print(f"{C_WHITE}{C_BRIGHT}INDUSTRY CATEGORY   :{C_RESET} {C_CYAN}{category}{C_RESET}")
    print(f"{C_CYAN}{'-' * 82}{C_RESET}")
    print(f"{C_WHITE}Attacker Pretext Persona :{C_RESET} {C_MAGENTA}{caller}{C_RESET}")
    print(f"{C_WHITE}Spoofed Caller ID Line   :{C_RESET} {C_RED}{spoofed_num}{C_RESET}")
    print(f"{C_WHITE}Target Profile Persona   :{C_RESET} {C_WHITE}{target}{C_RESET}")
    print(f"{C_WHITE}Psychological Intensity  :{C_RESET} {C_YELLOW}{score}/100{C_RESET} ({C_BRIGHT}{tier}{C_RESET})")
    print(f"{C_CYAN}{'-' * 82}{C_RESET}")

    # Psychological Radar
    print(f"{C_YELLOW}{C_BRIGHT}Psychological Manipulation Levers:{C_RESET}")
    print(render_ascii_trigger_bar("Urgency & Time Scarcity", triggers.get("urgency", 0)))
    print(render_ascii_trigger_bar("Authority & Hierarchy", triggers.get("authority", 0)))
    print(render_ascii_trigger_bar("Fear & Intimidation", triggers.get("fear_intimidation", 0)))
    print(render_ascii_trigger_bar("Scarcity / Exclusivity", triggers.get("scarcity", 0)))
    print(render_ascii_trigger_bar("Sympathy & Helpfulness", triggers.get("sympathy_helpfulness", 0)))
    print(f"{C_CYAN}{'-' * 82}{C_RESET}")

    # Vishing Call Script Progression
    v_script = scenario.get("vishing_script", {})
    print(f"{C_YELLOW}{C_BRIGHT}🎙️ VISHING DIALOGUE FLOW (5-PHASE ATTACK PROGRESSION):{C_RESET}")
    
    p1 = v_script.get("phase_1_intro", "").replace("[Victim Name]", victim_name)
    p2 = v_script.get("phase_2_hook", "").replace("[Victim Name]", victim_name)
    p3 = v_script.get("phase_3_the_ask", "").replace("[Victim Name]", victim_name)
    p5 = v_script.get("phase_5_exit", "").replace("[Victim Name]", victim_name)

    print(f"  {C_CYAN}[Phase 1: Introduction & Pretext Setup]{C_RESET}")
    print(f"  {C_WHITE}\"{p1}\"{C_RESET}\n")

    print(f"  {C_CYAN}[Phase 2: The Hook & Fabricated Crisis]{C_RESET}")
    print(f"  {C_WHITE}\"{p2}\"{C_RESET}\n")

    print(f"  {C_RED}{C_BRIGHT}[Phase 3: The Ask (Credential/Token Exploitation)]{C_RESET}")
    print(f"  {C_WHITE}\"{p3}\"{C_RESET}\n")

    print(f"  {C_CYAN}[Phase 4: Handling Victim Objections (Pre-Scripted Counters)]{C_RESET}")
    objections = v_script.get("phase_4_objections", {})
    for obj_victim, counter in objections.items():
        print(f"    {C_YELLOW}• {obj_victim}{C_RESET}")
        print(f"      {C_DIM}└── Counter-Pretext: \"{counter}\"{C_RESET}")
    print()

    print(f"  {C_CYAN}[Phase 5: Exit Strategy & Compromise Masking]{C_RESET}")
    print(f"  {C_WHITE}\"{p5}\"{C_RESET}")
    print(f"{C_CYAN}{'-' * 82}{C_RESET}")

    # Smishing Lure Preview
    s_lure = scenario.get("smishing_lure", {})
    s_sender = s_lure.get("sender_id", "SMS-ALERT")
    s_body = s_lure.get("message_body", "").replace("[Victim Name]", victim_name)
    chars, segs, single_sms = calculate_sms_segments(s_body)

    print(f"{C_YELLOW}{C_BRIGHT}📱 CORRESPONDING SMISHING LURE (MOBILE SHORT-MESSAGE PREVIEW):{C_RESET}")
    print(f"  {C_WHITE}Spoofed Sender Tag :{C_RESET} {C_RED}{C_BRIGHT}{s_sender}{C_RESET}")
    print(f"  {C_WHITE}Message Length     :{C_RESET} {C_CYAN}{chars} chars{C_RESET} ({'1 Segment' if single_sms else f'{segs} Segments'})")
    print(f"  {C_WHITE}Deceptive Link     :{C_RESET} {C_YELLOW}{s_lure.get('deceptive_url', 'N/A')}{C_RESET}")
    print(f"  ┌{'─' * 74}┐")
    print(f"  │ {s_body:<72} │")
    print(f"  └{'─' * 74}┘")
    print(f"{C_CYAN}{'-' * 82}{C_RESET}")

    # Technical Indicators & Defenses
    tech = scenario.get("technical_indicators", {})
    defenses = scenario.get("defensive_countermeasures", [])

    print(f"{C_YELLOW}{C_BRIGHT}🛡️ TECHNICAL FORENSICS & ENTERPRISE DEFENSIVE CONTROLS:{C_RESET}")
    print(f"  {C_WHITE}Spoofing Vector  :{C_RESET} {C_DIM}{tech.get('spoofing_vector', 'N/A')}{C_RESET}")
    print(f"  {C_WHITE}Smishing Channel :{C_RESET} {C_DIM}{tech.get('smishing_channel', 'N/A')}{C_RESET}")
    print(f"  {C_WHITE}Defense Bypass   :{C_RESET} {C_DIM}{tech.get('defense_bypass', 'N/A')}{C_RESET}")
    print(f"\n  {C_GREEN}{C_BRIGHT}Recommended Out-of-Band & Architectural Mitigations:{C_RESET}")
    for idx, d in enumerate(defenses, 1):
        print(f"    {C_GREEN}[{idx}]{C_RESET} {d}")
    print(f"{C_CYAN}{'=' * 82}{C_RESET}\n")


# =============================================================================
# INTERACTIVE SIMULATION & BENCHMARK FUNCTIONS
# =============================================================================

def run_interactive_call_roleplay(scenario: Dict, victim_name: str = "Alex"):
    """Walk through an interactive step-by-step voice call simulation."""
    print(f"\n{C_MAGENTA}{'=' * 82}{C_RESET}")
    print(f"{C_WHITE}{C_BRIGHT}⚡ INITIATING LIVE VISHING CALL SIMULATION: {scenario.get('title')}{C_RESET}")
    print(f"{C_WHITE}{C_DIM}In this roleplay mode, you will experience how attackers maneuver phone pretexts.{C_RESET}")
    print(f"{C_MAGENTA}{'=' * 82}{C_RESET}\n")

    v_script = scenario.get("vishing_script", {})
    p1 = v_script.get("phase_1_intro", "").replace("[Victim Name]", victim_name)
    p2 = v_script.get("phase_2_hook", "").replace("[Victim Name]", victim_name)
    p3 = v_script.get("phase_3_the_ask", "").replace("[Victim Name]", victim_name)
    p5 = v_script.get("phase_5_exit", "").replace("[Victim Name]", victim_name)
    objections = v_script.get("phase_4_objections", {})

    print(f"{C_YELLOW}[Phone Rings... Incoming Call from: {C_RED}{scenario.get('spoofed_caller_id')}{C_YELLOW}]{C_RESET}")
    input(f"{C_CYAN}  --> Press [ENTER] to answer the call... {C_RESET}")

    print(f"\n{C_CYAN}CALLER:{C_RESET} \"{p1}\"\n")
    input(f"{C_CYAN}  --> Press [ENTER] to continue... {C_RESET}")

    print(f"\n{C_CYAN}CALLER:{C_RESET} \"{p2}\"\n")
    input(f"{C_CYAN}  --> Press [ENTER] to continue to the exploit phase... {C_RESET}")

    print(f"\n{C_RED}{C_BRIGHT}CALLER (THE ASK):{C_RESET} \"{p3}\"\n")

    # Present Victim Choices
    print(f"{C_YELLOW}{C_BRIGHT}[DECISION POINT] How do you respond to this request?{C_RESET}")
    obj_keys = list(objections.keys())
    for i, obj_text in enumerate(obj_keys, 1):
        print(f"  [{i}] {obj_text}")
    print(f"  [{len(obj_keys) + 1}] Comply immediately and read back the requested token/credentials.")
    print(f"  [{len(obj_keys) + 2}] Hang up immediately and verify via Out-of-Band official phone directory.")

    while True:
        try:
            choice = input(f"\n{C_CYAN}  Select your response (1-{len(obj_keys) + 2}) > {C_RESET}").strip()
            if not choice.isdigit():
                print(f"{C_RED}[!] Please enter a valid number.{C_RESET}")
                continue
            idx = int(choice)
            if 1 <= idx <= len(obj_keys):
                selected_obj = obj_keys[idx - 1]
                counter_text = objections[selected_obj]
                print(f"\n{C_YELLOW}YOU:{C_RESET} \"{selected_obj}\"")
                print(f"{C_CYAN}CALLER (COUNTER-PRETEXT):{C_RESET} \"{counter_text}\"\n")
                input(f"{C_CYAN}  --> Press [ENTER] to conclude the simulation... {C_RESET}")
                break
            elif idx == len(obj_keys) + 1:
                print(f"\n{C_RED}[!] CRITICAL COMPROMISE: You complied with the vishing pretext!{C_RESET}")
                print(f"{C_RED}    The attacker captured your authentication token and gained unauthorized access.{C_RESET}\n")
                break
            elif idx == len(obj_keys) + 2:
                print(f"\n{C_GREEN}[✔] SUCCESSFUL DEFENSE: Out-of-band verification protocol executed!{C_RESET}")
                print(f"{C_GREEN}    By hanging up and verifying independently, you thwarted the vishing attack.{C_RESET}\n")
                return
            else:
                print(f"{C_RED}[!] Invalid choice. Please pick between 1 and {len(obj_keys) + 2}.{C_RESET}")
        except (KeyboardInterrupt, EOFError):
            print(f"\n{C_RED}[!] Simulation terminated.{C_RESET}")
            return

    print(f"\n{C_CYAN}CALLER:{C_RESET} \"{p5}\"")
    print(f"{C_DIM}[Call Disconnected]{C_RESET}\n")


def run_benchmark_audit(scenarios: List[Dict], export_reports: bool = True) -> List[Dict]:
    """Execute a comprehensive benchmark audit across all 10 social engineering scenarios."""
    print(f"\n{C_YELLOW}{C_BRIGHT}[*] EXECUTING 10-CATEGORY SOCIAL ENGINEERING BENCHMARK AUDIT...{C_RESET}")
    print(f"{C_WHITE}{C_DIM}Auditing trigger intensity, character segmentation, and defensive controls.{C_RESET}\n")

    header = f"{'#':<3} | {'Scenario ID':<18} | {'Category':<28} | {'Intensity':<12} | {'Risk Tier'}"
    print(header)
    print("-" * 88)

    audit_summary = []
    for idx, sc in enumerate(scenarios, 1):
        sc_id = sc.get("id", "unknown")
        cat = sc.get("category", "General")
        triggers = sc.get("psychological_triggers", {})
        score, tier = calculate_trigger_composite_score(triggers)
        s_body = sc.get("smishing_lure", {}).get("message_body", "")
        chars, segs, single_sms = calculate_sms_segments(s_body)

        audit_summary.append({
            "index": idx,
            "id": sc_id,
            "title": sc.get("title"),
            "category": cat,
            "intensity_score": score,
            "risk_tier": tier,
            "sms_characters": chars,
            "sms_segments": segs,
            "fits_single_sms": single_sms,
            "triggers": triggers,
            "defenses_count": len(sc.get("defensive_countermeasures", []))
        })

        if score >= 85:
            tier_colored = f"{C_RED}{tier}{C_RESET}"
        elif score >= 70:
            tier_colored = f"{C_YELLOW}{tier}{C_RESET}"
        else:
            tier_colored = f"{C_GREEN}{tier}{C_RESET}"

        print(f"{idx:<3} | {sc_id:<18} | {cat[:28]:<28} | {score:>3}/100     | {tier_colored}")

    print("-" * 88)
    print(f"{C_GREEN}[✔] Benchmark Complete: All 10 industry categories audited successfully.{C_RESET}")

    if export_reports:
        reports_dir = os.path.join(CURRENT_DIR, "reports")
        os.makedirs(reports_dir, exist_ok=True)

        json_out = os.path.join(reports_dir, "scenario_audit_results.json")
        with open(json_out, "w", encoding="utf-8") as f:
            json.dump(audit_summary, f, indent=4)
        print(f"{C_WHITE}[★] Structured Audit JSON Saved : {C_GREEN}{json_out}{C_RESET}")

        txt_out = os.path.join(reports_dir, "scenario_audit_results.txt")
        with open(txt_out, "w", encoding="utf-8") as f:
            f.write("PEER'S VISH & SMISH SIMULATOR — 10-CATEGORY BENCHMARK AUDIT\n")
            f.write("=" * 80 + "\n\n")
            for item in audit_summary:
                f.write(f"#{item['index']} | {item['id']} — {item['title']}\n")
                f.write(f"Category: {item['category']}\n")
                f.write(f"Composite Score: {item['intensity_score']}/100 ({item['risk_tier']})\n")
                f.write(f"SMS Payload: {item['sms_characters']} chars ({item['sms_segments']} segment)\n")
                f.write(f"Triggers: {item['triggers']}\n")
                f.write("-" * 80 + "\n")
        print(f"{C_WHITE}[★] Plaintext Audit Log Saved   : {C_GREEN}{txt_out}{C_RESET}\n")

    return audit_summary


# =============================================================================
# INTERACTIVE CLI DISPATCHER
# =============================================================================

def display_menu():
    """Display the master interactive CLI menu."""
    print(f"\n{C_CYAN}┌──────────────────────── MASTER CONTROL MENU ────────────────────────┐{C_RESET}")
    print(f"{C_CYAN}│{C_RESET} [1] {C_WHITE}Generate Full Attack Simulation (Choose from 10 Categories){C_RESET}     {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}│{C_RESET} [2] {C_WHITE}Interactive Live Call Roleplay (Step-by-Step Vishing Test){C_RESET}      {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}│{C_RESET} [3] {C_WHITE}Psychological Trigger Intensity Radar (0–100 Scorer){C_RESET}            {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}│{C_RESET} [4] {C_WHITE}Smishing Lure & GSM Character Segmentation Analyzer{C_RESET}             {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}│{C_RESET} [5] {C_WHITE}Telecom Defense Matrix (STIR/SHAKEN & Out-of-Band Protocols){C_RESET}   {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}│{C_RESET} [6] {C_WHITE}Run 10-Category Benchmark Audit (Exports JSON & TXT Logs){C_RESET}       {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}│{C_RESET} [7] {C_WHITE}Compile Executive 4-Page PDF Lab Report{C_RESET}                          {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}│{C_RESET} [8] {C_WHITE}Exit Simulation Suite{C_RESET}                                           {C_CYAN}│{C_RESET}")
    print(f"{C_CYAN}└──────────────────────────────────────────────────────────────────────┘{C_RESET}")


def select_scenario_interactive(scenarios: List[Dict]) -> Optional[Dict]:
    """Helper prompt allowing users to choose an attack scenario cleanly."""
    print(f"\n{C_YELLOW}{C_BRIGHT}Available Social Engineering Industry Categories:{C_RESET}")
    for idx, sc in enumerate(scenarios, 1):
        print(f"  [{idx:02d}] {C_CYAN}{sc.get('id'):<18}{C_RESET} — {sc.get('category')}")
    print(f"  [00] Return to main menu")

    while True:
        try:
            choice = input(f"\n{C_CYAN}Select scenario number (1-{len(scenarios)}) or ID > {C_RESET}").strip()
            if not choice:
                continue
            if choice in ("0", "00", "q", "exit"):
                return None

            # Try by numeric index
            if choice.isdigit():
                num = int(choice)
                if 1 <= num <= len(scenarios):
                    return scenarios[num - 1]
                else:
                    print(f"{C_RED}[!] Invalid number. Pick between 1 and {len(scenarios)}.{C_RESET}")
                    continue

            # Try by ID string
            matched = get_scenario_by_id(scenarios, choice)
            if matched:
                return matched

            print(f"{C_RED}[!] Scenario '{choice}' not found. Try again or type '0' to cancel.{C_RESET}")
        except (KeyboardInterrupt, EOFError):
            print()
            return None


def run_interactive_cli(scenarios: List[Dict]):
    """Main execution loop for the command-line interface."""
    while True:
        try:
            display_menu()
            choice = input(f"{C_CYAN}PEER-SIM > {C_RESET}").strip()

            if not choice:
                continue

            if choice in ("8", "exit", "quit", "q"):
                print(f"\n{C_GREEN}[*] Thank you for using PEER'S Vish & Smish Simulator. Stay secure!{C_RESET}\n")
                break

            elif choice == "1":
                sc = select_scenario_interactive(scenarios)
                if sc:
                    v_name = input(f"{C_CYAN}Enter target employee name (or press ENTER for default) > {C_RESET}").strip()
                    if not v_name:
                        v_name = "[Target Employee]"
                    print_scenario_card(sc, victim_name=v_name)

            elif choice == "2":
                sc = select_scenario_interactive(scenarios)
                if sc:
                    v_name = input(f"{C_CYAN}Enter target employee name (or press ENTER for 'Alex') > {C_RESET}").strip()
                    if not v_name:
                        v_name = "Alex"
                    run_interactive_call_roleplay(sc, victim_name=v_name)

            elif choice == "3":
                sc = select_scenario_interactive(scenarios)
                if sc:
                    triggers = sc.get("psychological_triggers", {})
                    score, tier = calculate_trigger_composite_score(triggers)
                    print(f"\n{C_YELLOW}{C_BRIGHT}--- PSYCHOLOGICAL TRIGGER RADAR: {sc.get('title')} ---{C_RESET}")
                    print(render_ascii_trigger_bar("Urgency & Time Scarcity", triggers.get("urgency", 0)))
                    print(render_ascii_trigger_bar("Authority & Hierarchy", triggers.get("authority", 0)))
                    print(render_ascii_trigger_bar("Fear & Intimidation", triggers.get("fear_intimidation", 0)))
                    print(render_ascii_trigger_bar("Scarcity / Exclusivity", triggers.get("scarcity", 0)))
                    print(render_ascii_trigger_bar("Sympathy & Helpfulness", triggers.get("sympathy_helpfulness", 0)))
                    print(f"\n  {C_WHITE}Composite Manipulation Index :{C_RESET} {C_BRIGHT}{score}/100 ({tier}){C_RESET}\n")

            elif choice == "4":
                sc = select_scenario_interactive(scenarios)
                if sc:
                    lure = sc.get("smishing_lure", {})
                    body = lure.get("message_body", "")
                    chars, segs, single_sms = calculate_sms_segments(body)
                    print(f"\n{C_YELLOW}{C_BRIGHT}--- SMISHING GSM PAYLOAD AUDIT ---{C_RESET}")
                    print(f"  {C_WHITE}Sender Tag   :{C_RESET} {C_RED}{lure.get('sender_id')}{C_RESET}")
                    print(f"  {C_WHITE}Total Chars  :{C_RESET} {C_CYAN}{chars}{C_RESET} / 160 GSM standard limit")
                    print(f"  {C_WHITE}SMS Segments :{C_RESET} {C_BRIGHT}{segs}{C_RESET} ({'Fits in single SMS' if single_sms else 'Concatenated SMS'})")
                    print(f"  {C_WHITE}Shortlink    :{C_RESET} {C_YELLOW}{lure.get('deceptive_url')}{C_RESET}")
                    print(f"  {C_WHITE}Message Body :{C_RESET} \"{body}\"\n")

            elif choice == "5":
                print(f"\n{C_CYAN}{'=' * 82}{C_RESET}")
                print(f"{C_YELLOW}{C_BRIGHT}TELECOM DEFENSE MATRIX: STIR/SHAKEN & CALLER ID AUTHENTICATION{C_RESET}")
                print(f"{C_CYAN}{'-' * 82}{C_RESET}")
                print(f"  {C_WHITE}• STIR (Secure Telephony Identity Revisited):{C_RESET} Cryptographically signs VoIP SIP invites.")
                print(f"  {C_WHITE}• SHAKEN (Signature-based Handling of Asserted information):{C_RESET} Carrier verification framework.")
                print(f"\n  {C_CYAN}Attestation Levels Defined:{C_RESET}")
                print(f"    {C_GREEN}[Full Attestation (A)]{C_RESET} Carrier knows customer & verifies right to use phone number.")
                print(f"    {C_YELLOW}[Partial Attestation (B)]{C_RESET} Carrier knows customer, but cannot verify right to use number.")
                print(f"    {C_RED}[Gateway Attestation (C)]{C_RESET} Carrier received call from international gateway without origin info.")
                print(f"\n  {C_GREEN}Enterprise Out-of-Band (OOB) Rule:{C_RESET}")
                print(f"    Never trust inbound caller ID. Terminate call and dial the published organization")
                print(f"    telephone number obtained independently from a verified physical card or directory.")
                print(f"{C_CYAN}{'=' * 82}{C_RESET}\n")

            elif choice == "6":
                run_benchmark_audit(scenarios, export_reports=True)

            elif choice == "7":
                try:
                    from scripts.generate_day04_pdf import create_day04_report
                    out_pdf = create_day04_report()
                    print(f"\n{C_GREEN}[✔] Official 4-Page Executive PDF Report successfully compiled at:{C_RESET}")
                    print(f"    {C_WHITE}{out_pdf}{C_RESET}\n")
                except Exception as e:
                    print(f"{C_RED}[!] Error compiling PDF report: {e}{C_RESET}")

            else:
                print(f"{C_RED}[!] Invalid option '{choice}'. Please pick a number from 1 to 8.{C_RESET}")

        except (KeyboardInterrupt, EOFError):
            print(f"\n{C_RED}[!] Session interrupted by user. Exiting...{C_RESET}\n")
            break


# =============================================================================
# MAIN CLI ENTRYPOINT & SCRIPTING FLAGS
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="PEER'S Vish & Smish Simulator — Multi-Category Social Engineering Simulation Suite"
    )
    parser.add_argument(
        "--scenario",
        type=str,
        default=None,
        help="Directly output simulation for a specific scenario ID (e.g. 'it_support', 'banking_fraud')",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available social engineering scenario categories",
    )
    parser.add_argument(
        "--test",
        action="store_true",
        help="Run the automated 10-category benchmark audit and export reports",
    )
    parser.add_argument(
        "--export-json",
        action="store_true",
        help="Export all 10 scenario definitions to reports/scenarios_export.json",
    )
    parser.add_argument(
        "--export-pdf",
        action="store_true",
        help="Compile the official 4-Page Executive Cybersecurity Lab Report PDF",
    )
    parser.add_argument(
        "--victim",
        type=str,
        default="[Target Employee]",
        help="Target employee name to inject into vishing and smishing scripts",
    )

    args = parser.parse_args()
    scenarios = load_scenarios()

    # Flag 1: List Scenarios
    if args.list:
        print(BANNER)
        print(f"{C_YELLOW}{C_BRIGHT}Available Social Engineering Industry Categories ({len(scenarios)} Total):{C_RESET}")
        for idx, sc in enumerate(scenarios, 1):
            triggers = sc.get("psychological_triggers", {})
            score, tier = calculate_trigger_composite_score(triggers)
            print(f"  [{idx:02d}] {C_CYAN}{sc.get('id'):<18}{C_RESET} | {sc.get('category'):<30} | {C_YELLOW}{score}/100{C_RESET} ({tier})")
        return

    # Flag 2: Benchmark Audit
    if args.test:
        print(BANNER)
        run_benchmark_audit(scenarios, export_reports=True)
        return

    # Flag 3: Export JSON
    if args.export_json:
        out_dir = os.path.join(CURRENT_DIR, "reports")
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "scenarios_export.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(scenarios, f, indent=4)
        print(f"{C_GREEN}[✔] Successfully exported {len(scenarios)} scenarios to: {out_path}{C_RESET}")
        return

    # Flag 4: Export PDF
    if args.export_pdf:
        try:
            from scripts.generate_day04_pdf import create_day04_report
            pdf_path = create_day04_report()
            print(f"{C_GREEN}[✔] Executive PDF compiled at: {pdf_path}{C_RESET}")
        except Exception as e:
            print(f"{C_RED}[!] Error compiling PDF: {e}{C_RESET}")
        return

    # Flag 5: Direct Scenario Evaluation
    if args.scenario:
        sc = get_scenario_by_id(scenarios, args.scenario)
        if not sc:
            print(f"{C_RED}[!] Scenario ID '{args.scenario}' not found. Use '--list' to see valid IDs.{C_RESET}")
            sys.exit(1)
        print(BANNER)
        print_scenario_card(sc, victim_name=args.victim)
        return

    # Default: Interactive CLI Master Menu
    print(BANNER)
    run_interactive_cli(scenarios)


if __name__ == "__main__":
    main()
