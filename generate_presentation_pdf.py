import os
from playwright.sync_api import sync_playwright

html_slides = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>BTP Presentation - Soft Robotic Gripper</title>
<style>
    @page {
        size: 297mm 167mm; /* 16:9 widescreen */
        margin: 0;
    }
    body {
        margin: 0;
        padding: 0;
        font-family: 'Arial', sans-serif;
        background-color: #f8fafc;
        color: #1e293b;
        -webkit-print-color-adjust: exact;
    }
    .slide {
        width: 297mm;
        height: 167mm;
        page-break-after: always;
        position: relative;
        box-sizing: border-box;
        overflow: hidden;
        background-color: #ffffff;
    }
    .slide-header {
        background-color: #003366;
        color: #ffffff;
        padding: 16px 30px;
        height: 52px;
    }
    .slide-header h2 {
        margin: 0;
        font-size: 20pt;
        font-weight: bold;
    }
    .slide-header p {
        margin: 3px 0 0 0;
        font-size: 10pt;
        color: #93c5fd;
    }
    .slide-content {
        padding: 24px 30px;
        height: calc(167mm - 120px);
        box-sizing: border-box;
    }
    .slide-footer {
        position: absolute;
        bottom: 10px;
        left: 30px;
        right: 30px;
        font-size: 8.5pt;
        color: #64748b;
        border-top: 1px solid #e2e8f0;
        padding-top: 5px;
        display: flex;
        justify-content: space-between;
    }
    .title-slide {
        background-color: #003366;
        color: #ffffff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 40px;
    }
    .title-slide h1 {
        font-size: 24pt;
        line-height: 1.3;
        margin-bottom: 20px;
        color: #ffffff;
    }
    .title-slide h3 {
        font-size: 13pt;
        font-weight: normal;
        color: #93c5fd;
        margin-bottom: 35px;
    }
    .title-slide .authors {
        font-size: 11.5pt;
        margin-bottom: 25px;
        line-height: 1.6;
    }
    .title-slide .supervisor {
        font-size: 12pt;
        color: #fef08a;
        margin-bottom: 30px;
    }
    .title-slide .inst {
        font-size: 10.5pt;
        color: #cbd5e1;
    }
    .grid-2 {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        height: 100%;
    }
    .grid-3 {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: 18px;
        height: 100%;
    }
    .card {
        background-color: #f1f5f9;
        border-radius: 8px;
        border-left: 5px solid #003366;
        padding: 16px 20px;
        box-sizing: border-box;
    }
    .card-teal { border-left-color: #0d9488; background-color: #f0fdf4; }
    .card-red { border-left-color: #dc2626; background-color: #fef2f2; }
    .card-blue { border-left-color: #2563eb; background-color: #eff6ff; }
    .card-amber { border-left-color: #d97706; background-color: #fffbeb; }
    
    .card h3 {
        margin-top: 0;
        margin-bottom: 12px;
        font-size: 13pt;
        color: #0f172a;
    }
    .card ul {
        margin: 0;
        padding-left: 18px;
        font-size: 10pt;
        line-height: 1.5;
        color: #334155;
    }
    .card li {
        margin-bottom: 6px;
    }
    .image-box {
        text-align: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .image-box img {
        max-width: 95%;
        max-height: 110mm;
        border-radius: 6px;
        border: 1px solid #cbd5e1;
    }
    .caption {
        font-size: 8.5pt;
        font-style: italic;
        color: #64748b;
        margin-top: 6px;
    }
</style>
</head>
<body>

<!-- SLIDE 1: TITLE -->
<div class="slide title-slide">
    <h1>DEVELOPMENT, NON-LINEAR MODELING, AND EMBEDDED TACTILE CONTROL OF A 3D-PRINTED COMPLIANT SOFT ROBOTIC GRIPPER</h1>
    <h3>BTP-I Project Stage Presentation | Mechanical Engineering (Manufacturing Science & Engineering)</h3>
    <div class="authors">
        <strong>Student Investigators:</strong><br>
        G. Chandana (23ME31008) &nbsp;|&nbsp; Shinde Sanchali Sanjay (23ME31029) &nbsp;|&nbsp; Saurav Shekhar (23ME31043)
    </div>
    <div class="supervisor">
        <strong>Supervisor:</strong> Prof. Sankha Deb<br>
        Department of Mechanical Engineering, IIT Kharagpur
    </div>
    <div class="inst">
        INDIAN INSTITUTE OF TECHNOLOGY, KHARAGPUR &nbsp;|&nbsp; NOVEMBER 2026
    </div>
</div>

<!-- SLIDE 2: INTRO -->
<div class="slide">
    <div class="slide-header">
        <h2>Introduction to Soft Robotics & Compliant Manipulation</h2>
        <p>Overcoming the limitations of traditional rigid robotic end-effectors</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="card card-red">
                <h3>Conventional Rigid Grippers</h3>
                <ul>
                    <li>Constructed from metallic links and discrete kinematic joints.</li>
                    <li>High positioning repeatability and rigidity in structured environments.</li>
                    <li>Point contact creates localized stress spikes on fragile workpieces.</li>
                    <li>Significant risk of crushing biological or delicate objects.</li>
                    <li>Requires complex multi-axis trajectory planning and force sensing.</li>
                </ul>
            </div>
            <div class="card card-teal">
                <h3>Soft & Compliant Grippers</h3>
                <ul>
                    <li>Replaces rigid links with continuously deformable elastomeric bodies.</li>
                    <li>Embodies mechanical intelligence directly into structural compliance.</li>
                    <li>Passively conforms to unknown, irregular 3D object geometries.</li>
                    <li>Distributes interaction forces over an expanded contact area.</li>
                    <li>Inherently safe for agricultural produce, medical vials, and humans.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 2</span>
    </div>
</div>

<!-- SLIDE 3: MOTIVATION -->
<div class="slide">
    <div class="slide-header">
        <h2>Background and Industrial Motivation</h2>
        <p>Target applications demanding gentle, adaptive, and sensorized manipulation</p>
    </div>
    <div class="slide-content">
        <div class="grid-3">
            <div class="card card-blue">
                <h3>Automated Agriculture</h3>
                <ul>
                    <li>Selective harvesting of soft-skinned fruits and vegetables (tomatoes, strawberries).</li>
                    <li>Eliminates internal tissue bruising that accelerates biological decay.</li>
                    <li>Adapts to natural variations in fruit size and curvature.</li>
                </ul>
            </div>
            <div class="card card-teal">
                <h3>Biomedical Logistics</h3>
                <ul>
                    <li>Handling thin-walled glass vials, filled fluid ampoules, and test tubes.</li>
                    <li>Prevents mechanical shock and brittle fracture during rapid sorting.</li>
                    <li>Conforms gently to anatomical specimens and surgical tools.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>Explosive Ordnance Disposal</h3>
                <ul>
                    <li>Interfacing with uncertain, aged, or structurally compromised munitions.</li>
                    <li>Spark-free polymer construction eliminates electrical discharge.</li>
                    <li>Prevents impact shock that could trigger detonation.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 3</span>
    </div>
</div>

<!-- SLIDE 4: PROBLEM STATEMENT -->
<div class="slide">
    <div class="slide-header">
        <h2>Formal Problem Statement & Key Challenges</h2>
        <p>Bridging the gap between structural compliance, payload capacity, and tactile perception</p>
    </div>
    <div class="slide-content">
        <div style="background-color: #eff6ff; border-left: 6px solid #1e40af; padding: 14px 20px; border-radius: 6px; margin-bottom: 20px;">
            <p style="font-size: 12.5pt; font-style: italic; color: #1e3a8a; margin: 0; line-height: 1.4;">
                "Conventional rigid end-effectors lack the compliance required to manipulate fragile objects without damage, while existing soft grippers suffer from low payload capacity, material hysteresis, tethered fluidic supplies, and an absence of localized feedback capable of detecting incipient slip without bulky optical systems."
            </p>
        </div>
        <div class="grid-2">
            <div class="card card-red">
                <h3>Critical Engineering Bottlenecks</h3>
                <ul>
                    <li>Non-linear hyperelastic material behavior requiring specialized FEA.</li>
                    <li>Viscoelastic relaxation during sustained holding tasks.</li>
                    <li>Planar sensor delamination and peeling on stretching soft skins.</li>
                </ul>
            </div>
            <div class="card card-teal">
                <h3>Proposed Engineering Solution</h3>
                <ul>
                    <li>Monolithic 3D-printed TPU 95A structure featuring circular living hinges.</li>
                    <li>Tendon-driven actuation with remote base-mounted servomotors.</li>
                    <li>Flush-recessed FSR402 tactile sensors + on-chip FFT slip detection.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 4</span>
    </div>
</div>

<!-- SLIDE 5: LITERATURE CORPUS -->
<div class="slide">
    <div class="slide-header">
        <h2>Consolidated Literature Review: Team Synthesis</h2>
        <p>Integration of individual research streams into a unified knowledge base</p>
    </div>
    <div class="slide-content">
        <div class="grid-3">
            <div class="card card-blue">
                <h3>Actuation & Kinematics (Sanchali)</h3>
                <ul>
                    <li>Evaluated pneumatic, tendon, SMA, and DEA architectures.</li>
                    <li>Mobility classification: constrained, underconstrained, deformable.</li>
                    <li>Highlighted payload vs compliance trade-off in fluidic bladders.</li>
                    <li>Base motors reduce distal finger inertia.</li>
                </ul>
            </div>
            <div class="card card-teal">
                <h3>Materials & Fabrication (Chandana)</h3>
                <ul>
                    <li>Evaluated silicones (Ecoflex, PDMS), TPUs, TPEs, and photopolymers.</li>
                    <li>Molding requires multi-step casting, degassing, and curing ovens.</li>
                    <li>Selected FDM 3D printing of TPU as the optimal fabrication route.</li>
                    <li>Eliminates tooling, enables rapid prototyping.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>Tactile Transduction (Saurav)</h3>
                <ul>
                    <li>Surveyed piezoresistive, capacitive, piezoelectric, and optical sensors.</li>
                    <li>Decoupled static contact force from dynamic slip micro-vibrations.</li>
                    <li>FSR402 thin-film piezoresistors provide ideal form factor.</li>
                    <li>Requires active analog filtering & drift mitigation.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 5</span>
    </div>
</div>

<!-- SLIDE 6: COMPARATIVE ANALYSIS -->
<div class="slide">
    <div class="slide-header">
        <h2>Comparative Analysis of Actuation Paradigms</h2>
        <p>Multi-attribute engineering trade-offs governing methodology selection</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="image-box">
                <img src="../Figures and Diagrams/comparative_radar_chart.png" alt="Radar Comparison">
                <div class="caption">Figure: Multi-attribute radar comparison across 6 engineering dimensions.</div>
            </div>
            <div class="card card-blue">
                <h3>Comparative Engineering Takeaways</h3>
                <ul>
                    <li><strong>Pneumatic PneuNets:</strong> Maximum passive conformity, but tethered compressor, bulky valves, and seam rupture risks under pressure.</li>
                    <li><strong>Shape Memory Alloy (SMA):</strong> High energy density, but slow cooling lag (3–15 s), severe thermal hysteresis, and substrate degradation.</li>
                    <li><strong>Dielectric Elastomers (DEAs):</strong> Fast response, but hazardous driving voltages (&gt;1–5 kV) and breakdown risks.</li>
                    <li><strong>Monolithic Tendon TPU (Selected):</strong> High payload ratio (3:1 to 5:1), completely untethered battery operation, rapid FDM printing, and straightforward servomotor PWM control.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 6</span>
    </div>
</div>

<!-- SLIDE 7: RESEARCH GAPS -->
<div class="slide">
    <div class="slide-header">
        <h2>Identified Research Gaps in Published Literature</h2>
        <p>Explicit limitations motivating our proposed methodology</p>
    </div>
    <div class="slide-content">
        <div class="grid-2" style="grid-template-rows: 1fr 1fr;">
            <div class="card card-red">
                <h3>Gap 1: Compliance vs. Payload Capacity</h3>
                <ul>
                    <li>Pure elastomeric bladders buckle under lateral/torsional loads.</li>
                    <li>Payloads typically restricted to &lt;200–400 grams.</li>
                    <li>Need for flexure mechanisms combining compliance with structural load capacity.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>Gap 2: Interfacial Sensor Delamination</h3>
                <ul>
                    <li>Planar sensors bonded to stretching silicone skin experience severe peeling shear.</li>
                    <li>Cyclic bending causes electrical trace rupture and sensor detachment.</li>
                    <li>Need for recessed, strain-isolated sensor pockets on rigid contact pads.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>Gap 3: Bulky Slip Detection Systems</h3>
                <ul>
                    <li>State-of-the-art slip sensing relies on heavy optical cameras (GelSight).</li>
                    <li>Computationally intensive image processing unsuited for mobile arms.</li>
                    <li>Need for lightweight, edge-computed tactile vibration analysis.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>Gap 4: Embedded Edge Control Disconnect</h3>
                <ul>
                    <li>Many research prototypes rely on desktop MATLAB scripts.</li>
                    <li>Lack of deterministic real-time operating systems running on-board.</li>
                    <li>Need for FreeRTOS dual-core embedded control coupled to ROS 2.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 7</span>
    </div>
</div>

<!-- SLIDE 8: OBJECTIVES & SCOPE -->
<div class="slide">
    <div class="slide-header">
        <h2>Project Objectives & Technical Scope</h2>
        <p>Specific measurable targets across mechanical, sensing, and control domains</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="card card-blue">
                <h3>Main & Specific Sub-Objectives</h3>
                <ul>
                    <li><strong>Main:</strong> Establish the design, modeling, fabrication, and control methodology for a compliant gripper.</li>
                    <li><strong>Design Strategy:</strong> Define circular living hinge geometry using Howell PRBM formulations.</li>
                    <li><strong>Material Selection:</strong> Formulate direct-drive FDM printing with flexible TPU 95A filament.</li>
                    <li><strong>Simulation Strategy:</strong> Formulate hyperelastic constitutive modeling for BTP-II simulation.</li>
                    <li><strong>Signal Conditioning:</strong> Design Sallen-Key 2nd-order Butterworth LPF (\(f_c = 20\text{ Hz}\)).</li>
                    <li><strong>Firmware Architecture:</strong> Design dual-core FreeRTOS pipeline (1 kHz FFT / Servo PWM).</li>
                    <li><strong>Validation Plan:</strong> Outline pull-out force benchmarking and autonomous slip prevention.</li>
                </ul>
            </div>
            <div class="card card-teal">
                <h3>Technical Scope & Boundaries</h3>
                <ul>
                    <li><strong>COMPLETED IN STAGE-I:</strong></li>
                    <li>• Multi-thematic literature review & comparative technology evaluation.</li>
                    <li>• Selection of monolithic FDM TPU tendon-driven gripper methodology.</li>
                    <li>• Analytical kinematic formulations (Howell PRBM & Capstan friction).</li>
                    <li>• Embedded signal processing & FreeRTOS architectural design.</li>
                    <li><strong>PLANNED FOR STAGE-II (BTP-II):</strong></li>
                    <li>• SolidWorks 3D CAD modeling & Ansys non-linear hyperelastic FEA.</li>
                    <li>• Physical prototype 3D printing, sensor assembly, & experimental trials.</li>
                    <li><strong>OUT-OF-SCOPE:</strong></li>
                    <li>• High-speed sorting (&gt;3 m/s), multi-axis shear arrays, underwater trials.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 8</span>
    </div>
</div>

<!-- SLIDE 9: SELECTED METHODOLOGY -->
<div class="slide">
    <div class="slide-header">
        <h2>Confirmed Methodology: Monolithic 3D-Printed Tendon Gripper</h2>
        <p>Synthesis of compliant mechanisms, additive manufacturing, and embedded sensing</p>
    </div>
    <div class="slide-content">
        <div class="grid-3">
            <div class="card card-blue">
                <h3>1. Structural Compliance</h3>
                <ul>
                    <li>Monolithic FDM 3D printing with flexible TPU 95A.</li>
                    <li>Replaces discrete mechanical pins with living hinges.</li>
                    <li>Zero joint assembly, zero backlash, zero lubrication.</li>
                    <li>Horizontal build orientation maximizes inter-layer tensile strength.</li>
                </ul>
            </div>
            <div class="card card-teal">
                <h3>2. Tendon Transmission</h3>
                <ul>
                    <li>Remote base-mounted metal-gear digital servomotors (DS3218).</li>
                    <li>Braided Dyneema cable (&gt;30 kg rating) pulling through low-friction guides.</li>
                    <li>Micro-PTFE tubing inserts minimize Capstan friction losses.</li>
                    <li>Passive elastic restoration driven by stored TPU strain energy.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>3. Embedded Intelligence</h3>
                <ul>
                    <li>FSR402 thin-film sensors recessed flush in contact pads.</li>
                    <li>Analog 2nd-order Butterworth filtering for normal force \(F_n\).</li>
                    <li>On-chip 256-point FFT on ESP32 Core 0 for slip vibrations.</li>
                    <li>Closed-loop servomotor torque tightening in &lt;35 milliseconds.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 9</span>
    </div>
</div>

<!-- SLIDE 10: KINEMATICS -->
<div class="slide">
    <div class="slide-header">
        <h2>Kinematic Modeling & Pseudo-Rigid-Body Formulation</h2>
        <p>Analytical modeling of flexure notch living hinges and tendon routing</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="image-box">
                <img src="../Figures and Diagrams/gripper_kinematics_diagram.png" alt="Kinematics Diagram">
                <div class="caption">Figure: Kinematic profile of the monolithic compliant finger under cable tension.</div>
            </div>
            <div class="card card-blue">
                <h3>Compliant Living Hinge Mechanics</h3>
                <ul>
                    <li><strong>Howell Pseudo-Rigid-Body Model (PRBM):</strong> Circular flexure notches modeled as characteristic pivots with torsional stiffness \(K_\theta\):<br>
                    <span style="font-weight: bold; color: #003366;">\(K_\theta = \frac{E \cdot w \cdot t^{2.5}}{9 \pi \sqrt{r}}\)</span></li>
                    <li>Where \(E\) = flexural modulus of TPU 95A, \(w\) = width, \(t\) = throat thickness (1.6 mm), \(r\) = notch radius (2.5 mm).</li>
                    <li><strong>Capstan Tendon Friction Law across joints:</strong><br>
                    <span style="font-weight: bold; color: #003366;">\(T_{\text{distal}} = T_{\text{base}} \cdot e^{-\sum \mu_f \theta_i}\)</span></li>
                    <li>Micro-PTFE sleeves reduce \(\mu_f\) to ~0.08, maximizing force delivery to distal tactile pads.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 10</span>
    </div>
</div>

<!-- SLIDE 11: MATERIAL & SIMULATION STRATEGY -->
<div class="slide">
    <div class="slide-header">
        <h2>Proposed Material Selection & Planned Simulation Strategy</h2>
        <p>Structural selection of TPU 95A and non-linear hyperelastic modeling approach for BTP-II</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="card card-blue">
                <h3>Material Selection: TPU 95A</h3>
                <ul>
                    <li>Evaluated silicones (Ecoflex, PDMS), photopolymers, and polyurethanes.</li>
                    <li>Silicone molding requires multi-part molds, vacuum degassing, and curing ovens.</li>
                    <li>Direct FDM 3D printing of TPU 95A eliminates molds and enables rapid prototyping.</li>
                    <li>Shore 95A provides high flexural resilience while preventing out-of-plane torsional buckling.</li>
                    <li>Monolithic printing enables continuous living hinges without assembly pins or mechanical backlash.</li>
                </ul>
            </div>
            <div class="card card-teal">
                <h3>Planned Hyperelastic FEA Strategy (BTP-II)</h3>
                <ul>
                    <li><strong>Non-linear Mechanics:</strong> TPU undergoes large elastic deformations and strain-stiffening. Hookean linear elasticity is invalid for large flexure bending.</li>
                    <li><strong>Selected Constitutive Law:</strong> 2-Parameter Mooney-Rivlin strain energy formulation:<br>
                    <span style="font-weight: bold; color: #003366;">\(W = C_{10}(I_1 - 3) + C_{01}(I_2 - 3) + \frac{1}{D_1}(J - 1)^2\)</span></li>
                    <li><strong>Planned BTP-II Simulation Goals:</strong></li>
                    <li>• Model finger curl angle versus tendon tension prior to 3D printing.</li>
                    <li>• Evaluate Von Mises stress concentrations at flexure notches to ensure high fatigue life.</li>
                    <li><em>Status: Modeling methodology decided; simulation runs will be performed in BTP-II.</em></li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 11</span>
    </div>
</div>

<!-- SLIDE 12: MECHATRONICS -->
<div class="slide">
    <div class="slide-header">
        <h2>Mechatronic & Embedded Firmware Architecture</h2>
        <p>Hardware-software co-design uniting analog filtering, FreeRTOS, and micro-ROS</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="image-box">
                <img src="../Figures and Diagrams/mechatronics_architecture.png" alt="Mechatronics Architecture">
                <div class="caption">Figure: Integrated mechatronic and FreeRTOS embedded architecture.</div>
            </div>
            <div class="card card-red">
                <h3>Dual-Core FreeRTOS Pipeline</h3>
                <ul>
                    <li><strong>Core 0 (1 kHz DMA Task):</strong>
                        <ul>
                            <li>High-speed 12-bit ADC sampling.</li>
                            <li>2nd-order Butterworth LPF (\(f_c = 20\text{ Hz}\)).</li>
                            <li>256-point Radix-4 FFT spectral calculation.</li>
                            <li>Incipient slip threshold evaluation.</li>
                        </ul>
                    </li>
                    <li><strong>Core 1 (100 Hz Control Task):</strong>
                        <ul>
                            <li>Closed-loop servomotor PWM torque update.</li>
                            <li>Hysteresis compensation lookup.</li>
                            <li>micro-ROS DDS publishing over serial/WiFi.</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 12</span>
    </div>
</div>

<!-- SLIDE 13: SLIP DETECTION -->
<div class="slide">
    <div class="slide-header">
        <h2>Tactile Signal Processing & Autonomous Slip Prevention</h2>
        <p>Real-time frequency-domain FFT vibration spike detection</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="image-box">
                <img src="../Figures and Diagrams/slip_detection_fft_workflow.png" alt="Slip Detection Workflow">
                <div class="caption">Figure: Tactile signal decomposition and FFT slip-detection pipeline.</div>
            </div>
            <div class="card card-teal">
                <h3>Spectral Energy Triggering</h3>
                <ul>
                    <li><strong>Time Domain:</strong> Normal clamping force \(F_n\) resides in low-frequency band (0–20 Hz).</li>
                    <li><strong>Dynamic Friction:</strong> Incipient micro-vibrations generate sharp tactile energy spikes in 100–300 Hz band.</li>
                    <li><strong>On-Chip FFT Metric:</strong><br>
                    <span style="font-weight: bold; color: #003366;">\(E_{\text{slip}} = \sum_{k=25}^{76} |X[k]|^2\)</span></li>
                    <li><strong>Autonomous Compensation:</strong> When \(E_{\text{slip}}\) exceeds dynamic baseline threshold, ESP32 commands immediate servomotor torque boost in &lt;35 ms, arresting slip.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 13</span>
    </div>
</div>

<!-- SLIDE 14: CURRENT STATUS -->
<div class="slide">
    <div class="slide-header">
        <h2>Current Progress & Project Status (BTP-I Baseline)</h2>
        <p>Clear differentiation between completed conceptual decisions and proposed BTP-II execution</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="card card-teal">
                <h3>Work Completed in Stage-I</h3>
                <ul>
                    <li>• <strong>Literature Review:</strong> Comprehensive synthesis of actuation, materials, and tactile sensing.</li>
                    <li>• <strong>Methodology Decision:</strong> Multi-criteria selection of Monolithic FDM TPU Tendon Gripper.</li>
                    <li>• <strong>Conceptual Design:</strong> Selected circular living hinge architecture and Dyneema routing.</li>
                    <li>• <strong>Theoretical Kinematics:</strong> Howell PRBM living hinge stiffness & Capstan friction equations.</li>
                    <li>• <strong>Signal Architecture:</strong> Sallen-Key Butterworth filter & dual-core FreeRTOS pipeline.</li>
                    <li>• <strong>Implementation Plan:</strong> Structured 16-week execution roadmap for BTP-II.</li>
                </ul>
            </div>
            <div class="card card-blue">
                <h3>Status Clarification: Decisions & Planning</h3>
                <ul>
                    <li><strong>IMPORTANT ACADEMIC CLARIFICATION:</strong></li>
                    <li><em style="font-size: 11pt; color: #003366; font-weight: bold;">"We have only decided what we will do."</em></li>
                    <li>• In strict compliance with academic standards, no SolidWorks CAD models were constructed in Stage-I.</li>
                    <li>• No Ansys FEA simulations were executed in Stage-I.</li>
                    <li>• No physical prototypes were 3D printed or experimentally tested in Stage-I.</li>
                    <li>• All 3D CAD modeling, FEA simulation, fabrication, sensor wiring, and experimental trials are scheduled for Stage-II (BTP-II).</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 14</span>
    </div>
</div>

<!-- SLIDE 15: CHALLENGES -->
<div class="slide">
    <div class="slide-header">
        <h2>Anticipated Engineering Challenges & Mitigations</h2>
        <p>Risk mitigation strategy formulated for next-semester manufacturing & testing</p>
    </div>
    <div class="slide-content">
        <div class="grid-2" style="grid-template-rows: 1fr 1fr;">
            <div class="card card-red">
                <h3>TPU Extrusion Jamming</h3>
                <ul>
                    <li><strong>Cause:</strong> Flexible filament buckling in direct-drive gear under backpressure.</li>
                    <li><strong>Mitigation:</strong> Use direct-drive extruder with constrained path; print at 20 mm/s; disable retraction.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>Inter-Layer Shear Cleavage</h3>
                <ul>
                    <li><strong>Cause:</strong> Anisotropic Z-axis weakness during high flexural bending.</li>
                    <li><strong>Mitigation:</strong> Print fingers flat horizontally; set nozzle to 225°C to achieve 100% polymer weld.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>Tendon Friction Hysteresis</h3>
                <ul>
                    <li><strong>Cause:</strong> Dyneema cable abrading 3D-printed layer ridges in channels.</li>
                    <li><strong>Mitigation:</strong> Insert micro-PTFE tubing (OD 2 mm, ID 1 mm) along internal cable channels.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>FSR Sensor Resistance Drift</h3>
                <ul>
                    <li><strong>Cause:</strong> Conductive polymer relaxation under continuous load.</li>
                    <li><strong>Mitigation:</strong> Firmware implements dynamic AC baseline tracking, decoupling static and AC slip signals.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 15</span>
    </div>
</div>

<!-- SLIDE 16: ROADMAP -->
<div class="slide">
    <div class="slide-header">
        <h2>BTP-II Semester-Wise Implementation Roadmap</h2>
        <p>16-week timeline, task breakdown, and technical milestones</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="image-box">
                <img src="../Figures and Diagrams/gantt_chart_btp2.png" alt="Gantt Chart">
                <div class="caption">Figure: BTP-II 16-week implementation Gantt chart.</div>
            </div>
            <div class="card card-blue">
                <h3>16-Week Deliverables Schedule</h3>
                <ul>
                    <li><strong>W1–W3:</strong> Detailed CAD modeling (.STEP assembly & 2D drawings).</li>
                    <li><strong>W4–W6:</strong> Ansys hyperelastic FEA (simulation dataset & report).</li>
                    <li><strong>W7–W8:</strong> FDM TPU 3D printing & Dyneema rigging (hardware prototype).</li>
                    <li><strong>W9–W11:</strong> Analog sensor PCB & ESP32 FreeRTOS firmware.</li>
                    <li><strong>W12–W14:</strong> Static calibration & pull-out force trials.</li>
                    <li><strong>W15–W16:</strong> Live slip-prevention demonstration & defense.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 16</span>
    </div>
</div>

<!-- SLIDE 17: OUTCOMES -->
<div class="slide">
    <div class="slide-header">
        <h2>Expected Outcomes & Final Demonstration (BTP-II)</h2>
        <p>Tangible engineering deliverables to be presented to the evaluation committee</p>
    </div>
    <div class="slide-content">
        <div class="grid-3">
            <div class="card card-blue">
                <h3>1. Autonomous Grasping</h3>
                <ul>
                    <li>Conforming gently to diverse shapes: spheres, cylinders, fragile eggs, soft fruits.</li>
                    <li>Zero crushing damage on fragile surfaces.</li>
                    <li>Payload capacity of 800–1500 g on a gripper self-weight of &lt;450 g (Payload ratio &gt;2:1).</li>
                </ul>
            </div>
            <div class="card card-teal">
                <h3>2. Real-Time Telemetry</h3>
                <ul>
                    <li>Live graphical dashboard streaming contact force and FFT spectral density.</li>
                    <li>Integrated micro-ROS client publishing to ROS 2 on host workstation.</li>
                    <li>Deterministic multi-tasking executing on ESP32 dual cores.</li>
                </ul>
            </div>
            <div class="card card-red">
                <h3>3. Slip Prevention Demo</h3>
                <ul>
                    <li>Live physical test: external dislodging tension applied to a grasped object.</li>
                    <li>On-chip FFT detects tactile micro-vibrations in 100–300 Hz band.</li>
                    <li>Servomotors automatically tighten grip within &lt;35 ms, arresting slip before drop.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 17</span>
    </div>
</div>

<!-- SLIDE 18: CONCLUSION & REFS -->
<div class="slide">
    <div class="slide-header">
        <h2>Conclusion & Key References</h2>
        <p>Summary of Stage-I accomplishments and primary citations</p>
    </div>
    <div class="slide-content">
        <div class="grid-2">
            <div class="card card-teal">
                <h3>Conclusions</h3>
                <ul>
                    <li>Stage-I establishes a complete, technically sound research direction combining compliant mechanics, additive manufacturing, tactile perception, and real-time edge control.</li>
                    <li>Monolithic FDM TPU printing eliminates mold delays and chemical hazards of silicone casting.</li>
                    <li>Tendon-driven base servomotors optimize payload-to-weight ratio while maintaining safe contact compliance.</li>
                    <li>The integrated FreeRTOS / FFT slip detection framework provides deterministic autonomy without bulky optical cameras.</li>
                    <li>The 16-week BTP-II roadmap establishes measurable milestones leading to a validated physical prototype.</li>
                </ul>
            </div>
            <div class="card card-blue">
                <h3>Key Verifiable References</h3>
                <ul>
                    <li>[1] Whitesides, G. M. (2018). Soft Robotics. Angew. Chem.</li>
                    <li>[2] Rus, D., & Tolley, M. T. (2015). Design of Soft Robots. Nature.</li>
                    <li>[3] Shintake, J., et al. (2018). Soft Grippers. Adv. Mater.</li>
                    <li>[4] Hughes, J., et al. (2016). Soft Manipulators. Front. Robot. AI.</li>
                    <li>[5] Dahiya, R. S., et al. (2010). Tactile Sensing. IEEE T-RO.</li>
                    <li>[6] Howell, L. L. (2001). Compliant Mechanisms. Wiley.</li>
                    <li>[7] Mooney, M. (1940). Theory of Large Elastic Deformation. J. Appl. Phys.</li>
                    <li>[8] Student Literature Reviews: Sanchali (2026), Saurav (2026), Chandana (2026), Joint Report (2026), Dept. Mech. Eng., IIT Kharagpur.</li>
                </ul>
            </div>
        </div>
    </div>
    <div class="slide-footer">
        <span>Department of Mechanical Engineering, IIT Kharagpur</span>
        <span>Slide 18</span>
    </div>
</div>

</body>
</html>
"""

html_path = os.path.abspath("Presentation/slides.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_slides)
print(f"Wrote {html_path}")

pdf_path = os.path.abspath("Presentation/BTP_Presentation_Soft_Robotic_Gripper.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1920, "height": 1080})
    page.goto("file:///" + html_path.replace("\\", "/"))
    page.wait_for_timeout(2000)
    page.pdf(
        path=pdf_path,
        width="297mm",
        height="167mm",
        print_background=True,
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"}
    )
    browser.close()

print(f"Generated {pdf_path} successfully via Playwright Chromium.")

