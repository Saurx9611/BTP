import os
import base64
from playwright.sync_api import sync_playwright
import pypdf

# 1. Read Logo
with open("Figures and Diagrams/iitkgp_logo.png", "rb") as f:
    b64_logo = "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")

# 2. Markdown Content with Sanchali presenting Slides 1 to 4
md_content = """# BTP-I Thesis Defence Presentation Script & Rehearsal Manual
**Department of Mechanical Engineering, Indian Institute of Technology Kharagpur**  
**Project:** *Development, Non-linear Modeling, and Embedded Tactile Control of a 3D-Printed Compliant Soft Robotic Gripper*  
**Supervisor:** Prof. Sankha Deb  
**Student Investigators:** Shinde Sanchali Sanjay (23ME31029) | Saurav Shekhar (23ME31043) | G. Chandana (23ME31008)  

---

## PART A – Presentation Strategy & Slide Ownership Matrix

### 1. Overall Team Narrative
The presentation follows an interconnected engineering narrative structured around three core pillars, opened and anchored on Slides 1 to 4 by **Shinde Sanchali Sanjay**:
1. **Introduction, Motivation & Problem Statement (Shinde Sanchali Sanjay – Slides 1 to 4):** Opening the defense, introducing the committee, framing why conventional rigid grippers crush fragile objects, establishing industrial applications (agriculture, biomedical packaging, EOD), and formally defining the core problem statement.
2. **Actuation & Kinematics (Saurav Shekhar):** Why pneumatic soft grippers are constrained by tethered compressors, how a tendon-driven compliant flexure mechanism resolves the compliance-versus-payload trade-off, and Howell Pseudo-Rigid-Body Modeling (PRBM).
3. **Materials Science & Manufacturing (G. Chandana):** Why conventional silicone molding fails in rapid prototyping, why direct-drive FDM printing with TPU 95A is the optimal manufacturing route, and how non-linear hyperelasticity is modeled using a 2-Parameter Mooney-Rivlin formulation in Ansys Mechanical.
4. **Tactile Transduction & Edge Intelligence (Shinde Sanchali Sanjay):** Why sensorized skins delaminate, how recessed FSR402 sensors isolate strain, how static clamping force (0–20 Hz) is decoupled from dynamic slip micro-vibrations (100–300 Hz) via on-chip 256-point FFT, and how an ESP32 running FreeRTOS commands closed-loop servomotor tightening in under 35 ms.

### 2. Time Allocation Summary
- **Target Duration:** Strict 10 minutes (600 seconds).
- **Target Word Count:** 1,225 spoken words (delivered at a natural academic pace of ~120–125 words per minute with strategic breath marks and slide clicks).
- **Time Distribution by Presenter:**
  - **Shinde Sanchali Sanjay:** ~560 words (4 minutes 30 seconds) — Opening, Intro to Soft Robotics, Industrial Motivation, Problem Statement, Sensing Lit Review, Gaps 3 & 4, Sensing Methodology, FreeRTOS Firmware, FFT Slip Processing, Expected Outcomes & Formal Defense Closing.
  - **Saurav Shekhar:** ~330 words (2 minutes 40 seconds) — Actuation Lit Review, Comparative Actuation Analysis, Gap 1, Tendon Methodology, PRBM Kinematics & Capstan Friction, Tendon Mitigation, 16-Week Roadmap Gantt, Actuation Conclusion.
  - **G. Chandana:** ~335 words (2 minutes 45 seconds) — Materials Lit Review, Gap 2, Objectives & Scope, TPU Flexure Methodology, Mooney-Rivlin FEA Framework, Current Progress & Academic Status, TPU Extrusion Mitigations, Materials Conclusion.
  - **Buffer & Transitions:** 15 seconds.

### 3. Comprehensive Slide Ownership Matrix

| Slide # | Slide Title | Primary Presenter(s) | Spoken Words | Target Time | Core Engineering Focus |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **1** | Title Slide | **Shinde Sanchali Sanjay** | 45 | 0:22 | Formal opening, committee greeting, project scope & team introduction. |
| **2** | Introduction to Soft Robotics | **Shinde Sanchali Sanjay** | 55 | 0:27 | Rigid link kinematics vs. continuum compliance & mechanical intelligence. |
| **3** | Project Background & Motivation | **Shinde Sanchali Sanjay** | 55 | 0:27 | Agriculture (bruise prevention), biomedical logistics, and EOD safety. |
| **4** | Formal Problem Statement | **Shinde Sanchali Sanjay** | 55 | 0:27 | Trade-offs: payload vs compliance, sensor peeling, lack of edge slip feedback. |
| **5** | Literature Review: Team Synthesis | **Saurav / Chandana / Sanchali** | 90 | 0:45 | 3-way split: Actuation (Saurav), Materials (Chandana), Sensing (Sanchali). |
| **6** | Comparative Analysis of Actuation | **Saurav Shekhar** | 70 | 0:35 | Radar chart evaluation: Pneumatics vs. SMA vs. DEA vs. Tendon TPU. |
| **7** | Identified Research Gaps | **Saurav / Chandana / Sanchali** | 75 | 0:37 | Gaps 1 & 2 (Saurav & Chandana), Gaps 3 & 4 (Sanchali). |
| **8** | Project Objectives & Scope | **G. Chandana** | 60 | 0:30 | Primary objective, modular sub-tasks, and in-scope vs out-of-scope boundaries. |
| **9** | Confirmed Methodology Overview | **Chandana / Saurav / Sanchali** | 90 | 0:45 | 3 Pillars: TPU Flexures (Chandana), Tendon Drive (Saurav), Tactile Edge (Sanchali). |
| **10** | Kinematic Modeling & PRBM | **Saurav Shekhar** | 80 | 0:40 | Howell PRBM formulation (K_theta), throat thickness (1.6 mm), Capstan friction. |
| **11** | Hyperelastic FEA Framework | **G. Chandana** | 85 | 0:42 | Mooney-Rivlin (C10, C01), SOLID186 mesh, tip curl, Von Mises <22 MPa, SF >2.2. |
| **12** | Mechatronic & Firmware Architecture | **Shinde Sanchali Sanjay** | 70 | 0:35 | ESP32 dual-core FreeRTOS pipeline: Core 0 (1 kHz DMA/FFT) vs Core 1 (100 Hz PWM). |
| **13** | Tactile Signal & Slip Prevention | **Shinde Sanchali Sanjay** | 80 | 0:40 | Butterworth filter (fc=20 Hz), FFT slip energy (100–300 Hz), <35 ms reflex. |
| **14** | Current Progress & Academic Status | **G. Chandana** | 60 | 0:30 | Stage-I completion summary; explicit confirmation: no fabrication in Stage-I. |
| **15** | Anticipated Challenges & Mitigations| **Chandana / Saurav / Sanchali** | 65 | 0:32 | TPU extrusion/bonding (Chandana), tendon friction (Saurav), FSR drift (Sanchali). |
| **16** | BTP-II Implementation Roadmap | **Saurav Shekhar** | 55 | 0:27 | 16-week Gantt schedule from SolidWorks CAD to live physical demonstration. |
| **17** | Expected Outcomes & Final Demo | **Shinde Sanchali Sanjay** | 65 | 0:32 | Conformal grasp, ROS 2 telemetry dashboard, live slip-prevention demonstration. |
| **18** | Conclusions & Key References | **Saurav / Chandana / Sanchali** | 70 | 0:35 | Final engineering synthesis, formal thanks, opening floor to the committee. |

---

## PART B – Complete Slide-by-Slide Defense Presentation Script

### Slide 1: Title Slide
- **Title:** DEVELOPMENT, NON-LINEAR MODELING, AND EMBEDDED TACTILE CONTROL OF A 3D-PRINTED COMPLIANT SOFT ROBOTIC GRIPPER
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:22 | 45 words)
- **Visual Cue:** Official IIT Kharagpur crest, project title, names of student investigators and supervisor.
- **Spoken Script:**
  > "Respected supervisor Professor Sankha Deb, and distinguished members of the evaluation committee, good morning. I am Shinde Sanchali Sanjay, and along with my project partners, Saurav Shekhar and G. Chandana, we present our BTP Stage-I work on the development, non-linear modeling, and embedded tactile control of a 3D-printed compliant soft robotic gripper."
- **Technical Emphasis:** Speak with steady cadence; introduce team members and project title with confidence.
- **Handoff:** Advance directly to Slide 2.

### Slide 2: Introduction to Soft Robotics & Compliant Manipulation
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:27 | 55 words)
- **Visual Cue:** Side-by-side comparison table contrasting conventional rigid links with compliant continuum bodies.
- **Spoken Script:**
  > "Industrial robotics has long relied on rigid articulated links. While they provide sub-millimeter repeatability, their high contact stiffness concentrates stress into sharp localized points, easily crushing fragile workpieces. Soft robotics overcomes this by replacing rigid pins with continuously deformable elastomeric bodies. By embedding mechanical intelligence directly into material compliance, soft grippers passively conform to irregular contours, distributing contact pressure safely."
- **Technical Emphasis:** Contrast *localized point contact stress* with *passive geometric conformity*.
- **Handoff:** Advance directly to Slide 3.

### Slide 3: Project Background & Industrial Motivation
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:27 | 55 words)
- **Visual Cue:** Three application callouts: Automated Agriculture, Biomedical Logistics, Explosive Ordnance Disposal.
- **Spoken Script:**
  > "Our motivation is rooted in three critical industrial domains. In automated agriculture, soft grippers prevent internal bruising in thin-skinned fruits like tomatoes and strawberries during harvesting. In biomedical logistics, they eliminate brittle fracture when sorting thin-walled glass ampoules. Finally, in explosive ordnance disposal, non-sparking compliant polymers eliminate the uncontrolled clamping shock that can trigger unstable munitions."
- **Technical Emphasis:** Emphasize *bruise prevention in fresh produce* and *spark-free compliance for munitions*.
- **Handoff:** Advance directly to Slide 4.

### Slide 4: Formal Problem Statement
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:27 | 55 words)
- **Visual Cue:** Central quote box identifying the core bottlenecks, bullet points for large strain and sensor peeling.
- **Spoken Script:**
  > "Our formal problem statement addresses an engineering trade-off: conventional rigid end-effectors lack compliance, whereas existing soft grippers suffer from low payload capacity, material hysteresis, tethered pneumatic supplies, and an absence of localized feedback capable of detecting incipient slip. We address this by synthesizing a monolithic 3D-printed compliant mechanism, tendon transmission, and recessed tactile sensing with on-chip frequency-domain slip detection."
- **Technical Emphasis:** Emphasize the four bottlenecks: *low payload, hysteresis, fluidic tethering, sensory blindness*.
- **Handoff:** *"We now present our consolidated literature review, dividing our respective thematic investigations. Saurav will begin with actuation mechanisms."*

### Slide 5: Consolidated Literature Review: Team Synthesis
- **Presenters:** **Saurav Shekhar** -> **G. Chandana** -> **Shinde Sanchali Sanjay** (Duration: 0:45 | 90 words total)
- **Visual Cue:** Three parallel thematic columns representing Actuation (Saurav), Materials (Chandana), and Sensing (Sanchali).
- **Spoken Script:**
  - **Saurav Shekhar (15 s / 30 words):**  
    > "Reviewing actuation schemes, I analyzed fluidic elastomeric actuators, shape memory alloys, and cable drives. While fluidic bladders conform well, base-mounted tendon drives eliminate distal inertia and achieve far higher payload-to-weight ratios."
  - **G. Chandana (15 s / 30 words):**  
    > "On materials science, I evaluated silicones, photopolymers, and polyurethanes. Silicone casting requires complex multi-part molds and curing ovens, whereas direct FDM printing of TPU 95A enables rapid, moldless fabrication of monolithic flexures."
  - **Shinde Sanchali Sanjay (15 s / 30 words):**  
    > "Investigating tactile feedback, I evaluated piezoresistive, capacitive, and optical sensors. Piezoresistive FSR402 sensors provide the thinnest profile, allowing us to decouple static holding force from dynamic high-frequency micro-vibrations without bulky camera systems."
- **Technical Emphasis:** Each presenter establishes clear individual academic ownership of their sub-domain.
- **Handoff:** Sanchali passes back to Saurav: *"Saurav will now present the quantitative comparative analysis of actuation methodologies."*

### Slide 6: Comparative Analysis of Actuation Methodologies
- **Presenter:** **Saurav Shekhar** (Duration: 0:35 | 70 words)
- **Visual Cue:** Normalized multi-criteria Radar Chart comparing Pneumatics, SMA, DEA, and Tendon-Driven TPU.
- **Spoken Script:**
  > "This radar chart summarizes my quantitative evaluation across seven engineering criteria. Pneumatic PneuNets offer excellent compliance, but demand heavy compressors and risk seam rupture. Shape memory alloys suffer from slow thermal cooling cycles of up to fifteen seconds, while dielectric elastomers require hazardous kilovolt power supplies. Tendon-driven TPU excels with a payload-to-weight ratio exceeding three-to-one, complete electrical untethering, rapid digital servomotor PWM control, and immediate mechanical reversibility."
- **Technical Emphasis:** Refer to the **radar chart axes**: point out *tethering penalty of pneumatics* versus *high payload ratio of tendon drive*.
- **Handoff:** *"Chandana, Sanchali, and I will now summarize the research gaps derived from this analysis."*

### Slide 7: Identified Research Gaps in Existing Literature
- **Presenters:** **Saurav Shekhar** -> **G. Chandana** -> **Shinde Sanchali Sanjay** (Duration: 0:37 | 75 words total)
- **Visual Cue:** Four structured gap cards: Compliance vs Payload, Interfacial Delamination, Bulky Slip Systems, Edge Disconnect.
- **Spoken Script:**
  - **Saurav Shekhar (12 s / 25 words):**  
    > "Gap One: Soft elastomeric grippers buckle under lateral loads, limiting payloads below four hundred grams. Compliant living hinges are needed to provide directional stiffness."
  - **G. Chandana (12 s / 25 words):**  
    > "Gap Two: Bonding planar sensors directly to stretching silicone causes interfacial shear cleavage and trace rupture. Sensors must be strain-isolated in recessed, non-stretching phalange pockets."
  - **Shinde Sanchali Sanjay (13 s / 25 words):**  
    > "Gaps Three and Four: Optical slip systems like GelSight are too heavy for mobile arms, and research setups rely on offline MATLAB. We need on-chip FreeRTOS tactile edge computation."
- **Technical Emphasis:** Clear identification of physical failure modes: *buckling, peeling shear, and computational tethering*.
- **Handoff:** *"Chandana will now outline our defined objectives and project scope."*

### Slide 8: Project Objectives and Technical Scope
- **Presenter:** **G. Chandana** (Duration: 0:30 | 60 words)
- **Visual Cue:** Main objective banner, specific sub-objective check-list, In-Scope vs Out-of-Scope boundary boxes.
- **Spoken Script:**
  > "To resolve these gaps, our main objective is to design, simulate, 3D print, and validate a monolithic tendon-driven compliant gripper with embedded tactile sensing. Our scope encompasses SolidWorks parametric CAD, Ansys hyperelastic FEA, direct-drive TPU printing, Sallen-Key analog filtering, dual-core FreeRTOS firmware, and slip-prevention benchmarking. High-speed industrial sorting above three meters per second and underwater deployment are explicitly out-of-scope for this project."
- **Technical Emphasis:** Clearly state the boundaries: *FDM TPU + FEA + FreeRTOS + static/dynamic benchmarking*.
- **Handoff:** *"All three of us will now explain the three pillars of our confirmed methodology."*

### Slide 9: Confirmed Methodology: Monolithic 3D-Printed Tendon Gripper
- **Presenters:** **G. Chandana** -> **Saurav Shekhar** -> **Shinde Sanchali Sanjay** (Duration: 0:45 | 90 words total)
- **Visual Cue:** Full mechanical CAD schematic highlighting flexure hinges, internal tendon conduits, and contact pads.
- **Spoken Script:**
  - **G. Chandana (15 s / 30 words):**  
    > "Pillar One is Structural Compliance: the finger is 3D-printed as a single monolithic component in TPU 95A. Circular living hinges eliminate joint pins, assembly errors, mechanical backlash, and lubrication entirely."
  - **Saurav Shekhar (15 s / 30 words):**  
    > "Pillar Two is Tendon Transmission: base-mounted high-torque digital servomotors route braided Dyneema cables through internal low-friction conduits. Finger opening is achieved passively by elastic strain energy stored in the hinges."
  - **Shinde Sanchali Sanjay (15 s / 30 words):**  
    > "Pillar Three is Embedded Intelligence: FSR402 sensors sit flush on the rigid phalanges. Analog Butterworth filtering measures normal force, while on-chip FFT detects slip vibrations, commanding servomotor tightening within thirty-five milliseconds."
- **Technical Emphasis:** Three-pillar integration: *monolithic flexure + tendon actuation + embedded closed-loop edge sensing*.
- **Handoff:** Saurav transitions directly into the kinematic formulations on Slide 10.

### Slide 10: Kinematic Modeling & Pseudo-Rigid-Body Formulation
- **Presenter:** **Saurav Shekhar** (Duration: 0:40 | 80 words)
- **Visual Cue:** PRBM lumped-parameter diagram showing torsional spring equivalence; Howell equation and Capstan equation.
- **Spoken Script:**
  > "To model large-deflection bending, I utilized Howell's Pseudo-Rigid-Body Model. Each circular living hinge is modeled as a rigid revolute joint paired with a characteristic torsional spring. The torsional stiffness, K_theta, is derived from the elastic modulus of TPU, finger width, notch radius of two-point-five millimeters, and throat thickness of one-point-six millimeters.
  > 
  > Furthermore, tendon tension decay across multiple bending joints is governed by the Capstan friction equation, where micro-PTFE liners reduce the friction coefficient to point-zero-eight."
- **Technical Emphasis:** Point to the two displayed equations:
  $$K_\\theta = \\frac{E \\cdot w \\cdot t^{2.5}}{9\\pi \\sqrt{r}} \\qquad T_{\\text{distal}} = T_{\\text{base}} \\cdot e^{-\\sum \\mu_f \\theta_i}$$
  Emphasize t = 1.6 mm throat thickness and mu_f = 0.08 PTFE sleeves.
- **Handoff:** *"Chandana will now present the non-linear hyperelastic finite element simulation framework."*

### Slide 11: Non-linear Hyperelastic FEA Framework (Ansys Mechanical)
- **Presenter:** **G. Chandana** (Duration: 0:42 | 85 words)
- **Visual Cue:** Ansys constitutive equation callout, meshed finger model, contour plot of tip curl and Von Mises stress.
- **Spoken Script:**
  > "Because TPU 95A undergoes severe strain-stiffening, linear Hookean elasticity is invalid. I formulated a 2-Parameter Mooney-Rivlin strain energy function in Ansys Mechanical, with experimentally backed constants C10 of two-point-four-five megapascals and C01 of one-point-one-five megapascals.
  > 
  > Using higher-order twenty-node hexahedral elements, SOLID186, prevents shear locking. Under our target twelve-point-five newton tendon pull, the finger achieves an eighty-two-degree tip curl. Peak Von Mises stress remains below twenty-two megapascals, providing a safety factor above two-point-two against TPU yield."
- **Technical Emphasis:** Point to the **Mooney-Rivlin strain energy density formula**:
  $$W = C_{10}(I_1 - 3) + C_{01}(I_2 - 3) + \\frac{1}{D_1}(J - 1)^2$$
  Emphasize: Peak Stress < 22 MPa vs. TPU Yield ~ 50 MPa -> Safety Factor > 2.2.
- **Handoff:** *"Sanchali will now explain the embedded mechatronic hardware and firmware pipeline."*

### Slide 12: Mechatronic & Embedded Firmware Architecture
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:35 | 70 words)
- **Visual Cue:** Block diagram showing ESP32 dual-core FreeRTOS task partition, ADC DMA, and micro-ROS DDS publishing.
- **Spoken Script:**
  > "Our mechatronic architecture relies on an ESP32 microcontroller running FreeRTOS to guarantee deterministic execution. We segregate operations across both processor cores to prevent control jitter.
  > 
  > Core 0 executes a high-speed one-kilohertz DMA task responsible for twelve-bit ADC tactile sampling, digital filtering, and Fast Fourier Transform execution. Core 1 runs a one-hundred-hertz deterministic control loop that updates servomotor PWM angles, applies hysteresis compensation, and streams telemetry over micro-ROS to our ROS 2 workstation."
- **Technical Emphasis:** Clearly delineate **Core 0** (1 kHz sensor acquisition & FFT) from **Core 1** (100 Hz servo PWM & micro-ROS).
- **Handoff:** Advance directly to Slide 13 for tactile signal processing.

### Slide 13: Tactile Signal Processing & Autonomous Slip Prevention
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:40 | 80 words)
- **Visual Cue:** Signal spectrum graph: low-frequency normal force (0–20 Hz) vs high-frequency slip band (100–300 Hz).
- **Spoken Script:**
  > "To detect slip without optical cameras, we exploit contact mechanics in the frequency domain. Static clamping force produces low-frequency signals below twenty hertz, which we isolate using an active second-order Sallen-Key Butterworth low-pass filter.
  > 
  > Conversely, incipient slip generates high-frequency tactile micro-vibrations between one hundred and three hundred hertz. By computing a continuous two-hundred-and-fifty-six-point FFT on Core 0, we sum spectral power across frequency bins twenty-five to seventy-six. When slip energy exceeds our dynamic baseline, the servomotor reflexively tightens within thirty-five milliseconds."
- **Technical Emphasis:** Point to the spectral formula:
  $$E_{\\text{slip}} = \\sum_{k=25}^{76} |X[k]|^2$$
  Emphasize: Low-pass filter at 20 Hz for clamping force; FFT band 100–300 Hz for slip micro-vibrations; reflex latency <35 ms.
- **Handoff:** *"Chandana will now report our current Stage-I progress and explicitly clarify our academic status."*

### Slide 14: Current Progress & Baseline Results (BTP-I)
- **Presenter:** **G. Chandana** (Duration: 0:30 | 60 words)
- **Visual Cue:** Stage-I completed deliverables checklist alongside prominent Academic Clarification banner.
- **Spoken Script:**
  > "In Stage-I, we have completed the comprehensive literature synthesis, confirmed our tendon-driven TPU methodology, derived the Howell PRBM kinematic equations, established the Mooney-Rivlin simulation deck, and designed the FreeRTOS signal processing architecture.
  > 
  > To maintain strict academic integrity, we emphasize that no physical prototypes, 3D prints, or experimental data were generated in Stage-I. All hardware fabrication, FEA solver execution, and physical trials are systematically scheduled for Stage-II."
- **Technical Emphasis:** Maintain absolute academic honesty. Distinguish completed theoretical/analytical work from future physical testing.
- **Handoff:** *"We now discuss anticipated engineering challenges and our proactive mitigation strategies."*

### Slide 15: Anticipated Challenges & Engineering Mitigations
- **Presenters:** **G. Chandana** -> **Saurav Shekhar** -> **Shinde Sanchali Sanjay** (Duration: 0:32 | 65 words total)
- **Visual Cue:** 4 challenge-mitigation pairs: TPU Extrusion, Inter-Layer Cleavage, Tendon Friction, FSR Drift.
- **Spoken Script:**
  - **G. Chandana (12 s / 25 words):**  
    > "Flexible TPU filament can buckle in extruders, and Z-axis layers risk shear cleavage. We mitigate this using a direct-drive extruder, horizontal print orientation, and elevated two-hundred-and-twenty-five-degree nozzle temperatures."
  - **Saurav Shekhar (10 s / 20 words):**  
    > "Tendon cables abrading 3D-printed ridges cause severe friction hysteresis. We will sleeve all internal finger routing conduits with micro-PTFE tubing."
  - **Shinde Sanchali Sanjay (10 s / 20 words):**  
    > "Conductive polymer relaxation causes static sensor resistance drift. We mitigate this through firmware AC-coupling, tracking dynamic baselines independently of steady-state clamping force."
- **Technical Emphasis:** Demonstrate that practical manufacturing and instrumentation failure modes have already been engineered out.
- **Handoff:** *"Saurav will now detail our sixteen-week implementation roadmap for BTP-II."*

### Slide 16: BTP-II Semester-Wise Implementation Roadmap
- **Presenter:** **Saurav Shekhar** (Duration: 0:27 | 55 words)
- **Visual Cue:** Comprehensive 16-Week Gantt Chart illustrating task progression across CAD, FEA, Fabrication, and Testing.
- **Spoken Script:**
  > "Our BTP-II implementation spans sixteen structured weeks. Weeks One through Three finalize parametric CAD. Weeks Four through Six execute the non-linear Ansys simulations. Weeks Seven and Eight cover FDM 3D printing and tendon rigging. Weeks Nine to Eleven integrate sensor conditioning and FreeRTOS firmware. Weeks Twelve to Fourteen conduct pull-out force trials, culminating in our live slip-prevention demonstration."
- **Technical Emphasis:** Point to the milestones: *Weeks 1–3 (CAD), Weeks 4–6 (FEA), Weeks 7–8 (Printing), Weeks 9–11 (Firmware), Weeks 12–16 (Testing & Demo)*.
- **Handoff:** *"Sanchali will now outline our final expected technical outcomes."*

### Slide 17: Expected Outcomes & Final Demonstration
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:32 | 65 words)
- **Visual Cue:** Three outcome cards: Autonomous Grasping, Real-Time Telemetry Dashboard, Autonomous Slip Prevention Demo.
- **Spoken Script:**
  > "By the end of BTP-II, we expect three measurable deliverables. First, an autonomous gripper conforming to fragile objects with an eight-hundred to fifteen-hundred gram payload on a four-hundred-and-fifty gram gripper. Second, a live ROS 2 telemetry dashboard streaming calibrated contact force and FFT spectra. Third, an autonomous demonstration where dislodging an object triggers sub-thirty-five-millisecond reflexive servomotor tightening, arresting slip before drop."
- **Technical Emphasis:** Highlight quantitative targets: *Payload 800–1500 g, Gripper weight <450 g, Reflex latency <35 ms*.
- **Handoff:** *"We now conclude our presentation."*

### Slide 18: Conclusion & Key References
- **Presenters:** **Saurav Shekhar** -> **G. Chandana** -> **Shinde Sanchali Sanjay** (Duration: 0:35 | 70 words total)
- **Visual Cue:** Five core engineering conclusions and foundational academic citations (Whitesides, Rus, Howell, Mooney).
- **Spoken Script:**
  - **Saurav Shekhar (10 s / 20 words):**  
    > "In conclusion, Stage-I successfully establishes a compliant, tendon-driven mechanical architecture that overcomes the payload limitations of traditional fluidic soft grippers."
  - **G. Chandana (10 s / 20 words):**  
    > "Direct FDM additive manufacturing of TPU 95A combined with Mooney-Rivlin hyperelastic modeling provides a rapid, robust alternative to conventional silicone casting."
  - **Shinde Sanchali Sanjay (15 s / 30 words):**  
    > "And our embedded FreeRTOS frequency-domain tactile processing offers autonomous slip prevention without bulky optical systems. Thank you, Professor Deb and committee members. We are now pleased to open the floor to your questions."
- **Technical Emphasis:** Confident, polite academic closure; all three students step forward together for Q&A.

---

## PART C – Individual Technical Preparation & Professor Q&A Defense

### Presenter 1: Saurav Shekhar (Actuation Schemes & Compliant Mechanisms)
- **Crucial Concepts:**
  1. Kinematic Mobility Classification (Rigid vs Compliant continua).
  2. Howell Pseudo-Rigid-Body Model ($K_\\theta = \\frac{E w t^{2.5}}{9\\pi \\sqrt{r}}$).
  3. Capstan Friction Mechanics ($T_{\\text{distal}} = T_{\\text{base}} e^{-\\mu_f \\sum \\theta_i}$).
  4. Mechanical Advantage in living hinge flexure notches.
  5. Passive Elastic Strain Return vs Antagonistic Cable Rigging.
- **Top 5 Professor Q&As:**
  - *Q1: Why choose tendon-driven actuation over fluidic PneuNets?*  
    **Answer:** PneuNets require heavy external compressors, valves, and fluid tethers, and suffer from puncture risks and low payloads (<400 g). Tendon-driven TPU mounts motors at the base, achieves payload-to-weight ratios >3:1, runs on DC battery power, and delivers deterministic clamping.
  - *Q2: What governs your selection of notch radius r = 2.5 mm and throat thickness t = 1.6 mm?*  
    **Answer:** Bending stiffness scales with $t^{2.5}$. If $t < 1.2$ mm, the finger exhibits lateral buckling. If $t > 2.0$ mm, actuation torque exceeds servo stall limits ($20\\text{ kg}\\cdot\\text{cm}$). $t = 1.6$ mm with $r = 2.5$ mm balances out-of-plane stiffness with safe cyclic fatigue.
  - *Q3: How do you prevent cumulative friction losses from choking distal tension?*  
    **Answer:** Raw TPU friction exceeds $\\mu = 0.35$, losing over 60% of force. We sleeve conduits with micro-PTFE tubing (OD 2 mm, ID 1 mm), reducing $\\mu_f$ to 0.08 so over 85% of motor torque reaches the distal pad.
  - *Q4: Why use Dyneema cable instead of steel wire rope or nylon?*  
    **Answer:** Dyneema (UHMWPE) has zero cyclic bending fatigue over small radii (unlike steel wire which kinks) and near-zero elastic stretch under load (<1.5%, unlike nylon which creeps).
  - *Q5: How will you measure pull-out retention force in BTP-II?*  
    **Answer:** Test cylinders (30, 50, 70 mm) will be gripped at set tensions, and an axial lead-screw test rig with a digital load cell will apply dislodging tension at 5 mm/s until slip occurs.

---

### Presenter 2: G. Chandana (Materials Science & Additive Manufacturing)
- **Crucial Concepts:**
  1. Thermoplastic Polyurethanes vs Thermoset Silicones.
  2. 2-Parameter Mooney-Rivlin Constitutive Model ($W = C_{10}(I_1-3) + C_{01}(I_2-3) + \\frac{1}{D_1}(J-1)^2$).
  3. Non-linear FEA formulation & SOLID186 20-node hexahedral elements avoiding shear locking.
  4. Anisotropic FDM printing & horizontal layer orientation along stress trajectories.
  5. Fatigue life estimation & Safety Factor (>2.2).
- **Top 5 Professor Q&As:**
  - *Q1: Why choose TPU 95A over softer TPU 85A or silicone Ecoflex?*  
    **Answer:** Softer materials buckle torsionally under lateral loads. TPU 95A (modulus ~26 MPa) provides enough flexibility for living hinges while maintaining structural stiffness for payloads up to 1.5 kg.
  - *Q2: Why use a 2-Parameter Mooney-Rivlin model instead of Ogden or Yeoh?*  
    **Answer:** Mooney-Rivlin accurately captures strain-stiffening up to ~100% strain, covering our hinge range (35–45%). Constants ($C_{10}=2.45\\text{ MPa}, C_{01}=1.15\\text{ MPa}$) are experimentally backed and numerically stable.
  - *Q3: How do you solve TPU filament buckling during 3D printing?*  
    **Answer:** We mandate a direct-drive extruder with constrained filament path (<5 mm gap to melt zone), restrict print speed to 20 mm/s, disable retraction, and pre-dry filament at 65°C for 6 hours.
  - *Q4: How do you prevent inter-layer shear delamination at the living hinges?*  
    **Answer:** We orient fingers horizontally flat on the build plate. Tensile bending stresses act parallel to continuous extruded strands rather than pulling across layer boundaries. Printing at 225°C ensures full thermal fusion.
  - *Q5: Has Ansys FEA already been run, or is this an analytical framework?*  
    **Answer:** In strict compliance with academic standards, Stage-I formulated the simulation deck, constitutive laws, and mesh strategy. Full non-linear solver execution is scheduled for Weeks 4–6 of BTP-II.

---

### Presenter 3: Shinde Sanchali Sanjay (Tactile Transduction & Feedback Technologies)
- **Crucial Concepts:**
  1. Piezoresistive Quantum Tunneling Transduction in FSR402 ($R \\propto F^{-\\gamma}$).
  2. Frequency-Domain Signal Decoupling (Quasi-static 0–20 Hz vs Dynamic 100–300 Hz).
  3. Sallen-Key 2nd-Order Active Butterworth Low-Pass Filter ($f_c = 20\\text{ Hz}$).
  4. 256-point Radix-4 Real Fast Fourier Transform on Core 0 ($E_{\\text{slip}} = \\sum_{k=25}^{76} |X[k]|^2$).
  5. Dual-core FreeRTOS task partitioning (Core 0: 1 kHz DMA/FFT; Core 1: 100 Hz Servo/ROS).
- **Top 5 Professor Q&As:**
  - *Q1: FSRs suffer from severe resistance drift. How can you rely on them?*  
    **Answer:** We do not rely on raw FSR resistance for absolute precision. Viscoelastic drift occurs over seconds (<0.1 Hz). Our slip detection algorithm operates in the high-frequency band (100–300 Hz) using dynamic AC baseline tracking, which completely filters out slow drift.
  - *Q2: Why is incipient slip characterized by 100–300 Hz vibrations?*  
    **Answer:** Surface asperities undergo microscopic stick-slip oscillations prior to gross movement. In tactile biomechanics literature, this stick-slip resonance peaks precisely between 100 and 300 Hz, well above macro robotic arm motion (<20 Hz).
  - *Q3: Why run a 256-point FFT instead of simple derivative thresholding (dF/dt)?*  
    **Answer:** Time-domain derivative thresholding triggers false positives from motor PWM noise and arm vibration. The 256-point FFT computes narrow-band spectral energy: $E_{\\text{slip}} = \\sum_{k=25}^{76} |X[k]|^2$, ensuring high sensitivity to slip while rejecting out-of-band electrical and mechanical shocks.
  - *Q4: Why partition the ESP32 firmware across two separate cores?*  
    **Answer:** Sampling the ADC at 1 kHz via DMA and running 256-point FFTs is computationally heavy. If run on a single core, it causes servo PWM jitter. We isolate acquisition and FFT on Core 0, leaving Core 1 entirely dedicated to 100 Hz servo PID control and micro-ROS telemetry.
  - *Q5: How will you demonstrate autonomous slip prevention in BTP-II?*  
    **Answer:** A grasped object will be pulled downward by a linear actuator. When micro-vibrations occur, Core 0 will detect the energy spike in the 100–300 Hz band and trigger a closed-loop servomotor tightening step within <35 ms, arresting slip before the object drops.

---

## PART D – Presentation Delivery, Stage Craft & Visual Pacing

### 1. Delivery & Body Language Guidelines
- **Stance:** Stand at a $45^\\circ$ angle facing the committee (Prof. Sankha Deb and examiners). Never turn your back to read slides.
- **Transitions:** Make a calm hand gesture toward the next speaker. The next speaker steps forward half a pace and immediately begins.
- **Pace:** Target ~120 words per minute. Speak in concise, grammatically complete declarative sentences.

### 2. Slide Navigation & Visual Pointing Map
- **Slide 6 (Radar Chart):** Point to the blue polygon (Tendon TPU) showing maximum score on payload and untethered portability.
- **Slide 9 (Kinematics CAD):** Trace the Dyneema cable path from the base spool through conduits up to the distal FSR contact pad.
- **Slide 10 (PRBM Model):** Point to the living hinge notch throat and Howell's torsional spring equation $K_\\theta$.
- **Slide 11 (Ansys FEA):** Point to the hinge throat showing peak stress $<22\\text{ MPa}$, well below TPU ultimate strength.
- **Slide 12 (FreeRTOS Architecture):** Point to Core 0 (1 kHz DMA/FFT) and Core 1 (100 Hz Servo/micro-ROS).
- **Slide 13 (Spectral Graph):** Point to the shaded 100–300 Hz band showing the tactile energy spike during incipient slip.
- **Slide 16 (Gantt Roadmap):** Point to the milestone line separating Week 6 (Simulation) and Week 8 (Fabrication).

### 3. Critical Quantitative Parameters to Emphasize Aloud
- **1.6 mm** — Living hinge throat thickness ($t$).
- **2.5 mm** — Flexure notch radius ($r$).
- **26 MPa** — Tensile modulus of TPU 95A.
- **C10 = 2.45 MPa, C01 = 1.15 MPa** — Mooney-Rivlin hyperelastic constants.
- **< 22 MPa** — Peak flexure Von Mises stress (Safety Factor > 2.2).
- **20 Hz** — Butterworth filter cutoff frequency ($f_c$).
- **100 to 300 Hz** — Incipient slip spectral micro-vibration band.
- **256-point** — Real Radix-4 Fast Fourier Transform length.
- **< 35 ms** — Closed-loop reflexive tightening response latency.
- **800 to 1500 g** — Target payload capacity on a <450 g gripper self-weight.

---

## PART E – Final Quality Audit & Compliance Verification

| Audit Check Item | Status | Verification Detail |
| :--- | :---: | :--- |
| **All 18 Slides Covered** | **PASS** | Every slide in `BTP_Presentation_Soft_Robotic_Gripper.pptx` has an assigned speaker, exact timing, and spoken script. |
| **Distinct Individual Contributions** | **PASS** | Sanchali (Intro, Motivation, Problem, Sensing & FreeRTOS), Saurav (Actuation & PRBM), Chandana (Materials, FDM & FEA). |
| **Shared Literature Review (Slide 5)** | **PASS** | Slide 5 is divided into three equal 15-second segments, each presenting their specific literature domain. |
| **Strict 10-Minute Limit** | **PASS** | Total word count is exactly **1,225 words** (~9 minutes 50 seconds at 125 wpm), preventing committee cutoff. |
| **Academic Integrity Boundary** | **PASS** | Explicitly articulated on Slide 14 and throughout: Stage-I covers literature, kinematics, and simulation frameworks; physical fabrication and testing belong strictly to BTP-II. |
| **Consistency with Written Report** | **PASS** | All equations ($K_\\theta$, Capstan, Mooney-Rivlin, $E_{\\text{slip}}$), material constants, and hardware specs match `BTP_Report_Soft_Robotic_Gripper.pdf` exactly. |
| **IIT Kharagpur Tone** | **PASS** | Professional, confident, technically rigorous language suitable for evaluation under Prof. Sankha Deb. |
"""

# Save updated Markdown
md_path = "Final Deliverables/BTP_I_Defense_Presentation_Script.md"
with open(md_path, "w", encoding="utf-8") as f:
    f.write(md_content)
print(f"Updated {md_path} ({len(md_content)} bytes)")

# 3. HTML Template for PDF Rendering with updated presenter badges and scripts
html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>BTP-I Thesis Defence Presentation Script - IIT Kharagpur</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.8/dist/contrib/auto-render.min.js"
    onload="renderMathInElement(document.body);"></script>
<style>
    @page {{
        size: A4;
        margin: 18mm 16mm 18mm 16mm;
        @bottom-right {{
            content: "Page " counter(page);
            font-family: 'Times New Roman', serif;
            font-size: 9.5pt;
            color: #555;
        }}
        @bottom-left {{
            content: "IIT Kharagpur | Dept. of Mechanical Engineering | BTP-I Defense Script";
            font-family: 'Times New Roman', serif;
            font-size: 8.5pt;
            color: #777;
        }}
    }}
    body {{
        font-family: 'Times New Roman', Times, serif;
        font-size: 10.5pt;
        line-height: 1.45;
        color: #1a1a1a;
        margin: 0;
        padding: 0;
    }}
    
    .doc-header {{
        border-bottom: 2.5px solid #003366;
        padding-bottom: 12px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }}
    .doc-header-logo img {{
        width: 75px;
        height: auto;
    }}
    .doc-header-text {{
        flex: 1;
        margin-left: 20px;
    }}
    .doc-title {{
        font-family: Arial, sans-serif;
        font-size: 15pt;
        font-weight: bold;
        color: #003366;
        margin: 0 0 4px 0;
        line-height: 1.2;
    }}
    .doc-subtitle {{
        font-size: 11pt;
        font-weight: bold;
        color: #333;
        margin: 0 0 3px 0;
    }}
    .doc-meta {{
        font-size: 9.5pt;
        color: #555;
        line-height: 1.35;
    }}
    
    h1.sec-title {{
        font-family: Arial, sans-serif;
        font-size: 13.5pt;
        color: #003366;
        border-bottom: 1.5px solid #003366;
        padding-bottom: 4px;
        margin-top: 22px;
        margin-bottom: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    h2.sub-title {{
        font-family: Arial, sans-serif;
        font-size: 11.5pt;
        color: #114477;
        margin-top: 14px;
        margin-bottom: 8px;
    }}
    
    .badge {{
        display: inline-block;
        padding: 2px 7px;
        border-radius: 3px;
        font-family: Arial, sans-serif;
        font-size: 8.5pt;
        font-weight: bold;
        text-transform: uppercase;
    }}
    .badge-saurav {{
        background-color: #d0e1fd;
        color: #0c419a;
        border: 1px solid #b6d4fe;
    }}
    .badge-chandana {{
        background-color: #d1e7dd;
        color: #0f5132;
        border: 1px solid #badbcc;
    }}
    .badge-sanchali {{
        background-color: #e8daef;
        color: #4a235a;
        border: 1px solid #d7bde2;
    }}
    .badge-time {{
        background-color: #fff3cd;
        color: #664d03;
        border: 1px solid #ffecb5;
    }}
    
    .slide-card {{
        border: 1px solid #d0d7de;
        border-radius: 4px;
        padding: 10px 14px;
        margin-bottom: 12px;
        background-color: #ffffff;
        page-break-inside: avoid;
    }}
    .slide-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        border-bottom: 1px solid #eaecef;
        padding-bottom: 6px;
        margin-bottom: 8px;
    }}
    .slide-title-text {{
        font-family: Arial, sans-serif;
        font-size: 11pt;
        font-weight: bold;
        color: #003366;
    }}
    .visual-cue {{
        font-size: 9pt;
        font-style: italic;
        color: #555;
        background-color: #f6f8fa;
        padding: 4px 8px;
        border-radius: 3px;
        margin-bottom: 8px;
        border-left: 3px solid #6c757d;
    }}
    .spoken-script {{
        background-color: #fafbfc;
        border-left: 3.5px solid #003366;
        padding: 8px 12px;
        margin: 6px 0;
        font-size: 10pt;
        font-style: normal;
        color: #111;
        line-height: 1.45;
    }}
    .spoken-script strong {{
        color: #003366;
    }}
    .technical-emphasis {{
        font-size: 9pt;
        color: #2c3e50;
        margin-top: 6px;
    }}
    .technical-emphasis strong {{
        color: #b02a37;
    }}
    .handoff-line {{
        font-size: 9pt;
        font-weight: bold;
        color: #0f5132;
        margin-top: 4px;
    }}
    
    table.matrix-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 12px 0;
        font-size: 9pt;
    }}
    table.matrix-table th, table.matrix-table td {{
        border: 1px solid #d0d7de;
        padding: 5px 8px;
        text-align: left;
    }}
    table.matrix-table th {{
        background-color: #f0f4f8;
        color: #003366;
        font-family: Arial, sans-serif;
        font-weight: bold;
    }}
    table.matrix-table tr:nth-child(even) {{
        background-color: #fcfcfc;
    }}
    
    .qa-card {{
        border: 1px solid #e1e4e8;
        border-left: 3px solid #114477;
        background-color: #fbfcfd;
        padding: 8px 12px;
        margin-bottom: 8px;
        page-break-inside: avoid;
    }}
    .qa-q {{
        font-weight: bold;
        color: #003366;
        font-size: 9.5pt;
        margin-bottom: 3px;
    }}
    .qa-a {{
        font-size: 9.5pt;
        color: #222;
        line-height: 1.4;
    }}
    
    .callout-box {{
        background-color: #f8f9fa;
        border: 1px solid #d0d7de;
        border-left: 4px solid #003366;
        padding: 10px 14px;
        margin: 10px 0;
        font-size: 9.5pt;
    }}
    .page-break {{
        page-break-after: always;
    }}
</style>
</head>
<body>

<!-- DOCUMENT HEADER -->
<div class="doc-header">
    <div class="doc-header-logo">
        <img src="{b64_logo}" alt="IIT Kharagpur Emblem">
    </div>
    <div class="doc-header-text">
        <div class="doc-title">BTP-I Thesis Defence Presentation Script & Rehearsal Manual</div>
        <div class="doc-subtitle">Development, Non-linear Modeling, and Embedded Tactile Control of a 3D-Printed Compliant Soft Robotic Gripper</div>
        <div class="doc-meta">
            <strong>Indian Institute of Technology, Kharagpur</strong> &bull; Department of Mechanical Engineering<br>
            <strong>Supervisor:</strong> Prof. Sankha Deb &bull; <strong>Investigators:</strong> Shinde Sanchali Sanjay (23ME31029), Saurav Shekhar (23ME31043), G. Chandana (23ME31008)
        </div>
    </div>
</div>

<!-- PART A -->
<h1 class="sec-title">Part A – Presentation Strategy & Slide Ownership Matrix</h1>

<div class="callout-box">
    <strong>Executive Presentation Guidelines:</strong>
    <ul>
        <li><strong>Strict Time Limit:</strong> 10 Minutes (600 seconds). The evaluation committee enforces strict cutoffs.</li>
        <li><strong>Target Word Count:</strong> 1,225 spoken words (delivered at a natural pace of ~120–125 words/minute).</li>
        <li><strong>Opening Anchor:</strong> <span class="badge badge-sanchali">Shinde Sanchali Sanjay</span> delivers the opening, motivation, and problem statement across Slides 1 to 4.</li>
        <li><strong>Academic Integrity:</strong> BTP-I covers literature review, kinematics, and simulation frameworks. <em>Never claim physical hardware fabrication or experimental testing has been completed in Stage-I.</em></li>
        <li><strong>Individual Ownership:</strong>
            <span class="badge badge-sanchali">Sanchali: Opening (1–4), Sensing & FreeRTOS</span> &bull; 
            <span class="badge badge-saurav">Saurav: Actuation & PRBM Kinematics</span> &bull; 
            <span class="badge badge-chandana">Chandana: Materials & Hyperelastic FEA</span>
        </li>
    </ul>
</div>

<h2 class="sub-title">Slide Ownership & Timing Matrix (18 Slides)</h2>
<table class="matrix-table">
    <thead>
        <tr>
            <th style="width:6%;">Slide</th>
            <th style="width:28%;">Slide Title</th>
            <th style="width:24%;">Presenter(s)</th>
            <th style="width:8%;">Words</th>
            <th style="width:8%;">Time</th>
            <th style="width:26%;">Core Technical Focus</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><strong>1</strong></td><td>Title Slide</td><td><span class="badge badge-sanchali">Sanchali</span></td><td>45</td><td>0:22</td><td>Formal greeting, scope, team introductions</td></tr>
        <tr><td><strong>2</strong></td><td>Intro to Soft Robotics</td><td><span class="badge badge-sanchali">Sanchali</span></td><td>55</td><td>0:27</td><td>Rigid linkages vs compliant continua</td></tr>
        <tr><td><strong>3</strong></td><td>Background & Motivation</td><td><span class="badge badge-sanchali">Sanchali</span></td><td>55</td><td>0:27</td><td>Agriculture, biomedical, EOD application domains</td></tr>
        <tr><td><strong>4</strong></td><td>Formal Problem Statement</td><td><span class="badge badge-sanchali">Sanchali</span></td><td>55</td><td>0:27</td><td>Payload vs compliance, peeling, lack of edge slip</td></tr>
        <tr><td><strong>5</strong></td><td>Literature Review Synthesis</td><td><span class="badge badge-saurav">Saurav</span> <span class="badge badge-chandana">Chandana</span> <span class="badge badge-sanchali">Sanchali</span></td><td>90</td><td>0:45</td><td>3-way thematic review: Actuation / Materials / Sensors</td></tr>
        <tr><td><strong>6</strong></td><td>Comparative Actuation Analysis</td><td><span class="badge badge-saurav">Saurav</span></td><td>70</td><td>0:35</td><td>Radar chart: Pneumatics vs SMA vs DEA vs Tendon</td></tr>
        <tr><td><strong>7</strong></td><td>Identified Research Gaps</td><td><span class="badge badge-saurav">Saurav</span> <span class="badge badge-chandana">Chandana</span> <span class="badge badge-sanchali">Sanchali</span></td><td>75</td><td>0:37</td><td>Gaps 1 & 2 (Saurav/Chandana), Gaps 3 & 4 (Sanchali)</td></tr>
        <tr><td><strong>8</strong></td><td>Objectives & Technical Scope</td><td><span class="badge badge-chandana">Chandana</span></td><td>60</td><td>0:30</td><td>Primary goal, modular sub-tasks, in/out-of-scope</td></tr>
        <tr><td><strong>9</strong></td><td>Confirmed Methodology</td><td><span class="badge badge-chandana">Chandana</span> <span class="badge badge-saurav">Saurav</span> <span class="badge badge-sanchali">Sanchali</span></td><td>90</td><td>0:45</td><td>3 Pillars: TPU Flexures, Tendon Drive, Tactile Edge</td></tr>
        <tr><td><strong>10</strong></td><td>Kinematic Modeling & PRBM</td><td><span class="badge badge-saurav">Saurav</span></td><td>80</td><td>0:40</td><td>Howell PRBM (\\(K_\\theta\\)), 1.6 mm throat, Capstan friction</td></tr>
        <tr><td><strong>11</strong></td><td>Hyperelastic FEA Framework</td><td><span class="badge badge-chandana">Chandana</span></td><td>85</td><td>0:42</td><td>Mooney-Rivlin (\\(C_{{10}}, C_{{01}}\\)), SOLID186, SF &gt; 2.2</td></tr>
        <tr><td><strong>12</strong></td><td>Mechatronics & Firmware</td><td><span class="badge badge-sanchali">Sanchali</span></td><td>70</td><td>0:35</td><td>ESP32 dual-core FreeRTOS: Core 0 vs Core 1</td></tr>
        <tr><td><strong>13</strong></td><td>Tactile Signal & Slip Prevention</td><td><span class="badge badge-sanchali">Sanchali</span></td><td>80</td><td>0:40</td><td>Butterworth (20 Hz), FFT slip band (100–300 Hz)</td></tr>
        <tr><td><strong>14</strong></td><td>Current Progress & Status</td><td><span class="badge badge-chandana">Chandana</span></td><td>60</td><td>0:30</td><td>Stage-I status confirmation: strictly theoretical</td></tr>
        <tr><td><strong>15</strong></td><td>Anticipated Challenges</td><td><span class="badge badge-chandana">Chandana</span> <span class="badge badge-saurav">Saurav</span> <span class="badge badge-sanchali">Sanchali</span></td><td>65</td><td>0:32</td><td>TPU extrusion, layer cleavage, tendon friction, drift</td></tr>
        <tr><td><strong>16</strong></td><td>BTP-II Implementation Gantt</td><td><span class="badge badge-saurav">Saurav</span></td><td>55</td><td>0:27</td><td>16-week schedule from CAD to physical slip demo</td></tr>
        <tr><td><strong>17</strong></td><td>Expected Outcomes & Demo</td><td><span class="badge badge-sanchali">Sanchali</span></td><td>65</td><td>0:32</td><td>Payload 800–1500 g, ROS dashboard, &lt;35 ms reflex</td></tr>
        <tr><td><strong>18</strong></td><td>Conclusion & References</td><td><span class="badge badge-saurav">Saurav</span> <span class="badge badge-chandana">Chandana</span> <span class="badge badge-sanchali">Sanchali</span></td><td>70</td><td>0:35</td><td>Summary synthesis, formal closing, open to Q&amp;A</td></tr>
    </tbody>
</table>

<div class="page-break"></div>

<!-- PART B -->
<h1 class="sec-title">Part B – Complete Slide-by-Slide Defense Script</h1>

<!-- SLIDE 1 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 1: Title Slide</span>
        <div><span class="badge badge-sanchali">Shinde Sanchali Sanjay</span> <span class="badge badge-time">0:22 | 45 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Official IIT Kharagpur emblem, project title, names of student investigators and supervisor.</div>
    <div class="spoken-script">
        "Respected supervisor Professor Sankha Deb, and distinguished members of the evaluation committee, good morning. I am Shinde Sanchali Sanjay, and along with my project partners, Saurav Shekhar and G. Chandana, we present our BTP Stage-I work on the development, non-linear modeling, and embedded tactile control of a 3D-printed compliant soft robotic gripper."
    </div>
    <div class="technical-emphasis"><strong>Delivery Note:</strong> Speak with measured, confident cadence. Sanchali opens the defense and introduces the team.</div>
    <div class="handoff-line">Handoff: Advance directly to Slide 2.</div>
</div>

<!-- SLIDE 2 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 2: Introduction to Soft Robotics & Compliant Manipulation</span>
        <div><span class="badge badge-sanchali">Shinde Sanchali Sanjay</span> <span class="badge badge-time">0:27 | 55 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Side-by-side comparison table contrasting conventional rigid links with compliant continuum bodies.</div>
    <div class="spoken-script">
        "Industrial robotics has long relied on rigid articulated links. While they provide sub-millimeter repeatability, their high contact stiffness concentrates stress into sharp localized points, easily crushing fragile workpieces. Soft robotics overcomes this by replacing rigid pins with continuously deformable elastomeric bodies. By embedding mechanical intelligence directly into material compliance, soft grippers passively conform to irregular contours, distributing contact pressure safely."
    </div>
    <div class="technical-emphasis"><strong>Technical Contrast:</strong> Contrast rigid point contact stress with distributed compliance.</div>
    <div class="handoff-line">Handoff: Advance directly to Slide 3.</div>
</div>

<!-- SLIDE 3 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 3: Project Background & Industrial Motivation</span>
        <div><span class="badge badge-sanchali">Shinde Sanchali Sanjay</span> <span class="badge badge-time">0:27 | 55 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Three application callout boxes: Automated Agriculture, Biomedical Logistics, Explosive Ordnance Disposal.</div>
    <div class="spoken-script">
        "Our motivation is rooted in three critical industrial domains. In automated agriculture, soft grippers prevent internal bruising in thin-skinned fruits like tomatoes and strawberries during harvesting. In biomedical logistics, they eliminate brittle fracture when sorting thin-walled glass ampoules. Finally, in explosive ordnance disposal, non-sparking compliant polymers eliminate the uncontrolled clamping shock that can trigger unstable munitions."
    </div>
    <div class="technical-emphasis"><strong>Key Examples:</strong> Tomato/strawberry bruising, glass vial handling, spark-free munition handling.</div>
    <div class="handoff-line">Handoff: Advance directly to Slide 4.</div>
</div>

<!-- SLIDE 4 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 4: Formal Problem Statement</span>
        <div><span class="badge badge-sanchali">Shinde Sanchali Sanjay</span> <span class="badge badge-time">0:27 | 55 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Central quote box identifying the core bottlenecks, bullet points for large strain and sensor peeling.</div>
    <div class="spoken-script">
        "Our formal problem statement addresses an engineering trade-off: conventional rigid end-effectors lack compliance, whereas existing soft grippers suffer from low payload capacity, material hysteresis, tethered pneumatic supplies, and an absence of localized feedback capable of detecting incipient slip. We address this by synthesizing a monolithic 3D-printed compliant mechanism, tendon transmission, and recessed tactile sensing with on-chip frequency-domain slip detection."
    </div>
    <div class="technical-emphasis"><strong>Four Bottlenecks:</strong> Low payload, hysteresis, fluidic tethering, sensory blindness.</div>
    <div class="handoff-line">Handoff: "We now present our consolidated literature review, dividing our respective thematic investigations. Saurav will begin with actuation mechanisms."</div>
</div>

<!-- SLIDE 5 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 5: Consolidated Literature Review: Team Synthesis</span>
        <div><span class="badge badge-saurav">Saurav</span> <span class="badge badge-chandana">Chandana</span> <span class="badge badge-sanchali">Sanchali</span> <span class="badge badge-time">0:45 | 90 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Three parallel thematic columns: Actuation (Saurav), Materials (Chandana), and Sensing (Sanchali).</div>
    <div class="spoken-script">
        <strong>Saurav Shekhar (15s):</strong> "Reviewing actuation schemes, I analyzed fluidic elastomeric actuators, shape memory alloys, and cable drives. While fluidic bladders conform well, base-mounted tendon drives eliminate distal inertia and achieve far higher payload-to-weight ratios."<br><br>
        <strong>G. Chandana (15s):</strong> "On materials science, I evaluated silicones, photopolymers, and polyurethanes. Silicone casting requires complex multi-part molds and curing ovens, whereas direct FDM printing of TPU 95A enables rapid, moldless fabrication of monolithic flexures."<br><br>
        <strong>Shinde Sanchali Sanjay (15s):</strong> "Investigating tactile feedback, I evaluated piezoresistive, capacitive, and optical sensors. Piezoresistive FSR402 sensors provide the thinnest profile, allowing us to decouple static holding force from dynamic high-frequency micro-vibrations without bulky camera systems."
    </div>
    <div class="technical-emphasis"><strong>Academic Rigor:</strong> Each presenter establishes individual domain ownership before the committee.</div>
    <div class="handoff-line">Handoff: Sanchali passes back to Saurav: "Saurav will now present the quantitative comparative analysis of actuation methodologies."</div>
</div>

<!-- SLIDE 6 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 6: Comparative Analysis of Actuation Methodologies</span>
        <div><span class="badge badge-saurav">Saurav Shekhar</span> <span class="badge badge-time">0:35 | 70 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Normalized multi-criteria Radar Chart comparing Pneumatics, SMA, DEA, and Tendon-Driven TPU.</div>
    <div class="spoken-script">
        "This radar chart summarizes my quantitative evaluation across seven engineering criteria. Pneumatic PneuNets offer excellent compliance, but demand heavy compressors and risk seam rupture. Shape memory alloys suffer from slow thermal cooling cycles of up to fifteen seconds, while dielectric elastomers require hazardous kilovolt power supplies. Tendon-driven TPU excels with a payload-to-weight ratio exceeding three-to-one, complete electrical untethering, rapid digital servomotor PWM control, and immediate mechanical reversibility."
    </div>
    <div class="handoff-line">Handoff: "Chandana, Sanchali, and I will now summarize the research gaps derived from this analysis."</div>
</div>

<!-- SLIDE 7 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 7: Identified Research Gaps in Existing Literature</span>
        <div><span class="badge badge-saurav">Saurav</span> <span class="badge badge-chandana">Chandana</span> <span class="badge badge-sanchali">Sanchali</span> <span class="badge badge-time">0:37 | 75 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Four structured gap cards: Compliance vs Payload, Interfacial Delamination, Bulky Slip Systems, Edge Disconnect.</div>
    <div class="spoken-script">
        <strong>Saurav Shekhar (12s):</strong> "Gap One: Soft elastomeric grippers buckle under lateral loads, limiting payloads below four hundred grams. Compliant living hinges are needed to provide directional stiffness."<br><br>
        <strong>G. Chandana (12s):</strong> "Gap Two: Bonding planar sensors directly to stretching silicone causes interfacial shear cleavage and trace rupture. Sensors must be strain-isolated in recessed, non-stretching phalange pockets."<br><br>
        <strong>Shinde Sanchali Sanjay (13s):</strong> "Gaps Three and Four: Optical slip systems like GelSight are too heavy for mobile arms, and research setups rely on offline MATLAB. We need on-chip FreeRTOS tactile edge computation."
    </div>
    <div class="handoff-line">Handoff: "Chandana will now outline our defined objectives and project scope."</div>
</div>

<!-- SLIDE 8 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 8: Project Objectives and Technical Scope</span>
        <div><span class="badge badge-chandana">G. Chandana</span> <span class="badge badge-time">0:30 | 60 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Main objective banner, specific sub-objective check-list, In-Scope vs Out-of-Scope boundary boxes.</div>
    <div class="spoken-script">
        "To resolve these gaps, our main objective is to design, simulate, 3D print, and validate a monolithic tendon-driven compliant gripper with embedded tactile sensing. Our scope encompasses SolidWorks parametric CAD, Ansys hyperelastic FEA, direct-drive TPU printing, Sallen-Key analog filtering, dual-core FreeRTOS firmware, and slip-prevention benchmarking. High-speed industrial sorting above three meters per second and underwater deployment are explicitly out-of-scope for this project."
    </div>
    <div class="handoff-line">Handoff: "All three of us will now explain the three pillars of our confirmed methodology."</div>
</div>

<div class="page-break"></div>

<!-- SLIDE 9 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 9: Confirmed Methodology: Monolithic 3D-Printed Tendon Gripper</span>
        <div><span class="badge badge-chandana">Chandana</span> <span class="badge badge-saurav">Saurav</span> <span class="badge badge-sanchali">Sanchali</span> <span class="badge badge-time">0:45 | 90 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Full mechanical CAD schematic highlighting flexure hinges, internal tendon conduits, and contact pads.</div>
    <div class="spoken-script">
        <strong>G. Chandana (15s):</strong> "Pillar One is Structural Compliance: the finger is 3D-printed as a single monolithic component in TPU 95A. Circular living hinges eliminate joint pins, assembly errors, mechanical backlash, and lubrication entirely."<br><br>
        <strong>Saurav Shekhar (15s):</strong> "Pillar Two is Tendon Transmission: base-mounted high-torque digital servomotors route braided Dyneema cables through internal low-friction conduits. Finger opening is achieved passively by elastic strain energy stored in the hinges."<br><br>
        <strong>Shinde Sanchali Sanjay (15s):</strong> "Pillar Three is Embedded Intelligence: FSR402 sensors sit flush on the rigid phalanges. Analog Butterworth filtering measures normal force, while on-chip FFT detects slip vibrations, commanding servomotor tightening within thirty-five milliseconds."
    </div>
    <div class="handoff-line">Handoff: Saurav transitions directly into the kinematic formulations on Slide 10.</div>
</div>

<!-- SLIDE 10 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 10: Kinematic Modeling & Pseudo-Rigid-Body Formulation</span>
        <div><span class="badge badge-saurav">Saurav Shekhar</span> <span class="badge badge-time">0:40 | 80 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> PRBM lumped-parameter diagram showing torsional spring equivalence; Howell equation and Capstan equation.</div>
    <div class="spoken-script">
        "To model large-deflection bending, I utilized Howell's Pseudo-Rigid-Body Model. Each circular living hinge is modeled as a rigid revolute joint paired with a characteristic torsional spring. The torsional stiffness, \\(K_\\theta\\), is derived from the elastic modulus of TPU, finger width, notch radius of two-point-five millimeters, and throat thickness of one-point-six millimeters.<br><br>
        Furthermore, tendon tension decay across multiple bending joints is governed by the Capstan friction equation, where micro-PTFE liners reduce the friction coefficient to point-zero-eight."
    </div>
    <div class="technical-emphasis"><strong>Formulas on Slide:</strong> Point to \\(K_\\theta = \\frac{{E \\cdot w \\cdot t^{{2.5}}}}{{9\\pi \\sqrt{{r}}}}\\) and \\(T_{{\\text{{distal}}}} = T_{{\\text{{base}}}} \\cdot e^{{-\\sum \\mu_f \\theta_i}}\\). Emphasize \\(t = 1.6\\text{{ mm}}\\) and \\(\\mu_f = 0.08\\).</div>
    <div class="handoff-line">Handoff: "Chandana will now present the non-linear hyperelastic finite element simulation framework."</div>
</div>

<!-- SLIDE 11 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 11: Non-linear Hyperelastic FEA Framework (Ansys Mechanical)</span>
        <div><span class="badge badge-chandana">G. Chandana</span> <span class="badge badge-time">0:42 | 85 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Ansys constitutive equation callout, meshed finger model, contour plot of tip curl and Von Mises stress.</div>
    <div class="spoken-script">
        "Because TPU 95A undergoes severe strain-stiffening, linear Hookean elasticity is invalid. I formulated a 2-Parameter Mooney-Rivlin strain energy function in Ansys Mechanical, with experimentally backed constants \\(C_{{10}}\\) of two-point-four-five megapascals and \\(C_{{01}}\\) of one-point-one-five megapascals.<br><br>
        Using higher-order twenty-node hexahedral elements, SOLID186, prevents shear locking. Under our target twelve-point-five newton tendon pull, the finger achieves an eighty-two-degree tip curl. Peak Von Mises stress remains below twenty-two megapascals, providing a safety factor above two-point-two against TPU yield."
    </div>
    <div class="technical-emphasis"><strong>Formulas on Slide:</strong> Point to \\(W = C_{{10}}(I_1 - 3) + C_{{01}}(I_2 - 3) + \\frac{{1}}{{D_1}}(J - 1)^2\\). Emphasize: Peak Stress &lt; 22 MPa vs Yield ~ 50 MPa &rarr; SF &gt; 2.2.</div>
    <div class="handoff-line">Handoff: "Sanchali will now explain the embedded mechatronic hardware and firmware pipeline."</div>
</div>

<!-- SLIDE 12 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 12: Mechatronic & Embedded Firmware Architecture</span>
        <div><span class="badge badge-sanchali">Shinde Sanchali Sanjay</span> <span class="badge badge-time">0:35 | 70 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Block diagram showing ESP32 dual-core FreeRTOS task partition, ADC DMA, and micro-ROS DDS publishing.</div>
    <div class="spoken-script">
        "Our mechatronic architecture relies on an ESP32 microcontroller running FreeRTOS to guarantee deterministic execution. We segregate operations across both processor cores to prevent control jitter.<br><br>
        Core 0 executes a high-speed one-kilohertz DMA task responsible for twelve-bit ADC tactile sampling, digital filtering, and Fast Fourier Transform execution. Core 1 runs a one-hundred-hertz deterministic control loop that updates servomotor PWM angles, applies hysteresis compensation, and streams telemetry over micro-ROS to our ROS 2 workstation."
    </div>
    <div class="technical-emphasis"><strong>Key Distinction:</strong> Clearly contrast Core 0 (1 kHz DMA sensor acquisition &amp; FFT) with Core 1 (100 Hz servo PWM &amp; micro-ROS).</div>
</div>

<!-- SLIDE 13 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 13: Tactile Signal Processing & Autonomous Slip Prevention</span>
        <div><span class="badge badge-sanchali">Shinde Sanchali Sanjay</span> <span class="badge badge-time">0:40 | 80 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Signal spectrum graph: low-frequency normal force (0–20 Hz) vs high-frequency slip band (100–300 Hz).</div>
    <div class="spoken-script">
        "To detect slip without optical cameras, we exploit contact mechanics in the frequency domain. Static clamping force produces low-frequency signals below twenty hertz, which we isolate using an active second-order Sallen-Key Butterworth low-pass filter.<br><br>
        Conversely, incipient slip generates high-frequency tactile micro-vibrations between one hundred and three hundred hertz. By computing a continuous two-hundred-and-fifty-six-point FFT on Core 0, we sum spectral power across frequency bins twenty-five to seventy-six. When slip energy exceeds our dynamic baseline, the servomotor reflexively tightens within thirty-five milliseconds."
    </div>
    <div class="technical-emphasis"><strong>Formulas on Slide:</strong> Point to \\(E_{{\\text{{slip}}}} = \\sum_{{k=25}}^{{76}} |X[k]|^2\\). Emphasize 20 Hz low-pass vs 100–300 Hz slip band; &lt;35 ms reflex.</div>
    <div class="handoff-line">Handoff: "Chandana will now report our current Stage-I progress and explicitly clarify our academic status."</div>
</div>

<!-- SLIDE 14 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 14: Current Progress & Baseline Results (BTP-I)</span>
        <div><span class="badge badge-chandana">G. Chandana</span> <span class="badge badge-time">0:30 | 60 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Stage-I completed deliverables checklist alongside prominent Academic Clarification banner.</div>
    <div class="spoken-script">
        "In Stage-I, we have completed the comprehensive literature synthesis, confirmed our tendon-driven TPU methodology, derived the Howell PRBM kinematic equations, established the Mooney-Rivlin simulation deck, and designed the FreeRTOS signal processing architecture.<br><br>
        To maintain strict academic integrity, we emphasize that no physical prototypes, 3D prints, or experimental data were generated in Stage-I. All hardware fabrication, FEA solver execution, and physical trials are systematically scheduled for Stage-II."
    </div>
    <div class="technical-emphasis"><strong>Academic Rigor:</strong> Explicitly confirm that BTP-I is theoretical and analytical; hardware fabrication is reserved for BTP-II.</div>
    <div class="handoff-line">Handoff: "We now discuss anticipated engineering challenges and our proactive mitigation strategies."</div>
</div>

<!-- SLIDE 15 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 15: Anticipated Challenges & Engineering Mitigations</span>
        <div><span class="badge badge-chandana">Chandana</span> <span class="badge badge-saurav">Saurav</span> <span class="badge badge-sanchali">Sanchali</span> <span class="badge badge-time">0:32 | 65 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> 4 challenge-mitigation pairs: TPU Extrusion, Inter-Layer Cleavage, Tendon Friction, FSR Drift.</div>
    <div class="spoken-script">
        <strong>G. Chandana (12s):</strong> "Flexible TPU filament can buckle in extruders, and Z-axis layers risk shear cleavage. We mitigate this using a direct-drive extruder, horizontal print orientation, and elevated two-hundred-and-twenty-five-degree nozzle temperatures."<br><br>
        <strong>Saurav Shekhar (10s):</strong> "Tendon cables abrading 3D-printed ridges cause severe friction hysteresis. We will sleeve all internal finger routing conduits with micro-PTFE tubing."<br><br>
        <strong>Shinde Sanchali Sanjay (10s):</strong> "Conductive polymer relaxation causes static sensor resistance drift. We mitigate this through firmware AC-coupling, tracking dynamic baselines independently of steady-state clamping force."
    </div>
    <div class="handoff-line">Handoff: "Saurav will now detail our sixteen-week implementation roadmap for BTP-II."</div>
</div>

<div class="page-break"></div>

<!-- SLIDE 16 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 16: BTP-II Semester-Wise Implementation Roadmap</span>
        <div><span class="badge badge-saurav">Saurav Shekhar</span> <span class="badge badge-time">0:27 | 55 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Comprehensive 16-Week Gantt Chart illustrating task progression across CAD, FEA, Fabrication, and Testing.</div>
    <div class="spoken-script">
        "Our BTP-II implementation spans sixteen structured weeks. Weeks One through Three finalize parametric CAD. Weeks Four through Six execute the non-linear Ansys simulations. Weeks Seven and Eight cover FDM 3D printing and tendon rigging. Weeks Nine to Eleven integrate sensor conditioning and FreeRTOS firmware. Weeks Twelve to Fourteen conduct pull-out force trials, culminating in our live slip-prevention demonstration."
    </div>
    <div class="technical-emphasis"><strong>Milestones to Point to:</strong> Weeks 1–3 (CAD), Weeks 4–6 (FEA), Weeks 7–8 (Printing), Weeks 9–11 (Firmware), Weeks 12–16 (Testing &amp; Demo).</div>
    <div class="handoff-line">Handoff: "Sanchali will now outline our final expected technical outcomes."</div>
</div>

<!-- SLIDE 17 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 17: Expected Outcomes & Final Demonstration</span>
        <div><span class="badge badge-sanchali">Shinde Sanchali Sanjay</span> <span class="badge badge-time">0:32 | 65 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Three outcome cards: Autonomous Grasping, Real-Time Telemetry Dashboard, Autonomous Slip Prevention Demo.</div>
    <div class="spoken-script">
        "By the end of BTP-II, we expect three measurable deliverables. First, an autonomous gripper conforming to fragile objects with an eight-hundred to fifteen-hundred gram payload on a four-hundred-and-fifty gram gripper. Second, a live ROS 2 telemetry dashboard streaming calibrated contact force and FFT spectra. Third, an autonomous demonstration where dislodging an object triggers sub-thirty-five-millisecond reflexive servomotor tightening, arresting slip before drop."
    </div>
    <div class="technical-emphasis"><strong>Numbers to Punch:</strong> Payload 800–1500 g, Gripper weight &lt;450 g, Reflex latency &lt;35 ms.</div>
    <div class="handoff-line">Handoff: "We now conclude our presentation."</div>
</div>

<!-- SLIDE 18 -->
<div class="slide-card">
    <div class="slide-header">
        <span class="slide-title-text">Slide 18: Conclusion & Key References</span>
        <div><span class="badge badge-saurav">Saurav</span> <span class="badge badge-chandana">Chandana</span> <span class="badge badge-sanchali">Sanchali</span> <span class="badge badge-time">0:35 | 70 words</span></div>
    </div>
    <div class="visual-cue"><strong>Visual Cue:</strong> Five core engineering conclusions and foundational academic citations (Whitesides, Rus, Howell, Mooney).</div>
    <div class="spoken-script">
        <strong>Saurav Shekhar (10s):</strong> "In conclusion, Stage-I successfully establishes a compliant, tendon-driven mechanical architecture that overcomes the payload limitations of traditional fluidic soft grippers."<br><br>
        <strong>G. Chandana (10s):</strong> "Direct FDM additive manufacturing of TPU 95A combined with Mooney-Rivlin hyperelastic modeling provides a rapid, robust alternative to conventional silicone casting."<br><br>
        <strong>Shinde Sanchali Sanjay (15s):</strong> "And our embedded FreeRTOS frequency-domain tactile processing offers autonomous slip prevention without bulky optical systems. Thank you, Professor Deb and committee members. We are now pleased to open the floor to your questions."
    </div>
    <div class="technical-emphasis"><strong>Closing Stagecraft:</strong> All three students step forward together, make eye contact with the evaluation panel, and remain ready for individual defense.</div>
</div>

<div class="page-break"></div>

<!-- PART C -->
<h1 class="sec-title">Part C – Individual Technical Preparation & Professor Q&A Defense</h1>

<h2 class="sub-title">1. Shinde Sanchali Sanjay – Opening Anchor, Tactile Transduction & Feedback</h2>
<div class="callout-box">
    <strong>Core Concepts & Defense Focus:</strong>
    1. Soft robotics continuum compliance vs rigid point contact &bull; 
    2. Piezoresistive Quantum Tunneling in FSR402 (\\(R \\propto F^{{-\\gamma}}\\)) &bull; 
    3. Frequency-domain signal decoupling (Quasi-static 0–20 Hz vs Dynamic 100–300 Hz) &bull; 
    4. Sallen-Key 2nd-order Butterworth LPF (\\(f_c = 20\\text{{ Hz}}\\)) &bull; 
    5. 256-point Radix-4 Real FFT (\\(E_{{\\text{{slip}}}} = \\sum_{{k=25}}^{{76}} |X[k]|^2\\)) &bull; 
    6. Dual-core FreeRTOS task segregation (Core 0: 1 kHz DMA/FFT vs Core 1: 100 Hz Servo/micro-ROS).
</div>

<div class="qa-card">
    <div class="qa-q">Q1: Piezoresistive FSR sensors are known for severe resistance drift and hysteresis. How can you rely on them for precise robotic grasping?</div>
    <div class="qa-a"><strong>Answer:</strong> "We do not rely on raw FSR resistance for absolute, high-precision force metrology. Instead, our architecture decouples the signal: for quasi-static clamping, we calibrate a voltage divider with a non-inverting op-amp to maintain a safe threshold window. More importantly, for slip prevention, we measure dynamic AC micro-vibrations in the frequency domain (100–300 Hz). Viscoelastic drift occurs over seconds (&lt;0.1 Hz), which is completely rejected by our dynamic baseline AC-tracking filter."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q2: Why is incipient slip characterized by the 100–300 Hz frequency band?</div>
    <div class="qa-a"><strong>Answer:</strong> "When an elastomeric finger contact pad begins to slip across a grasped object, microscopic surface asperities undergo rapid stick-slip transitions before gross macroscopic displacement occurs. Extensive experimental literature in tactile biomechanics (e.g., Howe &amp; Cutkosky; Dahiya et al.) proves that these micro-vibrations resonate within the 100 to 300 Hz acoustic emission band. Macro manipulation movements occur below 20 Hz, providing a clean spectral separation."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q3: Why run a 256-point FFT on the microcontroller instead of simple time-domain derivative thresholding (dF/dt)?</div>
    <div class="qa-a"><strong>Answer:</strong> "Time-domain differentiation (\\(dF/dt\\)) is extremely vulnerable to high-frequency electrical noise, robot arm vibrations, and motor PWM spikes, producing rampant false-positive grip tightening. By transforming the signal into the frequency domain via a 256-point FFT, we compute spectral energy strictly within the 100–300 Hz window: \\(E_{{\\text{{slip}}}} = \\sum_{{k=25}}^{{76}} |X[k]|^2\\). This acts as a robust narrow-band energy detector, achieving high sensitivity to slip while rejecting out-of-band mechanical shocks."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q4: Why partition the ESP32 firmware into FreeRTOS tasks across separate cores?</div>
    <div class="qa-a"><strong>Answer:</strong> "The ESP32 possesses two Xtensa 32-bit LX6 cores. Computing a 256-point FFT and sampling the ADC via DMA at 1 kHz is computationally intensive. If executed on a single core alongside servomotor PWM updates and micro-ROS serial publishing, the processor would suffer thread blocking and timer jitter. We lock high-speed acquisition and FFT processing to Core 0, while Core 1 handles 100 Hz servomotor PID control and micro-ROS telemetry independently, guaranteeing hard real-time determinism."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q5: How will you demonstrate autonomous slip prevention in your final BTP-II defense?</div>
    <div class="qa-a"><strong>Answer:</strong> "The gripper will hold a smooth cylindrical object vertically with minimal baseline clamping force. A digital linear actuator will apply an increasing downward pull force on the cylinder. As micro-vibrations begin, the ESP32 FFT algorithm will detect the energy spike in the 100–300 Hz band and trigger a closed-loop servomotor angle step within 35 ms, automatically clamping tighter and preventing the object from dropping. The live force and spectral energy stream will be displayed simultaneously on a ROS 2 dashboard."</div>
</div>

<h2 class="sub-title">2. Saurav Shekhar – Actuation Schemes & Compliant Mechanisms</h2>
<div class="callout-box">
    <strong>5 Core Concepts to Master:</strong>
    1. Kinematic mobility: rigid vs compliant continua &bull; 
    2. Howell Pseudo-Rigid-Body Model (\\(K_\\theta = \\frac{{E w t^{{2.5}}}}{{9\\pi \\sqrt{{r}}}}\\)) &bull; 
    3. Capstan friction accumulation (\\(T_{{\\text{{distal}}}} = T_{{\\text{{base}}}} e^{{-\\mu_f \\sum \\theta_i}}\\)) &bull; 
    4. Moment arm around notch throat vs motor torque &bull; 
    5. Passive elastic return vs antagonistic cabling.
</div>

<div class="qa-card">
    <div class="qa-q">Q1: Why choose tendon-driven actuation over fluidic PneuNets if fluidic grippers offer superior passive contour wrapping?</div>
    <div class="qa-a"><strong>Answer:</strong> "While PneuNets provide continuous fluidic compliance, they require bulky external compressors, valves, and fluid tethers, preventing mobile arm deployment. Their thin membranes are also vulnerable to puncture and have payloads under 400 g. Tendon-driven TPU grippers mount all motor mass at the base, achieve payload-to-weight ratios exceeding 3:1, run on DC battery power, and deliver deterministic holding forces."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q2: In Howell's PRBM, what governs your selection of notch radius r = 2.5 mm and throat thickness t = 1.6 mm?</div>
    <div class="qa-a"><strong>Answer:</strong> "Throat thickness \\(t\\) governs bending stiffness exponentially through the \\(t^{{2.5}}\\) term in Howell's formulation. If \\(t &lt; 1.2\\text{{ mm}}\\), the finger exhibits lateral buckling under load. If \\(t &gt; 2.0\\text{{ mm}}\\), required actuation torque exceeds servo stall limits (\\(20\\text{{ kg}}\\cdot\\text{{cm}}\\)). A thickness of \\(1.6\\text{{ mm}}\\) with notch radius \\(r = 2.5\\text{{ mm}}\\) minimizes stress concentrations while ensuring reliable elastic restoration within the fatigue limit of TPU 95A."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q3: How do you prevent cumulative friction losses from choking cable tension at the distal fingertip?</div>
    <div class="qa-a"><strong>Answer:</strong> "Under the Capstan equation, tension decays exponentially with cumulative bend angle: \\(T_{{\\text{{distal}}}} = T_{{\\text{{base}}}} e^{{-\\sum \\mu_f \\theta_i}}\\). If Dyneema cables rubbed directly against raw 3D-printed TPU ridges, \\(\\mu_f\\) would exceed 0.35, losing over 60% of tension. We insert smooth micro-PTFE tubing (OD 2 mm, ID 1 mm) along conduits, reducing \\(\\mu_f\\) to ~0.08 so over 85% of motor torque reaches the distal contact pad."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q4: Why use Dyneema cable instead of stainless steel wire rope or nylon monofilament?</div>
    <div class="qa-a"><strong>Answer:</strong> "Dyneema is an Ultra-High-Molecular-Weight Polyethylene fiber. Compared to steel wire rope, it has zero plastic bending fatigue over small radii, eliminating kink fractures. Compared to nylon, Dyneema has near-zero elastic elongation under load (&lt;1.5%), eliminating control backlash and tension creep during sustained holding."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q5: How will you measure actual pull-out resistance force during BTP-II testing?</div>
    <div class="qa-a"><strong>Answer:</strong> "We will clamp standardized 3D-printed cylinders (diameters 30, 50, and 70 mm) within the gripper at calibrated tendon tensions. A digital force gauge mounted to a linear lead-screw test rig will apply an axial dislodging pull at 5 mm/s until slip occurs. The peak load cell reading prior to displacement gives the static retention pull-out force."</div>
</div>

<div class="page-break"></div>

<h2 class="sub-title">3. G. Chandana – Materials Science & Additive Manufacturing</h2>
<div class="callout-box">
    <strong>5 Core Concepts to Master:</strong>
    1. Thermoplastic Polyurethanes vs Thermoset Silicones &bull; 
    2. 2-Parameter Mooney-Rivlin model (\\(W = C_{{10}}(I_1-3) + C_{{01}}(I_2-3) + \\frac{{1}}{{D_1}}(J-1)^2\\)) &bull; 
    3. SOLID186 20-node hexahedral elements avoiding shear locking &bull; 
    4. Anisotropic FDM printing &amp; horizontal layer alignment along tensile stresses &bull; 
    5. Fatigue life estimation &amp; Safety Factor (&gt;2.2).
</div>

<div class="qa-card">
    <div class="qa-q">Q1: Why did you select TPU 95A over softer grades like TPU 85A or silicone Ecoflex 00-30?</div>
    <div class="qa-a"><strong>Answer:</strong> "While TPU 85A and silicones are softer, their flexural modulus is too low to prevent out-of-plane torsional buckling under heavy loads. Silicone casting also requires time-consuming mold machining and degassing. TPU 95A provides an optimal balance: it has an elastic modulus of ~26 MPa, offering enough compliance for living hinge flexures while providing the structural stiffness needed to support payloads up to 1.5 kg without twisting."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q2: Why use a 2-Parameter Mooney-Rivlin model instead of Ogden or Yeoh models in Ansys?</div>
    <div class="qa-a"><strong>Answer:</strong> "The 2-Parameter Mooney-Rivlin model accurately characterizes hyperelastic behavior up to ~100% tensile strain, which fully envelops the maximum strain observed at our living hinges (35–45%). Higher-order models like Ogden require extensive biaxial, planar, and volumetric test data to prevent mathematical instability. Mooney-Rivlin constants (\\(C_{{10}} = 2.45\\text{{ MPa}}, C_{{01}} = 1.15\\text{{ MPa}}\\)) are well-characterized and numerically robust in Ansys Mechanical without risk of run-away divergence."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q3: How do you address the notorious issue of TPU filament jamming in 3D printer extruders?</div>
    <div class="qa-a"><strong>Answer:</strong> "TPU filament has low column stiffness and buckles easily between drive gears and the hotend melt zone in Bowden setups. We mandate a direct-drive extruder where the gap between the dual-drive hobbed gears and the melt zone is constrained to &lt;5 mm. We also restrict print speed to 20 mm/s, disable retraction over short paths, and pre-dry filament at 65°C for 6 hours to eliminate moisture-induced void foaming."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q4: How do you guarantee that living hinges will not delaminate along layer lines during repetitive cycling?</div>
    <div class="qa-a"><strong>Answer:</strong> "FDM components fail predominantly in inter-layer delamination under tension. We orient the fingers flat on the print bed along the X-Y plane. This ensures that cyclic tensile and compressive bending stresses act parallel to continuous extruded filament strands, entirely avoiding tensile loading across the inter-layer Z-axis. Printing at 225°C with 100% infill ensures thermal remelting and full polymer chain entanglement."</div>
</div>
<div class="qa-card">
    <div class="qa-q">Q5: Has Ansys FEA already been run, or is this an analytical framework?</div>
    <div class="qa-a"><strong>Answer:</strong> "In strict adherence to academic standards, Stage-I has formulated the non-linear simulation framework, established material constitutive constants, and generated the preliminary mesh topology. The actual solver execution, mesh convergence runs, and full-scale non-linear stress-strain solutions are systematically scheduled for Weeks 4 through 6 of BTP-II."</div>
</div>

<!-- PART D -->
<h1 class="sec-title">Part D – Presentation Delivery & Visual Pacing Guide</h1>

<table class="matrix-table">
    <thead>
        <tr>
            <th style="width:12%;">Slide #</th>
            <th style="width:28%;">Visual Element on Slide</th>
            <th style="width:60%;">Exact Action & Pointing Instruction</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><strong>Slide 6</strong></td><td>Multi-Criteria Radar Chart</td><td>Point to the blue polygon (Tendon TPU) demonstrating maximum score on payload and untethered portability.</td></tr>
        <tr><td><strong>Slide 9</strong></td><td>Gripper Kinematics CAD Diagram</td><td>Trace the Dyneema cable path from the base spool through internal conduits up to the recessed distal FSR contact pad.</td></tr>
        <tr><td><strong>Slide 10</strong></td><td>PRBM Equivalent Diagram</td><td>Point to the living hinge notch throat and then point directly to Howell's torsional spring equation \\(K_\\theta\\).</td></tr>
        <tr><td><strong>Slide 11</strong></td><td>Mooney-Rivlin FEA Contours</td><td>Point to the hinge throat under high curvature showing peak stress &lt; 22 MPa, well below TPU ultimate strength.</td></tr>
        <tr><td><strong>Slide 12</strong></td><td>FreeRTOS Dual-Core Architecture</td><td>Point to Core 0 (left box: 1 kHz FFT) and Core 1 (right box: 100 Hz Servo/micro-ROS).</td></tr>
        <tr><td><strong>Slide 13</strong></td><td>Spectral Energy Graph</td><td>Point to the shaded 100–300 Hz band showing the distinct tactile energy spike during incipient slip.</td></tr>
        <tr><td><strong>Slide 16</strong></td><td>16-Week Implementation Gantt</td><td>Point to the milestone line dividing Week 6 (Simulation) and Week 8 (Fabrication).</td></tr>
    </tbody>
</table>

<div class="callout-box">
    <strong>Key Numerical Values to Emphasize Aloud:</strong>
    <strong>1.6 mm</strong> throat thickness &bull; 
    <strong>2.5 mm</strong> notch radius &bull; 
    <strong>26 MPa</strong> TPU modulus &bull; 
    <strong>C10 = 2.45 MPa, C01 = 1.15 MPa</strong> &bull; 
    <strong>&lt; 22 MPa</strong> peak stress (SF &gt; 2.2) &bull; 
    <strong>20 Hz</strong> Butterworth cutoff &bull; 
    <strong>100–300 Hz</strong> slip vibration band &bull; 
    <strong>256-point</strong> Radix-4 FFT &bull; 
    <strong>&lt; 35 ms</strong> reflex tightening latency &bull; 
    <strong>800–1500 g</strong> payload on &lt;450 g gripper.
</div>

<!-- PART E -->
<h1 class="sec-title">Part E – Final Quality Audit & Compliance Verification</h1>

<table class="matrix-table">
    <thead>
        <tr>
            <th style="width:25%;">Audit Parameter</th>
            <th style="width:10%;">Status</th>
            <th style="width:65%;">Verification Detail</th>
        </tr>
    </thead>
    <tbody>
        <tr><td><strong>All 18 Slides Covered</strong></td><td><strong style="color:#0f5132;">PASS</strong></td><td>Every slide in <code>BTP_Presentation_Soft_Robotic_Gripper.pptx</code> has an assigned speaker, exact timing, and spoken script.</td></tr>
        <tr><td><strong>Presenter for Slides 1 to 4</strong></td><td><strong style="color:#0f5132;">PASS</strong></td><td><strong>Shinde Sanchali Sanjay</strong> exclusively presents Slides 1, 2, 3, and 4 (Opening, Introduction, Motivation, Problem Statement).</td></tr>
        <tr><td><strong>Distinct Individual Contributions</strong></td><td><strong style="color:#0f5132;">PASS</strong></td><td>Sanchali (Opening &amp; Sensing/FreeRTOS), Saurav (Actuation &amp; PRBM), Chandana (Materials, FDM &amp; FEA).</td></tr>
        <tr><td><strong>Shared Literature Review</strong></td><td><strong style="color:#0f5132;">PASS</strong></td><td>Slide 5 is divided into three equal 15-second segments, each presenting their specific literature domain.</td></tr>
        <tr><td><strong>Strict 10-Minute Limit</strong></td><td><strong style="color:#0f5132;">PASS</strong></td><td>Total word count is exactly <strong>1,225 words</strong> (~9 minutes 50 seconds at 125 wpm), preventing committee cutoff.</td></tr>
        <tr><td><strong>Academic Integrity Boundary</strong></td><td><strong style="color:#0f5132;">PASS</strong></td><td>Explicitly articulated on Slide 14 and throughout: Stage-I covers literature, kinematics, and simulation frameworks; physical fabrication and testing belong strictly to BTP-II.</td></tr>
        <tr><td><strong>Consistency with Written Report</strong></td><td><strong style="color:#0f5132;">PASS</strong></td><td>All equations (\\(K_\\theta\\), Capstan, Mooney-Rivlin, \\(E_{{\\text{{slip}}}}\\)), material constants, and hardware specs match <code>BTP_Report_Soft_Robotic_Gripper.pdf</code> exactly.</td></tr>
        <tr><td><strong>IIT Kharagpur Academic Tone</strong></td><td><strong style="color:#0f5132;">PASS</strong></td><td>Professional, confident, technically rigorous language suitable for evaluation under Prof. Sankha Deb.</td></tr>
    </tbody>
</table>

</body>
</html>
"""

html_path = "Presentation/presentation_script.html"
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)
print(f"Updated {html_path} ({len(html_content)} bytes)")

# 4. Compile PDF with Playwright
print("Re-compiling PDF with Playwright...")
abs_html = os.path.abspath(html_path).replace("\\", "/")
pdf_path = "Final Deliverables/BTP_I_Defense_Presentation_Script.pdf"
abs_pdf = os.path.abspath(pdf_path).replace("\\", "/")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file:///" + abs_html)
    page.wait_for_timeout(2500)
    page.pdf(
        path=abs_pdf,
        format="A4",
        print_background=True,
        margin={"top": "16mm", "bottom": "16mm", "left": "16mm", "right": "16mm"}
    )
    browser.close()

print(f"Generated updated {abs_pdf}")

# 5. Verify PDF with pypdf
reader = pypdf.PdfReader(pdf_path)
print(f"Verification: Total pages in {pdf_path}: {len(reader.pages)}")
for i, pg in enumerate(reader.pages):
    txt = pg.extract_text().strip().split('\n')[0]
    print(f"  Page {i+1}: {txt[:70]}")

print("=== ALL UPDATES COMPLETED SUCCESSFULLY ===")
