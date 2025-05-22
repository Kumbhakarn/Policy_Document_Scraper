# HDFC Policy Document Scraper

Automates extraction and download of policy PDFs from the HDFC Life website.

## Setup

1. Clone the repo.
2. Install Python 3.7+.
3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
4. Ensure Chrome and matching ChromeDriver are installed.

## Usage

Run the main scraper script:

```bash
python hdfc_policy_scraper.py
```

This will:

* Scrape policy section HTML files.
* Download PDFs (top 5 per section).
* Extract metadata and save to CSV.

## Output

* HTML files → `HDFC_Policy_Documents/html_data/`
* PDFs → `HDFC_Policy_Documents/pdf_data/`
* Metadata CSV → `HDFC_Policy_Documents/policy_data.csv`

## Requirements

* selenium
* requests
* beautifulsoup4
* PyPDF2
* pandas
