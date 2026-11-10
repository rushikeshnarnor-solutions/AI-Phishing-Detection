# AI Phishing & Scam Detection System

An explainable cybersecurity demo that checks pasted URLs and messages for common phishing indicators.

## Features
- URL parsing and heuristic checks
- Suspicious phrase detection
- Risk score with explanations
- Safe-use guidance and clear limitations

## Run locally
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

## How it works
The baseline combines simple URL indicators (HTTP, IP-based host, unusually long host, multiple hyphens, embedded credentials) with suspicious message phrases. The score is a demonstration metric and is not a calibrated probability.

## Responsible use
- A low score does not mean a URL is safe.
- Do not submit private messages containing sensitive personal information.
- Do not use this tool as a replacement for endpoint protection, email security, or professional incident response.

## Suggested extensions
- Train and evaluate a supervised classifier on a properly licensed dataset.
- Add domain reputation checks through a trusted threat-intelligence API.
- Add feature importance and confusion-matrix reporting.
- Add URL defanging and safe sandbox analysis.
