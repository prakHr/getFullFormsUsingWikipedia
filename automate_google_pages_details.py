import rpa as r
from pprint import pprint
from bs4 import BeautifulSoup
import traceback

def get_insider_page_details(url, query, page_id, google_search_btn_id):
    try:
        r.init()
        r.dom('window.moveTo(0,0); window.resizeTo(screen.width, screen.height);')
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

def get_insider_page_details_with_navigation(url, query_id, query, page_id, google_search_btn_id, open_next_page, next_button_id):
    try:
        r.init()
        r.dom('window.moveTo(0,0); window.resizeTo(screen.width, screen.height);')
        
        r.url(url)

        # Type query
        r.type(query_id, query)

        r.wait(1)

        # Click Google Search button
        r.click(google_search_btn_id)

        r.wait(3)
        for i in range(open_next_page): 
            print("Navigating to next page...")
            r.click(next_button_id)
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


        
def automate_google_query(url, query_id, query, page_id, google_search_btn_id, page_size,next_button_id,stop_page):
    results = {}
    counter = 1
    open_next_page = 0
        
    while True:
        print(f"Processing page {counter}...")
        if counter==stop_page:
            break
        for page_num in range(1, page_size):
            print(f"Processing page {counter}...")
        
            if counter==stop_page:
                break
            
            page_idd = f"{page_id}[{page_num}]"
            print("Page ID:", page_idd)
            if counter%(page_size-1)==0:
                print("Navigating to next page...")
                open_next_page += 1 

            result = get_insider_page_details_with_navigation(url, query_id, query, page_idd, google_search_btn_id, open_next_page, next_button_id)
            results[f"Page {counter}"] = result
            counter += 1
        
        
    return results

if __name__ == "__main__":
    # url = "https://www.google.com"
    # query = "kung fu panda"
    # page_id = "(//h3)[1]"
    # google_search_btn_id = "btnK"
    # results = get_insider_page_details(url, query, page_id, google_search_btn_id)
    # pprint(results)


    url = "https://www.google.com"
    query = "kung fu panda" 
    page_id = "(//h3)"
    google_search_btn_id = f'//*[@name="btnK"]'
    page_size = 10
    next_button_id = '//span[normalize-space()="Next"]'
    stop_page = 14
    query_id = '//*[@name="q"]'
    results = automate_google_query(url,query_id, query, page_id, google_search_btn_id, page_size, next_button_id, stop_page)
    pprint(results)


