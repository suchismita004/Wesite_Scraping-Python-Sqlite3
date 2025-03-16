import requests
import sqlite3
import time
from bs4 import BeautifulSoup

start_time=time.time()
# Step 1: Connect to SQLite
db = "scraped_data.db"

conn = sqlite3.connect(db)

cursor = conn.cursor()

# Step 2: Create a table to store scraped content

#Drop table if exits to remove all previous stotred record
cursor.execute("DROP TABLE IF EXISTS scraped_content")
cursor.execute("""

    CREATE TABLE IF NOT EXISTS scraped_content (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        paragraph TEXT

    )

""")

conn.commit()
print("-------------------------------------------------------------")
print(f"Connected to database: {db}")
# Step 3: Choose a website to scrape("URL of your choice ")
URL = "https://example.com"
try:
    print(f"1.Fetching data from: {URL} ...")
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    # Step 4: Check if the page loaded successfully
    if response.status_code == 200:
        print("2.Page loaded successfully!")
        # Step 5: Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        # Step 6: Extract all <p> tags (paragraphs)
        paragraphs = soup.find_all("p")
        print(f"3.Found {len(paragraphs)} paragraphs!")
        # Step 7: Store the extracted paragraphs in the database
        saved_count = 0
        for para in paragraphs:
            text = para.get_text(strip=True)  
            if text:
                cursor.execute("INSERT INTO scraped_content (paragraph) VALUES (?)", (text,))
                saved_count += 1
        conn.commit()
        print(f"4.{saved_count} paragraphs saved to the database!\n")
    else:
        print(f"Failed to load the page. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()
    print("Database connection closed.")
print("-------------------------------------------------------------")
# Step 8: Retrieve and display saved data
print("--------------- Previewing saved paragraphs: ----------------")
conn = sqlite3.connect(db)
cursor = conn.cursor()
cursor.execute("SELECT * FROM scraped_content LIMIT 10")
for row in cursor.fetchall():
    print(f"{row[1]}\n")
cursor.close()
conn.close()
end_time=time.time()
execution_time=end_time-start_time
print(f"--------------- Execution Time: {execution_time:.2f} seconds-----------------")
