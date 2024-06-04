import requests
from bs4 import BeautifulSoup

def fetch_html(url):
    """
    Fetch the HTML content of a webpage.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The HTML content of the webpage, or None if an error occurs.
    """
    # Define headers to mimic a browser request and avoid being blocked
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    try:
        # Send HTTP GET request to the provided URL
        response = requests.get(url, headers=headers)
        # Raise an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        # Return the HTML content of the page
        return response.text
    except requests.exceptions.RequestException as e:
        # Print the error if the request failed
        print(f"Error fetching the URL: {e}")
        return None

def parse_html(html_content):
    """
    Parse the HTML content and extract links and headings.

    Args:
        html_content (str): The HTML content of the webpage.

    Returns:
        dict: A dictionary with extracted links and headings, or None if an error occurs.
    """
    try:
        # Create a BeautifulSoup object to parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract all links with 'href' attribute
        links = [a['href'] for a in soup.find_all('a', href=True)]

        # Extract all headings of different levels
        headings = {
            'h1': [h1.get_text(strip=True) for h1 in soup.find_all('h1')],
            'h2': [h2.get_text(strip=True) for h2 in soup.find_all('h2')],
            'h3': [h3.get_text(strip=True) for h3 in soup.find_all('h3')],
        }

        # Return the extracted links and headings
        return {'links': links, 'headings': headings}
    except Exception as e:
        # Print the error if parsing failed
        print(f"Error parsing HTML content: {e}")
        return None

def main(url):
    """
    Main function to scrape the webpage.

    Args:
        url (str): The URL of the webpage to scrape.
    """
    # Fetch the HTML content from the URL
    html_content = fetch_html(url)
    if html_content:
        # Parse the HTML content to extract links and headings
        extracted_data = parse_html(html_content)
        if extracted_data:
            # Print the extracted links
            print("Links:")
            for link in extracted_data['links']:
                print(link)

            # Print the extracted headings
            print("\nHeadings:")
            for level, headings in extracted_data['headings'].items():
                print(f"{level.upper()}:")
                for heading in headings:
                    print(f"  - {heading}")
    else:
        # Print an error message if fetching the HTML content failed
        print("Failed to retrieve HTML content.")

if __name__ == "__main__":
    # Example URL to scrape; replace with the desired URL
    url = "https://example.com"
    main(url)
