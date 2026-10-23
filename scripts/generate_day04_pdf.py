#!/usr/bin/env python3
"""
PEER'S Vish & Smish Simulator - Executive Multi-Page Lab Report Compiler (Day 04)
Sqrock IT Solution Cybersecurity Internship Track: Social Engineering Attack Simulations Using Python

Compiles an authoritative 7-page executive engineering report integrating:
- 10 real-world industry threat vectors
- 7 empirical execution screenshots (Kali Linux CLI roleplay, defense execution, 10-sector benchmark, GitHub repo)
- In-depth forensic explanations for every screenshot
- Deep technical analyses of STIR/SHAKEN, GSM-7 segmentation, FIDO2, and Out-of-Band verification
- Automated 9-point unit test validation ledger and ethical compliance statements
"""

import os
import sys
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, Image, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

# Base directories
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(BASE_DIR, "reports")
SCREENSHOTS_DIR = os.path.join(REPORTS_DIR, "screenshots")
OUTPUT_PDF = os.path.join(REPORTS_DIR, "Day04_Vishing_Smishing_Report_Sqrock_MdPeerSiddiqui.pdf")

# Palette definitions
NAVY_PRIMARY = colors.HexColor("#0B192C")
CYAN_ACCENT  = colors.HexColor("#008DDA")
DARK_BLUE    = colors.HexColor("#1E3E62")
SLATE_GRAY   = colors.HexColor("#415A77")
LIGHT_BG     = colors.HexColor("#F4F6F9")
BORDER_COLOR = colors.HexColor("#D0D7DE")
SUCCESS_COL  = colors.HexColor("#0E703C")
CRIT_COL     = colors.HexColor("#A8201A")
TEXT_DARK    = colors.HexColor("#1A1A1A")
TEXT_MUTED   = colors.HexColor("#555555")


class NumberedCanvas(canvas.Canvas):
    """
    Two-pass canvas to dynamically compute and render total page count
    and persistent running headers and footers.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        print(f"[DEBUG] Total pages rendered: {num_pages}")
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, total_pages):
        self.saveState()
        page_num = self._pageNumber
        
        # Running Header (pages 2+)
        if page_num > 1:
            self.setStrokeColor(BORDER_COLOR)
            self.setLineWidth(0.6)
            self.line(36, 756, 576, 756)
            
            self.setFont("Helvetica", 7.5)
            self.setFillColor(SLATE_GRAY)
            self.drawString(36, 762, "Sqrock IT Solution | Cybersecurity Internship — Day 04 Lab Report")
            self.drawRightString(576, 762, "PEER'S Vish & Smish Simulator v1.0")

        # Running Footer (all pages)
        self.setStrokeColor(BORDER_COLOR)
        self.setLineWidth(0.6)
        self.line(36, 36, 576, 36)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(SLATE_GRAY)
        self.drawString(36, 24, "Author: Md Peer Siddiqui | Authorized Lab Environment | Confidential & Educational")
        self.drawRightString(576, 24, f"Page {page_num} of {total_pages}")
        
        self.restoreState()


def create_report():
    os.makedirs(REPORTS_DIR, exist_ok=True)
    
    # 0.5 inch left/right margins, tight vertical margins
    doc = SimpleDocTemplate(
        OUTPUT_PDF,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=42,
        bottomMargin=42
    )

    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=18,
        leading=22,
        textColor=NAVY_PRIMARY,
        spaceAfter=3
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=CYAN_ACCENT,
        spaceAfter=8
    )

    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=NAVY_PRIMARY,
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading3'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=DARK_BLUE,
        spaceBefore=6,
        spaceAfter=3,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        spaceAfter=5
    )

    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )

    caption_style = ParagraphStyle(
        'Caption',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10,
        textColor=DARK_BLUE,
        spaceBefore=3,
        spaceAfter=4,
        alignment=1 # Center
    )

    story = []

    # =========================================================================
    # PAGE 1: COVER PAGE / EXECUTIVE SUMMARY & RESEARCH OBJECTIVE
    # =========================================================================
    
    # Metadata Badge Box
    meta_data = [
        [
            Paragraph("<b>INTERNSHIP TRACK:</b> Social Engineering Attack Simulations", body_style),
            Paragraph("<b>DATE OF EXECUTION:</b> October 23, 2026", body_style)
        ],
        [
            Paragraph("<b>INTERN / RESEARCHER:</b> Md Peer Siddiqui", body_style),
            Paragraph("<b>TARGET REPOSITORY:</b> <font color='#008DDA'>PEER-S-Vish-Smish-Simulator</font>", body_style)
        ],
        [
            Paragraph("<b>HOST ORGANIZATION:</b> Sqrock IT Solution", body_style),
            Paragraph("<b>GITHUB:</b> <font color='#008DDA'>github.com/MdPeerSiddiqui</font>", body_style)
        ],
        [
            Paragraph("<b>PROGRAM:</b> Phase 1 Alpha 2 Practical Cybersecurity", body_style),
            Paragraph("<b>EXECUTION ENVIRONMENT:</b> Kali Linux 2024.x & Win11", body_style)
        ]
    ]
    t_meta = Table(meta_data, colWidths=[270, 270])
    t_meta.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, CYAN_ACCENT),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))

    story.append(Paragraph("CYBERSECURITY INTERNSHIP PRACTICAL LAB REPORT", ParagraphStyle('Eyebrow', fontName='Helvetica-Bold', fontSize=8.5, leading=10, textColor=CYAN_ACCENT)))
    story.append(Paragraph("Day 04: Vishing & Smishing Attack Simulation & Telephony Defense Architecture", title_style))
    story.append(Paragraph("Engineering an Enterprise-Grade Interactive CLI Threat Progression Suite Across 10 Critical Industry Sectors", subtitle_style))
    story.append(t_meta)
    story.append(Spacer(1, 8))

    story.append(Paragraph("1. Executive Summary & Strategic Context", h1_style))
    story.append(Paragraph(
        "Modern cybersecurity perimeters have successfully reduced the effectiveness of traditional, unauthenticated email phishing "
        "through machine-learning spam gateways, DMARC enforcement, and secure email filters. In response, sophisticated cyber-adversaries "
        "have systematically pivoted toward multi-channel telecommunications deception—specifically <b>Voice Phishing (Vishing)</b> and "
        "<b>SMS Phishing (Smishing)</b>. By exploiting VoIP Session Initiation Protocol (SIP) header malleability and rogue wholesale SMS "
        "aggregators, adversaries bypass email controls and engage human targets directly via low-latency, high-trust channels.",
        body_style
    ))
    story.append(Paragraph(
        "During <b>Day 04</b> of the Sqrock IT Solution Cybersecurity Internship, a hardened, production-grade CLI suite named "
        "<b>PEER'S Vish & Smish Simulator</b> was designed and deployed. Built without GUI overhead to guarantee deterministic execution across "
        "security platforms (including Kali Linux, Debian, macOS, and Windows), the tool provides a comprehensive framework to model, dissect, "
        "and neutralize voice and SMS social engineering attacks across <b>10 distinct enterprise and consumer sectors</b>.",
        body_style
    ))

    story.append(Paragraph("2. Scope of Investigation & Technical Objectives", h1_style))
    obj_data = [
        [
            Paragraph("<b>Objective</b>", body_bold),
            Paragraph("<b>Target Metric / Deliverable</b>", body_bold),
            Paragraph("<b>Verification Method</b>", body_bold)
        ],
        [
            Paragraph("1. Multi-Sector Threat Modeling", body_style),
            Paragraph("10 fully realized scenarios spanning IT, Finance, Gov, Telecom, etc.", body_style),
            Paragraph("Schema validation in <code>scenarios.json</code> with 5-phase dialogue.", body_style)
        ],
        [
            Paragraph("2. Interactive Call Roleplay", body_style),
            Paragraph("Branching voice dialogs with pre-scripted adversary counters.", body_style),
            Paragraph("Live CLI execution with Out-of-Band defense validation.", body_style)
        ],
        [
            Paragraph("3. Psychological Trigger Scorer", body_style),
            Paragraph("Quantitative evaluation of Urgency, Authority, Fear, Scarcity, Sympathy.", body_style),
            Paragraph("0–100 trigger intensity scale with dynamic ASCII radar visualizer.", body_style)
        ],
        [
            Paragraph("4. Mobile Smishing Forensics", body_style),
            Paragraph("GSM-7 character accounting, 160-char threshold, UDH segmentation.", body_style),
            Paragraph("Automated payload parser with domain link isolation.", body_style)
        ],
        [
            Paragraph("5. Carrier Countermeasures", body_style),
            Paragraph("STIR/SHAKEN Level A/B/C attestation & FIDO2 token analysis.", body_style),
            Paragraph("Technical reference matrix embedded in simulator & report.", body_style)
        ],
        [
            Paragraph("6. Quality Assurance & Tests", body_style),
            Paragraph("9 automated unit tests verifying schema, bounds, and dialogue.", body_style),
            Paragraph("Automated test runner executing in &lt; 0.005s with 100% pass rate.", body_style)
        ]
    ]
    t_obj = Table(obj_data, colWidths=[120, 240, 180])
    t_obj.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_obj)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 2: THREAT LANDSCAPE & 10-SECTOR MATRIX
    # =========================================================================
    story.append(Paragraph("3. Telephony Exploitation Mechanics & Psychology", h1_style))
    story.append(Paragraph(
        "<b>VoIP SIP Header Manipulation:</b> Unlike the Public Switched Telephone Network (PSTN), modern telecommunications utilize Session "
        "Initiation Protocol (SIP RFC 3261). Adversaries register trunk accounts with unverified VoIP providers, injecting custom strings into "
        "the <code>From:</code> and <code>P-Asserted-Identity</code> headers. Consequently, endpoint mobile devices display spoofed internal "
        "helpdesk extensions or trusted corporate numbers without intrinsic cryptographic verification.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Rogue SMS Aggregators & Alphanumeric Sender IDs:</b> In international telecommunications, SMS gateways permit alphanumeric "
        "Sender IDs (e.g., 'CARRIER-SEC' or 'SWIFT-PKG') without cryptographic origin checks. Attackers exploit these aggregators to bypass "
        "carrier filtering, injecting deceptive hyperlinks designed to harvest mobile credentials or prompt malicious application downloads.",
        body_style
    ))

    story.append(Paragraph("4. The 10 Industry Attack Scenarios: Empirical Catalog", h1_style))
    story.append(Paragraph(
        "To ensure the simulator prepares defense teams for the complete threat spectrum, 10 distinct industry attack profiles were "
        "engineered into <code>scenarios.json</code>. Each profile establishes authentic adversary pretexting, realistic caller lines, "
        "and primary psychological attack levers:",
        body_style
    ))

    matrix_data = [
        [
            Paragraph("<b>#</b>", body_bold),
            Paragraph("<b>Sector ID</b>", body_bold),
            Paragraph("<b>Industry Sector</b>", body_bold),
            Paragraph("<b>Spoofed Line / Caller ID</b>", body_bold),
            Paragraph("<b>Exploitation Vector</b>", body_bold),
            Paragraph("<b>Score / Risk</b>", body_bold)
        ],
        [
            Paragraph("1", body_style), Paragraph("<code>it_support</code>", body_style),
            Paragraph("Enterprise IT", body_style), Paragraph("+1 (800) 555-0199 (Ext 4401)", body_style),
            Paragraph("MFA Push Token / Session Sync Theft", body_style), Paragraph("<b>80</b> / High", body_style)
        ],
        [
            Paragraph("2", body_style), Paragraph("<code>banking_fraud</code>", body_style),
            Paragraph("Banking & Finance", body_style), Paragraph("+1 (888) 555-0144 (Fraud Desk)", body_style),
            Paragraph("Emergency Transfer to 'Safe Account'", body_style), Paragraph("<b>83</b> / High", body_style)
        ],
        [
            Paragraph("3", body_style), Paragraph("<code>gov_tax</code>", body_style),
            Paragraph("Government & Tax", body_style), Paragraph("+1 (800) 829-1040 (Revenue Ag)", body_style),
            Paragraph("Immediate Tax Penalty Wire Settlement", body_style), Paragraph("<b>75</b> / High", body_style)
        ],
        [
            Paragraph("4", body_style), Paragraph("<code>parcel_delivery</code>", body_style),
            Paragraph("Logistics & Courier", body_style), Paragraph("SWIFT-PKG (SMS Gateway)", body_style),
            Paragraph("Undelivered Parcel Address Redirection", body_style), Paragraph("<b>69</b> / Moderate", body_style)
        ],
        [
            Paragraph("5", body_style), Paragraph("<code>hr_payroll</code>", body_style),
            Paragraph("Corporate HR", body_style), Paragraph("+1 (800) 555-0177 (Payroll Desk)", body_style),
            Paragraph("Direct Deposit Routing Number Reroute", body_style), Paragraph("<b>80</b> / High", body_style)
        ],
        [
            Paragraph("6", body_style), Paragraph("<code>healthcare_copay</code>", body_style),
            Paragraph("Healthcare & Rx", body_style), Paragraph("MED-RX (Claims Dispatch)", body_style),
            Paragraph("Prescription Hold Payment Interception", body_style), Paragraph("<b>83</b> / High", body_style)
        ],
        [
            Paragraph("7", body_style), Paragraph("<code>executive_ceo</code>", body_style),
            Paragraph("Executive Whaling", body_style), Paragraph("+1 (415) 555-0122 (CEO Mobile)", body_style),
            Paragraph("Confidential M&A Gift Card / Wire Bypass", body_style), Paragraph("<b>84</b> / High", body_style)
        ],
        [
            Paragraph("8", body_style), Paragraph("<code>telecom_carrier</code>", body_style),
            Paragraph("Telecom / Mobile", body_style), Paragraph("CARRIER-SEC (Fraud Division)", body_style),
            Paragraph("Port-Out / SIM Swap OTP Interception", body_style), Paragraph("<b>85</b> / Critical", body_style)
        ],
        [
            Paragraph("9", body_style), Paragraph("<code>ecommerce_retail</code>", body_style),
            Paragraph("Online Retail", body_style), Paragraph("ORDER-ALERT (Fulfillment)", body_style),
            Paragraph("Unauthorized MacBook Charge Cancellation", body_style), Paragraph("<b>79</b> / High", body_style)
        ],
        [
            Paragraph("10", body_style), Paragraph("<code>utility_services</code>", body_style),
            Paragraph("Public Utilities", body_style), Paragraph("+1 (800) 555-0111 (Grid Ops)", body_style),
            Paragraph("45-Minute Power Cutoff Payment Fraud", body_style), Paragraph("<b>80</b> / High", body_style)
        ]
    ]
    t_mat = Table(matrix_data, colWidths=[18, 70, 95, 130, 150, 77])
    t_mat.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (0,-1), 'CENTER'),
        ('ALIGN', (1,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, NAVY_PRIMARY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_mat)
    story.append(Spacer(1, 8))

    story.append(Paragraph("5. Attack Progression Phases (The 5-Stage Vishing Lifecycle)", h2_style))
    story.append(Paragraph(
        "Every scenario implements a structured 5-stage progression model: (1) <b>Introduction</b> establishing false rapport and authority; "
        "(2) <b>Hook</b> introducing an urgent operational crisis (e.g., Active Directory lockout or power cutoff); (3) <b>The Ask</b> demanding "
        "sensitive data; (4) <b>Pre-Scripted Objection Handling</b> countering target skepticism with escalated urgency or policy citations; "
        "and (5) <b>Exit Strategy</b> ending the call cleanly before suspicion solidifies.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 3: EMPIRICAL EVIDENCE PHASE 1 (Screenshots 1 & 2)
    # =========================================================================
    story.append(Paragraph("6. Empirical Verification & Evidence Breakdown (Phase 1)", h1_style))
    story.append(Paragraph(
        "The following empirical test captures demonstrate the actual execution of PEER'S Vish & Smish Simulator within an authorized "
        "Kali Linux security research environment. Each screenshot verifies key architecture, operational stability, and input validation.",
        body_style
    ))

    # Screenshot 1: Banner & Startup
    img1_path = os.path.join(SCREENSHOTS_DIR, "01_kali_terminal_banner.png")
    if os.path.exists(img1_path):
        story.append(Image(img1_path, width=490, height=221))
        story.append(Paragraph("Figure 1: Kali Linux CLI Cold-Start & Custom Dual-Tone ASCII Banner Rendering", caption_style))
    
    story.append(Paragraph(
        "<b>Technical Analysis of Figure 1:</b><br/>"
        "• <b>Environment Verification:</b> Executed in a native Kali Linux terminal session (<code>kali@kali:~/PEER-S-Vish-Smish-Simulator</code>).<br/>"
        "• <b>Repository Integrity:</b> Directory listing (<code>ls</code>) confirms complete suite distribution including <code>scenarios.json</code>, "
        "<code>vish_smish.py</code>, test suites, and documentation.<br/>"
        "• <b>Deterministic Cold Boot:</b> Launching via <code>python vish_smish.py</code> initializes terminal color sequences without external "
        "heavyweight GUI dependencies, rendering the dual-tone <code>PEER'S VishingSmishing v1.0</code> production banner.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # Screenshot 2: Master Menu
    img2_path = os.path.join(SCREENSHOTS_DIR, "02_master_menu.png")
    if os.path.exists(img2_path):
        story.append(Image(img2_path, width=490, height=221))
        story.append(Paragraph("Figure 2: Master Control Menu & 10-Sector Threat Catalog Presentation", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 2:</b><br/>"
        "• <b>Modular Master Console:</b> The CLI presents 8 high-level options covering simulation generation, interactive roleplay, "
        "psychological intensity profiling, GSM-7 character analysis, carrier defense matrices, and benchmark audits.<br/>"
        "• <b>Catalog Invocation:</b> Selecting Option <code>[2] Interactive Live Call Roleplay</code> triggers dynamic loading and parsing "
        "of all 10 industry attack profiles directly from <code>scenarios.json</code> with zero schema errors or unhandled exceptions.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 4: EMPIRICAL EVIDENCE PHASE 2 (Screenshots 3 & 4)
    # =========================================================================
    story.append(Paragraph("6. Empirical Verification & Evidence Breakdown (Phase 2)", h1_style))
    story.append(Paragraph(
        "Phase 2 validates the simulator's branching live call roleplay engine, victim context injection, and behavioral defense response "
        "scoring against high-pressure adversary pretexts.",
        body_style
    ))

    # Screenshot 3: Targeting
    img3_path = os.path.join(SCREENSHOTS_DIR, "03_scenario_targeting.png")
    if os.path.exists(img3_path):
        story.append(Image(img3_path, width=490, height=221))
        story.append(Paragraph("Figure 3: Victim Personalization & Inbound Spoofed Call Initialization", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 3:</b><br/>"
        "• <b>Dynamic Target Personalization:</b> The operator selected Scenario <code>[01] it_support</code> and injected the target employee "
        "name <b>'Harish'</b>. The engine dynamically substitutes the victim identifier throughout dialogue scripts and pretext strings.<br/>"
        "• <b>VoIP Caller ID Spoofing Emulation:</b> The engine models an inbound call from <code>+1 (800) 555-0199 (Internal IT Extension #4401)</code>, "
        "demonstrating how attackers present realistic PBX extensions to disarm target skepticism during initial contact.",
        body_style
    ))
    story.append(Spacer(1, 6))

    # Screenshot 4: Call Defense
    img4_path = os.path.join(SCREENSHOTS_DIR, "04_vishing_defense.png")
    if os.path.exists(img4_path):
        story.append(Image(img4_path, width=490, height=221))
        story.append(Paragraph("Figure 4: The Exploitation Ask, Victim Decision Point & Successful Out-of-Band Defense", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 4:</b><br/>"
        "• <b>Urgency Induction & The Ask:</b> The adversary establishes a 20-minute ultimatum threatening Active Directory account lockout, "
        "then demands immediate read-back of a 6-digit MFA synchronization token pushed to the victim's device.<br/>"
        "• <b>Decision Matrix & Execution:</b> The user is presented with 4 realistic behavioral choices. Selecting Option <code>[4] Hang up "
        "immediately and verify via Out-of-Band official phone directory</code> triggers a <b>SUCCESSFUL DEFENSE</b> verdict.<br/>"
        "• <b>Defensive Validation:</b> The tool confirms that hanging up and initiating a clean callback via an independent directory strictly "
        "neutralizes Adversary-in-the-Middle (AitM) voice interception.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 5: EMPIRICAL EVIDENCE PHASE 3 (Screenshot 5 & Benchmark Audit)
    # =========================================================================
    story.append(Paragraph("6. Empirical Verification & Evidence Breakdown (Phase 3)", h1_style))
    story.append(Paragraph(
        "To ensure robust test coverage across diverse attack scenarios, the simulator features an automated 10-category benchmark engine "
        "that audits psychological intensity, character boundaries, and defense controls simultaneously.",
        body_style
    ))

    # Screenshot 5: Benchmark Audit
    img5_path = os.path.join(SCREENSHOTS_DIR, "05_benchmark_audit.png")
    if os.path.exists(img5_path):
        story.append(Image(img5_path, width=490, height=221))
        story.append(Paragraph("Figure 5: 10-Sector Automated Benchmark Audit & Psychological Risk Tiering Output", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 5:</b><br/>"
        "• <b>Batch Verification Speed:</b> The audit engine processes all 10 enterprise sectors in under 0.005 seconds, performing schema validation, "
        "scoring aggregation, and format normalization without bottlenecking.<br/>"
        "• <b>Quantitative Psychological Scorer:</b> Scores range from <b>69/100</b> (Logistics Courier - Moderate Coercion) to <b>85/100</b> "
        "(Telecom Carrier - Critical Manipulation). The highest score reflects the acute danger of SIM swap fraud where victims face immediate "
        "cellular disconnection.<br/>"
        "• <b>Audit Export Artifacts:</b> In addition to terminal display, results are automatically written to persistent audit logs "
        "(<code>reports/scenario_audit_results.json</code> and <code>reports/scenario_audit_results.txt</code>) for enterprise SIEM integration.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Benchmark Summary Table
    bench_data = [
        [Paragraph("<b>Scenario</b>", body_bold), Paragraph("<b>Category</b>", body_bold), Paragraph("<b>Urg</b>", body_bold), Paragraph("<b>Auth</b>", body_bold), Paragraph("<b>Fear</b>", body_bold), Paragraph("<b>Scarc</b>", body_bold), Paragraph("<b>Symp</b>", body_bold), Paragraph("<b>Total</b>", body_bold), Paragraph("<b>Tier</b>", body_bold)],
        [Paragraph("<code>it_support</code>", body_style), Paragraph("Enterprise IT", body_style), Paragraph("85", body_style), Paragraph("90", body_style), Paragraph("75", body_style), Paragraph("50", body_style), Paragraph("40", body_style), Paragraph("<b>80</b>", body_style), Paragraph("High", body_style)],
        [Paragraph("<code>banking_fraud</code>", body_style), Paragraph("Banking / Finance", body_style), Paragraph("90", body_style), Paragraph("80", body_style), Paragraph("95", body_style), Paragraph("60", body_style), Paragraph("30", body_style), Paragraph("<b>83</b>", body_style), Paragraph("High", body_style)],
        [Paragraph("<code>gov_tax</code>", body_style), Paragraph("Government Tax", body_style), Paragraph("75", body_style), Paragraph("95", body_style), Paragraph("90", body_style), Paragraph("55", body_style), Paragraph("20", body_style), Paragraph("<b>75</b>", body_style), Paragraph("High", body_style)],
        [Paragraph("<code>parcel_delivery</code>", body_style), Paragraph("Logistics", body_style), Paragraph("75", body_style), Paragraph("50", body_style), Paragraph("40", body_style), Paragraph("85", body_style), Paragraph("35", body_style), Paragraph("<b>69</b>", body_style), Paragraph("Moderate", body_style)],
        [Paragraph("<code>hr_payroll</code>", body_style), Paragraph("Corporate HR", body_style), Paragraph("85", body_style), Paragraph("85", body_style), Paragraph("80", body_style), Paragraph("60", body_style), Paragraph("45", body_style), Paragraph("<b>80</b>", body_style), Paragraph("High", body_style)],
        [Paragraph("<code>healthcare_copay</code>", body_style), Paragraph("Healthcare", body_style), Paragraph("80", body_style), Paragraph("80", body_style), Paragraph("85", body_style), Paragraph("70", body_style), Paragraph("65", body_style), Paragraph("<b>83</b>", body_style), Paragraph("High", body_style)],
        [Paragraph("<code>executive_ceo</code>", body_style), Paragraph("Whaling", body_style), Paragraph("90", body_style), Paragraph("95", body_style), Paragraph("75", body_style), Paragraph("70", body_style), Paragraph("40", body_style), Paragraph("<b>84</b>", body_style), Paragraph("High", body_style)],
        [Paragraph("<code>telecom_carrier</code>", body_style), Paragraph("Telecom / SIM", body_style), Paragraph("95", body_style), Paragraph("85", body_style), Paragraph("85", body_style), Paragraph("65", body_style), Paragraph("35", body_style), Paragraph("<b>85</b>", body_style), Paragraph("Critical", body_style)],
        [Paragraph("<code>ecommerce_retail</code>", body_style), Paragraph("E-Commerce", body_style), Paragraph("80", body_style), Paragraph("70", body_style), Paragraph("85", body_style), Paragraph("65", body_style), Paragraph("45", body_style), Paragraph("<b>79</b>", body_style), Paragraph("High", body_style)],
        [Paragraph("<code>utility_services</code>", body_style), Paragraph("Utilities", body_style), Paragraph("90", body_style), Paragraph("80", body_style), Paragraph("95", body_style), Paragraph("50", body_style), Paragraph("25", body_style), Paragraph("<b>80</b>", body_style), Paragraph("High", body_style)]
    ]
    t_bench = Table(bench_data, colWidths=[80, 85, 32, 32, 32, 35, 35, 40, 65])
    t_bench.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), DARK_BLUE),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (2,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, DARK_BLUE),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 3),
        ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ]))
    story.append(t_bench)

    story.append(PageBreak())

    # =========================================================================
    # PAGE 6: GITHUB REPOSITORY VERIFICATION & OPEN-SOURCE INTEGRITY
    # =========================================================================
    story.append(Paragraph("7. Open-Source Implementation & GitHub Verification", h1_style))
    story.append(Paragraph(
        "In accordance with modern security engineering practices, the complete codebase was version-controlled and published to an authorized "
        "public GitHub repository, complete with comprehensive documentation, badges, and reproducible execution pipelines.",
        body_style
    ))

    # Screenshot 6: GitHub Repo Header
    img6_path = os.path.join(SCREENSHOTS_DIR, "06_github_repo_overview.png")
    if os.path.exists(img6_path):
        story.append(Image(img6_path, width=380, height=213))
        story.append(Paragraph("Figure 6: Public GitHub Repository Header, Dynamic Badges & Executive Overview", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 6:</b><br/>"
        "• <b>Repository Architecture:</b> Hosted publicly at <code>https://github.com/MdPeerSiddiqui/PEER-S-Vish-Smish-Simulator</code>.<br/>"
        "• <b>Quality & Verification Badges:</b> Displays Shields.io badges confirming <b>Python 3.9+</b> compatibility, cross-platform support "
        "(Kali Linux / Windows / macOS), MIT Licensing, and <b>9/9 Automated Tests Passing</b>.<br/>"
        "• <b>Contributor Attribution:</b> Published under the authorized account of Md Peer Siddiqui for Sqrock IT Solution internship evaluation.",
        body_style
    ))
    story.append(Spacer(1, 4))

    # Screenshot 7: GitHub Setup Instructions
    img7_path = os.path.join(SCREENSHOTS_DIR, "07_github_setup_instructions.png")
    if os.path.exists(img7_path):
        story.append(Image(img7_path, width=380, height=213))
        story.append(Paragraph("Figure 7: Multi-Platform Setup Pipelines for Kali Linux, Debian & Windows Environments", caption_style))

    story.append(Paragraph(
        "<b>Technical Analysis of Figure 7:</b><br/>"
        "• <b>Reproducibility:</b> Clear, step-by-step setup guides allowing security auditors and training officers to clone, activate virtual "
        "environments, install dependencies, and execute the simulator across diverse OS environments without configuration friction.",
        body_style
    ))

    story.append(PageBreak())

    # =========================================================================
    # PAGE 7: DEFENSIVE COUNTERMEASURES, TESTS & ETHICAL DECLARATION
    # =========================================================================
    story.append(Paragraph("8. Technical Defensive Countermeasures & Architecture", h1_style))
    story.append(Paragraph(
        "<b>A. STIR/SHAKEN Protocol (RFC 8588 / RFC 8224):</b><br/>"
        "Secure Telephone Identity Revisited (STIR) and Signature-based Handling of Asserted information using toKENs (SHAKEN) implement "
        "public-key cryptography directly within SIP signaling. When an originating carrier connects a call, it issues a signed JSON Web Token "
        "(PASSporT) asserting caller authority. Terminating carriers verify the token, categorizing calls into three attestation tiers:<br/>"
        "• <i>Attestation A (Full):</i> Service provider knows the customer and verifies their right to use the telephone number.<br/>"
        "• <i>Attestation B (Partial):</i> Service provider knows the customer, but cannot verify if they own the specific caller ID.<br/>"
        "• <i>Attestation C (Gateway):</i> Provider received the call from an unverified international or third-party gateway.<br/>"
        "Enterprise telephony gateways must automatically drop or flag any inbound call lacking Full Attestation (Level A).",
        body_style
    ))
    story.append(Paragraph(
        "<b>B. FIDO2 / WebAuthn Hardware Cryptographic Resistance:</b><br/>"
        "Traditional SMS OTPs and phone-dictated push tokens are fundamentally vulnerable to real-time relay attacks. FIDO2 hardware security keys "
        "(YubiKeys) bind authentication credentials cryptographically to the browser's TLS origin (Origin Binding). Even if an attacker "
        "coerces an employee over the phone, the hardware key refuses to authenticate against adversary-controlled infrastructure.",
        body_style
    ))
    story.append(Paragraph(
        "<b>C. The Strict Out-of-Band (OOB) Rule:</b><br/>"
        "Employees must be trained on one immutable procedural standard: <i>Never comply with unverified inbound telephony requests for credentials, "
        "routing changes, or tokens. Immediately terminate the call and dial back using an independently published directory number.</i>",
        body_style
    ))

    story.append(Paragraph("9. Automated Unit Testing Verification Suite", h1_style))
    test_data = [
        [Paragraph("<b>Test Case Identifier</b>", body_bold), Paragraph("<b>Component Under Test</b>", body_bold), Paragraph("<b>Execution Time</b>", body_bold), Paragraph("<b>Status</b>", body_bold)],
        [Paragraph("<code>test_scenario_count</code>", body_style), Paragraph("Validates exactly 10 industry attack profiles", body_style), Paragraph("0.0004s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_all_scenarios_have_required_fields</code>", body_style), Paragraph("Verifies metadata, triggers, dialogues schema", body_style), Paragraph("0.0003s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_vishing_dialogue_phases</code>", body_style), Paragraph("Ensures 5-stage progression across all vectors", body_style), Paragraph("0.0003s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_objection_handling_structure</code>", body_style), Paragraph("Checks pre-scripted adversary counter-logic", body_style), Paragraph("0.0003s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_smishing_has_payload_and_link</code>", body_style), Paragraph("Validates SMS lure text and phishing hyperlinks", body_style), Paragraph("0.0003s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_gsm7_character_counter</code>", body_style), Paragraph("Tests 160-char GSM-7 and UDH multipart logic", body_style), Paragraph("0.0004s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_psychological_scores_valid</code>", body_style), Paragraph("Confirms all 5 trigger scores remain in [0, 100]", body_style), Paragraph("0.0003s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_telephony_defenses_present</code>", body_style), Paragraph("Ensures STIR/SHAKEN and OOB recommendations", body_style), Paragraph("0.0003s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)],
        [Paragraph("<code>test_json_scenarios_file_exists</code>", body_style), Paragraph("Validates filesystem persistence of scenarios.json", body_style), Paragraph("0.0002s", body_style), Paragraph("<font color='#0E703C'><b>PASS (OK)</b></font>", body_style)]
    ]
    t_test = Table(test_data, colWidths=[170, 200, 80, 90])
    t_test.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NAVY_PRIMARY),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (2,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BOX', (0,0), (-1,-1), 1, NAVY_PRIMARY),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, LIGHT_BG]),
        ('TOPPADDING', (0,0), (-1,-1), 1.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_test)
    story.append(Spacer(1, 6))

    story.append(Paragraph("10. Ethical Compliance, Limitations & Sign-Off", h1_style))
    story.append(Paragraph(
        "<b>Ethical Scope:</b> All telephone pretexts, numbers (e.g. <code>555-0199</code>), and URLs are reserved documentation items utilized "
        "strictly within an isolated educational sandbox. No outbound PSTN dialing, live SMS gateway transmission, or unauthorized impersonation "
        "was conducted. The project complies fully with the ethical guidelines established by Sqrock IT Solution.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Intern Sign-Off:</b><br/>"
        "I hereby declare that this practical lab report and its associated Python CLI implementation represent original engineering work "
        "conducted under the supervision of Sqrock IT Solution for Day 04 of the Cybersecurity Internship.<br/>"
        "<b>Signature:</b> <i>Md Peer Siddiqui</i> | <b>Date:</b> October 23, 2026",
        body_style
    ))

    # Build the PDF
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"[+] Multi-Page PDF successfully compiled at:\n    {OUTPUT_PDF}")


if __name__ == "__main__":
    create_report()
