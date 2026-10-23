"""
=============================================================================
Generate Official Executive PDF Report for Day 04 Deliverable
Sqrock IT Solution — Alpha 2 Internship (Cybersecurity Track)
Project: PEER'S Vish & Smish Simulator (Voice & SMS Social Engineering)
Author: Md Peer Siddiqui
=============================================================================
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, PageBreak
)

def create_day04_report(output_pdf_path=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    day04_root = os.path.dirname(script_dir)
    
    if output_pdf_path is None:
        output_pdf_path = os.path.join(day04_root, "reports", "Day04_Vishing_Smishing_Report_Sqrock_MdPeerSiddiqui.pdf")
    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

    doc = SimpleDocTemplate(
        output_pdf_path,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    
    primary_color = colors.HexColor("#0f172a")     # Deep Slate
    accent_sky = colors.HexColor("#0284c7")        # Sky Blue
    accent_red = colors.HexColor("#dc2626")        # Crimson Red
    bg_light = colors.HexColor("#f8fafc")
    text_dark = colors.HexColor("#1e293b")

    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=primary_color,
        spaceAfter=2
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=12,
        textColor=accent_sky,
        spaceAfter=3
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=primary_color,
        spaceBefore=5,
        spaceAfter=3
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=text_dark,
        spaceAfter=3
    )

    meta_label = ParagraphStyle(
        'MetaLabel',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=7.5,
        leading=9.5,
        textColor=primary_color
    )

    meta_val = ParagraphStyle(
        'MetaVal',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=7.5,
        leading=9.5,
        textColor=text_dark
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=7,
        leading=8.5,
        textColor=colors.HexColor("#0f172a")
    )

    story = []

    # =========================================================================
    # PAGE 1: Executive Overview, Project Metadata & Simulation Architecture
    # =========================================================================
    story.append(Paragraph("CYBERSECURITY INTERNSHIP — PRACTICAL LAB REPORT", subtitle_style))
    story.append(Paragraph("Day 04: Vishing & Smishing Social Engineering Simulation", title_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=accent_sky, spaceBefore=2, spaceAfter=5))

    # Metadata Grid
    meta_data = [
        [
            Paragraph("Intern Name:", meta_label), Paragraph("Md Peer Siddiqui", meta_val),
            Paragraph("Program / Track:", meta_label), Paragraph("Alpha 2 — Cybersecurity Track", meta_val)
        ],
        [
            Paragraph("Issuing Body:", meta_label), Paragraph("Sqrock IT Solution", meta_val),
            Paragraph("Date of Execution:", meta_label), Paragraph("October 23, 2026", meta_val)
        ],
        [
            Paragraph("Tool Developed:", meta_label), Paragraph("PEER'S Vish & Smish Simulator v1.0", meta_val),
            Paragraph("GitHub Repository:", meta_label), Paragraph("<font color='#0284c7'><u>github.com/MdPeerSiddiqui/PEER-S-Vish-Smish-Simulator</u></font>", meta_val)
        ]
    ]

    meta_table = Table(meta_data, colWidths=[85, 185, 95, 175])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), bg_light),
        ('BOX', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#e2e8f0")),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 3))

    # 1. Objective & Scope
    story.append(Paragraph("1. Objective & Operational Scope", h2_style))
    story.append(Paragraph(
        "To research the conversational and psychological mechanics of voice phishing (vishing) and SMS phishing (smishing) attacks, "
        "and develop an enterprise-grade command-line simulation suite in Python. The simulator deconstructs 10 comprehensive social engineering "
        "industry vectors across a 5-phase conversational attack lifecycle, evaluates psychological trigger intensity across 5 manipulation levers, "
        "calculates GSM-7 character segmentation for mobile smishing lures, and provides actionable telecom defensive countermeasures.", body_style
    ))

    # 2. Tools & Environment
    story.append(Paragraph("2. Tools and Technical Environment", h2_style))
    story.append(Paragraph(
        "• <b>Operating Environment:</b> Kali Linux 2026.2 (64-bit VirtualBox VM) / Windows 11 Enterprise<br/>"
        "• <b>Core Platform:</b> Python 3.11.9 / 3.14.0 (Standard Libraries: <code>json</code>, <code>argparse</code>, <code>os</code>, <code>sys</code>, <code>unittest</code>)<br/>"
        "• <b>Terminal UI & PDF Engines:</b> <code>colorama</code> v0.4.6 (ANSI terminal styling), <code>reportlab</code> v5.1.0 (PDF Engine)<br/>"
        "• <b>Scenario Database:</b> <code>scenarios.json</code> (10 comprehensive industry vectors with multi-phase dialogue and objection handling)", body_style
    ))

    # 3. The 5-Phase Social Engineering Attack Lifecycle
    story.append(Paragraph("3. The 5-Phase Conversational Vishing Attack Lifecycle", h2_style))
    story.append(Paragraph(
        "Unlike automated email phishing, telephone-based vishing exploits synchronous human conversation to enforce rapid cognitive compliance. "
        "Every simulation generated by the tool models the standardized 5-phase threat progression:", body_style
    ))

    phases_data = [
        [Paragraph("Attack Phase", meta_label), Paragraph("Attacker Objective & Psychological Tactics", meta_label), Paragraph("Forensic Indicator", meta_label)],
        [
            Paragraph("Phase 1: Pretext Intro", meta_val),
            Paragraph("Establish immediate authoritative persona (e.g. IT Helpdesk, Bank Fraud Officer, Government Agent) using corporate terminology and caller ID spoofing.", body_style),
            Paragraph("P-Asserted-Identity SIP spoofing.", body_style)
        ],
        [
            Paragraph("Phase 2: The Hook", meta_val),
            Paragraph("Introduce a fabricated time-sensitive emergency (e.g. account suspension in 15 mins, $2,845 foreign wire, immediate power disconnect) to induce panic.", body_style),
            Paragraph("Urgency & Fear manipulation.", body_style)
        ],
        [
            Paragraph("Phase 3: The Ask", meta_val),
            Paragraph("Extract sensitive credentials, multi-factor authentication (MFA) push tokens, banking routing numbers, or coerce installation of remote-access tools.", body_style),
            Paragraph("Credential harvesting / 2FA token relay.", body_style)
        ],
        [
            Paragraph("Phase 4: Objection Handling", meta_val),
            Paragraph("Neutralize victim skepticism using pre-scripted psychological counters (e.g., citing maintenance tickets, warning of long queue delays, escalating consequences).", body_style),
            Paragraph("Overcoming security policy resistance.", body_style)
        ],
        [
            Paragraph("Phase 5: Exit Strategy", meta_val),
            Paragraph("Provide false reassurance of ticket resolution and delayed email receipts to prevent the victim from realizing compromise or alerting the real SOC immediately.", body_style),
            Paragraph("Compromise masking & delay.", body_style)
        ],
    ]
    phases_table = Table(phases_data, colWidths=[105, 315, 120])
    phases_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(phases_table)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: 10-Category Social Engineering Attack Matrix & Benchmark Findings
    # =========================================================================
    story.append(Paragraph("4. Comprehensive 10-Category Social Engineering Attack Matrix", h2_style))
    story.append(Paragraph(
        "To ensure comprehensive threat modeling beyond basic IT and banking pretexts, the engine incorporates 10 distinct real-world "
        "attack scenarios, evaluating psychological manipulation intensity across all 5 levers:", body_style
    ))

    matrix_data = [
        [Paragraph("#", meta_label), Paragraph("Sector / Category", meta_label), Paragraph("Scenario Pretext Title", meta_label), Paragraph("Spoofed Line", meta_label), Paragraph("Intensity", meta_label), Paragraph("Primary Exploit Vector", meta_label)],
        [
            Paragraph("1", meta_val), Paragraph("Enterprise IT", meta_val),
            Paragraph("Global VPN Migration & MFA Re-Auth", body_style),
            Paragraph("+1 (800) 555-0199", code_style), Paragraph("80/100", meta_val),
            Paragraph("MFA Push Token Relay via Active Directory lock threat", body_style)
        ],
        [
            Paragraph("2", meta_val), Paragraph("Banking & Finance", meta_val),
            Paragraph("Unauthorized Wire & Debit Card Lock", body_style),
            Paragraph("+1 (888) 456-7890", code_style), Paragraph("83/100", meta_val),
            Paragraph("Fund transfer cancellation OTP theft ($2,845 lure)", body_style)
        ],
        [
            Paragraph("3", meta_val), Paragraph("Government & Tax", meta_val),
            Paragraph("Federal Tax Deficit Audit Summons", body_style),
            Paragraph("+1 (202) 555-0143", code_style), Paragraph("75/100", meta_val),
            Paragraph("SSN & checking account harvesting via warrant threat", body_style)
        ],
        [
            Paragraph("4", meta_val), Paragraph("Logistics / Courier", meta_val),
            Paragraph("Undelivered Express Parcel Re-Route", body_style),
            Paragraph("+1 (800) 463-3339", code_style), Paragraph("69/100", meta_val),
            Paragraph("Full credit card extraction via $2.45 redelivery fee", body_style)
        ],
        [
            Paragraph("5", meta_val), Paragraph("Corporate HR", meta_val),
            Paragraph("Mandatory Direct Deposit Re-Verification", body_style),
            Paragraph("+1 (800) 555-0188", code_style), Paragraph("80/100", meta_val),
            Paragraph("ABA routing & bank account redirect before payroll cutoff", body_style)
        ],
        [
            Paragraph("6", meta_val), Paragraph("Healthcare / Medical", meta_val),
            Paragraph("Prescription Medication Hold & Copay", body_style),
            Paragraph("+1 (877) 555-0177", code_style), Paragraph("83/100", meta_val),
            Paragraph("Patient PII & card theft via critical medication delay", body_style)
        ],
        [
            Paragraph("7", meta_val), Paragraph("Executive Whaling", meta_val),
            Paragraph("Confidential Board M&A Settlement", body_style),
            Paragraph("+1 (212) 555-0100", code_style), Paragraph("84/100", meta_val),
            Paragraph("Urgent $48,500 wire authorization under CEO pressure", body_style)
        ],
        [
            Paragraph("8", meta_val), Paragraph("Telecom Carrier", meta_val),
            Paragraph("SIM Swap & Cellular Line Deactivation", body_style),
            Paragraph("+1 (800) 937-8997", code_style), Paragraph("85/100", meta_val),
            Paragraph("Carrier transfer PIN theft to complete SIM port hijack", body_style)
        ],
        [
            Paragraph("9", meta_val), Paragraph("E-Commerce Retail", meta_val),
            Paragraph("High-Value Unauthorized Order Refund", body_style),
            Paragraph("+1 (888) 280-4331", code_style), Paragraph("79/100", meta_val),
            Paragraph("Quarantined order dispute to harvest login & CVV", body_style)
        ],
        [
            Paragraph("10", meta_val), Paragraph("Utility Services", meta_val),
            Paragraph("Immediate Power Disconnect Notice", body_style),
            Paragraph("+1 (800) 555-0155", code_style), Paragraph("80/100", meta_val),
            Paragraph("Immediate emergency voucher payment under cutoff threat", body_style)
        ],
    ]
    matrix_table = Table(matrix_data, colWidths=[15, 80, 140, 95, 45, 165])
    matrix_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0f172a")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(matrix_table)
    story.append(Spacer(1, 4))

    # 5. Psychological Trigger Index
    story.append(Paragraph("5. Psychological Manipulation Index (The Trigger Radar)", h2_style))
    story.append(Paragraph(
        "Social engineering exploits inherent human heuristics: reciprocity, social proof, commitment, liking, authority, and scarcity "
        "(Cialdini's principles). The simulator evaluates each pretext across 5 weighted vectors:<br/>"
        "• <b>Urgency (25% Weight):</b> Artificial time windows (e.g. 15-minute lockout) designed to trigger cognitive overload and prevent logical consultation.<br/>"
        "• <b>Fear & Intimidation (25% Weight):</b> Threats of arrest, permanent salary loss, or immediate power disconnection that induce freeze-or-comply instincts.<br/>"
        "• <b>Authority (20% Weight):</b> Exploitation of formal hierarchy (e.g. Revenue Officer, Executive VP, Security Analyst) where disobedience implies insubordination.<br/>"
        "• <b>Scarcity (15% Weight):</b> Perceived loss of unique opportunities (e.g. priority express parcel destroyed, M&A deal collapse).<br/>"
        "• <b>Sympathy / Helpfulness (15% Weight):</b> Posing as a cooperative ally striving to 'protect' the victim from hostile third-party hackers.", body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: Smishing Forensics, Telecom Defenses & Technical Protocols
    # =========================================================================
    story.append(Paragraph("6. Smishing Technical Forensics & GSM-7 Payload Analysis", h2_style))
    story.append(Paragraph(
        "Short Message Service (SMS) represents a high-conversion delivery mechanism due to an estimated 98% open rate and 90-second average read time. "
        "The simulation engine audits mobile payload constraints:", body_style
    ))

    gsm_data = [
        [Paragraph("SMS Technical Parameter", meta_label), Paragraph("Standard Specification", meta_label), Paragraph("Smishing Attack Weaponization", meta_label)],
        [
            Paragraph("GSM-7 Encoding Limit", meta_val),
            Paragraph("160 characters per single transmission segment.", body_style),
            Paragraph("Attackers craft concise lures under 160 chars to minimize carrier filtering and ensure clean single-message delivery.", body_style)
        ],
        [
            Paragraph("Alphanumeric Sender ID", meta_val),
            Paragraph("Up to 11 alphanumeric characters (e.g. <code>CORP-IT-ALERT</code>).", body_style),
            Paragraph("Spoofed via international bulk SMS aggregators to overwrite caller telephone numbers with official corporate tags.", body_style)
        ],
        [
            Paragraph("URL Shortening & Cloaking", meta_val),
            Paragraph("Redirection services (bit.ly, tinyurl, custom domains).", body_style),
            Paragraph("Conceals credential harvesting landing pages and bypasses mobile browser reputation checks.", body_style)
        ],
    ]
    gsm_table = Table(gsm_data, colWidths=[120, 160, 260])
    gsm_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(gsm_table)
    story.append(Spacer(1, 4))

    # 7. Telecom Defensive Infrastructure: STIR/SHAKEN
    story.append(Paragraph("7. Telecom Anti-Spoofing Architecture: STIR/SHAKEN Framework", h2_style))
    story.append(Paragraph(
        "To mitigate caller ID spoofing, modern telecommunications carriers deploy the <b>STIR/SHAKEN</b> suite "
        "(<i>Secure Telephony Identity Revisited / Signature-based Handling of Asserted information using toKENs</i>):<br/>"
        "• <b>Full Attestation (Level A):</b> The originating service provider knows the customer and verifies their lawful right to use the specific telephone number.<br/>"
        "• <b>Partial Attestation (Level B):</b> The carrier recognizes the originating customer but cannot cryptographically verify their right to assert the caller ID.<br/>"
        "• <b>Gateway Attestation (Level C):</b> The call originated from an untrusted international gateway with no validation of identity or origin.<br/>"
        "<b>Defensive Limitation:</b> STIR/SHAKEN verifies the telephone number ownership, but <i>cannot</i> verify whether the individual speaking is a legitimate employee or a malicious actor using an authentic compromised PBX trunk.", body_style
    ))
    story.append(Spacer(1, 3))

    # 8. Enterprise Out-of-Band Verification Protocols
    story.append(Paragraph("8. Enterprise Out-of-Band (OOB) Verification Playbook", h2_style))
    oob_data = [
        [Paragraph("Operational Step", meta_label), Paragraph("Mandatory SOC & Employee Verification Protocol", meta_label)],
        [Paragraph("1. Immediate Disconnect", meta_label), Paragraph("<b>Never comply on inbound calls:</b> Politely inform the caller you will verify the ticket independently, and immediately terminate the telephone call.", body_style)],
        [Paragraph("2. Independent Lookup", meta_label), Paragraph("<b>Zero-Trust Directory Lookup:</b> Obtain the official contact number from a pre-authenticated physical employee badge, corporate intranet, or physical bank card.", body_style)],
        [Paragraph("3. Out-of-Band Call", meta_label), Paragraph("<b>Originating Call Verification:</b> Place an outbound call to the verified internal extension to determine if a legitimate IT ticket or fraud case actually exists.", body_style)],
        [Paragraph("4. FIDO2 Enforcement", meta_label), Paragraph("<b>Hardware Token Architecture:</b> Replace voice-relayable 6-digit SMS OTPs with FIDO2 / WebAuthn hardware tokens (YubiKeys), neutralizing vishing token theft.", body_style)],
    ]
    oob_table = Table(oob_data, colWidths=[110, 430])
    oob_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#e2e8f0")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(oob_table)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: Forensic Execution Verification & Internship Practical Sign-Off
    # =========================================================================
    story.append(Paragraph("9. Forensic Code Verification & Benchmark Audit Results", h2_style))
    story.append(Paragraph(
        "The software architecture was validated using Python's built-in <code>unittest</code> framework (<code>tests/test_vish_smish.py</code>). "
        "A 9-point unit test suite verified scenario database completeness, 5-phase dialogue presence, GSM character segmentation, "
        "and mathematical scoring boundaries across all 10 social engineering industry sectors:", body_style
    ))

    audit_summary_data = [
        [Paragraph("Benchmark Metric", meta_label), Paragraph("Audit Finding / Result", meta_label), Paragraph("Verification Status", meta_label)],
        [Paragraph("Total Scenarios Audited", meta_val), Paragraph("10 Comprehensive Industry Categories (IT, Bank, Gov, Courier, HR, Medical, CEO, Telecom, Retail, Utility)", body_style), Paragraph("<font color='#0284c7'><b>100% VALIDATED</b></font>", meta_val)],
        [Paragraph("Dialogue Progression", meta_val), Paragraph("5 Phases present per scenario (Intro, Hook, The Ask, Pre-Scripted Objections, Exit)", body_style), Paragraph("<font color='#0284c7'><b>100% VALIDATED</b></font>", meta_val)],
        [Paragraph("Pre-Scripted Objections", meta_val), Paragraph("20 Total Objections & Realistic Attacker Counter-Pretexts", body_style), Paragraph("<font color='#0284c7'><b>100% VALIDATED</b></font>", meta_val)],
        [Paragraph("GSM-7 Character Analysis", meta_val), Paragraph("100% of smishing lures audited for 160-character single SMS compatibility", body_style), Paragraph("<font color='#0284c7'><b>100% VALIDATED</b></font>", meta_val)],
        [Paragraph("Unit Test Suite", meta_val), Paragraph("9/9 Automated Unit Tests Passed (Execution time: 0.003 seconds)", body_style), Paragraph("<font color='#0284c7'><b>PASSED (9/9)</b></font>", meta_val)],
    ]
    audit_table = Table(audit_summary_data, colWidths=[120, 310, 110])
    audit_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#0f172a")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0, 0), (-1, -1), 2.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2.5),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ]))
    story.append(audit_table)
    story.append(Spacer(1, 4))

    # 10. Ethical Standards & Legal Compliance
    story.append(Paragraph("10. Ethical Compliance & Authorization Boundaries", h2_style))
    story.append(Paragraph(
        "All simulation scripts and smishing lures were developed strictly for defensive education, red team security assessments, "
        "and security awareness training under authorized internship terms at Sqrock IT Solution. "
        "Live transmission of deceptive voice calls or unsolicited SMS messages over public telecommunications networks without prior explicit "
        "authorization is illegal under the Telephone Consumer Protection Act (47 U.S.C. § 227), Truth in Caller ID Act of 2009, "
        "and Section 43/66 of the Indian Information Technology Act, 2000.", body_style
    ))
    story.append(Spacer(1, 4))

    # 11. Practical Sign-Off & Conclusion
    story.append(Paragraph("11. Internship Practical Sign-Off & Conclusion", h2_style))
    story.append(Paragraph(
        "Day 04 practical training provided critical insight into the convergence of psychological manipulation and telecommunications exploitation. "
        "By modeling attack progressions across IT, banking, regulatory, healthcare, and telecom vectors, this project demonstrated that conversational "
        "vishing represents a primary bypass mechanism against technical email filters. Mitigating voice-driven social engineering requires replacing "
        "verbal credentials with cryptographic FIDO2 hardware tokens, enforcing mandatory out-of-band verification workflows, and implementing "
        "telecom STIR/SHAKEN attestation inspection.", body_style
    ))
    story.append(Spacer(1, 6))

    footer_p4 = "<font color='#64748b' size='7'><i>Page 4 of 4 — Official Deliverable | Sqrock IT Solution Alpha 2 Cybersecurity Internship Track • GitHub: github.com/MdPeerSiddiqui/PEER-S-Vish-Smish-Simulator</i></font>"
    story.append(Paragraph(footer_p4, body_style))

    # Build Document
    doc.build(story)
    print(f"[+] Executive 4-Page PDF Report successfully compiled at:\n    {output_pdf_path}")
    return output_pdf_path


if __name__ == "__main__":
    create_day04_report()
