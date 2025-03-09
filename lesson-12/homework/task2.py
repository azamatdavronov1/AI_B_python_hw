import requests
from bs4 import BeautifulSoup
import sqlite3
import pandas as pd

DB_FILE = "jobs.db"
URL = "https://realpython.github.io/fake-jobs"


def setup_database():
    db = sqlite3.connect(DB_FILE)
    db.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            link TEXT,
            UNIQUE(title, company, location)
        )
    """)
    db.close()


def get_jobs():
    site = requests.get(URL).text
    soup = BeautifulSoup(site, "html.parser")

    jobs = []
    for job in soup.select(".card-content"):
        title = job.select_one(".title").text.strip() if job.select_one(".title") else "N/A"
        company = job.select_one(".company").text.strip() if job.select_one(".company") else "N/A"
        location = job.select_one(".location").text.strip() if job.select_one(".location") else "N/A"

        description_elem = job.select_one(".description")
        description = description_elem.text.strip() if description_elem else "No description available"

        link_elem = job.find("a", string="Apply")
        link = link_elem["href"] if link_elem else "No link available"

        jobs.append((title, company, location, description, link))

    return jobs


def save_jobs(jobs):
    db = sqlite3.connect(DB_FILE)
    cursor = db.cursor()

    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (title, company, location, description, link)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(title, company, location) 
            DO UPDATE SET description=excluded.description, link=excluded.link
        """, job)

    db.commit()
    db.close()


def search_jobs(location=None, company=None):
    db = sqlite3.connect(DB_FILE)
    cursor = db.cursor()

    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")

    cursor.execute(query, params)
    results = cursor.fetchall()
    db.close()

    return results


def export_jobs(location=None, company=None, filename="jobs.csv"):
    jobs = search_jobs(location, company)

    if jobs:
        df = pd.DataFrame(jobs, columns=["ID", "Title", "Company", "Location", "Description", "Link"])
        df.to_csv(filename, index=False)
        print(f"Saved to {filename}")
    else:
        print("No jobs found.")


if __name__ == "__main__":
    setup_database()
    save_jobs(get_jobs())
    print("Jobs saved!")

    print("\nJobs in New York:")
    print(search_jobs(location="New York"))

    export_jobs(location="New York")
