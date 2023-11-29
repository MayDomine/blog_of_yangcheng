from scholarly import scholarly
import json

# Set up a ProxyGenerator object to use free proxies
# This needs to be done only once per session

# Replace with the Google Scholar ID of the researcher
author_id = 'OlLjVUcAAAAJ'

# Retrieve the author's data
search_query = scholarly.search_author_id(author_id)
author = scholarly.fill(search_query)

# File to save the publications
filename = "publications.jsonl"

with open(filename, "w") as file:
    for publication in author['publications'][:10]:
        filled_pub = scholarly.fill(publication)
        # Write each publication's details as a JSON object on a new line
        # 写入 JSONL 文件
        json.dump(filled_pub, file)
        file.write("\n")

print(f"Publications saved to {filename}")
