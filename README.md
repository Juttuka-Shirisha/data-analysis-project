# PubMed Fetcher

This project fetches research papers from PubMed with at least one author affiliated with a pharmaceutical or biotech company.

## Installation

1. Install [Poetry](https://python-poetry.org/docs/)
2. Run the following command to install dependencies:

   ```sh
   poetry install
   ```

## Usage

```sh
poetry run get-papers-list "cancer research" --file output.csv
```
