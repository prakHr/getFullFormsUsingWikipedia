# getFullFormsUsingWikipedia
1. get titles of topics from wikipedia
2. automation of google page details

# python get_wiki_title.py

This function prints the titles of possible wiki topics:

```python
queries = ["CPU", "GPU", "RAM", "SSD", "HDD", "SingleShot", "MultiShot", "AutoFocus", "Aperture", "ISO", "ShutterSpeed"]
id = "#firstHeading"
wiki_url = "https://en.wikipedia.org/wiki/"
results = asyncio.run(get_Titles(queries, id, wiki_url))
pprint(results)
```

# python automate_google_pages_details.py

This function automates the soup of any number of pages:

```python
url, query, page_id, google_search_btn_id = "https://www.google.com", "kung fu panda", "(//h3)[1]", "btnK"
results = get_insider_page_details(url, query, page_id, google_search_btn_id)
pprint(results)
```
