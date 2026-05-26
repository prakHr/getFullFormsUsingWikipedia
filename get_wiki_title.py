from playwright.async_api import async_playwright
import asyncio
from pprint import pprint

async def get_name(page, query, id, wiki_url):
    await page.goto(
        f"{wiki_url}{query}"
    )

    return {
        "query": query,
        "full_form": await page.text_content(id)
    }

async def get_Titles(queries,id,wiki_url):
    
    async with async_playwright() as p:
        browser = await p.chromium.launch()

        tasks = []

        for q in queries:
            page = await browser.new_page()
            tasks.append(get_name(page, q,id,wiki_url))

        results = await asyncio.gather(*tasks)


        await browser.close()
        return results



queries = ["CPU", "GPU", "RAM", "SSD", "HDD", "SingleShot", "MultiShot", "AutoFocus", "Aperture", "ISO", "ShutterSpeed"]
id = "#firstHeading"
wiki_url = "https://en.wikipedia.org/wiki/"
results = asyncio.run(get_Titles(queries, id, wiki_url))
pprint(results)