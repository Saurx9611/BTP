import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Color Palette
C_NAVY = RGBColor(0x00, 0x33, 0x66)
C_DARK = RGBColor(0x1E, 0x29, 0x3B)
C_LIGHT_BG = RGBColor(0xF8, 0xFA, 0xFC)
C_CARD_BG = RGBColor(0xED, 0xF2, 0xF7)
C_ACCENT_BLUE = RGBColor(0x25, 0x63, 0xEB)
C_ACCENT_TEAL = RGBColor(0x0D, 0x94, 0x88)
C_ACCENT_RED = RGBColor(0xDC, 0x26, 0x26)
C_WHITE = RGBColor(0xFF, 0xFF, 0xFF)

blank_layout = prs.slide_layouts[6]

def create_slide_base(title_text, subtitle_text="BTP-I Project Stage Presentation | IIT Kharagpur"):
    slide = prs.slides.add_slide(blank_layout)
    
    # Header bar background
    header_box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.15))
    header_box.fill.solid()
    header_box.fill.fore_color.rgb = C_NAVY
    header_box.line.color.rgb = C_NAVY
    
    # Title text
    tx_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.12), Inches(11.7), Inches(0.6))
    tf = tx_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.name = "Arial"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = C_WHITE
    
    # Subtitle text
    sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.68), Inches(11.7), Inches(0.4))
    tf_sub = sub_box.text_frame
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = subtitle_text
    p_sub.font.name = "Arial"
    p_sub.font.size = Pt(11)
    p_sub.font.color.rgb = RGBColor(0x93, 0xC5, 0xFD)
    
    # Footer
    foot_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.7), Inches(0.35))
    tf_f = foot_box.text_frame
    p_f = tf_f.paragraphs[0]
    p_f.text = "Department of Mechanical Engineering, IIT Kharagpur | Soft Robotic Grippers using Tactile Sensor"
    p_f.font.name = "Arial"
    p_f.font.size = Pt(9.5)
    p_f.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)
    
    return slide

def add_card(slide, left, top, width, height, title, items, bg_color=C_CARD_BG, border_color=C_NAVY):
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    card.line.color.rgb = border_color
    card.line.width = Pt(1.5)
    
    tb = slide.shapes.add_textbox(left + Inches(0.15), top + Inches(0.15), width - Inches(0.3), height - Inches(0.3))
    tf = tb.text_frame
    tf.word_wrap = True
    
    p0 = tf.paragraphs[0]
    p0.text = title
    p0.font.name = "Arial"
    p0.font.size = Pt(14)
    p0.font.bold = True
    p0.font.color.rgb = border_color
    p0.space_after = Pt(8)
    
    for item in items:
        p = tf.add_paragraph()
        p.text = "• " + item
        p.font.name = "Arial"
        p.font.size = Pt(11)
        p.font.color.rgb = C_DARK
        p.space_after = Pt(4)

# ==================== SLIDE 1: TITLE ====================
slide1 = prs.slides.add_slide(blank_layout)
bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
bg1.fill.solid()
bg1.fill.fore_color.rgb = C_NAVY
bg1.line.color.rgb = C_NAVY

t_box = slide1.shapes.add_textbox(Inches(1.0), Inches(1.2), Inches(11.333), Inches(2.2))
tf = t_box.text_frame
tf.word_wrap = True
p = tf.paragraphs[0]
p.text = "DEVELOPMENT, NON-LINEAR MODELING, AND EMBEDDED TACTILE CONTROL OF A 3D-PRINTED COMPLIANT SOFT ROBOTIC GRIPPER"
p.font.name = "Arial"
p.font.size = Pt(26)
p.font.bold = True
p.font.color.rgb = C_WHITE
p.alignment = PP_ALIGN.CENTER

p_sub = tf.add_paragraph()
p_sub.text = "BTP-I Project Stage Presentation | Mechanical Engineering (Manufacturing Science & Engineering)"
p_sub.font.name = "Arial"
p_sub.font.size = Pt(14)
p_sub.font.color.rgb = RGBColor(0x93, 0xC5, 0xFD)
p_sub.alignment = PP_ALIGN.CENTER
p_sub.space_before = Pt(12)

team_box = slide1.shapes.add_textbox(Inches(1.5), Inches(3.8), Inches(10.333), Inches(1.8))
tf_team = team_box.text_frame
tf_team.word_wrap = True

p_auth = tf_team.paragraphs[0]
p_auth.text = "Student Investigators:\nG. Chandana (23ME31008)  |  Shinde Sanchali Sanjay (23ME31029)  |  Saurav Shekhar (23ME31043)"
p_auth.font.name = "Arial"
p_auth.font.size = Pt(13)
p_auth.font.bold = True
p_auth.font.color.rgb = C_WHITE
p_auth.alignment = PP_ALIGN.CENTER
p_auth.space_after = Pt(12)

p_sup = tf_team.add_paragraph()
p_sup.text = "Supervisor: Prof. Sankha Deb\nDepartment of Mechanical Engineering, Indian Institute of Technology, Kharagpur"
p_sup.font.name = "Arial"
p_sup.font.size = Pt(13)
p_sup.font.color.rgb = RGBColor(0xFE, 0xF0, 0x8A)
p_sup.alignment = PP_ALIGN.CENTER

# ==================== SLIDE 2: INTRODUCTION ====================
s2 = create_slide_base("Introduction to Soft Robotics & Compliant Manipulation")
add_card(s2, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2),
         "Conventional Rigid Grippers",
         ["Engineered with rigid metallic links and discrete kinematic joints.",
          "High positioning repeatability and high stiffness in structured lines.",
          "Point contact creates localized stress spikes on target workpieces.",
          "High risk of crushing delicate, soft, or biological structures.",
          "Requires complex multi-axis inverse kinematics & vision tracking."],
         bg_color=RGBColor(0xFE, 0xF2, 0xF2), border_color=C_ACCENT_RED)

add_card(s2, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2),
         "Soft & Compliant Robotic Grippers",
         ["Replaces rigid linkages with continuously deformable elastomeric bodies.",
          "Embodies mechanical intelligence into material structural compliance.",
          "Passively conforms to unknown, irregular 3D contours.",
          "Distributes interaction forces over an expanded contact area.",
          "Inherently safe for fragile, delicate, and human-collaborative tasks."],
         bg_color=RGBColor(0xEC, 0xFD, 0xF5), border_color=C_ACCENT_TEAL)

# ==================== SLIDE 3: MOTIVATION & APPLICATIONS ====================
s3 = create_slide_base("Project Background & Industrial Motivation")
add_card(s3, Inches(0.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "Automated Agriculture",
         ["Gentle harvesting of soft-skinned fruits and vegetables (tomatoes, strawberries).",
          "Eliminates internal bruising that triggers accelerated biological decay.",
          "Adapts to natural variations in produce size, ripeness, and orientation."],
         border_color=C_ACCENT_BLUE)

add_card(s3, Inches(4.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "Biomedical Logistics",
         ["Handling thin-walled glass vials, filled fluid ampoules, and test tubes.",
          "Prevents mechanical shock and brittle fracture during sorting.",
          "Conforms to delicate anatomical specimens and surgical equipment."],
         border_color=C_ACCENT_TEAL)

add_card(s3, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "Explosive Ordnance Disposal",
         ["Interfacing with uncertain, aged, or structurally compromised munitions.",
          "Non-sparking, spark-free polymer construction.",
          "Eliminates uncontrolled clamping impact that could trigger detonation."],
         border_color=C_ACCENT_RED)

# ==================== SLIDE 4: PROBLEM STATEMENT ====================
s4 = create_slide_base("Formal Problem Statement")
p_box = s4.shapes.add_textbox(Inches(1.0), Inches(1.6), Inches(11.333), Inches(2.0))
tf_p = p_box.text_frame
tf_p.word_wrap = True
p = tf_p.paragraphs[0]
p.text = "\"Conventional rigid end-effectors lack the compliance required to manipulate fragile and irregularly shaped objects without inflicting structural damage, while existing soft grippers suffer from low payload capacity, material hysteresis, tethered fluidic supplies, and an absence of localized feedback capable of detecting incipient slip without bulky optical systems.\""
p.font.name = "Arial"
p.font.size = Pt(17)
p.font.italic = True
p.font.bold = True
p.font.color.rgb = C_NAVY
p.alignment = PP_ALIGN.CENTER

add_card(s4, Inches(0.8), Inches(3.8), Inches(5.6), Inches(2.9),
         "Key Research Bottlenecks",
         ["Non-linear hyperelastic material behavior & large strains.",
          "Material viscoelastic relaxation during sustained holding.",
          "Severe sensor delamination on stretching elastomeric bladders."],
         border_color=C_ACCENT_RED)

add_card(s4, Inches(6.8), Inches(3.8), Inches(5.7), Inches(2.9),
         "Proposed Solution Approach",
         ["Monolithic 3D-printed TPU 95A structure with living hinges.",
          "Tendon-driven actuation with remote base-mounted servomotors.",
          "Recessed FSR402 sensors + on-chip FFT for slip prevention."],
         border_color=C_ACCENT_TEAL)

# ==================== SLIDE 5: LITERATURE CORPUS ====================
s5 = create_slide_base("Consolidated Literature Review: Team Synthesis")
add_card(s5, Inches(0.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "Actuation & Kinematics (Sanchali)",
         ["Comprehensive review of soft actuation (pneumatic, tendon, SMA, DEA).",
          "Mobility classification: constrained, underconstrained, deformable.",
          "Identified payload vs compliance trade-off in fluidic grippers.",
          "Tendon-driven base motors reduce distal finger inertia."],
         border_color=C_ACCENT_BLUE)

add_card(s5, Inches(4.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "Materials & Fabrication (Chandana)",
         ["Evaluated silicones (Ecoflex, PDMS), TPUs, TPEs, and photopolymers.",
          "Molding requires multi-step casting, degassing, and curing ovens.",
          "Confirmed FDM 3D printing of TPU as the optimal manufacturing route.",
          "Eliminates molds, enables rapid geometric iterations."],
         border_color=C_ACCENT_TEAL)

add_card(s5, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "Tactile Transduction (Saurav)",
         ["Surveyed piezoresistive, capacitive, piezoelectric, and optical sensors.",
          "Decoupled static contact force from high-frequency slip vibration.",
          "FSR402 thin-film piezoresistors provide ideal form factor.",
          "Highlighted need for active filtering & drift compensation."],
         border_color=C_ACCENT_RED)

# ==================== SLIDE 6: COMPARATIVE ANALYSIS ====================
s6 = create_slide_base("Comparative Analysis of Actuation Methodologies")
if os.path.exists("Figures and Diagrams/comparative_radar_chart.png"):
    s6.shapes.add_picture("Figures and Diagrams/comparative_radar_chart.png", Inches(0.8), Inches(1.4), Inches(5.8), Inches(5.3))

add_card(s6, Inches(7.0), Inches(1.5), Inches(5.5), Inches(5.2),
         "Engineering Trade-Off Evaluation",
         ["Pneumatics: Maximum shape conformity, but tethered compressor, bulky valves, and risk of seam rupture under pressure.",
          "Shape Memory Alloy (SMA): High energy density, but very slow cooling lag (3-15 s), severe hysteresis, and thermal fatigue.",
          "Dielectric Elastomers: High strain, but hazardous driving voltages (>1-5 kV) and dielectric breakdown risks.",
          "Monolithic Tendon TPU (Selected): High payload ratio (3:1 to 5:1), completely untethered battery operation, rapid FDM printing, and straightforward servomotor PWM control."],
         border_color=C_ACCENT_BLUE)

# ==================== SLIDE 7: RESEARCH GAPS ====================
s7 = create_slide_base("Identified Research Gaps in Existing Literature")
add_card(s7, Inches(0.8), Inches(1.5), Inches(5.6), Inches(2.5),
         "Gap 1: Compliance vs. Payload Trade-Off",
         ["Pure elastomeric bladders buckle under lateral/torsional loads.",
          "Payloads typically restricted to <200-400 grams.",
          "Need for flexure mechanisms combining compliance with structural load capacity."],
         border_color=C_ACCENT_RED)

add_card(s7, Inches(6.8), Inches(1.5), Inches(5.7), Inches(2.5),
         "Gap 2: Interfacial Sensor Delamination",
         ["Planar sensors bonded to stretching silicone skin experience severe peeling shear.",
          "Cyclic bending causes electrical trace rupture and sensor detachment.",
          "Need for recessed, strain-isolated sensor pockets on rigid contact pads."],
         border_color=C_ACCENT_RED)

add_card(s7, Inches(0.8), Inches(4.2), Inches(5.6), Inches(2.6),
         "Gap 3: Bulky Slip Detection Systems",
         ["State-of-the-art slip sensing relies on heavy optical cameras (GelSight).",
          "Computationally intensive image processing unsuited for mobile arms.",
          "Need for lightweight, edge-computed tactile vibration analysis."],
         border_color=C_ACCENT_RED)

add_card(s7, Inches(6.8), Inches(4.2), Inches(5.7), Inches(2.6),
         "Gap 4: Embedded Edge vs Host Disconnect",
         ["Many research prototypes rely on desktop MATLAB scripts.",
          "Lack of deterministic real-time operating systems running on-board.",
          "Need for FreeRTOS dual-core embedded control coupled to ROS 2."],
         border_color=C_ACCENT_RED)

# ==================== SLIDE 8: OBJECTIVES & SCOPE ====================
s8 = create_slide_base("Project Objectives and Technical Scope")
add_card(s8, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2),
         "Main & Specific Sub-Objectives",
         ["Main: Establish the design, modeling, fabrication, and control methodology for a compliant gripper.",
          "Design Strategy: Define circular living hinge geometry using Howell PRBM formulations.",
          "Material Selection: Formulate direct-drive FDM printing with flexible TPU 95A filament.",
          "Simulation Strategy: Formulate hyperelastic constitutive modeling for BTP-II simulation.",
          "Signal Conditioning: Design Sallen-Key 2nd-order Butterworth LPF (fc = 20 Hz).",
          "Firmware Architecture: Design dual-core FreeRTOS pipeline (1 kHz FFT / Servo PWM).",
          "Validation Plan: Outline pull-out force benchmarking and autonomous slip prevention."],
         border_color=C_ACCENT_BLUE)

add_card(s8, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2),
         "Technical Scope & Boundaries",
         ["COMPLETED IN STAGE-I:",
          "• Multi-thematic literature review & comparative technology evaluation.",
          "• Selection of monolithic FDM TPU tendon-driven gripper methodology.",
          "• Analytical kinematic formulations (Howell PRBM & Capstan friction).",
          "• Embedded signal processing & FreeRTOS architectural design.",
          "PLANNED FOR STAGE-II (BTP-II):",
          "• SolidWorks 3D CAD modeling & Ansys non-linear hyperelastic FEA.",
          "• Physical prototype 3D printing, sensor assembly, & experimental trials.",
          "OUT-OF-SCOPE:",
          "• High-speed sorting (>3 m/s), multi-axis shear arrays, underwater trials."],
         border_color=C_ACCENT_TEAL)

# ==================== SLIDE 9: SELECTED METHODOLOGY ====================
s9 = create_slide_base("Confirmed Methodology: Monolithic 3D-Printed Tendon Gripper")
add_card(s9, Inches(0.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "1. Structural Compliance",
         ["Monolithic FDM 3D printing with flexible TPU 95A.",
          "Replaces discrete mechanical pins with living hinges.",
          "Zero joint assembly, zero mechanical backlash, zero lubrication.",
          "Horizontal build orientation maximizes inter-layer tensile strength."],
         border_color=C_ACCENT_BLUE)

add_card(s9, Inches(4.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "2. Tendon Transmission",
         ["Remote base-mounted metal-gear digital servomotors (DS3218).",
          "Braided Dyneema cable (>30 kg rating) pulling through low-friction guides.",
          "Micro-PTFE tubing inserts minimize Capstan friction losses.",
          "Passive elastic restoration driven by stored TPU strain energy."],
         border_color=C_ACCENT_TEAL)

add_card(s9, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "3. Embedded Intelligence",
         ["FSR402 thin-film sensors recessed flush in contact pads.",
          "Analog 2nd-order Butterworth filtering for normal force Fn.",
          "On-chip 256-point FFT on ESP32 Core 0 for slip vibrations.",
          "Closed-loop servomotor torque tightening in <35 milliseconds."],
         border_color=C_ACCENT_RED)

# ==================== SLIDE 10: KINEMATICS & PRBM ====================
s10 = create_slide_base("Kinematic Modeling & Pseudo-Rigid-Body Formulation")
if os.path.exists("Figures and Diagrams/gripper_kinematics_diagram.png"):
    s10.shapes.add_picture("Figures and Diagrams/gripper_kinematics_diagram.png", Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2))

# Card 1: Compliant Living Hinge Mechanics
add_card(s10, Inches(6.6), Inches(1.5), Inches(5.9), Inches(2.4),
         "Compliant Living Hinge Mechanics (PRBM)",
         ["Howell PRBM: Circular notches modeled as torsional spring joints:",
          "  K_theta = (E * w * t^2.5) / (9 * pi * sqrt(r))  [t = 1.6 mm, r = 2.5 mm, w = 20 mm]",
          "Capstan Tendon Friction Law across living hinges:",
          "  T_distal = T_base * exp(-sum(mu_f * theta_i))",
          "Micro-PTFE sleeves minimize friction to mu_f <= 0.08, maximizing force delivery."],
         border_color=C_ACCENT_BLUE)

# Card 2: Underactuated Mechanical Intelligence & Contact Progression
add_card(s10, Inches(6.6), Inches(4.05), Inches(5.9), Inches(2.65),
         "Underactuated Mechanical Intelligence & Grasping Sequence",
         ["1 Actuator -> 3 DOFs: Single Dyneema tendon drives MCP, PIP, DIP joints (zero inverse kinematics needed).",
          "Phase 1 (In-Flight Flexure): Cable tension T flexes all joints simultaneously proportional to compliance K_theta_i.",
          "Phase 2 (Proximal Arrest): Object contact creates counter-moment M_contact, locking proximal link rotation.",
          "Phase 3 (Passive Conformal Wrap): Tension bypasses arrested link via PTFE sleeve to curl distal joints around irregular contours.",
          "Phase 4 & 5 (Sensor Lock & Return): Distal pad engages FSR402; slacking tendon releases stored strain energy for passive spring return."],
         border_color=C_ACCENT_TEAL)

# ==================== SLIDE 11: MATERIAL & SIMULATION STRATEGY ====================
s11 = create_slide_base("Proposed Material Selection & Planned Simulation Strategy")
add_card(s11, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2),
         "Material Selection: TPU 95A",
         ["Evaluated silicones (Ecoflex, PDMS), photopolymers, and polyurethanes.",
          "Silicone molding requires multi-part molds, vacuum degassing, and curing ovens.",
          "Direct FDM 3D printing of TPU 95A eliminates molds and enables rapid prototyping.",
          "Shore 95A provides high flexural resilience while preventing out-of-plane torsional buckling.",
          "Monolithic printing enables continuous living hinges without assembly pins or mechanical backlash."],
         border_color=C_ACCENT_BLUE)

add_card(s11, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2),
         "Planned Hyperelastic FEA Strategy (BTP-II)",
         ["Non-linear Mechanics: TPU undergoes large elastic deformations and strain-stiffening.",
          "Hookean linear elasticity is invalid for large flexure bending.",
          "Selected Constitutive Law: 2-Parameter Mooney-Rivlin strain energy formulation:",
          "  W = C10*(I1 - 3) + C01*(I2 - 3) + (1/D1)*(J - 1)^2",
          "Planned BTP-II Simulation Goals:",
          "• Model finger curl angle versus tendon tension prior to 3D printing.",
          "• Evaluate Von Mises stress concentrations at flexure notches to ensure high fatigue life.",
          "Status: Modeling methodology decided; simulation runs will be performed in BTP-II."],
         border_color=C_ACCENT_TEAL)

# ==================== SLIDE 12: MECHATRONICS & SENSING ====================
s12 = create_slide_base("Mechatronic & Embedded Firmware Architecture")
if os.path.exists("Figures and Diagrams/mechatronics_architecture.png"):
    s12.shapes.add_picture("Figures and Diagrams/mechatronics_architecture.png", Inches(0.8), Inches(1.5), Inches(7.2), Inches(5.2))

add_card(s12, Inches(8.3), Inches(1.5), Inches(4.3), Inches(5.2),
         "Dual-Core FreeRTOS Pipeline",
         ["Core 0 (1 kHz DMA Task):",
          "• High-speed 12-bit ADC sampling.",
          "• 2nd-order Butterworth LPF (fc = 20 Hz).",
          "• 256-point Radix-4 FFT spectral calculation.",
          "• Incipient slip threshold evaluation.",
          "Core 1 (100 Hz Control Task):",
          "• Closed-loop servomotor PWM torque update.",
          "• Hysteresis compensation lookup.",
          "• micro-ROS DDS publishing over serial/WiFi."],
         border_color=C_ACCENT_RED)

# ==================== SLIDE 13: SLIP DETECTION WORKFLOW ====================
s13 = create_slide_base("Tactile Signal Processing & Autonomous Slip Prevention")
if os.path.exists("Figures and Diagrams/slip_detection_fft_workflow.png"):
    s13.shapes.add_picture("Figures and Diagrams/slip_detection_fft_workflow.png", Inches(0.8), Inches(1.5), Inches(6.8), Inches(5.2))

add_card(s13, Inches(7.9), Inches(1.5), Inches(4.7), Inches(5.2),
         "Spectral Energy Triggering",
         ["Time Domain: Normal clamping force Fn resides in low-frequency band (0-20 Hz).",
          "Dynamic Friction: Incipient micro-vibrations generate sharp tactile energy spikes in 100-300 Hz band.",
          "On-Chip FFT Metric:",
          "E_slip = sum(|X[k]|^2) for k in [25, 76]",
          "Autonomous Compensation: When E_slip exceeds dynamic baseline threshold, ESP32 commands immediate servomotor torque boost in <35 ms, arresting slip."],
         border_color=C_ACCENT_TEAL)

# ==================== SLIDE 14: CURRENT STATUS & RESULTS ====================
s14 = create_slide_base("Current Progress & Baseline Results (BTP-I)")
add_card(s14, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2),
         "Work Completed in Stage-I",
         ["• Literature Review: Comprehensive synthesis of actuation, materials, and tactile sensing.",
          "• Methodology Decision: Multi-criteria selection of Monolithic FDM TPU Tendon Gripper.",
          "• Conceptual Design: Selected circular living hinge architecture and Dyneema routing.",
          "• Theoretical Kinematics: Howell PRBM living hinge stiffness & Capstan friction equations.",
          "• Signal Architecture: Sallen-Key Butterworth filter & dual-core FreeRTOS pipeline.",
          "• Implementation Plan: Structured 16-week execution roadmap for BTP-II."],
         border_color=C_ACCENT_TEAL)

add_card(s14, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2),
         "Status Clarification: Decisions & Planning",
         ["IMPORTANT ACADEMIC CLARIFICATION:",
          "\"We have only decided what we will do.\"",
          "• In strict compliance with academic standards, no SolidWorks CAD models were constructed in Stage-I.",
          "• No Ansys FEA simulations were executed in Stage-I.",
          "• No physical prototypes were 3D printed or experimentally tested in Stage-I.",
          "• All 3D CAD modeling, FEA simulation, fabrication, sensor wiring, and experimental trials are scheduled for Stage-II (BTP-II)."],
         border_color=C_ACCENT_BLUE)

# ==================== SLIDE 15: CHALLENGES & MITIGATIONS ====================
s15 = create_slide_base("Anticipated Challenges & Engineering Mitigations")
add_card(s15, Inches(0.8), Inches(1.5), Inches(5.6), Inches(2.5),
         "TPU Extrusion Jamming",
         ["Cause: Flexible filament buckling in direct-drive gear under backpressure.",
          "Mitigation: Use direct-drive extruder with constrained path; print at 20 mm/s; disable retraction."],
         border_color=C_ACCENT_RED)

add_card(s15, Inches(6.8), Inches(1.5), Inches(5.7), Inches(2.5),
         "Inter-Layer Shear Cleavage",
         ["Cause: Anisotropic Z-axis weakness during high flexural bending.",
          "Mitigation: Print fingers flat horizontally; set nozzle to 225°C to achieve 100% polymer weld."],
         border_color=C_ACCENT_RED)

add_card(s15, Inches(0.8), Inches(4.2), Inches(5.6), Inches(2.6),
         "Tendon Friction Hysteresis",
         ["Cause: Dyneema cable abrading 3D-printed layer ridges in channels.",
          "Mitigation: Insert micro-PTFE tubing (OD 2 mm, ID 1 mm) along internal cable channels."],
         border_color=C_ACCENT_RED)

add_card(s15, Inches(6.8), Inches(4.2), Inches(5.7), Inches(2.6),
         "FSR Sensor Resistance Drift",
         ["Cause: Conductive polymer relaxation under continuous load.",
          "Mitigation: Firmware implements dynamic AC baseline tracking, decoupling static and AC slip signals."],
         border_color=C_ACCENT_RED)

# ==================== SLIDE 16: NEXT-PHASE ROADMAP ====================
s16 = create_slide_base("BTP-II Semester-Wise Implementation Roadmap")
if os.path.exists("Figures and Diagrams/gantt_chart_btp2.png"):
    s16.shapes.add_picture("Figures and Diagrams/gantt_chart_btp2.png", Inches(0.8), Inches(1.5), Inches(7.2), Inches(5.2))

add_card(s16, Inches(8.3), Inches(1.5), Inches(4.3), Inches(5.2),
         "16-Week Deliverables",
         ["• W1–W3: Detailed CAD modeling (.STEP assembly & 2D drawings).",
          "• W4–W6: Ansys hyperelastic FEA (simulation dataset & report).",
          "• W7–W8: FDM TPU 3D printing & Dyneema rigging (hardware prototype).",
          "• W9–W11: Analog sensor PCB & ESP32 FreeRTOS firmware.",
          "• W12–W14: Static calibration & pull-out force trials.",
          "• W15–W16: Live slip-prevention demonstration & defense."],
         border_color=C_ACCENT_BLUE)

# ==================== SLIDE 17: EXPECTED OUTCOMES ====================
s17 = create_slide_base("Expected Outcomes & Final Demonstration")
add_card(s17, Inches(0.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "1. Autonomous Grasping",
         ["Conforming gently to diverse shapes: spheres, cylinders, fragile eggs, soft fruits.",
          "Zero crushing damage on fragile surfaces.",
          "Payload capacity of 800 - 1500 g on a gripper self-weight of <450 g (Payload ratio >2:1)."],
         border_color=C_ACCENT_BLUE)

add_card(s17, Inches(4.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "2. Real-Time Telemetry",
         ["Live graphical dashboard streaming contact force and FFT spectral density.",
          "Integrated micro-ROS client publishing to ROS 2 on host workstation.",
          "Deterministic multi-tasking executing on ESP32 dual cores."],
         border_color=C_ACCENT_TEAL)

add_card(s17, Inches(8.8), Inches(1.5), Inches(3.7), Inches(5.2),
         "3. Slip Prevention Demo",
         ["Live physical test: external dislodging tension applied to a grasped object.",
          "On-chip FFT detects tactile micro-vibrations in 100-300 Hz band.",
          "Servomotors automatically tighten grip within <35 ms, arresting slip before drop."],
         border_color=C_ACCENT_RED)

# ==================== SLIDE 18: CONCLUSION & REFERENCES ====================
s18 = create_slide_base("Conclusion & Key References")
add_card(s18, Inches(0.8), Inches(1.5), Inches(5.6), Inches(5.2),
         "Conclusions",
         ["• Stage-I establishes a complete, technically sound research direction combining compliant mechanics, additive manufacturing, tactile perception, and real-time edge control.",
          "• Monolithic FDM TPU printing eliminates mold delays and chemical hazards of silicone casting.",
          "• Tendon-driven base servomotors optimize payload-to-weight ratio while maintaining safe contact compliance.",
          "• The integrated FreeRTOS / FFT slip detection framework provides deterministic autonomy without bulky optical cameras.",
          "• The 16-week BTP-II roadmap establishes measurable milestones leading to a validated physical prototype."],
         border_color=C_ACCENT_TEAL)

add_card(s18, Inches(6.8), Inches(1.5), Inches(5.7), Inches(5.2),
         "Key References",
         ["[1] Whitesides, G. M. (2018). Soft Robotics. Angew. Chem.",
          "[2] Rus, D., & Tolley, M. T. (2015). Design of Soft Robots. Nature.",
          "[3] Shintake, J., et al. (2018). Soft Grippers. Adv. Mater.",
          "[4] Hughes, J., et al. (2016). Soft Manipulators. Front. Robot. AI.",
          "[5] Dahiya, R. S., et al. (2010). Tactile Sensing. IEEE T-RO.",
          "[6] Howell, L. L. (2001). Compliant Mechanisms. Wiley.",
          "[7] Mooney, M. (1940). Theory of Large Elastic Deformation. J. Appl. Phys.",
          "[8] Student Literature Reviews: Sanchali (2026), Saurav (2026), Chandana (2026), Joint Report (2026), Dept. Mech. Eng., IIT Kharagpur."],
         border_color=C_ACCENT_BLUE)

os.makedirs("Presentation", exist_ok=True)
prs.save("Presentation/BTP_Presentation_Soft_Robotic_Gripper.pptx")
print("Generated Presentation/BTP_Presentation_Soft_Robotic_Gripper.pptx successfully.")

