from bs4 import BeautifulSoup
import requests
import urllib

def extract_next_page_link(page_url, next_page_div):
    """Extracts the link to the next page from the given HTML div."""
    
    if next_page_div:
        next_button = next_page_div.find("a", class_="primaryButton")
        if next_button and next_button.get("href"):
            return urllib.parse.urljoin(page_url, next_button["href"].split("#")[0])
    return None


def extract_mp3_link(page_url):
    """
    Extracts the MP3 link and the next page link from a given URL.
    
    Args:
        page_url (str): The URL of the page to scrape.

    Returns:
        tuple: (mp3_link, next_page_link), where `mp3_link` is the MP3 URL (or None)
               and `next_page_link` is the next page's URL (or None).
    """
    response = requests.get(page_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    
    next_page_div = soup.find("div", class_="navLinkNext")
    next_page_link = extract_next_page_link(page_url, next_page_div)

    try:
        audio_div = soup.find("div", class_="jsAudioPlayer")
        mp3_link = audio_div.find("a", class_="streaming")["href"]
        return mp3_link, next_page_link
    
    except Exception as e:
        return None, next_page_link
