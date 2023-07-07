---
title: 'Network representation learning with rich text information'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Liu, Zhiyuan
  - Zhao, Deli 
  - Sun, Maosong
  - Chang, Edward Y

# # Author notes (optional)
# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'

date: '2015'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2015-07-25T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *International Joint Conferences on Artificial Intelligence*
publication_short: In *IJCAI*

abstract: Representation learning has shown its effectiveness in many tasks such as image classification and text mining. Network representation learning aims at learning distributed vector representation for each vertex in a network, which is also increasingly recognized as an important aspect for network analysis. Most network representation learning methods investigate network structures for learning. In reality, network vertices contain rich information (such as text), which cannot be well applied with algorithmic frameworks of typical representation learning methods. By proving that DeepWalk, a state-of-the-art network representation method, is actually equivalent to matrix factorization (MF), we propose text-associated DeepWalk (TADW). TADW incorporates text features of vertices into network representation learning under the framework of matrix factorization. We evaluate our method and various baseline methods by applying them to the task of multi-class classification of vertices. The experimental results show that, our method outperforms other baselines on all three datasets, especially when networks are noisy and training ratio is small.

# Summary. An optional shortened abstract.
summary: ""

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://nlp.csai.tsinghua.edu.cn/~lzy/publications/ijcai2015_network.pdf'
url_code: 'https://github.com/albertyang33/TADW'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
# projects:
#   - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

{{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}}

Supplementary notes can be added here, including [code, math, and images](https://wowchemy.com/docs/writing-markdown-latex/).
