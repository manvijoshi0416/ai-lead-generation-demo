# AI-Based Lead Generation Demo

## Overview
This project is a prototype web agent built as part of an internship evaluation task.  
The goal is to identify, enrich, and rank potential biotech and pharma professionals who may be interested in 3D in-vitro models for drug safety and toxicology research.

The project demonstrates the full pipeline from data collection to AI-based lead prioritization.

---

## Project Pipeline

### Stage 1: Identification (Web Scraping)
A lightweight web scraper is implemented using Python to collect recent toxicology-related publications from PubMed.  
The scraper extracts paper titles, authors, publication year, and paper URLs.

Output:
- `scraped_pubmed_papers.csv`

---

### Stage 2: Enrichment
Author names from the scraped publications are manually enriched to simulate a real web agent pipeline.  
Enrichment includes:
- Current role and company (via LinkedIn search)
- Role seniority
- Company funding stage
- Biotech hub location
- Scientific relevance and recency

This step is performed manually to respect platform restrictions on sites like LinkedIn.

Output:
- `leads_dataset.csv`

---

### Stage 3: AI-Based Ranking
A rule-based propensity scoring engine assigns a score (0–100) to each lead based on:
- Role seniority
- Scientific intent and publication recency
- Company funding stage
- Biotech hub location

Leads are then ranked and labeled as High, Medium, or Low priority.

Output:
- `ranked_leads.csv`

---

## Files in This Repository

- `pubmed_scraper.py` – Scrapes PubMed for toxicology-related publications  
- `scraped_pubmed_papers.csv` – Raw scraped scientific data  
- `leads_dataset.csv` – Enriched person-level dataset  
- `scoring.py` – AI-based scoring and ranking logic  
- `ranked_leads.csv` – Final ranked output  
- `requirements.txt` – Python dependencies  

---

## How to Run

1. Install dependencies:
pip install -r requirements.txt

2. Run the PubMed scraper:
python pubmed_scraper.py

3. Run the scoring script:
python scoring.py
