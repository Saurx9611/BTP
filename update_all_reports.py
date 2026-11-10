import os
import base64
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from playwright.sync_api import sync_playwright
import zipfile
import shutil

print("Step 1: Reading logo as base64...")
with open("Figures and Diagrams/iitkgp_logo.png", "rb") as f:
    b64_logo = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

# Read existing report.html to get body content after title page
with open("Report/report.html", "r", encoding="utf-8") as f:
    current_html = f.read()

# Split at CERTIFICATE
cert_marker = '<h1 class="chapter-title">Certificate of Approval</h1>'
idx = current_html.find(cert_marker)
if idx == -1:
    raise ValueError("Certificate marker not found in report.html")

body_after_title = current_html[idx:]

# Build new HTML with exact front page
new_html_header = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Soft Robotic Grippers using Tactile Sensor - BTP Report</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body);"></script>
<style>
    @page {{
        size: A4;
        margin: 18mm 18mm 20mm 18mm;
        @bottom-right {{
            content: counter(page);
            font-family: 'Times New Roman', serif;
            font-size: 10pt;
        }}
    }}
    @page :first {{
        margin: 0;
        @bottom-right {{
            content: none;
        }}
    }}
    body {{
        font-family: 'Times New Roman', Times, serif;
        font-size: 11.5pt;
        line-height: 1.5;
        color: #111;
        text-align: justify;
        margin: 0;
        padding: 0;
    }}
    
    /* COVER PAGE FULL BLEED CONTAINER */
    .cover-page {{
        width: 210mm;
        height: 297mm;
        box-sizing: border-box;
        padding: 13mm 15mm 13mm 15mm;
        page-break-after: always;
        display: flex;
        flex-direction: column;
        background: #ffffff;
    }}
    
    /* RECTANGULAR BORDER BOX MATCHING USER IMAGE EXACTLY */
    .cover-border-box {{
        width: 100%;
        height: 100%;
        box-sizing: border-box;
        border: 2px solid #000000;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        text-align: center;
        padding: 38px 24px 30px 24px;
    }}
    
    .front-title {{
        font-size: 20pt;
        font-weight: bold;
        color: #000000;
        margin-top: 10px;
        margin-bottom: 0px;
        line-height: 1.25;
        font-family: 'Times New Roman', serif;
    }}
    
    .front-submitted {{
        font-size: 13.5pt;
        color: #000000;
        line-height: 1.45;
        margin: 0;
    }}
    .front-submitted .iit-name {{
        font-size: 15pt;
        font-weight: bold;
        display: block;
        margin: 3px 0;
    }}
    
    .front-spec {{
        font-size: 13.5pt;
        font-style: italic;
        color: #000000;
        line-height: 1.45;
        margin: 0;
    }}
    
    .front-authors {{
        font-size: 13.5pt;
        font-weight: bold;
        color: #000000;
        line-height: 1.5;
        margin: 0;
    }}
    
    .front-supervision {{
        font-size: 13.5pt;
        color: #000000;
        line-height: 1.4;
        margin: 0;
    }}
    .front-supervision .prof-name {{
        font-size: 15pt;
        font-weight: bold;
        display: block;
        margin-top: 3px;
    }}
    
    .front-logo-box {{
        margin: 5px 0;
    }}
    .front-logo-box img {{
        width: 165px;
        height: auto;
        display: block;
        margin: 0 auto;
    }}
    
    .front-bottom {{
        font-size: 14pt;
        font-weight: bold;
        color: #000000;
        line-height: 1.4;
        margin-bottom: 5px;
    }}

    .page-break {{
        page-break-after: always;
    }}
    h1.chapter-title {{
        font-family: 'Arial', sans-serif;
        font-size: 17pt;
        color: #003366;
        border-bottom: 2px solid #003366;
        padding-bottom: 6px;
        margin-top: 30px;
        margin-bottom: 18px;
    }}
    h2.section-title {{
        font-family: 'Arial', sans-serif;
        font-size: 13.5pt;
        color: #114477;
        margin-top: 22px;
        margin-bottom: 10px;
    }}
    h3.subsection-title {{
        font-family: 'Arial', sans-serif;
        font-size: 12pt;
        color: #222;
        margin-top: 16px;
        margin-bottom: 8px;
    }}
    p {{
        margin-top: 0;
        margin-bottom: 10px;
    }}
    table {{
        width: 100%;
        border-collapse: collapse;
        margin: 16px 0;
        font-size: 10pt;
    }}
    th, td {{
        border: 1px solid #ccc;
        padding: 7px 10px;
        text-align: left;
    }}
    th {{
        background-color: #f0f4f8;
        color: #003366;
        font-weight: bold;
    }}
    tr:nth-child(even) {{
        background-color: #fafbfc;
    }}
    .table-caption, .figure-caption {{
        text-align: center;
        font-size: 10pt;
        font-style: italic;
        color: #444;
        margin-top: 6px;
        margin-bottom: 16px;
    }}
    .figure-container {{
        text-align: center;
        margin: 20px 0;
    }}
    .figure-container img {{
        max-width: 90%;
        height: auto;
        border: 1px solid #e0e0e0;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}
    .callout {{
        background-color: #f8f9fa;
        border-left: 4px solid #003366;
        padding: 12px 16px;
        margin: 16px 0;
        font-size: 11pt;
    }}
    .formula {{
        text-align: center;
        margin: 14px 0;
        font-size: 11.5pt;
    }}
    .ref-item {{
        padding-left: 28px;
        text-indent: -28px;
        margin-bottom: 8px;
        font-size: 10.5pt;
    }}
</style>
</head>
<body>

<!-- FRONT / TITLE PAGE -->
<div class="cover-page">
  <div class="cover-border-box">
    <div class="front-title">
        Soft Robotic Grippers using Tactile Sensor
    </div>
    
    <div class="front-submitted">
        Report submitted to<br>
        <span class="iit-name">Indian Institute of Technology, Kharagpur</span>
        For the fulfillment of BTP-I in
    </div>
    
    <div class="front-spec">
        Mechanical Engineering with specialisation in<br>
        Manufacturing Science and Engineering by
    </div>
    
    <div class="front-authors">
        G. Chandana (23ME31008)<br>
        Shinde Sanchali Sanjay (23ME31029)<br>
        Saurav Shekhar (23ME31043)
    </div>
    
    <div class="front-supervision">
        Under the<br>
        Supervision of<br>
        <span class="prof-name">Prof. Sankha Deb</span>
    </div>
    
    <div class="front-logo-box">
        <img src="{b64_logo}" alt="IIT Kharagpur Emblem">
    </div>
    
    <div class="front-bottom">
        Department of Mechanical Engineering<br>
        Indian Institute of Technology, Kharagpur - 721302
    </div>
  </div>
</div>
"""

full_new_html = new_html_header + body_after_title

with open("Report/report.html", "w", encoding="utf-8") as f:
    f.write(full_new_html)
print("Updated Report/report.html with exact front page.")

# Compile Report PDF
print("Step 2: Compiling Report PDF via Playwright...")
html_abs = os.path.abspath("Report/report.html")
pdf_abs = os.path.abspath("Report/BTP_Report_Soft_Robotic_Gripper.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file:///" + html_abs.replace("\\", "/"))
    page.wait_for_timeout(3000)
    page.pdf(
        path=pdf_abs,
        format="A4",
        print_background=True
    )
    # Take screenshot of the exact cover border box
    elem = page.query_selector(".cover-border-box")
    elem.screenshot(path="Report/front_page_preview.png")
    browser.close()

print(f"Generated {pdf_abs} and Report/front_page_preview.png")

# Now update DOCX
print("Step 3: Updating DOCX...")
doc = docx.Document()
for section in doc.sections:
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(0.8)
    section.bottom_margin = Inches(0.8)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)

# Normal Style
normal_style = doc.styles['Normal']
normal_style.font.name = 'Times New Roman'
normal_style.font.size = Pt(12)
normal_style.paragraph_format.line_spacing = 1.3
normal_style.paragraph_format.space_after = Pt(4)

# Create Front Page Table with single outer border
table_front = doc.add_table(rows=1, cols=1)
table_front.alignment = WD_TABLE_ALIGNMENT.CENTER
cell = table_front.cell(0, 0)
cell.width = Inches(6.5)

# Set 1.5pt black border around cell
tcPr = cell._tc.get_or_add_tcPr()
tcBorders = parse_xml(
    f'<w:tcBorders {nsdecls("w")}>\n'
    f'  <w:top w:val="single" w:sz="12" w:space="0" w:color="000000"/>\n'
    f'  <w:left w:val="single" w:sz="12" w:space="0" w:color="000000"/>\n'
    f'  <w:bottom w:val="single" w:sz="12" w:space="0" w:color="000000"/>\n'
    f'  <w:right w:val="single" w:sz="12" w:space="0" w:color="000000"/>\n'
    f'</w:tcBorders>'
)
tcPr.append(tcBorders)

# Inside cell, add paragraphs matching the layout
p_t = cell.paragraphs[0]
p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_t.paragraph_format.space_before = Pt(16)
p_t.paragraph_format.space_after = Pt(36)
r = p_t.add_run("Soft Robotic Grippers using Tactile Sensor")
r.bold = True
r.font.size = Pt(20)

p_sub = cell.add_paragraph()
p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sub.paragraph_format.space_after = Pt(32)
r = p_sub.add_run("Report submitted to\n")
r.font.size = Pt(13)
r2 = p_sub.add_run("Indian Institute of Technology, Kharagpur\n")
r2.bold = True
r2.font.size = Pt(14)
r3 = p_sub.add_run("For the fulfillment of BTP-I in")
r3.font.size = Pt(13)

p_spec = cell.add_paragraph()
p_spec.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_spec.paragraph_format.space_after = Pt(32)
r = p_spec.add_run("Mechanical Engineering with specialisation in\nManufacturing Science and Engineering by")
r.italic = True
r.font.size = Pt(13)

p_auth = cell.add_paragraph()
p_auth.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_auth.paragraph_format.space_after = Pt(32)
r = p_auth.add_run("G. Chandana (23ME31008)\nShinde Sanchali Sanjay (23ME31029)\nSaurav Shekhar (23ME31043)")
r.bold = True
r.font.size = Pt(13.5)

p_sup = cell.add_paragraph()
p_sup.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_sup.paragraph_format.space_after = Pt(20)
r = p_sup.add_run("Under the\nSupervision of\n")
r.font.size = Pt(13)
r2 = p_sup.add_run("Prof. Sankha Deb")
r2.bold = True
r2.font.size = Pt(14.5)

p_logo = cell.add_paragraph()
p_logo.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_logo.paragraph_format.space_after = Pt(24)
p_logo.add_run().add_picture("Figures and Diagrams/iitkgp_logo.png", width=Inches(1.8))

p_bot = cell.add_paragraph()
p_bot.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_bot.paragraph_format.space_after = Pt(16)
r = p_bot.add_run("Department of Mechanical Engineering\nIndian Institute of Technology, Kharagpur - 721302")
r.bold = True
r.font.size = Pt(13.5)

doc.add_page_break()

# Now re-append the remaining content into the docx
# We can run the existing docx generator logic for the remainder
def add_header_p(text, level, space_before=14, space_after=6):
    p = doc.add_heading(text, level=level)
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.keep_with_next = True
    run = p.runs[0]
    run.font.name = 'Arial'
    if level == 1:
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(0x00, 0x33, 0x66)
    elif level == 2:
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0x11, 0x44, 0x77)
    elif level == 3:
        run.font.size = Pt(12.5)
        run.font.bold = True
        run.font.color.rgb = RGBColor(0x22, 0x22, 0x22)
    return p

def set_cell_bg(c, fill_hex):
    tcPr = c._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

# CERTIFICATE
add_header_p('Certificate of Approval', level=1, space_before=18)
cert_p = doc.add_paragraph()
cert_p.add_run('This is to certify that the project report entitled ')
r_ct = cert_p.add_run('"Soft Robotic Grippers using Tactile Sensor"')
r_ct.bold = True
cert_p.add_run(' submitted by ')
r_st = cert_p.add_run('G. Chandana (23ME31008), Shinde Sanchali Sanjay (23ME31029), and Saurav Shekhar (23ME31043)')
r_st.bold = True
cert_p.add_run(' to the Indian Institute of Technology Kharagpur, for the partial fulfillment of the requirements for the award of the degree of Bachelor of Technology in Mechanical Engineering (with specialization in Manufacturing Science and Engineering), is a bona fide record of the work carried out by them under my supervision and guidance.\n\nThe project is currently at the literature-review-completed stage, and the proposed methodology, numerical simulation framework, and experimental implementation roadmap have been thoroughly examined and approved for progression into Project Stage-II (BTP-II).')

sig_p = doc.add_paragraph()
sig_p.paragraph_format.space_before = Pt(48)
sig_p.add_run('Prof. Sankha Deb\nSupervisor\nDepartment of Mechanical Engineering\nIndian Institute of Technology, Kharagpur\n\nDate: November 2026\nPlace: IIT Kharagpur')

doc.add_page_break()

# ABSTRACT
add_header_p('Abstract', level=1, space_before=18)
abs_p = doc.add_paragraph()
abs_p.add_run('Traditional robotic manipulation systems rely on rigid articulated linkages that exhibit high positioning repeatability but lack intrinsic compliance, rendering them prone to crushing delicate, fragile, or irregularly contoured objects in automated agriculture, biomedical packaging, and explosive ordnance handling. Soft robotic end-effectors address this limitation through structural deformability, enabling passive geometric conformity and safe contact pressure distribution. However, conventional soft grippers suffer from severe engineering bottlenecks: low payload capacity, material hysteresis, complex tethered fluidic supplies, sensor-skin delamination, and an absence of localized feedback capable of detecting incipient slip without bulky optical apparati.\n\nThis report establishes the complete Stage-I research foundation and detailed Stage-II implementation roadmap for a ')
r_abm = abs_p.add_run('Monolithic 3D-Printed (FDM TPU) Tendon-Driven Compliant Soft Robotic Gripper with Embedded Tactile Sensing')
r_abm.bold = True
abs_p.add_run('. Synthesizing an extensive multi-author literature corpus, the research evaluates fluidic elastomer actuators (PneuNets), shape memory alloys (Nitinol), and cable-driven compliant architectures. To overcome mold-tooling delays and fluid leakage risks, a direct additive manufacturing route using Thermoplastic Polyurethane (TPU 95A) is formulated, integrating circular flexure living hinges that eliminate mechanical joint backlash while maximizing structural fatigue life.\n\nTo provide deterministic grasp autonomy, thin-film Force Sensitive Resistors (FSR402) are integrated flush into the phalange contact pads. An integrated mechatronic architecture centered on a dual-core ESP32 executing FreeRTOS is developed. The tactile signal pipeline decouples static normal contact force estimation (via an active second-order low-pass Butterworth filter at fc = 20 Hz) from dynamic incipient slip micro-vibrations (via a 256-point Fast Fourier Transform analyzing the 100 - 300 Hz spectral energy band). This enables closed-loop servomotor torque compensation in under 35 milliseconds. A non-linear finite element analysis (FEA) framework utilizing Mooney-Rivlin hyperelastic strain energy formulations is established to predict tip deflection and stress concentrations prior to physical fabrication. Finally, a structured 16-week semester roadmap is detailed, establishing quantitative benchmarks for pull-out retention force, payload-to-weight ratio, and an autonomous slip-prevention demonstration on physical hardware.')

kw_p = doc.add_paragraph()
kw_p.paragraph_format.space_before = Pt(12)
r_kw = kw_p.add_run('Keywords: ')
r_kw.bold = True
kw_p.add_run('Soft Robotics, Compliant Mechanisms, Additive Manufacturing, TPU 95A, Tactile Sensing, FSR402, Fast Fourier Transform, Incipient Slip Detection, FreeRTOS, Hyperelastic FEA.')

doc.add_page_break()

# CHAPTER 1
add_header_p('Chapter 1: Introduction', level=1)
add_header_p('1.1 Background of Soft Robotics and Compliant Manipulation', level=2)
p = doc.add_paragraph('Robotic manipulation systems have traditionally been engineered around rigid mechanical kinematic chains composed of metallic or hard polymeric links joined by discrete revolute, prismatic, or spherical hinges. Such systems achieve sub-millimeter positioning accuracy, high structural rigidity, and substantial load-bearing capacities when operating in structured industrial environments where target workpieces possess invariant dimensions, known orientations, and high mechanical stiffness.\n\nHowever, modern automation requirements are rapidly shifting toward unstructured and semi-structured domains, such as the selective harvesting of fragile agricultural produce (e.g., tomatoes, strawberries, peaches), handling delicate specimens in biomedical logistics, sorting irregular post-consumer recycling items, and conducting hazardous explosive ordnance disposal (EOD). In these settings, traditional rigid end-effectors exhibit intrinsic limitations: localized stress concentrations causing workpiece rupture, severe control complexity for sensorless grasping of unknown contours, and dynamic contact chatter leading to dropped objects.')

p = doc.add_paragraph('Soft robotics represents a paradigm shift in end-effector design by replacing rigid links and discrete mechanical pins with continuously deformable elastomeric bodies and monolithic compliant mechanisms. By embodying mechanical intelligence directly into the elasticity of the material, soft grippers passively adapt their morphological shape to envelop complex contours upon contact, distributing interaction forces over an expanded surface area.')

add_header_p('1.2 Motivation and Industrial Relevance', level=2)
p = doc.add_paragraph('The primary motivation for this project stems from the critical need for a low-cost, self-contained, lightweight, and sensorized soft robotic gripper capable of executing delicate manipulation while providing real-time feedback regarding contact force and grasp stability.\n\nTarget industrial and societal applications include automated agricultural fruit picking without tissue damage, biomedical transport of thin-walled glass vials and filled ampoules without shock, and explosive ordnance disposal where uncontrolled clamping forces could trigger catastrophic detonation.')

add_header_p('1.3 Research Issues and Technical Challenges', level=2)
p = doc.add_paragraph('While passive compliance provides adaptability, it introduces substantial engineering challenges that do not exist in rigid mechanisms:\n1. Non-linear Continuum Mechanics: Soft elastomeric structures undergo geometric and material non-linearities requiring hyperelastic constitutive formulations.\n2. Hysteresis and Viscoelastic Relaxation: Energy dissipation causes loading and unloading curves to diverge, reducing open-loop repeatability.\n3. Tethering Bottlenecks: Conventional pneumatic soft grippers demand heavy compressors, pumps, and valves, restricting mobile deployment.\n4. Sensory Blindness: Without embedded tactile sensing, the controller cannot ascertain grasp stability or detect slip transitions.\n5. Interfacial Delamination: Embedding planar sensors onto stretching elastomeric skins induces severe peeling shear stresses.')

add_header_p('1.4 Broad Objectives', level=2)
p = doc.add_paragraph('To overcome these interconnected challenges, this research develops a monolithic 3D-printed compliant finger architecture fabricated from Thermoplastic Polyurethane (TPU 95A), driven by remote base-mounted servomotors via high-strength Dyneema tendons, equipped with embedded FSR402 tactile sensors, and governed by a dual-core ESP32 running FreeRTOS and micro-ROS for autonomous slip detection.')

# CHAPTER 2
add_header_p('Chapter 2: Literature Review', level=1)
add_header_p('2.1 Synthesis of Available Literature Work', level=2)
p = doc.add_paragraph('The literature review conducted by the team synthesizes three distinct thematic investigations:\n• Actuation Schemes and Compliant Mechanisms (Saurav Shekhar): Evaluated pneumatic, tendon-driven, SMA, and DEA architectures, emphasizing the trade-off between structural compliance and load capacity.\n• Materials Science and Additive Manufacturing (G. Chandana): Analyzed silicones (Ecoflex, PDMS), TPUs, and flexible photopolymers, concluding that direct FDM 3D printing of TPU filament eliminates mold-making delays and chemical curing hazards.\n• Tactile Transduction and Feedback Technologies (Shinde Sanchali Sanjay): Examined piezoresistive, capacitive, piezoelectric, and optical sensors, establishing FSR402 thin-film piezoresistors as optimal for grasping force detection.\n• Joint Framework (BTP-I Joint Report): Formulated the preliminary system uniting compliant structures, planned hyperelastic FEA modeling, FreeRTOS embedded processing, and FFT-based slip detection.')

add_header_p('2.2 Comparative Analysis of Existing Gripper Technologies', level=2)

table = doc.add_table(rows=5, cols=5)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ['Metric / Parameter', 'Pneumatic PneuNets', 'Tendon-Driven TPU (Selected)', 'Shape Memory Alloy (SMA)', 'Dielectric Elastomer (DEA)']
for i, h in enumerate(headers):
    c = table.cell(0, i)
    c.paragraphs[0].text = h
    c.paragraphs[0].runs[0].bold = True
    set_cell_bg(c, 'E0E8F0')

data = [
    ['Actuation Physics', 'Fluidic cavity pressure (ΔP)', 'Mechanical cable tension (T)', 'Joule-heated phase change', 'Maxwell electrostatic stress'],
    ['Primary Material', 'Silicone (Ecoflex, PDMS)', 'TPU 95A / 85A filament', 'Polymer + Nitinol wire', 'Silicone film + carbon grease'],
    ['Fabrication Route', 'Multi-part mold casting', 'Direct FDM 3D printing', 'Pre-straining & embedding', 'Multi-layer spin coating'],
    ['Payload-to-Weight', 'Moderate (1:1 - 2:1)', 'High (3:1 - 5:1)', 'Low-Moderate (0.5:1)', 'Low (<0.5:1)']
]
for row_idx, r_data in enumerate(data, start=1):
    for col_idx, val in enumerate(r_data):
        c = table.cell(row_idx, col_idx)
        c.paragraphs[0].text = val
        if col_idx == 0:
            c.paragraphs[0].runs[0].bold = True

p_cap = doc.add_paragraph()
p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap.add_run('Table 2.1: Multi-parameter comparison of candidate soft robotic gripper technologies.').italic = True

if os.path.exists('Figures and Diagrams/comparative_radar_chart.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture('Figures and Diagrams/comparative_radar_chart.png', width=Inches(4.8))
    p_img_cap = doc.add_paragraph()
    p_img_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img_cap.add_run('Figure 2.1: Multi-attribute radar comparison of candidate actuation technologies.').italic = True

add_header_p('2.3 Research Gaps and Limitations', level=2)
p = doc.add_paragraph('Five critical research gaps were identified in the literature:\n1. Compliance vs. Payload Capacity: Soft bladders buckle under lateral loads; rigid-compliant hybrid flexures bridge this gap.\n2. Sensor Delamination: Planar sensors bonded to stretching elastomeric skins peel under cyclic deformation.\n3. Lack of Compact Slip Perception: Existing slip-detecting grippers rely on heavy optical cameras (GelSight) unsuited for mobile arms.\n4. Material Viscoelastic Hysteresis: Open-loop controllers ignore TPU relaxation during sustained grasps.\n5. Edge Control Disconnect: Many prototypes lack deterministic onboard real-time operating systems integrated with ROS 2.')

# CHAPTER 3
add_header_p('Chapter 3: Objectives and Scope of Work', level=1)
add_header_p('3.1 Main Objective', level=2)
p = doc.add_paragraph('To design, model, fabricate, and experimentally validate an integrated Monolithic 3D-Printed Tendon-Driven Compliant Soft Robotic Gripper featuring embedded piezoresistive tactile sensing and real-time edge processing on an ESP32 microcontroller, culminating in an autonomous closed-loop demonstration of incipient slip detection and force compensation.')

add_header_p('3.2 Specific Sub-Objectives', level=2)
p = doc.add_paragraph('1. Synthesize parametric CAD models of compliant fingers with optimized circular living hinges and recessed sensor beds in SolidWorks.\n2. Perform non-linear hyperelastic FEA in Ansys Mechanical (Mooney-Rivlin / Yeoh) to predict bending deflections and verify safety factors.\n3. Optimize direct-drive FDM 3D printing of TPU 95A to ensure high inter-layer tensile strength.\n4. Design and fabricate an active analog signal conditioning circuit (2nd-order Butterworth low-pass filter, fc = 20 Hz).\n5. Implement an on-chip 256-point FFT algorithm on ESP32 Core 0 to detect micro-vibrations (100 - 300 Hz) indicative of incipient slip.\n6. Develop FreeRTOS dual-core firmware for closed-loop servo torque tightening in under 35 ms.\n7. Quantify static force calibration, pull-out retention force, and payload-to-weight ratio across a standardized test library.')

add_header_p('3.3 Scope and Limitations', level=2)
p = doc.add_paragraph('• In-Scope: CAD modeling, non-linear hyperelastic FEA, FDM 3D printing of TPU/PLA, FSR402 sensor integration, FreeRTOS firmware, and static/dynamic pull-out testing.\n• Out-of-Scope: High-speed industrial pick-and-place (>3 m/s), multi-axis shear force sensor arrays, underwater manipulation, and explosive field trials.')

# CHAPTER 4
add_header_p('Chapter 4: Proposed Methodology', level=1)
add_header_p('4.1 System Architecture', level=2)
p = doc.add_paragraph('The proposed system integrates mechanical compliance, tendon actuation, embedded tactile sensing, and dual-core edge processing into a cohesive mechatronic end-effector.')

if os.path.exists('Figures and Diagrams/mechatronics_architecture.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture('Figures and Diagrams/mechatronics_architecture.png', width=Inches(5.5))
    p_img_cap = doc.add_paragraph()
    p_img_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img_cap.add_run('Figure 4.1: Integrated mechatronic and FreeRTOS embedded architecture for the compliant gripper.').italic = True

add_header_p('4.2 Kinematic Modeling and Living Hinge Synthesis', level=2)
p = doc.add_paragraph('The finger is modeled as a monolithic beam with three localized circular flexure notches replicating human MCP, PIP, and DIP joints. According to Howell\'s Pseudo-Rigid-Body Model (PRBM), the equivalent torsional spring stiffness K_theta is expressed as:\n\nK_theta = (E * w * t^2.5) / (9 * pi * sqrt(r))\n\nwhere E is the instantaneous flexural modulus of TPU 95A, w is finger width, t is flexure throat thickness (1.6 mm), and r is notch radius (2.5 mm).')

if os.path.exists('Figures and Diagrams/gripper_kinematics_diagram.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture('Figures and Diagrams/gripper_kinematics_diagram.png', width=Inches(5.2))
    p_img_cap = doc.add_paragraph()
    p_img_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img_cap.add_run('Figure 4.2: Kinematic profile of the monolithic compliant finger under cable tension.').italic = True

add_header_p('4.2.1 Geometric Link Lengths and Kinematic Architecture', level=3)
p = doc.add_paragraph('The compliant finger architecture adopts an anthropomorphic 3-phalanx kinematic configuration. The monolithic flexible body is partitioned into three discrete functional phalanx segments interconnected by thin circular living hinge flexures:\n'
                      '• Proximal Phalanx (L1 = 35.0 mm): Anchored directly to the rigid palm base flange; initiates primary angular deflection during early tendon stroke.\n'
                      '• Intermediate Phalanx (L2 = 35.0 mm): Medial link segment that conforms around the lateral flanks of the grasped workpiece.\n'
                      '• Distal Phalanx (L3 = 35.0 mm): Fingertip segment incorporating an integrated 5.0 mm rounded tip and a precision circular recessed pocket (dia 18.3 mm, depth 0.6 mm) configured to seat the Interlink FSR402 thin-film tactile sensor flush with the grasping surface.\n\n'
                      'Accounting for the two notch opening gaps (g1 = g2 = 5.0 mm) and the distal fingertip extension, the total effective unbent beam length is L_total = 115.0 mm. The finger cross-section features a width of w = 20.0 mm and a height of h = 16.0 mm, providing high out-of-plane torsional rigidity against lateral twisting during asymmetric grasping while permitting compliant in-plane deflection. When assembled in a 3-finger radially symmetric array on an 80.0 mm pitch circle diameter (PCD) palm base, the fingers achieve a maximum tip curl angle of approx 82 degrees under a 12 - 15 mm tendon pull, providing an envelope grasp diameter of 25 - 85 mm.')

tab_links_data = [
    ['Parameter', 'Symbol', 'Value', 'Functional / Kinematic Rationale'],
    ['Proximal Phalanx Length', 'L1', '35.0 mm', 'Matches human proximal phalanx; provides primary envelope wrap.'],
    ['Intermediate Phalanx Length', 'L2', '35.0 mm', 'Replicates intermediate phalanx; guides medial curvature.'],
    ['Distal Phalanx Length', 'L3', '35.0 mm', 'Fingertip segment; houses recessed FSR402 contact pad (+5 mm tip).'],
    ['Total Finger Beam Length', 'L_total', '115.0 mm', 'Total effective finger length (L1 + g1 + L2 + g2 + L3 + tip).'],
    ['Finger Cross-Section Width', 'w', '20.0 mm', 'Ensures lateral torsional rigidity and stable planar bending.'],
    ['Finger Cross-Section Height', 'h', '16.0 mm', 'Accommodates internal 2 mm tendon conduit with 7 mm wall clearance.'],
    ['Flexure Throat Thickness', 't', '1.6 mm', 'Optimized for low bending resistance while maintaining structural integrity.'],
    ['Circular Notch Radius', 'r', '2.5 mm', 'Distributes bending stresses to minimize localized stress concentration.'],
    ['Notch Opening Gap', 'g', '5.0 mm', 'Provides clear angular clearance for up to 30 deg deflection per hinge.'],
    ['Tendon Moment Arm Offset', 'r_cable', '6.0 mm', 'Distance from flexure neutral axis to tendon channel centerline.'],
    ['Tendon Conduit Diameter', 'phi_c', '2.0 mm', 'Lined with low-friction micro-PTFE sleeve (OD 2.0 mm, ID 1.0 mm).'],
    ['Distal Sensor Recess', 'phi_s x d', 'phi 18.3 x 0.6 mm', 'Flush mounting bed for Interlink FSR402 active sensing area.'],
    ['Base Pitch Circle Diameter', 'phi_base', '80.0 mm', 'Symmetrical 3-finger equilateral radial mounting flange.'],
    ['Target Grasp Diameter', 'phi_grasp', '25.0 - 85.0 mm', 'Adaptive envelope grasping range for domestic and industrial items.'],
    ['Maximum Tip Curl Angle', 'theta_total', 'approx 82 deg', 'Cumulative angular deflection under 12 - 15 mm tendon stroke.']
]

table_links = doc.add_table(rows=len(tab_links_data), cols=4)
table_links.alignment = WD_TABLE_ALIGNMENT.CENTER
for c_i, h_val in enumerate(tab_links_data[0]):
    cell = table_links.cell(0, c_i)
    cell.paragraphs[0].text = h_val
    cell.paragraphs[0].runs[0].bold = True
    set_cell_bg(cell, 'E0E8F0')

for r_i, r_val in enumerate(tab_links_data[1:], start=1):
    for c_i, val in enumerate(r_val):
        cell = table_links.cell(r_i, c_i)
        cell.paragraphs[0].text = val
        if c_i == 0:
            cell.paragraphs[0].runs[0].bold = True

p_cap_links = doc.add_paragraph()
p_cap_links.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_links.add_run('Table 4.1: Geometric link lengths and kinematic dimensions of the compliant finger.').italic = True

add_header_p('4.2.2 Mechanical Design Constraints and Payload Specifications', level=3)
p = doc.add_paragraph('To guarantee long-term fatigue durability, reliable load holding, and repeatable actuation, the compliant gripper design is governed by strict mechanical, manufacturing, and operational constraints:\n'
                      '• Structural Stress & Fatigue Constraints: Under maximum tendon tension, bending stress concentrates at the throat of the circular flexure living hinges. The maximum allowable localized Von Mises stress is restricted to sigma_max <= 22.0 MPa. With the tensile yield strength of 3D-printed TPU 95A established at sigma_y approx 48 - 52 MPa, this ensures a structural safety factor of SF >= 2.2. This margin guarantees that all hinge deformations remain purely within the linear-elastic recovery regime, preventing permanent set, plastic necking, and low-cycle fatigue failure over >100,000 cycles. The maximum outer-fiber tensile strain is constrained to epsilon_max <= 45%, well below the material\'s ultimate failure strain (>450%).\n'
                      '• Additive Manufacturing Constraints: To avoid anisotropic delamination, all fingers are constrained to be 3D printed flat in the horizontal X-Y build plane. This guarantees that tensile bending stresses along the living hinge throat align parallel with continuous, uninterrupted extruded polymer road contours rather than across inter-layer Z-boundaries. Infill at the hinge throats is specified as 100% concentric.\n'
                      '• Tendon Actuation and Transmission Constraints: Actuation is achieved via single-acting high-strength Dyneema braided cable (breaking strength >250 N). Return extension is fully passive, powered by the stored elastic strain energy of the deformed living hinges. To mitigate friction losses along the internal routing conduits, the channel is lined with micro-PTFE tubing (mu_f <= 0.08), ensuring that nominal tendon pull remains T_nom approx 12.5 N with a peak operating ceiling of T_max <= 25.0 N.\n'
                      '• Payload Capacity and Dynamic Grasp Specifications: The gripper is engineered to handle a rated dynamic payload of 800 - 1500 g (0.8 - 1.5 kg) across cylinders, spheres, and rectangular objects, with a peak static envelope holding capacity of up to 2.0 kg (2000 g). With a total estimated gripper self-mass under 450 g (including 3 TPU fingers, PLA palm, servo mounting brackets, and spools), the design achieves an exceptional payload-to-weight ratio exceeding 3:1 (and up to 4.4:1 in static lock), outperforming conventional fluidic elastomer grippers (<1.5:1). Controlled normal clamping force spans 0.1 N (for delicate workpieces such as raw eggs and ripe fruit) to 20.0 N (for robust industrial parts), coupled with a dynamic slip-reflex latency under 35 ms.')

tab_const_data = [
    ['Domain', 'Design Parameter', 'Target / Limit', 'Governing Constraint and Engineering Rationale'],
    ['Structural / Stress', 'Peak Von Mises Stress', 'sigma_max <= 22.0 MPa', 'Safe margin below TPU 95A yield strength (sigma_y approx 50 MPa).'],
    ['Structural / Stress', 'Safety Factor (Yield)', 'SF >= 2.2', 'Prevents permanent plastic deformation and low-cycle fatigue.'],
    ['Structural / Stress', 'Maximum Bending Strain', 'epsilon_max <= 45%', 'Remains within reversible elastic regime (TPU elongation >450%).'],
    ['Manufacturing', 'Build Orientation', 'Flat in X-Y Plane', 'Ensures tensile bending stresses align with continuous filament beads.'],
    ['Manufacturing', 'Infill Density at Hinges', '100% Concentric', 'Eliminates internal voids and prevents inter-layer delamination.'],
    ['Transmission', 'Tendon Tensile Force', 'T_nom = 12.5 N (T_max <= 25 N)', 'Safe operating load for high-torque digital servomotor (MG996R).'],
    ['Transmission', 'Tendon Stroke', 'delta_x = 12 - 15 mm', 'Delivers 82 deg full envelope wrap across 3 living hinges.'],
    ['Transmission', 'Conduit Friction Coeff.', 'mu_f <= 0.08', 'Micro-PTFE sleeve minimizes Capstan tension loss along curved path.'],
    ['Payload & Force', 'Rated Grasp Payload', '800 - 1500 g (0.8 - 1.5 kg)', 'Operational capacity across irregular cylinders, spheres, and boxes.'],
    ['Payload & Force', 'Peak Static Payload', 'Up to 2.0 kg (2000 g)', 'Form-closure envelope grasp holding capacity under full lock.'],
    ['Payload & Force', 'Gripper Self-Weight', '< 450 g', 'Total mass of 3 fingers, palm base, servo mount, and spools.'],
    ['Payload & Force', 'Payload-to-Weight Ratio', '> 3:1 (up to 4.4:1)', 'Exceeds conventional fluidic/pneumatic soft grippers (< 1.5:1).'],
    ['Payload & Force', 'Normal Clamping Force', '0.1 - 20.0 N', 'Controllable range from fragile eggs (0.5 N) to rigid objects.'],
    ['Payload & Force', 'Closed-Loop Latency', '< 35 ms', 'Dynamic FFT reflex to servomotor torque tightening on slip.']
]

table_const = doc.add_table(rows=len(tab_const_data), cols=4)
table_const.alignment = WD_TABLE_ALIGNMENT.CENTER
for c_i, h_val in enumerate(tab_const_data[0]):
    cell = table_const.cell(0, c_i)
    cell.paragraphs[0].text = h_val
    cell.paragraphs[0].runs[0].bold = True
    set_cell_bg(cell, 'E0E8F0')

for r_i, r_val in enumerate(tab_const_data[1:], start=1):
    for c_i, val in enumerate(r_val):
        cell = table_const.cell(r_i, c_i)
        cell.paragraphs[0].text = val
        if c_i <= 1:
            cell.paragraphs[0].runs[0].bold = True

p_cap_const = doc.add_paragraph()
p_cap_const.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap_const.add_run('Table 4.2: Summary of mechanical design constraints, actuation limits, and payload specifications.').italic = True



add_header_p('4.3 Non-linear Hyperelastic Constitutive Formulation', level=2)
p = doc.add_paragraph('To accurately capture large strain behavior in planned BTP-II finite element simulations, TPU 95A is represented via the 2-Parameter Mooney-Rivlin strain energy density function W:\n\nW = C10*(I1 - 3) + C01*(I2 - 3) + (1/D1)*(J - 1)^2\n\nwhere C10 = 2.45 MPa, C01 = 1.15 MPa, and D1 represents material incompressibility. Hexahedral SOLID186 elements with quadratic displacement interpolation are utilized with large deflection formulation enabled.')

add_header_p('4.4 Tactile Sensing, Filtering, and Slip Detection', level=2)
p = doc.add_paragraph('The FSR402 sensor voltage divider signal is decoupled into static and dynamic regimes:\n1. Static Normal Force: Processed via a 2nd-order active Sallen-Key low-pass filter (fc = 20 Hz) to eliminate motor noise while preserving gripping force.\n2. Dynamic Incipient Slip: Sampled via 12-bit ADC at 1 kHz. An on-chip 256-point Radix-4 FFT computes spectral power in the 100 - 300 Hz band on ESP32 Core 0. When spectral power exceeds a dynamic threshold, a high-priority interrupt commands the Core 1 control task to increase servomotor PWM torque within <35 ms.')

if os.path.exists('Figures and Diagrams/slip_detection_fft_workflow.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture('Figures and Diagrams/slip_detection_fft_workflow.png', width=Inches(5.2))
    p_img_cap = doc.add_paragraph()
    p_img_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img_cap.add_run('Figure 4.3: Tactile signal decomposition and FFT slip-detection pipeline.').italic = True

# CHAPTER 5
add_header_p('Chapter 5: Results and Discussion', level=1)
add_header_p('5.1 Project Status Clarification', level=2)
p = doc.add_paragraph('In strict compliance with academic standards, it is documented that Stage-I (BTP-I) represents the completion of the literature survey, conceptual architecture, and preliminary modeling. No physical prototypes or experimental data were generated in Stage-I. This chapter delineates the simulation framework, experimental testing protocols, and anticipated engineering trade-offs formulated for execution in Stage-II (BTP-II).')

add_header_p('5.2 Kinematic and FEA Simulation Protocol', level=2)
p = doc.add_paragraph('Analytical evaluation shows that a flexure throat thickness of t = 1.6 mm with r = 2.5 mm achieves a total tip curl of 82 degrees under 12.5 N cable tension, enabling secure envelope grasping of objects between 25 mm and 85 mm in diameter. The Ansys FEA campaign will execute mesh convergence down to 0.4 mm elements, verifying that peak Von Mises stresses remain under 22 MPa (yield strength ~50 MPa), ensuring a safety factor of 2.2 for infinite fatigue life.')

add_header_p('5.3 Anticipated Technical Challenges and Mitigations', level=2)

table2 = doc.add_table(rows=6, cols=3)
table2.alignment = WD_TABLE_ALIGNMENT.CENTER
h2 = ['Anticipated Challenge', 'Root Cause', 'Engineering Mitigation Strategy']
for i, h in enumerate(h2):
    c = table2.cell(0, i)
    c.paragraphs[0].text = h
    c.paragraphs[0].runs[0].bold = True
    set_cell_bg(c, 'E0E8F0')

d2 = [
    ['TPU Filament Jamming', 'Buckling in drive gears under backpressure', 'Use direct-drive extruder with constrained path; print at 20 mm/s; zero retraction.'],
    ['Inter-Layer Shear Cleavage', 'Anisotropic Z-axis weakness during bending', 'Print fingers flat horizontally; set nozzle to 225 C for 100% polymer fusion.'],
    ['Tendon Friction Hysteresis', 'Cable abrading layer ridges in conduits', 'Insert micro-PTFE tubing (OD 2 mm, ID 1 mm) through all internal cable guides.'],
    ['FSR Sensor Drift', 'Conductive polymer relaxation under load', 'Firmware implements dynamic AC baseline tracking; decouple static and AC slip signals.'],
    ['Vibrational False Triggers', 'Motor gear chatter mimicking slip frequency', 'FFT algorithm requires 3 consecutive frame triggers (30 ms persistence) before boosting torque.']
]
for r_idx, r_data in enumerate(d2, start=1):
    for c_idx, val in enumerate(r_data):
        c = table2.cell(r_idx, c_idx)
        c.paragraphs[0].text = val
        if c_idx == 0:
            c.paragraphs[0].runs[0].bold = True

p_cap2 = doc.add_paragraph()
p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
p_cap2.add_run('Table 5.1: Anticipated technical challenges and mitigation strategies for BTP-II.').italic = True

# CHAPTER 6
add_header_p('Chapter 6: Conclusions and Plan for Next Phase', level=1)
add_header_p('6.1 Summary of Completed Stage-I Work', level=2)
p = doc.add_paragraph('Stage-I successfully established the research foundation and planned architecture for the soft robotic gripper:\n• Evaluated candidate actuation paradigms and confirmed Monolithic FDM TPU Tendon Actuation as the superior methodology over chemical silicone casting.\n• Formulated the analytical PRBM kinematic equations and selected the 2-Parameter Mooney-Rivlin hyperelastic constitutive strategy for planned BTP-II simulation.\n• Designed an integrated mechatronic pipeline uniting FSR402 sensors, active Butterworth filtering, dual-core FreeRTOS firmware, and an on-chip FFT slip-detection algorithm.\n• Strict Scope Boundary: Reaffirmed that in Stage-I, the team has only decided what we will do. No SolidWorks CAD models, Ansys FEA runs, or physical 3D prints were produced in Stage-I; all CAD modeling, FEA simulation, fabrication, and physical experimentation are scheduled for Stage-II.')

add_header_p('6.2 BTP-II 16-Week Implementation Roadmap', level=2)

if os.path.exists('Figures and Diagrams/gantt_chart_btp2.png'):
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.add_picture('Figures and Diagrams/gantt_chart_btp2.png', width=Inches(5.5))
    p_img_cap = doc.add_paragraph()
    p_img_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img_cap.add_run('Figure 6.1: BTP-II 16-week implementation Gantt chart.').italic = True

p = doc.add_paragraph('The planned milestones across the 16-week BTP-II semester are structured as follows:\n• Weeks 1–3: Detailed SolidWorks CAD modeling of fingers, living hinges, palm base, and spool mounts (Deliverable: .STEP assembly & drawings).\n• Weeks 4–6: Non-linear hyperelastic FEA in Ansys Mechanical; mesh convergence; stress validation (Deliverable: FEA simulation dataset).\n• Weeks 7–8: Direct-drive FDM 3D printing of TPU fingers and PLA base; Dyneema cable rigging (Deliverable: Assembled hardware prototype).\n• Weeks 9–11: Sensor PCB fabrication; ESP32 FreeRTOS firmware programming (Deliverable: Operational sensor & firmware subsystem).\n• Weeks 12–14: Quantitative benchmarking: FSR static calibration, pull-out force testing, slip-prevention tuning (Deliverable: Empirical test dataset).\n• Weeks 15–16: Final autonomous slip-prevention hardware demonstration and thesis defense (Deliverable: Final Thesis Report & Defense Deck).')

add_header_p('6.3 Expected Outcomes and Final Demonstration', level=2)
p = doc.add_paragraph('The culmination of BTP-II will be a live demonstration presented to Prof. Sankha Deb and the evaluation committee featuring:\n1. Autonomous adaptive grasping of geometrically diverse and fragile workpieces (eggs, fruit, light bulbs, metal cylinders) without structural damage.\n2. Real-time tactile telemetry streamed over micro-ROS to a host ROS 2 workstation.\n3. Autonomous slip-prevention demonstration: when an external tensile dislodging force is applied to a grasped object, on-chip FFT detects micro-vibrations and automatically tightens the servomotor grip within <35 ms, preventing the object from slipping out.')

# REFERENCES
add_header_p('References', level=1)
refs = [
    'Whitesides, G. M. (2018). Soft Robotics. Angewandte Chemie International Edition, 57(16), 4258-4273.',
    'Rus, D., & Tolley, M. T. (2015). Design, fabrication and control of soft robots. Nature, 521(7553), 467-475.',
    'Shintake, J., Cacucciolo, V., Floreano, D., & Shea, H. (2018). Soft Robotic Grippers for Agile and Delicate Manipulation. Advanced Materials, 30(29), 1707035.',
    'Hughes, J., Culha, U., Giardina, F., Guenther, F., Rosendo, A., & Iida, F. (2016). Soft Manipulators and Grippers: A Review. Frontiers in Robotics and AI, 3, 69.',
    'Polygerinos, P., Correll, N., Morin, S. A., Shepherd, R., & Whitesides, G. M. (2017). Soft Robotics: Review of Fluid-Driven Intrinsically Soft Devices; Manufacturing, Sensing, Control, and Applications in Wearable Devices. IEEE Systems, Man, and Cybernetics Magazine, 3(3), 12-25.',
    'Dahiya, R. S., Metta, G., Valle, M., & Sandini, G. (2010). Tactile Sensing—From Humans to Humanoids. IEEE Transactions on Robotics, 26(1), 1-20.',
    'Howell, L. L. (2001). Compliant Mechanisms. John Wiley & Sons, New York.',
    'Mooney, M. (1940). A Theory of Large Elastic Deformation. Journal of Applied Physics, 11(9), 582-592.',
    'Yeoh, O. H. (1993). Some Forms of the Strain Energy Function for Rubber. Rubber Chemistry and Technology, 66(5), 754-771.',
    'Shinde, S. S. (2026). Literature Review on Soft Robotics, Alternative Actuation Schemes, and Gripper Architectures. Department of Mechanical Engineering, IIT Kharagpur.',
    'Shekhar, S. (2026). Comprehensive Literature Survey on Tactile and Resistive Sensing Technologies for Soft Robotic Grippers. Department of Mechanical Engineering, IIT Kharagpur.',
    'Chandana, G. (2026). Investigation of Materials and Additive Fabrication Routes for Compliant Robotic Grippers. Department of Mechanical Engineering, IIT Kharagpur.',
    'Chandana, G., Shinde, S. S., & Shekhar, S. (2026). Soft Robotic Grippers using Tactile Sensor. BTP-I Project Report, Supervised by Prof. Sankha Deb, Department of Mechanical Engineering, IIT Kharagpur.'
]
for r in refs:
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.left_indent = Inches(0.4)
    p_ref.paragraph_format.first_line_indent = Inches(-0.4)
    p_ref.paragraph_format.space_after = Pt(4)
    p_ref.add_run(r)

doc.save("Report/BTP_Report_Soft_Robotic_Gripper.docx")
print("Generated updated Report/BTP_Report_Soft_Robotic_Gripper.docx")

# Step 4: Update LaTeX main.tex
print("Step 4: Updating Report/main.tex...")
latex_title_page = r'''\documentclass[12pt,a4paper]{report}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{geometry}
\geometry{top=20mm, bottom=20mm, left=25mm, right=20mm}
\usepackage{amsmath,amssymb,amsfonts}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{tabularx}
\usepackage{multirow}
\usepackage{hyperref}
\hypersetup{
    colorlinks=true,
    linkcolor=blue,
    citecolor=blue,
    urlcolor=cyan,
    pdftitle={Soft Robotic Grippers using Tactile Sensor},
    pdfauthor={G. Chandana, Shinde Sanchali Sanjay, Saurav Shekhar}
}
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small\nouppercase{\leftmark}}
\fancyhead[R]{\small\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\usepackage{setspace}
\onehalfspacing
\usepackage{cite}
\usepackage{caption}
\usepackage{subcaption}

\begin{document}

% ==================== TITLE PAGE (EXACT PROFESSOR FORMAT) ====================
\begin{titlepage}
\centering
\vspace*{-5mm}
\fbox{\begin{minipage}[c][0.93\textheight][c]{0.93\textwidth}
\centering
\vspace{6mm}
{\LARGE \textbf{Soft Robotic Grippers using Tactile Sensor}\par}
\vspace{16mm}
{\large Report submitted to\par}
\vspace{2mm}
{\Large \textbf{Indian Institute of Technology, Kharagpur}\par}
\vspace{2mm}
{\large For the fulfillment of BTP-I in\par}
\vspace{14mm}
{\large \textit{Mechanical Engineering with specialisation in}\par}
\vspace{1mm}
{\large \textit{Manufacturing Science and Engineering by}\par}
\vspace{14mm}
{\large \textbf{G. Chandana (23ME31008)}\par}
\vspace{2mm}
{\large \textbf{Shinde Sanchali Sanjay (23ME31029)}\par}
\vspace{2mm}
{\large \textbf{Saurav Shekhar (23ME31043)}\par}
\vspace{14mm}
{\large Under the\par}
\vspace{2mm}
{\large Supervision of\par}
\vspace{2mm}
{\Large \textbf{Prof. Sankha Deb}\par}
\vspace{8mm}
\includegraphics[width=46mm]{../Figures and Diagrams/iitkgp_logo.png}\par
\vspace{10mm}
{\Large \textbf{Department of Mechanical Engineering}\par}
\vspace{2mm}
{\Large \textbf{Indian Institute of Technology, Kharagpur - 721302}\par}
\vspace{4mm}
\end{minipage}}
\end{titlepage}
'''

with open("Report/main.tex", "r", encoding="utf-8") as f:
    tex_current = f.read()

# Replace titlepage section in LaTeX
idx_cert = tex_current.find(r"\chapter*{Certificate of Approval}")
if idx_cert != -1:
    new_tex = latex_title_page + "\n" + r"\newpage" + "\n" + r"\pagenumbering{roman}" + "\n" + r"\setcounter{page}{2}" + "\n\n" + tex_current[idx_cert:]
    with open("Report/main.tex", "w", encoding="utf-8") as f:
        f.write(new_tex)
    print("Updated Report/main.tex")

# Step 5: Copy to Final Deliverables & Package
print("Step 5: Updating Final Deliverables...")
shutil.copy2("Report/BTP_Report_Soft_Robotic_Gripper.pdf", "Final Deliverables/BTP_Report_Soft_Robotic_Gripper.pdf")
shutil.copy2("Report/BTP_Report_Soft_Robotic_Gripper.docx", "Final Deliverables/BTP_Report_Soft_Robotic_Gripper.docx")

zip_path = "Final Deliverables/BTP_Report_LaTeX_Source.zip"
with zipfile.ZipFile(zip_path, "w") as zf:
    zf.write("Report/main.tex", arcname="main.tex")
    zf.write("References/references.bib", arcname="references.bib")
    for fl in os.listdir("Figures and Diagrams"):
        zf.write(os.path.join("Figures and Diagrams", fl), arcname=os.path.join("Figures and Diagrams", fl))

print("All deliverables updated successfully!")
