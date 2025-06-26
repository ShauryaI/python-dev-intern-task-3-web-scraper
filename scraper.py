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

        # URL of the Reuters
        url = "https://www.reuters.com/world/india/"

        # Open the URL in the browser
        driver.get(url)

        headlines = driver.find_elements(By.CLASS_NAME,"media-story-card__headline__tFMEu")

        with open(TEXT_FILE_NAME, "w", encoding="utf-8") as text_file:
            for index, headline in enumerate(headlines, start=1):
                text_file.write(f"{index}. {headline.text}\n")
            else:
                print(f"For Top News Headlines, please check file: {TEXT_FILE_NAME}")

    except Exception as e:
        print("An error occurred:", e)

def main():
    web_scraper()

if __name__ == "__main__":
    main()