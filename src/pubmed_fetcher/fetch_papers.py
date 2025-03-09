import requests
import pandas as pd
import argparse
import json

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
DETAILS_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"

def fetch_pubmed_papers(query):
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10
    }
    response = requests.get(PUBMED_API_URL, params=params)
    data = response.json()
    return data["esearchresult"]["idlist"]

def fetch_paper_details(paper_ids):
    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }
    response = requests.get(DETAILS_API_URL, params=params)
    return response.json()

def extract_relevant_info(pubmed_data):
    papers = []
    for paper_id, details in pubmed_data["result"].items():
        # Skip summary metadata entry
        if paper_id == "uids":
            continue
        
        # Extract useful fields
        title = details.get("title", "No title available")
        authors = ", ".join([author["name"] for author in details.get("authors", [])])
        journal = details.get("source", "Unknown journal")
        pub_date = details.get("pubdate", "Unknown date")
        
        papers.append({
            "Paper ID": paper_id,
            "Title": title,
            "Authors": authors,
            "Journal": journal,
            "Publication Date": pub_date,
        })
    
    return papers

def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return
    
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers related to a topic.")
    parser.add_argument("query", help="Search query for PubMed")
    parser.add_argument("-f", "--file", help="Output CSV filename", default="papers.csv")
    args = parser.parse_args()

    paper_ids = fetch_pubmed_papers(args.query)
    paper_data = fetch_paper_details(paper_ids)
    filtered_papers = extract_relevant_info(paper_data)
    save_to_csv(filtered_papers, args.file)

if __name__ == "_main_":
    main

