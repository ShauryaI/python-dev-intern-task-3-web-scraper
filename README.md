# python-dev-intern-task-3-web-scraper
Python Developer Internship Task 3 (Web Scraper for News Headlines)

## Dependencies ##
We need to install requests and beautifulsoup4 for this. Requests for handling HTTP requests and beautifulsoup4 for parsing HTML. Run command mentioned below in the terminal:
>> pip install requests beautifulsoup4

## Types of Error in Network Call

1. ConnectionError: network problem (DNS failure, refused connection, etc.)
2. HTTPError: rare invalid HTTP response or regular unsuccessful (4xx/5xx) with Response.raise_for_status()
3. Timeout: request times out
4. TooManyRedirects: request exceeds the configured number of maximum redirections
5. RequestException: the default exception class for the Requests module. It includes a variety of exception types that might appear while processing a request.

## Steps ##

1. Step 1: Send an HTTP request to the website
    - Times of india has been selected for the scraping task (https://timesofindia.indiatimes.com/home/headlines)
    - In case of error: display the error message, 404 can be tested by mentioning wrong URL
    - In case of success: proceed with the next steps
2. Step 2: Parse the HTML content
3. Step 3: Identify the HTML elements containing the desired information
   - In case of Times of India, span tag with class 'w_tle' seems to be the one
4. Step 4: Extract and save the headlines in text file
    - For saving the headlines in a file, a nomenclature has been followed.
    - TOI_current-datetime.text as scraping can be routine task.
    - While creating file, we will explicitly define the encoding to fix the UnicodeEncodeError

## Why use Selenium ##
For websites like https://www.reuters.com/world/india/
Reuters has a special anti-bot solution (or requiring JavaScript execution) that blocks all requests not coming from a browser.
Should get error: Please enable JS and disable any ad blocker
But got: HTTP Error: 401 Client Error: HTTP Forbidden for url: https://www.reuters.com/world/india/

Let's try using a browser automation tool like Selenium to scrape news articles from Reuters.
Run command
>>> pip install selenium

When code is executed it opens a Chrome browser with message
Chrome is being controlled by automated test software

Logic same but different library and scraping worked.