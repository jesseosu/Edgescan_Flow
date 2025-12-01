# EdgeScan Flow – Smart Document Scanner Pipeline

A firmware-inspired simulation that mimics how Toshiba multifunction scanners process, tag, and upload scanned documents into a cloud system for document management.

## Features
- Simulates document scanning events
- Processes images: grayscale, thresholding, denoising
- Extracts text via OCR (Tesseract)
- Classifies documents into categories
- Uploads metadata and files to a Flask backend
- Displays scan history in a Streamlit dashboard

## Usage
1. Run `scanner_sim/scanner.py`
2. Start `cloud_api/app.py`
3. Launch `dashboard/dashboard.py`

## Deployment
Docker and GitHub Actions supported.