PubMed Fetcher

Overview

PubMed Fetcher is a command-line tool designed to fetch research papers from PubMed based on user-defined queries. The tool filters results to focus on authors affiliated with pharmaceutical or biotech companies and exports the relevant information to a CSV file.


---

Features

✅ Fetches research papers from PubMed using a keyword query.
✅ Filters papers based on author affiliations (e.g., pharmaceutical companies).
✅ Saves results in a structured CSV format.
✅ Provides a CLI interface for easy execution.
✅ Supports version control using Git.


---

Installation

1. Clone the Repository

If you haven’t cloned the repository yet, run the following command in your terminal:

git clone <your-repo-url>
cd pubmed_fetcher

2. Install Dependencies

This project uses Poetry for dependency management. Install dependencies by running:

poetry install

If Poetry is not installed, you can install it using:

pip install poetry


---

Usage

Running the CLI Tool

To fetch papers from PubMed, use the following command:

poetry run get-papers-list "cancer research"

Command Options:

Example:

poetry run get-papers-list "cancer research" -f results.csv


---

Project Structure

pubmed_fetcher/
├── src/  
│   ├── fetch_papers.py  # Main script for fetching papers  
│   ├── utils.py         # Utility functions  
├── tests/               # Unit tests  
├── poetry.lock          # Poetry dependency lock file  
├── pyproject.toml       # Poetry configuration file  
├── README.md            # Documentation  
├── results.csv          # Output file for fetched papers


---

Configuration (pyproject.toml)

Make sure your pyproject.toml file includes the following entry for CLI support:

[tool.poetry.scripts]
get-papers-list = "pubmed_fetcher.fetch_papers:main"

This allows you to run the CLI command as shown in the Usage section.


---

Tools & Libraries Used

The project is built using the following tools:

## Dependencies
This project requires the following Python libraries:

- *requests* – For making API requests to PubMed.
- *pandas* – For processing and saving CSV data.
- *numpy* – For handling numerical computations.
- *python-dateutil* – For managing datetime operations.
- *pytz* & *tzdata* – For timezone handling.
- *urllib3* & *certifi* – For secure HTTP requests.

To install all dependencies, run:
```bash
poetry install

---

How to Push Changes to GitHub

1. Initialize Git (if not already done)

git init


2. Add files to staging

git add .


3. Commit changes

git commit -m "Added CLI support and README update"


4. Add GitHub repository (if not already added)

git remote add origin <your-github-repo-url>


5. Push to GitHub

git push -u origin main




---

Troubleshooting

If you encounter issues, check the following:

✅ Ensure Poetry is installed correctly (poetry --version).
✅ Check if pyproject.toml has the correct script entry.
✅ Run poetry shell before executing the CLI command.
✅ If module import errors occur, try running:

poetry run python -m pubmed_fetcher.fetch_papers


---
