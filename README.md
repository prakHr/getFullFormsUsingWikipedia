# getFullFormsUsingWikipedia
get titles of topics from wikipedia

### python get_wiki_title.py

`
queries = ["CPU", "GPU", "RAM", "SSD", "HDD", "SingleShot", "MultiShot", "AutoFocus", "Aperture", "ISO", "ShutterSpeed"]

id = "#firstHeading"

wiki_url = "https://en.wikipedia.org/wiki/"

results = asyncio.run(get_Titles(queries, id, wiki_url))

pprint(results)
`
