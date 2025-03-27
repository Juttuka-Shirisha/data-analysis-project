import argparse
import sys
from pubmed_fetcher.fetcher import fetch_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Output file name")

    args = parser.parse_args()

    papers = fetch_papers(args.query, args.debug)
    if args.file:
        papers.to_csv(args.file, index=False)
        print(f"Results saved to {args.file}")
    else:
        print(papers)

if __name__ == "__main__":
    main()
