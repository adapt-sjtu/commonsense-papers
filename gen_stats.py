import re
import numpy as np
import pandas as pd
from collections import defaultdict, Counter
import spacy
nlp = spacy.load("en", disabled=["ner", "parser"])

"""
Plan to include statistics of
    - authors
    - keywords: non-stopping words in title
"""

author_cnt = Counter()
kwds_cnt = Counter()
my_stopwords = {"commonsense", "knowledge", "natural", "language"}
with open("README.md", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if re.search(r"^\*\*([^\*]+)\*\*", line):   # title
            title = re.search(r"^\*\*([^\*]+)\*\*", line).group(1)
            keywords = {x.lemma_.lower() for x in nlp(title) if not (x.is_stop or x.is_punct or x.lemma_.lower() in my_stopwords)}
            kwds_cnt.update(keywords)
            continue
        if re.search(r"^\*.+\*$", line):   # author
            authors = [x.strip() for x in line[1:-1].split(", ")]
            author_cnt.update(authors)

kwds_cnt = pd.DataFrame(pd.Series(kwds_cnt).sort_values(ascending=False), columns=["count"])
author_cnt = pd.DataFrame(pd.Series(author_cnt).sort_values(ascending=False), columns=["count"])

print("HTML")
print(kwds_cnt.head(10).to_html())
print("\n-----\n")
print(author_cnt.head(10).to_html())

print("Results (for human read)")
print(kwds_cnt.head(10))
print(author_cnt.head(10))
