import rpa as r
from pprint import pprint
from bs4 import BeautifulSoup
import traceback

def get_insider_page_details(url, query, page_id, google_search_btn_id):
    try:
        r.init()
        r.url(url)

        # Type query
        r.type('//*[@name="q"]', query)

        r.wait(1)

        # Click Google Search button
        r.click(f'//*[@name="{google_search_btn_id}"]')

        r.wait(3)

        # Click first search result
        r.click(page_id)

        r.wait(5)

        # Read entire visible page body
        page_text = r.read('//body')

        
        r.close()

        
        soup = BeautifulSoup(page_text, "html.parser")
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        # Extract readable text
        page_text = soup.get_text(
            separator="\n",
            strip=True
        )

        # Pretty HTML structure
        pretty_html = soup.prettify()

        return {
            "query": query,
            "page_text": page_text,
            "pretty_html": pretty_html
        }
        
    except Exception as e:
        return {
            "query": traceback.format_exc(),
            "page_text": "",
            "pretty_html": ""
        }

if __name__ == "__main__":
    url, query, page_id, google_search_btn_id = "https://www.google.com", "kung fu panda", "(//h3)[1]", "btnK"
    results = get_insider_page_details(url, query, page_id, google_search_btn_id)
    pprint(results)