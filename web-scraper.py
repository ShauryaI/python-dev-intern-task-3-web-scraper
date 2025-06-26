from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import json
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
TEXT_FILE_NAME = "REUTERS_" + formatted_datetime + ".txt"

def web_scraper():
    try:
        # Initialize the WebDriver
        driver = webdriver.Chrome(service=Service())

        # URL of the Reuters article
        url = "https://www.reuters.com/world/europe/excitement-relief-paris-notre-dame-cathedral-prepares-reopen-2024-11-29/"

        # Open the URL in the browser
        driver.get(url)

        # Extract the title from the <h1> tag
        title_element = driver.find_element(By.CSS_SELECTOR, "h1")
        title = title_element.text

        # Select all text elements
        paragraph_elements = driver.find_elements(By.CSS_SELECTOR, "[data-testid^='paragraph-']")

        # Aggregate their text
        content = " ".join(p.text for p in paragraph_elements)

        # Prepare the data to be exported as JSON
        article = {
            "title": title,
            "content": content
        }

        # Export data to a JSON file
        with open("article.json", "w", encoding="utf-8") as json_file:
            json.dump(article, json_file, ensure_ascii=False, indent=4)

    except Exception as e:
        print("An error occurred:", e)

def main():
    web_scraper()

if __name__ == "__main__":
    main()