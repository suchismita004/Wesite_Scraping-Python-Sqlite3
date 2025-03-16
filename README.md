# Wesite_Scraping-Python-Sqlite3
## 📌 Overview

This Python script extracts **paragraphs** (`<p>` tags) from a target website and stores them in an **SQLite database**. It ensures a clean slate by removing old data before saving fresh content, enhancing efficiency.

## ⚙️ Setup & Installation

1️⃣ Install the required dependencies:
    `pip install requests beautifulsoup4`

2️⃣ Run the script:
    `python websiteScraping.py`  

3️⃣ Verify stored data in SQLite:
  `sqlite3 scraped_data.db` 
  then 
  `SELECT * FROM scraped_content LIMIT 5;`  

## 📝 Features

✔ Extracts **paragraphs** (`<p>` tags) from any website  
✔ Stores extracted data in an **SQLite3** database  
✔ Automatically clears old data before saving new entries  
✔ Includes error handling for robust performance  
✔ Tracks and displays script **execution time**  


## 🔍 How It Works  

1. Retrieves the website's HTML using requests.
2. Parses and extracts <p> tags with BeautifulSoup.
3. Clears old data and creates a new database table.
4.Saves the extracted paragraphs into SQLite.
5.Tracks and displays the script's execution time.

## 📌 Example Output (Terminal Preview)

```plaintext
Connected to database: scraped_data.db
1.Fetching data from: https://example.com ...
2.Page loaded successfully!
3.Found 2 paragraphs!
4.2 paragraphs saved to the database!

Database connection closed.
-------------------------------------------------------------
--------------- Previewing saved paragraphs: ----------------
This domain is for use in illustrative examples in documents. You may use this
domain in literature without prior coordination or asking for permission.

More information...

--------------- Execution Time: 0.96 seconds -----------------
```

## 🚀 Customization  

- Change `URL` in `website_scraper.py` 

## ❌ Issues & Fixes

| Issue                                   | Fix                                         |
|-----------------------------------------|---------------------------------------------|
| `requests.exceptions.ConnectionError`   | Verify your internet connection or the URL. |
| `sqlite3.OperationalError: database is locked` | Ensure the database connection is closed before re-running. |
| No paragraphs found                     | Check if the site allows scraping.          |

## 📧 Need Help?  

Feel free to ask for improvements
