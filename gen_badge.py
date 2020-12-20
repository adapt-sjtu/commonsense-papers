import re
import numpy as np
import pandas as pd
from collections import defaultdict, Counter
import spacy
nlp = spacy.load("en_core_web_sm", disabled=["ner", "parser"])
import semanticscholar as sch
import markdown2
import jinja2

def str_sim(str1, str2):
    # currently use this simple heuristic
    chars1, chars2 = set(str1), set(str2)
    return len(chars1 & chars2) / max(min(len(chars1), len(chars2)), 1)

def most_sim_author(str1, author_list):
    best_sim, best_match = -1, None
    for str2 in author_list:
        sim0 = str_sim(str1, str2)
        if sim0 > best_sim:
            best_sim, best_match = sim0, str2
    return best_match

def special_cases(doi):
    paper_info = {}
    if doi == "10.5555/3032027.3032078":
        paper_info = sch.paper(f'CorpusID:27965578', timeout=2)
    return paper_info

# parameters
allow_search = True
TOP_KWDS = 10
TOP_AUTHORS = 15
TOP_VENUES = 5
my_stopwords = {"commonsense", "knowledge", "natural", "language"}
venue_rename = {"Transactions of the Association for Computational Linguistics": "TACL"}

paper_cnt = 0
author_cnt = Counter()
kwds_cnt = Counter()
venue_cnt = defaultdict(int)
lid2badges = defaultdict(str)
lid2citation_nums = defaultdict(str)
mention2aid = {}
aid2url = {}
curr_authors_info = None
readme_lines = []
with open("README.md", encoding="utf-8") as f:
    for lid, line in enumerate(f):
        line = line.strip()
        readme_lines.append(line)
        if re.search(r"^\*\*([^\*]+)\*\*", line):   # title
            title = re.search(r"^\*\*([^\*]+)\*\*", line).group(1)
            keywords = {x.lemma_.lower() for x in nlp(title) if not (x.is_stop or x.is_punct or x.lemma_.lower() in my_stopwords)}
            kwds_cnt.update(keywords)
            paper_cnt += 1
            doi = None
            # find arxiv id, and get details from semantic scholar API
            if re.search(r"https://arxiv.org/(pdf|abs)/(\d+\.\d+)", line):
                arxiv_id = re.search(r"https://arxiv.org/(pdf|abs)/(\d+\.\d+)", line).group(2)
                alt_badge = f' <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="{arxiv_id}"  style="float:left"></div> '
                lid2badges[lid] = alt_badge
                if allow_search:
                    paper_info = sch.paper(f'arxiv:{arxiv_id}', timeout=2)
                    citations = len(paper_info["citations"])
                    inf_citations = paper_info["influentialCitationCount"]
                    if inf_citations > 0:
                        lid2citation_nums[lid] = f" (Citations: {citations}, {inf_citations} influential) "
                    else:
                        lid2citation_nums[lid] = f" (Citations: {citations}) "
                    curr_authors_info = paper_info["authors"]
                    doi = paper_info.get('doi', None)
                    if doi is not None:
                        # use doi to link to Dimensions Badge
                        dim_badge = f' <span class="__dimensions_badge_embed__" data-doi="{doi}" data-style="small_rectangle"  style="float:left"></span> '
                        lid2badges[lid] = lid2badges[lid] + dim_badge
                else:
                    lid2citation_nums[lid] = " (Citations: ?) "
            # ACL id
            elif re.search(r"www.aclweb.org/anthology/(\S+).pdf", line):
                acl_id = re.search(r"www.aclweb.org/anthology/(\S+).pdf", line).group(1)
                if allow_search:
                    paper_info = sch.paper(f'ACL:{acl_id}', timeout=2)
                    citations = len(paper_info["citations"])
                    inf_citations = paper_info["influentialCitationCount"]
                    if inf_citations > 0:
                        lid2citation_nums[lid] = f" (Citations: {citations}, {inf_citations} influential) "
                    else:
                        lid2citation_nums[lid] = f" (Citations: {citations}) "
                    curr_authors_info = paper_info["authors"]
                    doi = paper_info.get('doi', None)
                    if doi is not None:
                        # use doi to link to both Badges
                        alt_badge = f' <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-doi="{doi}"  style="float:left"></div> '
                        lid2badges[lid] = alt_badge
                        dim_badge = f' <span class="__dimensions_badge_embed__" data-doi="{doi}" data-style="small_rectangle"  style="float:left"></span> '
                        lid2badges[lid] = lid2badges[lid] + dim_badge
            # ACM, directly with DOI
            elif re.search(r"dl.acm.org/doi/abs/(\S+)\)?", line):
                doi = re.search(r"dl.acm.org/doi/abs/(\S+)\)?", line).group(1).strip(")")
                if allow_search:
                    paper_info = sch.paper(f'{doi}', timeout=2)
                    if len(paper_info) == 0:
                        paper_info = special_cases(doi)
                        if len(paper_info) == 0:
                            continue
                    else:
                        continue
                    citations = len(paper_info["citations"])
                    inf_citations = paper_info["influentialCitationCount"]
                    if inf_citations > 0:
                        lid2citation_nums[lid] = f" (Citations: {citations}, {inf_citations} influential) "
                    else:
                        lid2citation_nums[lid] = f" (Citations: {citations}) "
                    curr_authors_info = paper_info["authors"]
                    doi = paper_info.get('doi', None)
                    if doi is not None:
                        # use doi to link to both Badges
                        alt_badge = f' <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-doi="{doi}"  style="float:left"></div> '
                        lid2badges[lid] = alt_badge
                        dim_badge = f' <span class="__dimensions_badge_embed__" data-doi="{doi}" data-style="small_rectangle"  style="float:left"></span> '
                        lid2badges[lid] = lid2badges[lid] + dim_badge
                else:
                    lid2citation_nums[lid] = " (Citations: ?) "
            else:
                lid2badges[lid] = ""
            print("doi", doi)
            try:
                beg = line.rfind(r"** ") + 3
                end = line.find("[") - 1
                venue_text = line[beg:end]
                if ")" in venue_text:
                    beg = venue_text.find(")")+1
                    venue_text = line[beg:end]
                tmp = venue_text.strip().split()
                venue, year = " ".join(tmp[:-1]), tmp[-1]

                # use info on semantic scholar to update venue
                if doi is not None:
                    venue_sch, year_sch = str(paper_info["venue"]), str(paper_info["year"])
                    # change to short name if in our list, else perserve the retrieved result
                    venue_sch = venue_rename.get(venue_sch, venue_sch)
                    if venue == 'arxiv' and (venue_sch != venue or year_sch != year):
                        print("Update paper venue!")
                        print(paper_info["title"], f"{venue} {year} -> {venue_sch} {year_sch}")
                        venue, year = venue_sch, year_sch
                        readme_lines[-1] = line[:beg] + f"{venue} {year}" + line[end:]
                if venue.strip() != "":
                    venue_cnt[venue] += 1
            except Exception as e:
                print(e)
                print(line)
                
        if re.search(r"^\*.+\*$", line):   # author
            authors = [x.strip() for x in line[1:-1].split(", ")]
            author_cnt.update(authors)
            if curr_authors_info != None:
                # match author mention with semantic scholar std name
                # first and last author should be accurately matched
                mention2aid[authors[0]] = curr_authors_info[0]['authorId']
                mention2aid[authors[-1]] = curr_authors_info[-1]['authorId']
                tmp_author2id = {}
                for author_info in curr_authors_info:
                    aid2url[author_info['authorId']] = author_info['url']
                    tmp_author2id[author_info['name']] = author_info['authorId']
                if len(authors) > 2:
                    for mention0 in authors[1:-1]:
                        if len(tmp_author2id) > 0:
                            matched_aname = most_sim_author(mention0, tmp_author2id)
                            mention2aid[mention0] = tmp_author2id[matched_aname]
                            del tmp_author2id[matched_aname]

            curr_authors_info = None

kwds_cnt = pd.DataFrame(pd.Series(kwds_cnt).sort_values(ascending=False), columns=["count"])
author_cnt = pd.DataFrame(pd.Series(author_cnt).sort_values(ascending=False), columns=["count"])
venue_cnt = pd.DataFrame(pd.Series(venue_cnt).sort_values(ascending=False), columns=["count"])

readme_to_md = "\n".join(readme_lines)
readme_to_md = re.sub(r'<anchor id="cnt">(.*?)</anchor>', f'<anchor id="cnt">{paper_cnt}</anchor>', readme_to_md)
html0 = kwds_cnt.head(TOP_KWDS).to_html()
readme_to_md = re.sub(r'<anchor id="keyword">\n(.*?)\n</anchor>', f'<anchor id="keyword">\n{html0}\n</anchor>', readme_to_md, flags=re.DOTALL)
html0 = author_cnt.head(TOP_AUTHORS).to_html()
for mention0 in author_cnt.index:
    if mention0 in mention2aid:
        url0 = aid2url[mention2aid[mention0]]
        html0 = html0.replace(mention0, f'<a href="{url0}">{mention0}</a>')
readme_to_md = re.sub(r'<anchor id="researcher">\n(.*?)\n</anchor>', f'<anchor id="researcher">\n{html0}\n</anchor>', readme_to_md, flags=re.DOTALL)
html0 = venue_cnt.head(TOP_VENUES).to_html()
readme_to_md = re.sub(r'<anchor id="venue">\n(.*?)\n</anchor>', f'<anchor id="venue">\n{html0}\n</anchor>', readme_to_md, flags=re.DOTALL)
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_to_md)

# write to website
for lid, cite_str in lid2citation_nums.items():
    if cite_str != "":
        readme_lines[lid] += cite_str
for lid, badge_str in lid2badges.items():
    if badge_str != "":
        readme_lines[lid] += (badge_str + "<br/>")
readme_to_html = "\n".join(readme_lines)
readme_to_html = re.sub(r'<anchor id="cnt">(.*?)</anchor>', f'<anchor id="cnt">{paper_cnt}</anchor>', readme_to_html)
html0 = kwds_cnt.head(TOP_KWDS).to_html()
readme_to_html = re.sub(r'<anchor id="keyword">\n(.*?)\n</anchor>', f'<anchor id="keyword">\n{html0}\n</anchor>', readme_to_html, flags=re.DOTALL)
html0 = author_cnt.head(TOP_AUTHORS).to_html()
for mention0 in author_cnt.index:
    if mention0 in mention2aid:
        url0 = aid2url[mention2aid[mention0]]
        html0 = html0.replace(mention0, f'<a href="{url0}">{mention0}</a>')
readme_to_html = re.sub(r'<anchor id="researcher">\n(.*?)\n</anchor>', f'<anchor id="researcher">\n{html0}\n</anchor>', readme_to_html, flags=re.DOTALL)
html0 = venue_cnt.head(TOP_VENUES).to_html()
readme_to_html = re.sub(r'<anchor id="venue">\n(.*?)\n</anchor>', f'<anchor id="venue">\n{html0}\n</anchor>', readme_to_html, flags=re.DOTALL)
html = markdown2.markdown(readme_to_html)

template = """
<head>
    <script type='text/javascript' charset="utf-8">{{dimensions_badge}}</script>
    <script type='text/javascript' charset="utf-8">{{altmetrics_badge}}</script>
</head>

{{main_body}}
"""

template = jinja2.Template(template)

template_vars = {
    "main_body": html,
    "dimensions_badge": open("static/badge.js", encoding="utf-8").read(),
    "altmetrics_badge": open("static/embed.js", encoding="utf-8").read()
}

html_out = template.render(template_vars)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_out)

print("Results (for human read)")
print("\n--Keyword--\n")
print(kwds_cnt.head(10))
print("\n--Author--\n")
print(author_cnt.head(10))
print("\n--Venue--\n")
print(venue_cnt.head(5))
print(f"Paper count: {paper_cnt}")