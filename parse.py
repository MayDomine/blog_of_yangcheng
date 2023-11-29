import json
import os
# 读取 JSONL 文件
with open('publications.jsonl', 'r') as file:
    publications = [json.loads(line) for line in file]

# 根据年份和引用量排序
publications.sort(key=lambda x: (x.get('bib', {}).get('pub_year', 0), x.get('num_citations', 0)), reverse=True)

# 生成前十篇出版物的 Markdown 文件
for pub in publications[:10]:
    title = pub['bib']['title']
    authors = [author for author in pub['bib']['author'].split(" and ")]
    authors = "\n\t-\t".join(["admin" if au == "Cheng Yang" else au for au in authors])
    year = pub['bib'].get('pub_year', '')
    doi = pub.get('doi', '')
    abstract = pub['bib'].get('abstract', '')
    url_pdf = pub.get('url_pdf', '')
    venue = pub['bib'].get('venue', '')
    if venue == "":
        venue = pub['bib'].get('journal', '')
    if venue == "":
        venue = pub['bib']['citation'].split(",")[0]
    markdown_content = f"""
---
title: '{title}'

authors:
  - {authors}

date: '{year}'
doi: '{doi}'

publishDate: '{year}-01-01T00:00:00Z'

publication_types: ['1']

publication: In *{venue}*

abstract: {abstract}

url_pdf: '{url_pdf}'
---

Supplementary notes can be added here.
"""
    # 写入文件
    os.makedirs(f'content/publication/{title}', exist_ok=True)
    with open(f"content/publication/{title}/index.md", 'w') as md_file:
        md_file.write(markdown_content)
    with open(f"content/publication/{title}/cite.bib", 'w') as bib_file:
        bib_file.write("")
