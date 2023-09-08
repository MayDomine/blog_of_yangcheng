---
title: 'A Post-Training Framework for Improving Heterogeneous Graph Neural Networks'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Gong, Xumeng
  - Shi, Chuan
  - Yu, Philip

# # Author notes (optional)
# author_notes:
#   - 'Equal contribution'
#   - 'Equal contribution'

date: '2023'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2023-06-26T00:00:00Z'

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ['1']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the ACM Web Conference 2023*
publication_short: In *WWW*

abstract: Recent years have witnessed the success of heterogeneous graph neural networks (HGNNs) in modeling heterogeneous information networks (HINs). In this paper, we focus on the benchmark task of HGNNs, i.e., node classification, and empirically find that typical HGNNs are not good at predicting the label of a test node whose receptive field (1) has few training nodes from the same category or (2) has multiple training nodes from different categories. A possible explanation is that their message passing mechanisms may involve noises from different categories, and cannot fully explore task-specific knowledge such as the label dependency between distant nodes. Therefore, instead of introducing a new HGNN model, we propose a general post-training framework that can be applied on any pretrained HGNNs to further inject task-specific knowledge and enhance their prediction performance. 

# Summary. An optional shortened abstract.
summary: ""

tags: []

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/pdf/2304.00698.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# image:
#   caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
#   focal_point: ''
#   preview_only: false

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
