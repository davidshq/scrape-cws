from comcrawl import IndexClient
import pandas as pd

client = IndexClient(['2023-06'], verbose=True)

client.search("chrome.google.com/webstore", threads=1)


client.results = (pd.DataFrame(client.results)
                  .drop_duplicates("urlkey", keep="last")
                  .to_dict("records"))

client.download(threads=1)

pd.DataFrame(client.results).to_csv("results.csv", index=False)