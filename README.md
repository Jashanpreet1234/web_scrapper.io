# web_scrapper.io
A simple yet powerful Python script to scrape and extract links and headings from any webpage. Utilizes requests for fetching HTML content and BeautifulSoup for parsing and data extraction.

Step 1: Fetching HTML Content
Analogy: Think of fetching HTML content like ordering a book from an online store. You give the store the URL of the book, and they send you the book's content.

Programming Explanation:

requests.get(url): This is like sending a request to the store to get the book.
response.raise_for_status(): You check if the store successfully processed your order (no errors).
response.text: This is the book you received from the store, containing all its content.

Code:
#importing libraries
import requests

def fetch_html(url):
    """
    Fetch the HTML content of a webpage.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Ensure we got a successful response
    return response.text

![image](https://github.com/Jashanpreet1234/web_scrapper.io/assets/105735825/8ce8d47a-46ca-4aae-b986-cd34d8caa968)

Step 2: Parsing HTML Content
Analogy: Now that you have the book, you need to read through it and highlight the important parts (like links and headings).

Programming Explanation:

BeautifulSoup(html_content, 'html.parser'): This is your highlighter. It helps you read and understand the structure of the book.
soup.find_all('a', href=True): You go through the book and find all references (links) and note them down.
soup.find_all('h1'): You find all the main headings in the book and note them down.
soup.find_all('h2') and soup.find_all('h3'): Similarly, you find and note down all the sub-headings.

Code: 

#Importing libraries
from bs4 import BeautifulSoup
def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract all links
    links = [a['href'] for a in soup.find_all('a', href=True)]

    # Extract all headings
    headings = {
        'h1': [h1.get_text(strip=True) for h1 in soup.find_all('h1')],
        'h2': [h2.get_text(strip=True) for h2 in soup.find_all('h2')],
        'h3': [h3.get_text(strip=True) for h3 in soup.find_all('h3')],
    }

    return {
        'links': links,
        'headings': headings
    }
![image](https://github.com/Jashanpreet1234/web_scrapper.io/assets/105735825/a4a9024b-f4c2-4913-853c-2035581f2a63)

Step 3: Coordinating the Workflow
Analogy: Finally, you compile all your notes (links and headings) into a summary and share it with others.

Programming Explanation:

try-except: This is your error handling. If the store can't send the book or if you can't find the highlights, you handle the error gracefully.
print: You output your notes in a readable format.

Code: 


def main(url):
    """
    Main function to scrape the webpage.
    
    Args:
        url (str): The URL of the webpage to scrape.
    """
    html_content = fetch_html(url)
    if html_content:
        extracted_data = parse_html(html_content)
        if extracted_data:
            # Print extracted data
            print("Links:")
            for link in extracted_data['links']:
                print(link)

            print("\nHeadings:")
            for level, headings in extracted_data['headings'].items():
                print(f"{level.upper()}:")
                for heading in headings:
                    print(f"  - {heading}")

if __name__ == "__main__":
    # Example URL to scrape
    url = "https://example.com"
    main(url)



![image](https://github.com/Jashanpreet1234/web_scrapper.io/assets/105735825/330de9e4-4a73-4435-85b9-e022f41016b3)



