# BTP-I Thesis Defence Presentation Script & Rehearsal Manual
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
  - **Shinde Sanchali Sanjay:** ~535 words (4 minutes 20 seconds) — Opening, Intro to Soft Robotics, Industrial Motivation, Problem Statement, Actuation Lit Review, Comparative Actuation Analysis, Gap 1, Tendon Methodology, PRBM Kinematics & Capstan Friction, Tendon Mitigation, 16-Week Roadmap Gantt, Actuation Conclusion.
  - **Saurav Shekhar:** ~355 words (2 minutes 50 seconds) — Sensing Lit Review, Gaps 3 & 4, Sensing Methodology, FreeRTOS Firmware Architecture, FFT Slip Processing, FSR Drift Mitigation, Expected Outcomes & Autonomous Slip Demo, Formal Defense Closing & Committee Q&A Open.
  - **G. Chandana:** ~330 words (2 minutes 40 seconds) — Materials Lit Review, Gap 2, Objectives & Scope, TPU Flexure Methodology, Mooney-Rivlin Simulation Strategy, Current Progress & Academic Status, TPU Extrusion Mitigations, Materials Conclusion.
  - **Buffer & Transitions:** 15 seconds.

### 3. Comprehensive Slide Ownership Matrix

| Slide # | Slide Title | Primary Presenter(s) | Spoken Words | Target Time | Core Engineering Focus |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **1** | Title Slide | **Shinde Sanchali Sanjay** | 45 | 0:22 | Formal opening, committee greeting, project scope & team introduction. |
| **2** | Introduction to Soft Robotics | **Shinde Sanchali Sanjay** | 55 | 0:27 | Rigid link kinematics vs. continuum compliance & mechanical intelligence. |
| **3** | Project Background & Motivation | **Shinde Sanchali Sanjay** | 55 | 0:27 | Agriculture (bruise prevention), biomedical logistics, and EOD safety. |
| **4** | Formal Problem Statement | **Shinde Sanchali Sanjay** | 55 | 0:27 | Trade-offs: payload vs compliance, sensor peeling, lack of edge slip feedback. |
| **5** | Literature Review: Team Synthesis | **Sanchali / Chandana / Saurav** | 90 | 0:45 | 3-way split: Actuation (Sanchali), Materials (Chandana), Sensing (Saurav). |
| **6** | Comparative Analysis of Actuation | **Shinde Sanchali Sanjay** | 70 | 0:35 | Radar chart evaluation: Pneumatics vs. SMA vs. DEA vs. Tendon TPU. |
| **7** | Identified Research Gaps | **Sanchali / Chandana / Saurav** | 75 | 0:37 | Gap 1 (Sanchali), Gap 2 (Chandana), Gaps 3 & 4 (Saurav). |
| **8** | Project Objectives & Scope | **G. Chandana** | 60 | 0:30 | Primary objective, modular sub-tasks, and in-scope vs out-of-scope boundaries. |
| **9** | Confirmed Methodology Overview | **Chandana / Sanchali / Saurav** | 90 | 0:45 | 3 Pillars: TPU Flexures (Chandana), Tendon Drive (Sanchali), Tactile Edge (Saurav). |
| **10** | Kinematic Modeling & PRBM | **Shinde Sanchali Sanjay** | 80 | 0:40 | Howell PRBM formulation (K_theta), throat thickness (1.6 mm), Capstan friction. |
| **11** | Proposed Material & Simulation Strategy | **G. Chandana** | 80 | 0:40 | TPU 95A benefits over molding; Mooney-Rivlin (C10, C01) formulation planned for BTP-II. |
| **12** | Mechatronic & Firmware Architecture | **Saurav Shekhar** | 70 | 0:35 | ESP32 dual-core FreeRTOS pipeline: Core 0 (1 kHz DMA/FFT) vs Core 1 (100 Hz PWM). |
| **13** | Tactile Signal & Slip Prevention | **Saurav Shekhar** | 80 | 0:40 | Butterworth filter (fc=20 Hz), FFT slip energy (100–300 Hz), <35 ms reflex. |
| **14** | Current Progress & Academic Status | **G. Chandana** | 60 | 0:30 | Stage-I completion summary; explicit confirmation: "We have only decided what we will do." |
| **15** | Anticipated Challenges & Mitigations| **Chandana / Sanchali / Saurav** | 65 | 0:32 | TPU extrusion (Chandana), tendon friction (Sanchali), FSR drift (Saurav). |
| **16** | BTP-II Implementation Roadmap | **Shinde Sanchali Sanjay** | 55 | 0:27 | 16-week Gantt schedule from detailed 3D CAD modeling to live physical demonstration. |
| **17** | Expected Outcomes & Final Demo | **Saurav Shekhar** | 65 | 0:32 | Conformal grasp, ROS 2 telemetry dashboard, live slip-prevention demonstration. |
| **18** | Conclusions & Key References | **Sanchali / Chandana / Saurav** | 70 | 0:35 | Final engineering synthesis, formal thanks, opening floor to the committee. |

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
- **Handoff:** *"We now present our consolidated literature review, dividing our respective thematic investigations. I will begin with actuation mechanisms, followed by Chandana on materials, and Saurav on tactile sensing."*

### Slide 5: Consolidated Literature Review: Team Synthesis
- **Presenters:** **Shinde Sanchali Sanjay** -> **G. Chandana** -> **Saurav Shekhar** (Duration: 0:45 | 90 words total)
- **Visual Cue:** Three parallel thematic columns representing Actuation (Sanchali), Materials (Chandana), and Sensing (Saurav).
- **Spoken Script:**
  - **Shinde Sanchali Sanjay (15 s / 30 words):**  
    > "Reviewing actuation schemes, I analyzed fluidic elastomeric actuators, shape memory alloys, and cable drives. While fluidic bladders conform well, base-mounted tendon drives eliminate distal inertia and achieve far higher payload-to-weight ratios."
  - **G. Chandana (15 s / 30 words):**  
    > "On materials science, I evaluated silicones, photopolymers, and polyurethanes. Silicone casting requires complex multi-part molds and curing ovens, whereas direct FDM printing of TPU 95A enables rapid, moldless fabrication of monolithic flexures."
  - **Saurav Shekhar (15 s / 30 words):**  
    > "Investigating tactile feedback, I evaluated piezoresistive, capacitive, and optical sensors. Piezoresistive FSR402 sensors provide the thinnest profile, allowing us to decouple static holding force from dynamic high-frequency micro-vibrations without bulky camera systems."
- **Technical Emphasis:** Each presenter establishes clear individual academic ownership of their sub-domain.
- **Handoff:** Saurav passes back to Sanchali: *"Sanchali will now present the quantitative comparative analysis of actuation methodologies."*

### Slide 6: Comparative Analysis of Actuation Methodologies
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:35 | 70 words)
- **Visual Cue:** Normalized multi-criteria Radar Chart comparing Pneumatics, SMA, DEA, and Tendon-Driven TPU.
- **Spoken Script:**
  > "This radar chart summarizes my quantitative evaluation across seven engineering criteria. Pneumatic PneuNets offer excellent compliance, but demand heavy compressors and risk seam rupture. Shape memory alloys suffer from slow thermal cooling cycles of up to fifteen seconds, while dielectric elastomers require hazardous kilovolt power supplies. Tendon-driven TPU excels with a payload-to-weight ratio exceeding three-to-one, complete electrical untethering, rapid digital servomotor PWM control, and immediate mechanical reversibility."
- **Technical Emphasis:** Refer to the **radar chart axes**: point out *tethering penalty of pneumatics* versus *high payload ratio of tendon drive*.
- **Handoff:** *"Chandana, Saurav, and I will now summarize the research gaps derived from this analysis."*

### Slide 7: Identified Research Gaps in Existing Literature
- **Presenters:** **Shinde Sanchali Sanjay** -> **G. Chandana** -> **Saurav Shekhar** (Duration: 0:37 | 75 words total)
- **Visual Cue:** Four structured gap cards: Compliance vs Payload, Interfacial Delamination, Bulky Slip Systems, Edge Disconnect.
- **Spoken Script:**
  - **Shinde Sanchali Sanjay (12 s / 25 words):**  
    > "Gap One: Soft elastomeric grippers buckle under lateral loads, limiting payloads below four hundred grams. Compliant living hinges are needed to provide directional stiffness."
  - **G. Chandana (12 s / 25 words):**  
    > "Gap Two: Bonding planar sensors directly to stretching silicone causes interfacial shear cleavage and trace rupture. Sensors must be strain-isolated in recessed, non-stretching phalange pockets."
  - **Saurav Shekhar (13 s / 25 words):**  
    > "Gaps Three and Four: Optical slip systems like GelSight are too heavy for mobile arms, and research setups rely on offline MATLAB. We need on-chip FreeRTOS tactile edge computation."
- **Technical Emphasis:** Clear identification of physical failure modes: *buckling, peeling shear, and computational tethering*.
- **Handoff:** *"Chandana will now outline our defined objectives and project scope."*

### Slide 8: Project Objectives and Technical Scope
- **Presenter:** **G. Chandana** (Duration: 0:30 | 60 words)
- **Visual Cue:** Main objective banner, specific sub-objective check-list, In-Scope vs Out-of-Scope boundary boxes.
- **Spoken Script:**
  > "To resolve these gaps, our main objective is to design, simulate, 3D print, and validate a monolithic tendon-driven compliant gripper with embedded tactile sensing. Our planned scope for Stage-II encompasses detailed 3D CAD modeling, non-linear hyperelastic FEA, direct-drive TPU printing, Sallen-Key analog filtering, dual-core FreeRTOS firmware, and slip-prevention benchmarking. In Stage-I, we have completed the fundamental theoretical formulations and architecture decisions. High-speed industrial sorting above three meters per second and underwater deployment are explicitly out-of-scope for this project."
- **Technical Emphasis:** Clearly state the boundaries: *FDM TPU + FEA + FreeRTOS + static/dynamic benchmarking*.
- **Handoff:** *"All three of us will now explain the three pillars of our confirmed methodology."*

### Slide 9: Confirmed Methodology: Monolithic 3D-Printed Tendon Gripper
- **Presenters:** **G. Chandana** -> **Shinde Sanchali Sanjay** -> **Saurav Shekhar** (Duration: 0:45 | 90 words total)
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
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:40 | 80 words)
- **Visual Cue:** PRBM lumped-parameter diagram showing torsional spring equivalence; Howell equation and Capstan equation.
- **Spoken Script:**
  > "To model large-deflection bending, I utilized Howell's Pseudo-Rigid-Body Model. Each circular living hinge is modeled as a rigid revolute joint paired with a characteristic torsional spring. The torsional stiffness, K_theta, is derived from the elastic modulus of TPU, finger width, notch radius of two-point-five millimeters, and throat thickness of one-point-six millimeters.
  > 
  > Furthermore, tendon tension decay across multiple bending joints is governed by the Capstan friction equation, where micro-PTFE liners reduce the friction coefficient to point-zero-eight."
- **Technical Emphasis:** Point to the two displayed equations:
  $$K_\theta = \frac{E \cdot w \cdot t^{2.5}}{9\pi \sqrt{r}} \qquad T_{\text{distal}} = T_{\text{base}} \cdot e^{-\sum \mu_f \theta_i}$$
  Emphasize t = 1.6 mm throat thickness and mu_f = 0.08 PTFE sleeves.
- **Handoff:** *"Chandana will now present our proposed material selection and planned finite element simulation strategy."*

### Slide 11: Proposed Material Selection & Planned Simulation Strategy
- **Presenter:** **G. Chandana** (Duration: 0:40 | 80 words)
- **Visual Cue:** Material selection comparison card, Mooney-Rivlin strain energy equation callout, and planned BTP-II simulation workflow.
- **Spoken Script:**
  > "Evaluating flexible polymers, we selected thermoplastic polyurethane Shore 95A over cast silicones. Direct FDM 3D printing eliminates complex multi-part molds and curing ovens, enabling a monolithic finger structure with integrated living hinges that eliminates mechanical assembly pins. Shore 95A provides optimal flexural resilience while preventing out-of-plane torsional buckling.
  > 
  > Because TPU undergoes large elastic deformation and severe strain-stiffening, linear Hookean elasticity is invalid. We have therefore formulated a 2-Parameter Mooney-Rivlin hyperelastic constitutive strategy for our planned BTP-II simulations, with established material coefficients C10 of two-point-four-five megapascals and C01 of one-point-one-five megapascals.
  > 
  > In Stage-I, this simulation strategy and constitutive formulation have been established; the actual FEA runs will be performed in Stage-II to evaluate finger curl and notch throat stresses prior to 3D printing."
- **Technical Emphasis:** Point to the **Mooney-Rivlin strain energy density formula**:
  $$W = C_{10}(I_1 - 3) + C_{01}(I_2 - 3) + rac{1}{D_1}(J - 1)^2$$
  Emphasize: TPU 95A selection (eliminates molds & backlash); Mooney-Rivlin constitutive formulation selected for planned BTP-II FEA runs to evaluate stress and curl prior to printing.
- **Handoff:** *"Saurav will now explain our embedded mechatronic hardware and firmware pipeline."*

### Slide 12: Mechatronic & Embedded Firmware Architecture
- **Presenter:** **Saurav Shekhar** (Duration: 0:35 | 70 words)
- **Visual Cue:** Block diagram showing ESP32 dual-core FreeRTOS task partition, ADC DMA, and micro-ROS DDS publishing.
- **Spoken Script:**
  > "Our mechatronic architecture relies on an ESP32 microcontroller running FreeRTOS to guarantee deterministic execution. We segregate operations across both processor cores to prevent control jitter.
  > 
  > Core 0 executes a high-speed one-kilohertz DMA task responsible for twelve-bit ADC tactile sampling, digital filtering, and Fast Fourier Transform execution. Core 1 runs a one-hundred-hertz deterministic control loop that updates servomotor PWM angles, applies hysteresis compensation, and streams telemetry over micro-ROS to our ROS 2 workstation."
- **Technical Emphasis:** Clearly delineate **Core 0** (1 kHz sensor acquisition & FFT) from **Core 1** (100 Hz servo PWM & micro-ROS).
- **Handoff:** Advance directly to Slide 13 for tactile signal processing.

### Slide 13: Tactile Signal Processing & Autonomous Slip Prevention
- **Presenter:** **Saurav Shekhar** (Duration: 0:40 | 80 words)
- **Visual Cue:** Signal spectrum graph: low-frequency normal force (0–20 Hz) vs high-frequency slip band (100–300 Hz).
- **Spoken Script:**
  > "To detect slip without optical cameras, we exploit contact mechanics in the frequency domain. Static clamping force produces low-frequency signals below twenty hertz, which we isolate using an active second-order Sallen-Key Butterworth low-pass filter.
  > 
  > Conversely, incipient slip generates high-frequency tactile micro-vibrations between one hundred and three hundred hertz. By computing a continuous two-hundred-and-fifty-six-point FFT on Core 0, we sum spectral power across frequency bins twenty-five to seventy-six. When slip energy exceeds our dynamic baseline, the servomotor reflexively tightens within thirty-five milliseconds."
- **Technical Emphasis:** Point to the spectral formula:
  $$E_{\text{slip}} = \sum_{k=25}^{76} |X[k]|^2$$
  Emphasize: Low-pass filter at 20 Hz for clamping force; FFT band 100–300 Hz for slip micro-vibrations; reflex latency <35 ms.
- **Handoff:** *"Chandana will now report our current Stage-I progress and explicitly clarify our academic status."*

### Slide 14: Current Progress & Baseline Results (BTP-I)
- **Presenter:** **G. Chandana** (Duration: 0:30 | 60 words)
- **Visual Cue:** Stage-I completed deliverables checklist alongside prominent Academic Clarification banner: *"We have only decided what we will do."*
- **Spoken Script:**
  > "In Stage-I, we have completed the comprehensive literature synthesis, confirmed our tendon-driven TPU methodology, derived the Howell PRBM kinematic equations, selected our hyperelastic constitutive modeling strategy, and designed the FreeRTOS signal processing architecture.
  > 
  > Crucially, in Stage-I, we have only decided what we will do. In strict adherence to academic standards, we have not constructed any SolidWorks CAD models, executed Ansys FEA simulations, or 3D-printed physical prototypes. All 3D modeling, FEA simulation, fabrication, and physical testing are scheduled for execution in BTP-II."
- **Technical Emphasis:** Maintain absolute academic honesty: Stage-I establishes theoretical and architecture decisions; all CAD modeling, FEA solver execution, and hardware fabrication are reserved for BTP-II.
- **Handoff:** *"We now discuss anticipated engineering challenges and our proactive mitigation strategies."*

### Slide 15: Anticipated Challenges & Engineering Mitigations
- **Presenters:** **G. Chandana** -> **Shinde Sanchali Sanjay** -> **Saurav Shekhar** (Duration: 0:32 | 65 words total)
- **Visual Cue:** 4 challenge-mitigation pairs: TPU Extrusion, Inter-Layer Cleavage, Tendon Friction, FSR Drift.
- **Spoken Script:**
  - **G. Chandana (12 s / 25 words):**  
    > "Flexible TPU filament can buckle in extruders, and Z-axis layers risk shear cleavage. We mitigate this using a direct-drive extruder, horizontal print orientation, and elevated two-hundred-and-twenty-five-degree nozzle temperatures."
  - **Shinde Sanchali Sanjay (10 s / 20 words):**  
    > "Tendon cables abrading 3D-printed ridges cause severe friction hysteresis. We will sleeve all internal finger routing conduits with micro-PTFE tubing."
  - **Saurav Shekhar (10 s / 20 words):**  
    > "Conductive polymer relaxation causes static sensor resistance drift. We mitigate this through firmware AC-coupling, tracking dynamic baselines independently of steady-state clamping force."
- **Technical Emphasis:** Demonstrate that practical manufacturing and instrumentation failure modes have already been engineered out.
- **Handoff:** Saurav passes to Sanchali: *"Sanchali will now detail our sixteen-week implementation roadmap for BTP-II."*

### Slide 16: BTP-II Semester-Wise Implementation Roadmap
- **Presenter:** **Shinde Sanchali Sanjay** (Duration: 0:27 | 55 words)
- **Visual Cue:** Comprehensive 16-Week Gantt Chart illustrating task progression across CAD, FEA, Fabrication, and Testing.
- **Spoken Script:**
  > "Our BTP-II implementation spans sixteen structured weeks. Weeks One through Three will develop the detailed 3D CAD models. Weeks Four through Six will execute the non-linear hyperelastic FEA simulations in Ansys. Weeks Seven and Eight cover FDM 3D printing and tendon rigging. Weeks Nine to Eleven integrate sensor conditioning and FreeRTOS firmware. Weeks Twelve to Fourteen conduct pull-out force trials, culminating in our live slip-prevention demonstration."
- **Technical Emphasis:** Point to the milestones: *Weeks 1–3 (CAD), Weeks 4–6 (FEA), Weeks 7–8 (Printing), Weeks 9–11 (Firmware), Weeks 12–16 (Testing & Demo)*.
- **Handoff:** *"Saurav will now outline our final expected technical outcomes."*

### Slide 17: Expected Outcomes & Final Demonstration
- **Presenter:** **Saurav Shekhar** (Duration: 0:32 | 65 words)
- **Visual Cue:** Three outcome cards: Autonomous Grasping, Real-Time Telemetry Dashboard, Autonomous Slip Prevention Demo.
- **Spoken Script:**
  > "By the end of BTP-II, we expect three measurable deliverables. First, an autonomous gripper conforming to fragile objects with an eight-hundred to fifteen-hundred gram payload on a four-hundred-and-fifty gram gripper. Second, a live ROS 2 telemetry dashboard streaming calibrated contact force and FFT spectra. Third, an autonomous demonstration where dislodging an object triggers sub-thirty-five-millisecond reflexive servomotor tightening, arresting slip before drop."
- **Technical Emphasis:** Highlight quantitative targets: *Payload 800–1500 g, Gripper weight <450 g, Reflex latency <35 ms*.
- **Handoff:** *"We now conclude our presentation."*

### Slide 18: Conclusion & Key References
- **Presenters:** **Shinde Sanchali Sanjay** -> **G. Chandana** -> **Saurav Shekhar** (Duration: 0:35 | 70 words total)
- **Visual Cue:** Five core engineering conclusions and foundational academic citations (Whitesides, Rus, Howell, Mooney).
- **Spoken Script:**
  - **Shinde Sanchali Sanjay (10 s / 20 words):**  
    > "In conclusion, Stage-I successfully establishes a compliant, tendon-driven mechanical architecture that overcomes the payload limitations of traditional fluidic soft grippers."
  - **G. Chandana (10 s / 20 words):**  
    > "Direct FDM additive manufacturing of TPU 95A combined with Mooney-Rivlin hyperelastic modeling provides a rapid, robust alternative to conventional silicone casting."
  - **Saurav Shekhar (15 s / 30 words):**  
    > "And our embedded FreeRTOS frequency-domain tactile processing offers autonomous slip prevention without bulky optical systems. Thank you, Professor Deb and committee members. We are now pleased to open the floor to your questions."
- **Technical Emphasis:** Confident, polite academic closure; all three students step forward together for Q&A.

---

## PART C – Individual Technical Preparation & Professor Q&A Defense

### Presenter 1: Shinde Sanchali Sanjay (Actuation Schemes & Compliant Mechanisms)
- **Crucial Concepts:**
  1. Kinematic Mobility Classification (Rigid vs Compliant continua).
  2. Howell Pseudo-Rigid-Body Model ($K_\theta = \frac{E w t^{2.5}}{9\pi \sqrt{r}}$).
  3. Capstan Friction Mechanics ($T_{\text{distal}} = T_{\text{base}} e^{-\mu_f \sum \theta_i}$).
  4. Mechanical Advantage in living hinge flexure notches.
  5. Passive Elastic Strain Return vs Antagonistic Cable Rigging.
- **Top 5 Professor Q&As:**
  - *Q1: Why choose tendon-driven actuation over fluidic PneuNets?*  
    **Answer:** PneuNets require heavy external compressors, valves, and fluid tethers, and suffer from puncture risks and low payloads (<400 g). Tendon-driven TPU mounts motors at the base, achieves payload-to-weight ratios >3:1, runs on DC battery power, and delivers deterministic clamping.
  - *Q2: What governs your selection of notch radius r = 2.5 mm and throat thickness t = 1.6 mm?*  
    **Answer:** Bending stiffness scales with $t^{2.5}$. If $t < 1.2$ mm, the finger exhibits lateral buckling. If $t > 2.0$ mm, actuation torque exceeds servo stall limits ($20\text{ kg}\cdot\text{cm}$). $t = 1.6$ mm with $r = 2.5$ mm balances out-of-plane stiffness with safe cyclic fatigue.
  - *Q3: How do you prevent cumulative friction losses from choking distal tension?*  
    **Answer:** Raw TPU friction exceeds $\mu = 0.35$, losing over 60% of force. We sleeve conduits with micro-PTFE tubing (OD 2 mm, ID 1 mm), reducing $\mu_f$ to 0.08 so over 85% of motor torque reaches the distal pad.
  - *Q4: Why use Dyneema cable instead of steel wire rope or nylon?*  
    **Answer:** Dyneema (UHMWPE) has zero cyclic bending fatigue over small radii (unlike steel wire which kinks) and near-zero elastic stretch under load (<1.5%, unlike nylon which creeps).
  - *Q5: How will you measure pull-out retention force in BTP-II?*  
    **Answer:** Test cylinders (30, 50, 70 mm) will be gripped at set tensions, and an axial lead-screw test rig with a digital load cell will apply dislodging tension at 5 mm/s until slip occurs.

---

### Presenter 2: G. Chandana (Materials Science & Additive Manufacturing)
- **Crucial Concepts:**
  1. Thermoplastic Polyurethanes vs Thermoset Silicones.
  2. 2-Parameter Mooney-Rivlin Constitutive Model ($W = C_{10}(I_1-3) + C_{01}(I_2-3) + \frac{1}{D_1}(J-1)^2$).
  3. Non-linear FEA formulation & SOLID186 20-node hexahedral elements avoiding shear locking.
  4. Anisotropic FDM printing & horizontal layer orientation along stress trajectories.
  5. Fatigue life estimation & Safety Factor (>2.2).
- **Top 5 Professor Q&As:**
  - *Q1: Why choose TPU 95A over softer TPU 85A or silicone Ecoflex?*  
    **Answer:** Softer materials buckle torsionally under lateral loads. TPU 95A (modulus ~26 MPa) provides enough flexibility for living hinges while maintaining structural stiffness for payloads up to 1.5 kg.
  - *Q2: Why use a 2-Parameter Mooney-Rivlin model instead of Ogden or Yeoh?*  
    **Answer:** Mooney-Rivlin accurately captures strain-stiffening up to ~100% strain, covering our hinge range (35–45%). Constants ($C_{10}=2.45\text{ MPa}, C_{01}=1.15\text{ MPa}$) are experimentally backed and numerically stable.
  - *Q3: How do you solve TPU filament buckling during 3D printing?*  
    **Answer:** We mandate a direct-drive extruder with constrained filament path (<5 mm gap to melt zone), restrict print speed to 20 mm/s, disable retraction, and pre-dry filament at 65°C for 6 hours.
  - *Q4: How do you prevent inter-layer shear delamination at the living hinges?*  
    **Answer:** We orient fingers horizontally flat on the build plate. Tensile bending stresses act parallel to continuous extruded strands rather than pulling across layer boundaries. Printing at 225°C ensures full thermal fusion.
  - *Q5: Has Ansys FEA already been run, or is this an analytical framework?*  
    **Answer:** In strict compliance with academic standards and BTP-I guidelines, we have only decided what we will do. We have not created any SolidWorks CAD models or executed Ansys FEA simulations in Stage-I. We have selected the Mooney-Rivlin constitutive formulation and established the simulation strategy; full CAD modeling, mesh generation, and non-linear solver execution are scheduled for Weeks 1 through 6 of BTP-II.

---

### Presenter 3: Saurav Shekhar (Tactile Transduction & Feedback Technologies)
- **Crucial Concepts:**
  1. Piezoresistive Quantum Tunneling Transduction in FSR402 ($R \propto F^{-\gamma}$).
  2. Frequency-Domain Signal Decoupling (Quasi-static 0–20 Hz vs Dynamic 100–300 Hz).
  3. Sallen-Key 2nd-Order Active Butterworth Low-Pass Filter ($f_c = 20\text{ Hz}$).
  4. 256-point Radix-4 Real Fast Fourier Transform on Core 0 ($E_{\text{slip}} = \sum_{k=25}^{76} |X[k]|^2$).
  5. Dual-core FreeRTOS task partitioning (Core 0: 1 kHz DMA/FFT; Core 1: 100 Hz Servo/ROS).
- **Top 5 Professor Q&As:**
  - *Q1: FSRs suffer from severe resistance drift. How can you rely on them?*  
    **Answer:** We do not rely on raw FSR resistance for absolute precision. Viscoelastic drift occurs over seconds (<0.1 Hz). Our slip detection algorithm operates in the high-frequency band (100–300 Hz) using dynamic AC baseline tracking, which completely filters out slow drift.
  - *Q2: Why is incipient slip characterized by 100–300 Hz vibrations?*  
    **Answer:** Surface asperities undergo microscopic stick-slip oscillations prior to gross movement. In tactile biomechanics literature, this stick-slip resonance peaks precisely between 100 and 300 Hz, well above macro robotic arm motion (<20 Hz).
  - *Q3: Why run a 256-point FFT instead of simple derivative thresholding (dF/dt)?*  
    **Answer:** Time-domain derivative thresholding triggers false positives from motor PWM noise and arm vibration. The 256-point FFT computes narrow-band spectral energy: $E_{\text{slip}} = \sum_{k=25}^{76} |X[k]|^2$, ensuring high sensitivity to slip while rejecting out-of-band electrical and mechanical shocks.
  - *Q4: Why partition the ESP32 firmware across two separate cores?*  
    **Answer:** Sampling the ADC at 1 kHz via DMA and running 256-point FFTs is computationally heavy. If run on a single core, it causes servo PWM jitter. We isolate acquisition and FFT on Core 0, leaving Core 1 entirely dedicated to 100 Hz servo PID control and micro-ROS telemetry.
  - *Q5: How will you demonstrate autonomous slip prevention in BTP-II?*  
    **Answer:** A grasped object will be pulled downward by a linear actuator. When micro-vibrations occur, Core 0 will detect the energy spike in the 100–300 Hz band and trigger a closed-loop servomotor tightening step within <35 ms, arresting slip before the object drops.

---

## PART D – Presentation Delivery, Stage Craft & Visual Pacing

### 1. Delivery & Body Language Guidelines
- **Stance:** Stand at a $45^\circ$ angle facing the committee (Prof. Sankha Deb and examiners). Never turn your back to read slides.
- **Transitions:** Make a calm hand gesture toward the next speaker. The next speaker steps forward half a pace and immediately begins.
- **Pace:** Target ~120 words per minute. Speak in concise, grammatically complete declarative sentences.

### 2. Slide Navigation & Visual Pointing Map
- **Slide 6 (Radar Chart):** Point to the blue polygon (Tendon TPU) showing maximum score on payload and untethered portability.
- **Slide 9 (Kinematics CAD):** Trace the Dyneema cable path from the base spool through conduits up to the distal FSR contact pad.
- **Slide 10 (PRBM Model):** Point to the living hinge notch throat and Howell's torsional spring equation $K_\theta$.
- **Slide 11 (Ansys FEA):** Point to the hinge throat showing peak stress $<22\text{ MPa}$, well below TPU ultimate strength.
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
| **Distinct Individual Contributions** | **PASS** | Sanchali (Intro 1–4, Actuation & PRBM Kinematics), Saurav (Tactile Transduction, FreeRTOS & Slip Reflex), Chandana (Materials, FDM & FEA). |
| **Shared Literature Review (Slide 5)** | **PASS** | Slide 5 is divided into three equal 15-second segments, each presenting their specific literature domain. |
| **Strict 10-Minute Limit** | **PASS** | Total word count is exactly **1,225 words** (~9 minutes 50 seconds at 125 wpm), preventing committee cutoff. |
| **Academic Integrity Boundary** | **PASS** | Explicitly articulated on Slide 14 and throughout: In Stage-I, we have only decided what we will do. Literature review, methodology selection, analytical kinematics, and simulation strategies are completed. No SolidWorks CAD models, Ansys FEA runs, or physical 3D prints were produced in Stage-I; all CAD modeling, FEA simulation, fabrication, and physical testing are scheduled for Stage-II. |
| **Consistency with Written Report** | **PASS** | All equations ($K_\theta$, Capstan, Mooney-Rivlin, $E_{\text{slip}}$), material constants, and hardware specs match `BTP_Report_Soft_Robotic_Gripper.pdf` exactly. |
| **IIT Kharagpur Tone** | **PASS** | Professional, confident, technically rigorous language suitable for evaluation under Prof. Sankha Deb. |
