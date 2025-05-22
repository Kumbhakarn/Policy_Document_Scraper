"""
1. Downloading policy section HTML files.
2. Downloading policy PDFs using UINs.
3. Extracting policy metadata from the downloaded HTML and saving it to a CSV.
Entry point for the full HDFC policy scraping pipeline.
"""
import os
from src.scraper import save_policy_sections_html
from src.downloader import download_pdfs_with_uin
from src.extractor import extract_policy_metadata_from_html
from src.utils import ensure_dir, log_info

def main():
    # Base directory where this script is located
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_DIR = os.path.join(BASE_DIR, "HDFC_Policy_Documents")

    # Project-relative folder paths
    html_dir    = os.path.join(DATA_DIR, "html_data")
    pdf_dir     = os.path.join(DATA_DIR, "pdf_data")
    output_csv  = os.path.join(DATA_DIR, "policy_data.csv")

    # Define the sections exactly as they appear on the policy page
    section_names = [
        "Savings & Investment (Live)",
        "Retirement (Live)",
        "Child Education (Live)",
        "Protection (Live)",
        "Health (Live)",
        "ULIP (Live)",
        "Pension (Live)",
        "Term (Live)",
        "Traditional Savings (Live)",
        "Group (Live)",
        "Annuity (Live)",
        "Child Plans (Live)",
        "Micro Insurance (Live)",
        "Others (Live)"
    ]

    # Ensure directories exist
    ensure_dir(html_dir)
    ensure_dir(pdf_dir)
    ensure_dir(os.path.dirname(output_csv))

    # Step 1: Scrape policy sections HTML
    log_info(" Scraping policy sections HTML…")
    save_policy_sections_html(output_folder=html_dir)

    # Step 2: Download PDFs with UIN detection
    log_info(" Downloading policy PDFs…")
    download_pdfs_with_uin(html_folder=html_dir, pdf_folder=pdf_dir)

    # Step 3: Extract metadata from **the HTML pages** (not PDFs) → CSV
    log_info(" Extracting metadata from HTML to CSV…")
    extract_policy_metadata_from_html(
        html_folder=html_dir,
        output_csv=output_csv,
        section_names=section_names
    )

    log_info(f" Pipeline complete. CSV written to: {output_csv}")

if __name__ == "__main__":
    main()
