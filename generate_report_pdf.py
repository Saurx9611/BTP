import os
from playwright.sync_api import sync_playwright

html_path = os.path.abspath("Report/report.html")
pdf_path = os.path.abspath("Report/BTP_Report_Soft_Robotic_Gripper.pdf")

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("file:///" + html_path.replace("\\", "/"))
    # Wait for KaTeX to render formulas
    page.wait_for_timeout(3000)
    page.pdf(
        path=pdf_path,
        format="A4",
        print_background=True,
        margin={"top": "22mm", "bottom": "22mm", "left": "25mm", "right": "20mm"}
    )
    browser.close()

print(f"Generated {pdf_path} successfully via Playwright Chromium.")
