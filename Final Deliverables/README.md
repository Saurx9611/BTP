# Soft Robotic Gripper: BTP Report & Presentation Package

**Department of Mechanical Engineering, Indian Institute of Technology, Kharagpur**  
**Specialisation:** Manufacturing Science and Engineering  
**Supervisor:** Prof. Sankha Deb  
**Student Team:** G. Chandana (23ME31008), Shinde Sanchali Sanjay (23ME31029), Saurav Shekhar (23ME31043)  

---

## 📁 Directory Structure & File Organization

```
c:\Users\saura\Desktop\BTP\
│
├── Final Deliverables/                              <-- FINAL COMPLETE PACKAGES
│   ├── BTP_Report_Soft_Robotic_Gripper.pdf          (16-Page Academic BTP-I Report PDF)
│   ├── BTP_Report_Soft_Robotic_Gripper.docx         (Editable Microsoft Word Document)
│   ├── BTP_Report_LaTeX_Source.zip                 (Complete Overleaf/LaTeX Deck + Figures)
│   ├── BTP_Presentation_Soft_Robotic_Gripper.pptx   (18-Slide Professional Presentation PPTX)
│   ├── BTP_Presentation_Soft_Robotic_Gripper.pdf   (18-Slide Presentation PDF for Defense)
│   ├── QUALITY_ASSURANCE_REPORT.md                 (Comprehensive Verification Audit)
│   └── README.md                                    (Usage & Build Guide)
│
├── Report/                                          <-- REPORT SOURCE FILES
│   ├── main.tex                                     (Master LaTeX Document)
│   ├── report.html                                  (KaTeX Pre-render HTML)
│   ├── BTP_Report_Soft_Robotic_Gripper.docx
│   └── BTP_Report_Soft_Robotic_Gripper.pdf
│
├── Presentation/                                    <-- PRESENTATION SOURCE FILES
│   ├── BTP_Presentation_Soft_Robotic_Gripper.pptx
│   ├── BTP_Presentation_Soft_Robotic_Gripper.pdf
│   └── slides.html                                  (16:9 Presentation HTML)
│
├── Figures and Diagrams/                            <-- 300 DPI VECTOR FIGURES
│   ├── comparative_radar_chart.png                  (Spider comparison across 6 metrics)
│   ├── gripper_kinematics_diagram.png               (Compliant finger & PRBM living hinges)
│   ├── mechatronics_architecture.png                (ESP32 FreeRTOS & micro-ROS pipeline)
│   ├── slip_detection_fft_workflow.png              (Normal force vs. FFT micro-vibration)
│   └── gantt_chart_btp2.png                         (16-Week BTP-II Implementation Gantt)
│
├── References/                                      <-- CITATIONS & BIBLIOGRAPHY
│   └── references.bib                               (BibTeX file with all verifiable citations)
│
├── Extracted Research Notes/                        <-- RESEARCH DATA DUMPS
│   ├── BTP_Report (1)_clean.txt
│   ├── Chandana's Litreature Work (1)_clean.txt
│   ├── Sanchali's Litreature Work (1)_clean.txt
│   └── Saurav's Literature Work (1)_clean.txt
│
└── Source Literature/                               <-- ORIGINAL UNTOUCHED SOURCE FILES
    ├── BTP_Report (1).pdf
    ├── Chandana's Litreature Work (1).pdf
    ├── Sanchali's Litreature Work (1).pdf
    └── Saurav's Literature Work (1).pdf
```

---

## 🛠️ How to Compile and Update the Sources

### 1. Editable Microsoft Word (`.docx`) & PowerPoint (`.pptx`)
* Open `Final Deliverables/BTP_Report_Soft_Robotic_Gripper.docx` directly in Microsoft Word or LibreOffice Writer to edit text, adjust margins, or export.
* Open `Final Deliverables/BTP_Presentation_Soft_Robotic_Gripper.pptx` in Microsoft PowerPoint or Google Slides to present or edit slide elements.

### 2. LaTeX Source Compilation (Overleaf or Local TeX Live)
* **Using Overleaf:** Simply upload `Final Deliverables/BTP_Report_LaTeX_Source.zip` directly to Overleaf. Set compiler to `pdfLaTeX` or `XeLaTeX` and hit **Recompile**.
* **Using Local Terminal:**
  ```bash
  cd Report
  pdflatex main.tex
  bibtex main
  pdflatex main.tex
  pdflatex main.tex
  ```

### 3. Re-generating PDFs via Playwright (Automated Pipeline)
* To re-render the high-fidelity PDFs from source HTML:
  ```bash
  python generate_report_pdf.py
  python generate_presentation_pdf.py
  ```

