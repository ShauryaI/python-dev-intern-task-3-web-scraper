import requests
from bs4 import BeautifulSoup
from datetime import datetime

current_datetime = datetime.now()
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H-%M-%S")
TEXT_FILE_NAME = "TOI_" + formatted_datetime + ".txt"

def web_scraper():
    url = "https://timesofindia.indiatimes.com/home/headlines"
    try:
        response = requests.get(url)
        response.raise_for_status() #If an error occurs, this method returns an HTTP Error object
        print("Request successful!")

        soup = BeautifulSoup(response.content, "html.parser")

        headline_elements = soup.find_all("span", class_="w_tle")

        with open(TEXT_FILE_NAME, "w", encoding="utf-8") as text_file:
            for index, headline in enumerate(headline_elements, start=1):
                text_file.write(f"{index}. {headline.text}\n")
            else:
                print(f"For Top News Headlines, please check file: {TEXT_FILE_NAME}")

    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
        print("A connection error or timeout occurred:", e)
    except requests.exceptions.HTTPError as e:
        print("HTTP Error:", e)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

def main():
    web_scraper()

if __name__ == "__main__":
    main()
