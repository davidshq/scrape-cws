from comcrawl import IndexClient

client = IndexClient(['2023-06'], verbose=True)

client.search("chrome.google.com/webstore/*")
client.download()

first_page_html = client.results[0]["html"]