import requests
from bs4 import BeautifulSoup
import pandas as pd

SEARCH_URL = "https://pubmed.ncbi.nlm.nih.gov/?term=liver+toxicity"

response = requests.get(SEARCH_URL)
soup = BeautifulSoup(response.text, "html.parser")

papers = soup.find_all("article", class_="full-docsum")

rows = []

for paper in papers[:10]: 
    link_tag = paper.find("a", class_="docsum-title")
    if not link_tag:
        continue

    paper_url = "https://pubmed.ncbi.nlm.nih.gov" + link_tag["href"]
    paper_page = requests.get(paper_url)
    paper_soup = BeautifulSoup(paper_page.text, "html.parser")

    title_tag = paper_soup.find("h1", class_="heading-title")
    title = title_tag.text.strip() if title_tag else "Unknown"

    author_tags = paper_soup.find_all("a", class_="full-name")
    authors = [a.text.strip() for a in author_tags]

    year_tag = paper_soup.find("span", class_="cit")
    year = year_tag.text.strip() if year_tag else "Unknown"

    rows.append({
        "paper_title": title,
        "authors": "; ".join(authors),
        "publication_year": year,
        "paper_url": paper_url
    })

df = pd.DataFrame(rows)
df.to_csv("scraped_pubmed_papers.csv", index=False)

print("PubMed data saved to scraped_pubmed_papers.csv")
