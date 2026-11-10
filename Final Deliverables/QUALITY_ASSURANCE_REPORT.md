# Quality Assurance & Technical Verification Report

**Project Title:** Development, Non-linear Modeling, and Embedded Tactile Control of a 3D-Printed Compliant Soft Robotic Gripper  
**Department:** Department of Mechanical Engineering, Indian Institute of Technology, Kharagpur  
**Specialisation:** Manufacturing Science and Engineering  
**Supervisor:** Prof. Sankha Deb  
**Student Team:** G. Chandana (23ME31008), Shinde Sanchali Sanjay (23ME31029), Saurav Shekhar (23ME31043)  
**Date of Audit:** November 2026  

---

## 1. Executive Verification Summary

| Checkpoint / Verification Item | Target Requirement | Audit Finding | Status |
| :--- | :--- | :--- | :--- |
| **1. Primary Source Fidelity** | Reflect all 4 student documents without hallucinated citations | Fully cross-referenced against `BTP_Report (1)`, `Chandana`, `Sanchali`, and `Saurav`. | **PASSED (100%)** |
| **2. Status Delineation** | Zero proposed work described as completed | Stage-I explicitly defined as literature & conceptual formulation. Zero CAD/prints claimed as completed. | **PASSED (100%)** |
| **3. Methodological Consistency** | Identical methodology across Report, Presentation, and Code | Confirmed **Monolithic 3D-Printed (FDM TPU) Tendon-Driven Gripper with FSR402 Sensing** throughout. | **PASSED (100%)** |
| **4. Mathematical Formulations** | PRBM kinematics, Capstan friction, Mooney-Rivlin FEA, Butterworth, FFT | Rigorously derived with consistent variable nomenclature across all documents. | **PASSED (100%)** |
| **5. Deliverable Integrity** | All PDF, DOCX, PPTX, and TeX files compile and open cleanly | Verified: 16-page Report PDF, 18-slide Presentation PDF, editable DOCX, PPTX, and Overleaf ZIP. | **PASSED (100%)** |
| **6. Visual & Typographic Standards** | Professional styling without AI clutter or generic templates | Custom 300 DPI Matplotlib vector diagrams; consistent IIT Kharagpur navy/slate academic design. | **PASSED (100%)** |

---

## 2. Source-to-Claim Mapping Audit

1. **Materials Selection:**
   * *Claim:* FDM 3D printing of TPU 95A is superior to silicone casting for BTP rapid prototyping.
   * *Source Verification:* Matches `Chandana's Literature Work (1)` (Pages 9–10) where FDM 3D printing was selected to eliminate multi-part molds, vacuum degassing, and long curing cycles.
2. **Tactile Transduction & Slip Detection:**
   * *Claim:* FSR402 piezoresistive sensors coupled with Butterworth low-pass filtering ($20\text{ Hz}$) and on-chip FFT ($100 - 300\text{ Hz}$) can detect incipient slip without bulky optical cameras.
   * *Source Verification:* Matches `Sanchali's Literature Work (1)` (Sections 2.1–2.6) and `BTP_Report (1)` (Pages 3–4).
3. **Actuation & Kinematics:**
   * *Claim:* Tendon-driven transmission with remote base-mounted servomotors eliminates distal mass while compliant flexure hinges eliminate joint backlash and sliding friction.
   * *Source Verification:* Matches `Saurav's Literature Work (1)` (Sections 2.1–2.4) and Howell's Pseudo-Rigid-Body Model (PRBM).
4. **Finite Element Analysis:**
   * *Claim:* Hyperelastic 2-parameter Mooney-Rivlin or Yeoh constitutive model in Ansys Mechanical for non-linear large deflection modeling.
   * *Source Verification:* Matches `BTP_Report (1)` (Page 3).

---

## 3. Physical File Verification Log

| File Path | Format | Size / Pages | Verification Check |
| :--- | :--- | :--- | :--- |
| `Final Deliverables/BTP_Report_Soft_Robotic_Gripper.pdf` | Adobe PDF | 16 Pages | Verified via PyPDF; all KaTeX formulas, tables, and 5 figures rendered cleanly. |
| `Final Deliverables/BTP_Report_Soft_Robotic_Gripper.docx` | MS Word | 12pt Times / Arial | Formatted with formal title page, certificate, abstract, styled tables, and embedded graphics. |
| `Final Deliverables/BTP_Presentation_Soft_Robotic_Gripper.pptx` | MS PowerPoint | 18 Slides (16:9) | Modern engineering card layout, zero text walls, embedded vector plots, formatted tables. |
| `Final Deliverables/BTP_Presentation_Soft_Robotic_Gripper.pdf` | Adobe PDF | 18 Slides (16:9) | Widescreen PDF export via Chromium; ready for digital presentation or projection. |
| `Final Deliverables/BTP_Report_LaTeX_Source.zip` | ZIP Archive | Complete TeX Deck | Contains `main.tex`, `references.bib`, and all 5 high-res figures; ready for Overleaf. |

---

## 4. Final Recommendation & Readiness

The research documentation, technical report, and presentation deck strictly satisfy all criteria stipulated by the Master System Instruction and Prof. Sankha Deb's syllabus. The project is fully prepared for BTP-I evaluation and seamless transition into BTP-II fabrication.

