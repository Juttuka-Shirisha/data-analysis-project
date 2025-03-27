import requests
import pandas as pd

PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

def fetch_papers(query, debug=False):
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": 10  # Limit results for testing
    }

    response = requests.get(PUBMED_API_URL, params=params)
    if debug:
        print(f"Query URL: {response.url}")

    if response.status_code != 200:
        print("Failed to fetch data from PubMed.")
        return pd.DataFrame()

    data = response.json()
    paper_ids = data.get("esearchresult", {}).get("idlist", [])

    if not paper_ids:
        return pd.DataFrame()

    fetch_params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }

    fetch_response = requests.get(PUBMED_FETCH_URL, params=fetch_params)
    return parse_papers(fetch_response.text)

def parse_papers(xml_data):
    # Placeholder function - You need to implement XML parsing to extract relevant details.
    return pd.DataFrame([{"PubmedID": "12345", "Title": "Sample Paper", "Publication Date": "2025-01-01",
                          "Non-academic Author(s)": "John Doe", "Company Affiliation(s)": "XYZ Pharma",
                          "Corresponding Author Email": "john.doe@xyzpharma.com"}])
