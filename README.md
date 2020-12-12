# commonsense-papers
Must-read papers on commonsense knowledge and others resources and tutorials

We aim to select the most representative and innovative papers in the research field of **commonsense knowledge**, and provide taxonomy/classification as well as statistics of these papers to give a quick overview of the field and help focused reading.

Contributed by [ADAPTers](https://adapt.seiee.sjtu.edu.cn/) (major efforts by Zhiling Zhang([@blmoistawinde](https://github.com/blmoistawinde)), Siyu Ren, Hongru Huang, Zelin Zhou, Yanzhu Guo)

Our list may not be complete. We will keep adding papers and improving it. [Contributions](CONTRIBUTING.md) are welcomed!

<script type='text/javascript' src='https://d1bxh8uas1mnw7.cloudfront.net/assets/embed.js'></script>
<script async src="https://badge.dimensions.ai/badge.js" charset="utf-8"></script>

<h2 id="toc">Table of Contents</h2>

- [commonsense-papers](#commonsense-papers)
  - [Statistics](#statistics)
  - [Tutorial and Survey](#tutorial-and-survey)
  - [Resources and Evaluation](#resources-and-evaluation)
    - [Commonsense Knowledge Bases/Models](#commonsense-knowledge-basesmodels)
    - [Related Knowledge Bases](#related-knowledge-bases)
    - [Datasets and Benchmarks](#datasets-and-benchmarks)
    - [Evaluation and Probing](#evaluation-and-probing)
  - [Knowledge Mining (Knowledge Base Completion)](#knowledge-mining-knowledge-base-completion)
  - [Applications](#applications)
    - [natural language inference (NLI) and commonsense reasoning (CSR)](#natural-language-inference-nli-and-commonsense-reasoning-csr)
    - [Machine Reading Comprehension (MRC)](#machine-reading-comprehension-mrc)
    - [Generation](#generation)
    - [Question Answering (QA)](#question-answering-qa)
    - [Vision, Robotics, Multimodal, Grounding and Speech](#vision-robotics-multimodal-grounding-and-speech)

## Statistics

Total papers in this repo: <anchor id="cnt">57</anchor> .

**Research Keywords**

Non-stopping words in title, indicating the hot topics in this field.

<anchor id="keyword">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>reasoning</th>
      <td>12</td>
    </tr>
    <tr>
      <th>graph</th>
      <td>6</td>
    </tr>
    <tr>
      <th>question</th>
      <td>5</td>
    </tr>
    <tr>
      <th>model</th>
      <td>5</td>
    </tr>
    <tr>
      <th>common</th>
      <td>4</td>
    </tr>
    <tr>
      <th>challenge</th>
      <td>4</td>
    </tr>
    <tr>
      <th>answering</th>
      <td>4</td>
    </tr>
    <tr>
      <th>pre</th>
      <td>4</td>
    </tr>
    <tr>
      <th>sense</th>
      <td>4</td>
    </tr>
    <tr>
      <th>reason</th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</anchor>

<br/>

**Researchers**

Most active researchers in this field

<anchor id="researcher">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/1699545">Yejin Choi</a></th>
      <td>14</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/2691021">Antoine Bosselut</a></th>
      <td>7</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/1857797">Chandra Bhagavatula</a></th>
      <td>7</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/51583409">Bill Yuchen Lin</a></th>
      <td>6</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/39227408">Ronan Le Bras</a></th>
      <td>5</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/1384550891">Xiang Ren</a></th>
      <td>4</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/2516777">Hannah Rashkin</a></th>
      <td>4</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/144590225">Dan Roth</a></th>
      <td>4</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/2729164">Maarten Sap</a></th>
      <td>4</td>
    </tr>
    <tr>
      <th><a href="https://www.semanticscholar.org/author/48212577">Hongming Zhang</a></th>
      <td>3</td>
    </tr>
  </tbody>
</table>
</anchor>

**Venues**

Just an estimation. May not be precise as arxiv papers may appear in other venues in the future.

<anchor id="venue">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>EMNLP</th>
      <td>11</td>
    </tr>
    <tr>
      <th>ACL</th>
      <td>11</td>
    </tr>
    <tr>
      <th>arxiv</th>
      <td>9</td>
    </tr>
    <tr>
      <th>AAAI</th>
      <td>5</td>
    </tr>
    <tr>
      <th>AKBC</th>
      <td>2</td>
    </tr>
  </tbody>
</table>
</anchor>

<br/>

## Tutorial and Survey

**Recent Advances in Natural Language Inference: A Survey of Benchmarks, Resources, and Approaches** arxiv 2019 [paper](https://arxiv.org/pdf/1904.01172) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1904.01172"  style="float:left"></div> <br/>

*Shane Storks, Qiaozi Gao, Joyce Y. Chai* (Citations: 27, 2 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1904.01172"  style="float:left"></div> <br/>

**T6: Commonsense Reasoning for Natural Language Processing.** ACL 2020. [slides and video](https://slideslive.com/38931667/t6-commonsense-reasoning-for-natural-language-processing) 

*Antoine Bosselut, Dan Roth, Maarten Sap, Vered Shwartz, Yejin Choi*

[back to table of contents](#toc)

## Resources and Evaluation

### Commonsense Knowledge Bases/Models
<br/>

**CYC: Toward programs with common sense** [data(OpenCyc)](https://github.com/asanchez75/opencyc) [homepage](https://www.cyc.com/)

**Commonsense causal reasoning between short texts** (CausalNet) KR 2016 [paper](http://www.cs.sjtu.edu.cn/~kzhu/papers/kzhu-copa.pdf) [homepage](https://adapt.seiee.sjtu.edu.cn/project_causal.html) [code](https://github.com/cs-zyluo/CausalNet)

*Zhiyi Luo, Yuchen Sha, Kenny Q. Zhu, Seung-won Hwang, Zhongyuan Wang*

**ConceptNet 5.5: an open multilingual graph of general knowledge** AAAI 2017. [paper](https://arxiv.org/pdf/1612.03975) [homepage](https://conceptnet.io/) [repo](https://github.com/commonsense/conceptnet5) [embedding(ConceptNet Numberbatch) repo](https://github.com/commonsense/conceptnet-numberbatch) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1612.03975"  style="float:left"></div> <br/>

*Robyn Speer, Joshua Chin, Catherine Havasi* (Citations: 604, 150 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1612.03975"  style="float:left"></div> <br/>

**ATOMIC: An Atlas of Machine Commonsense for If-Then Reasoning** AAAI 2019. [paper](https://arxiv.org/pdf/1811.00146.pdf) [homepage](https://homes.cs.washington.edu/~msap/atomic/) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1811.00146"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1609/AAAI.V33I01.33013027" data-style="small_rectangle"  style="float:left"></span> <br/>

*Maarten Sap, Ronan LeBras, Emily Allaway, Chandra Bhagavatula, Nicholas Lourie, Hannah Rashkin, Brendan Roof, Noah A. Smith, Yejin Choi* (Citations: 147, 36 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1811.00146"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1609/AAAI.V33I01.33013027" data-style="small_rectangle"  style="float:left"></span> <br/>

**COMET: Commonsense Transformers for Automatic Knowledge Graph Construction** ACL 2019 [paper](https://arxiv.org/abs/1906.05317) [homepage](https://mosaickg.apps.allenai.org/) [code](https://github.com/atcbosselut/comet-commonsense) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1906.05317"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/P19-1470" data-style="small_rectangle"  style="float:left"></span> <br/>

*Antoine Bosselut, Hannah Rashkin, Maarten Sap, Chaitanya Malaviya, Asli Celikyilmaz, Yejin Choi* (Citations: 115, 23 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1906.05317"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/P19-1470" data-style="small_rectangle"  style="float:left"></span> <br/>

**ASER: A Large-scale Eventuality Knowledge Graph.** WWW 2020 [paper](https://arxiv.org/pdf/1905.00270) [homepage](https://hkust-knowcomp.github.io/ASER/) [code](https://github.com/HKUST-KnowComp/ASER) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1905.00270"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1145/3366423.3380107" data-style="small_rectangle"  style="float:left"></span> <br/>

*Hongming Zhang, Xin Liu, Haojie Pan, Yangqiu Song, Cane Wing-Ki Leung* (Citations: 13, 2 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1905.00270"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1145/3366423.3380107" data-style="small_rectangle"  style="float:left"></span> <br/>

**Commonsense Properties from Query Logs and Question Answering Forums** (quasimodo) CIKM 2019 [paper](https://arxiv.org/pdf/1905.10989.pdf) [homepage](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/commonsense/quasimodo/) [code](https://github.com/Aunsiels/CSK) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1905.10989"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1145/3357384.3357955" data-style="small_rectangle"  style="float:left"></span> <br/>

*Julien Romero, Simon Razniewski, Koninika Pal, Jeff Z. Pan, Archit Sakhadeo, Gerhard Weikum* (Citations: 12, 1 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1905.10989"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1145/3357384.3357955" data-style="small_rectangle"  style="float:left"></span> <br/>

**TransOMCS: From Linguistic Graphs to Commonsense Knowledge**  IJCAI 2020 [paper](https://arxiv.org/pdf/2005.00206) [homepage](https://hkust-knowcomp.github.io/ASER/) [code](https://github.com/HKUST-KnowComp/TransOMCS) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.00206"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.24963/ijcai.2020/550" data-style="small_rectangle"  style="float:left"></span> <br/>

*Hongming Zhang, Daniel Khashabi, Yangqiu Song, Dan Roth* (Citations: 6, 2 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.00206"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.24963/ijcai.2020/550" data-style="small_rectangle"  style="float:left"></span> <br/>

**Paragraph-Level Commonsense Transformers with Recurrent Memory** (PARA-COMeT) arxiv 2020 [paper](https://arxiv.org/pdf/2010.01486) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2010.01486"  style="float:left"></div> <br/>

*Saadia Gabriel, Chandra Bhagavatula, Vered Shwartz, Ronan Le Bras, Maxwell Forbes, Yejin Choi* (Citations: 0) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2010.01486"  style="float:left"></div> <br/>

**COMET-ATOMIC 2020: On Symbolic and Neural Commonsense Knowledge Graphs** arxiv 2020 [paper](https://arxiv.org/pdf/2010.05953.pdf) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2010.05953"  style="float:left"></div> <br/>

*Jena D. Hwang, Chandra Bhagavatula, Ronan Le Bras, Jeff Da, Keisuke Sakaguchi, Antoine Bosselut, Yejin Choi* (Citations: 0) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2010.05953"  style="float:left"></div> <br/>

**CommonGen: A Constrained Text Generation Challenge for Generative Commonsense Reasoning** EMNLP 2020 Findings [paper](https://arxiv.org/pdf/1911.03705) [homepage](https://inklab.usc.edu/CommonGen/index.html) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1911.03705"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.findings-emnlp.165" data-style="small_rectangle"  style="float:left"></span> <br/>

*Bill Yuchen Lin, Wangchunshu Zhou, Ming Shen, Pei Zhou, Chandra Bhagavatula, Yejin Choi, Xiang Ren* (Citations: 8, 2 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1911.03705"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.findings-emnlp.165" data-style="small_rectangle"  style="float:left"></span> <br/>

### Related Knowledge Bases
<br/>

**WordNet: A Lexical Database for English** Communications of the ACM Vol. 38, No. 11: 39-41. 1995. [homepage] (https://wordnet.princeton.edu/)

*George A. Miller*

**Toward an Architecture for Never-Ending Language Learning** (NELL). AAAI 2010 [paper](http://rtw.ml.cmu.edu/papers/carlson-aaai10.pdf) [homepage](http://rtw.ml.cmu.edu/rtw/) 

*Andrew Carlson, Justin Betteridge, Bryan Kisiel, Burr Settles, Estevam R. Hruschka Jr., and Tom M. Mitchell*

**DBpedia – A Large-scale, Multilingual Knowledge Base Extracted from Wikipedia**. Semantic Web 2012 [paper](http://svn.aksw.org/papers/2013/SWJ_DBpedia/public.pdf) [homepage](https://wiki.dbpedia.org/)

*Jens Lehmann, Robert Isele, Max Jakob, Anja Jentzsch, Dimitris Kontokostas, Pablo N. Mendes, Sebastian Hellmann, Mohamed Morsey, Patrick van Kleef, Sören Auer, Christian Bizer*

### Datasets and Benchmarks
<br/>

**A Corpus and Cloze Evaluation for Deeper Understanding of Commonsense Stories** (Story Cloze Test) NAACL 2016 [paper](https://www.aclweb.org/anthology/N16-1098.pdf) [homepage](https://cs.rochester.edu/nlp/rocstories/)

*Nasrin Mostafazadeh, Nathanael Chambers, Xiaodong He, Devi Parikh, Dhruv Batra, Lucy Vanderwende, Pushmeet Kohli, James Allen*

**Modeling Naive Psychology of Characters in Simple Commonsense Stories** ACL 2018 [paper](https://arxiv.org/pdf/1805.06533) [homepage](https://uwnlp.github.io/storycommonsense/) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1805.06533"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/P18-1213" data-style="small_rectangle"  style="float:left"></span> <br/>

*Hannah Rashkin, Antoine Bosselut, Maarten Sap, Kevin Knight, Yejin Choi* (Citations: 32, 7 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1805.06533"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/P18-1213" data-style="small_rectangle"  style="float:left"></span> <br/>

**SemEval-2018 Task 11: Machine Comprehension Using Commonsense Knowledge** SemEval 2018 [paper](https://www.aclweb.org/anthology/S18-1119.pdf)

*Simon Ostermann, Michael Roth, Ashutosh Modi, Stefan Thater, Manfred Pinkal*

**Reasoning about Actions and State Changes by Injecting Commonsense Knowledge** (ProPara) EMNLP 2018 [paper](https://arxiv.org/pdf/1808.10012) [code](https://github.com/allenai/propara) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1808.10012"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/D18-1006" data-style="small_rectangle"  style="float:left"></span> <br/>

*Niket Tandon, Bhavana Dalvi Mishra, Joel Grus, Wen-tau Yih, Antoine Bosselut, Peter Clark* (Citations: 41, 7 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1808.10012"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/D18-1006" data-style="small_rectangle"  style="float:left"></span> <br/>

**CommonSenseqa: A question answering challenge targeting commonsense knowledge** NAACL 2019 [paper](https://arxiv.org/abs/1811.00937) [homepage](https://www.tau-nlp.org/commonsenseqa) [code](https://github.com/jonathanherzig/commonsenseqa) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1811.00937"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/N19-1421" data-style="small_rectangle"  style="float:left"></span> <br/>

*Alon Talmor, Jonathan Herzig, Nicholas Lourie, Jonathan Berant* (Citations: 146, 48 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1811.00937"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/N19-1421" data-style="small_rectangle"  style="float:left"></span> <br/>

**From Recognition to Cognition: Visual Commonsense Reasoning** CVPR 2019 [paper](http://openaccess.thecvf.com/content_CVPR_2019/papers/Zellers_From_Recognition_to_Cognition_Visual_Commonsense_Reasoning_CVPR_2019_paper.pdf) [code](https://github.com/rowanz/r2c/) [homepage](http://visualcommonsense.com/)

*Rowan Zellers, Yonatan Bisk, Ali Farhadi, Yejin Choi*

**oLMpics -- On what Language Model Pre-training Captures** arxiv 2019 [paper](https://arxiv.org/pdf/1912.13283.pdf) [code](https://github.com/alontalmor/oLMpics) [homepage](https://github.com/alontalmor/oLMpics) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1912.13283"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1162/tacl_a_00342" data-style="small_rectangle"  style="float:left"></span> <br/>

*Alon Talmor, Yanai Elazar, Yoav Goldberg, Jonathan Berant* (Citations: 56, 7 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1912.13283"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1162/tacl_a_00342" data-style="small_rectangle"  style="float:left"></span> <br/>

**ABDUCTIVE COMMONSENSE REASONING** (ART) ICLR 2020 [paper](https://arxiv.org/pdf/1908.05739) [homepage](http://abductivecommonsense.xyz/) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1908.05739"  style="float:left"></div> <br/>

*Chandra Bhagavatula, Ronan Le Bras, Chaitanya Malaviya, Keisuke Sakaguchi, Ari Holtzman, Hannah Rashkin, Doug Downey, Scott Wen-tau Yih, Yejin Choi* (Citations: 52, 7 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1908.05739"  style="float:left"></div> <br/>

**PIQA: Reasoning about Physical Commonsense in Natural Language** AAAI 2020 [paper](https://arxiv.org/pdf/1911.11641.pdf) [homepage](https://yonatanbisk.com/piqa/) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1911.11641"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1609/AAAI.V34I05.6239" data-style="small_rectangle"  style="float:left"></span> <br/>

*Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, Yejin Choi* (Citations: 39, 4 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1911.11641"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1609/AAAI.V34I05.6239" data-style="small_rectangle"  style="float:left"></span> <br/>

**Reasoning about Goals, Steps, and Temporal Ordering with WikiHow** EMNLP 2020 [paper](https://arxiv.org/pdf/2009.07690) [code](https://github.com/zharry29/wikihow-goal-step) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2009.07690"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.374" data-style="small_rectangle"  style="float:left"></span> <br/>

*Qing Lyu, Li Zhang, Chris Callison-Burch* (Citations: 0) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2009.07690"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.374" data-style="small_rectangle"  style="float:left"></span> <br/>

**Birds have four legs?! NumerSense: Probing Numerical Commonsense Knowledge of Pre-trained Language Models** EMNLP 2020 [paper](https://arxiv.org/pdf/2005.00683.pdf) [homepage](https://inklab.usc.edu/NumerSense/) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.00683"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.557" data-style="small_rectangle"  style="float:left"></span> <br/>

*Bill Yuchen Lin, Seyeon Lee, Rahul Khanna and Xiang Ren* (Citations: 2) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.00683"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.557" data-style="small_rectangle"  style="float:left"></span> <br/>

**A Review of Winograd Schema Challenge Datasets and Approaches** arxiv 2020 [paper](https://arxiv.org/abs/2004.13831) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2004.13831"  style="float:left"></div> <br/>

*Vid Kocijan, Thomas Lukasiewicz, Ernest Davis, Gary Marcus, Leora Morgenstern* (Citations: 2) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2004.13831"  style="float:left"></div> <br/>

[back to table of contents](#toc)

### Evaluation and Probing

**Reporting Bias and Knowledge Acquisition** AKBC 2013 [paper](https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemId=27832&itemFileId=142662)

*Jonathan Gordon, Benjamin Van Durme*

**Do Neural Language Representations Learn Physical Commonsense?** CogSci 2019 [paper](https://arxiv.org/pdf/1908.02899.pdf) [code](https://github.com/mbforbes/physical-commonsense) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1908.02899"  style="float:left"></div> <br/>

*Maxwell Forbes, Ari Holtzman, Yejin Choi* (Citations: 17, 1 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1908.02899"  style="float:left"></div> <br/>

**Joint Reasoning for Multi-Faceted Commonsense Knowledge** AKBC 2020 [paper](https://arxiv.org/pdf/2001.04170.pdf) [homepage](https://dice.mpi-inf.mpg.de/) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2001.04170"  style="float:left"></div> <br/>

*Yohan Chalier, Simon Razniewski, Gerhard Weikum* (Citations: 5) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2001.04170"  style="float:left"></div> <br/>

**Does BERT Solve Commonsense Task via Commonsense Knowledge?** arxiv 2020 [paper](https://arxiv.org/pdf/2008.03945) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2008.03945"  style="float:left"></div> <br/>

*Leyang Cui, Sijie Cheng, Yu Wu, Yue Zhang* (Citations: 2) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2008.03945"  style="float:left"></div> <br/>

**WinoWhy: A Deep Diagnosis of Essential Commonsense Knowledge for Answering Winograd Schema Challenge** ACL 2020 [paper](https://arxiv.org/pdf/2005.05763) [code](https://github.com/HKUST-KnowComp/WinoWhy) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.05763"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.acl-main.508" data-style="small_rectangle"  style="float:left"></span> <br/>

*Hongming Zhang, Xinran Zhao, Yangqiu Song* (Citations: 1) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.05763"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.acl-main.508" data-style="small_rectangle"  style="float:left"></span> <br/>

[back to table of contents](#toc)

## Knowledge Mining (Knowledge Base Completion)

**Automatic Extraction of Commonsense LocatedNear Knowledge** ACL 2018 [paper](https://arxiv.org/pdf/1711.04204) [code](https://github.com/adapt-sjtu/commonsense-locatednear) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1711.04204"  style="float:left"></div> <br/>

*Frank F. Xu, Bill Yuchen Lin, Kenny Q. Zhu* (Citations: 1) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1711.04204"  style="float:left"></div> <br/>

**Commonsense Knowledge Mining from Pretrained Models** EMNLP 2019 [paper](https://www.aclweb.org/anthology/D19-1109.pdf)

*Joe Davison, Joshua Feldman, Alexander Rush*

**Language Models as Knowledge Bases?** EMNLP 2019 [paper](https://arxiv.org/pdf/1909.01066.pdf) [code](https://github.com/facebookresearch/LAMA) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1909.01066"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/D19-1250" data-style="small_rectangle"  style="float:left"></span> <br/>

*Fabio Petroni, Tim Rocktäschel, Patrick Lewis, Anton Bakhtin, Yuxiang Wu, Alexander H. Miller, Sebastian Riedel* (Citations: 187, 33 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1909.01066"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/D19-1250" data-style="small_rectangle"  style="float:left"></span> <br/>

**Commonsense Knowledge Base Completion with Structural and Semantic Context** AAAI 2020 [paper](https://arxiv.org/pdf/1910.02915) [code](https://github.com/allenai/commonsense-kg-completion) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1910.02915"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1609/AAAI.V34I03.5684" data-style="small_rectangle"  style="float:left"></span> <br/>

*Chaitanya Malaviya, Chandra Bhagavatula, Antoine Bosselut, Yejin Choi* (Citations: 10, 3 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1910.02915"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1609/AAAI.V34I03.5684" data-style="small_rectangle"  style="float:left"></span> <br/>

**Temporal Common Sense Acquisition with Minimal Supervision** ACL 2020 [paper](https://arxiv.org/pdf/2005.04304.pdf) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.04304"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.acl-main.678" data-style="small_rectangle"  style="float:left"></span> <br/>

*Ben Zhou, Qiang Ning, Daniel Khashabi, Dan Roth* (Citations: 10) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.04304"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.acl-main.678" data-style="small_rectangle"  style="float:left"></span> <br/>

**Learning Physical Common Sense as Knowledge Graph Completion via BERT Data Augmentation and Constrained Tucker Factorization** EMNLP 2020 [paper](https://www.aclweb.org/anthology/2020.emnlp-main.266.pdf)

*Zhenjie Zhao, Evangelos Papalexakis, Xiaojuan Ma*

[back to table of contents](#toc)

## Applications

### natural language inference (NLI) and commonsense reasoning (CSR)
<br/>

**Neural natural language inference models enhanced with external knowledge** ACL 2018 [paper](https://arxiv.org/abs/1711.04289) [code](https://github.com/lukecq1231/kim) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1711.04289"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/P18-1224" data-style="small_rectangle"  style="float:left"></span> <br/>
- resource: WordNet
 (Citations: 116, 19 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1711.04289"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/P18-1224" data-style="small_rectangle"  style="float:left"></span> <br/>
*Qian Chen, Xiaodan Zhu, Zhen-Hua Ling, Diana Inkpen, Si Wei*

**Incorporating Structured Commonsense Knowledge in Story Completion** AAAI 2019 [paper](https://www.aaai.org/ojs/index.php/AAAI/article/download/5183/5055)
- resource: ConceptNet Numberbatch

*Jiaao Chen, Jianshu Chen, Zhou Yu*

**Contrastive Self-Supervised Learning for Commonsense Reasoning** ACL 2020 [paper](https://arxiv.org/pdf/2005.00669.pdf) [code](https://github.com/SAP-samples/acl2020-commonsense/) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.00669"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.acl-main.671" data-style="small_rectangle"  style="float:left"></span> <br/>

*Tassilo Klein, Moin Nabi* (Citations: 5) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.00669"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.acl-main.671" data-style="small_rectangle"  style="float:left"></span> <br/>

**Do Language Embeddings Capture Scales?** EMNLP Findings 2020 [paper](https://arxiv.org/pdf/2010.05345) [code](https://github.com/google-research-datasets/numbert) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2010.05345"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.findings-emnlp.439" data-style="small_rectangle"  style="float:left"></span> <br/>

*Xikun Zhang, Deepak Ramachandran, Ian Tenney, Yanai Elazar, Dan Roth* (Citations: 0) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2010.05345"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.findings-emnlp.439" data-style="small_rectangle"  style="float:left"></span> <br/>

**Differentiable Open-Ended Commonsense Reasoning** arxiv 2020 [paper](https://arxiv.org/pdf/2010.14439) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2010.14439"  style="float:left"></div> <br/>

*Bill Yuchen Lin, Haitian Sun, Bhuwan Dhingra, Manzil Zaheer, Xiang Ren, William W. Cohen* (Citations: 1) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2010.14439"  style="float:left"></div> <br/>

**Pre-training Text-to-Text Transformers for Concept-centric Common Sense** arxiv 2020 [paper](https://arxiv.org/pdf/2011.07956) [code](https://anonymous.4open.science/r/6fdeed55-ec2c-4ffa-aee8-0cc3b7f5ade5/) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2011.07956"  style="float:left"></div> <br/>

*Wangchunshu Zhou, Dong-Ho Lee, Ravi Kiran Selvam, Seyeon Lee, Bill Yuchen Lin, Xiang Ren* (Citations: 0) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2011.07956"  style="float:left"></div> <br/>

### Machine Reading Comprehension (MRC)
<br/>

**Enhancing Pre-Trained Language Representations with Rich Knowledge for Machine Reading Comprehension** ACL 2019 [paper](https://www.aclweb.org/anthology/P19-1226.pdf) [code](https://github.com/PaddlePaddle/Research/tree/master/NLP/ACL2019-KTNET)
- resource: WordNet, NELL 

*An Yang, Quan Wang, Jing Liu, Kai Liu, Yajuan Lyu, Hua Wu, Qiaoqiao She, Sujian Li*

### Generation
<br/>

**Diverse and Informative Dialogue Generation with Context-Specific Commonsense Knowledge Awareness** ACL 2020 [paper](https://www.aclweb.org/anthology/2020.acl-main.515.pdf) [code](https://github.com/pku-orangecat/ACL2020-ConKADI)
- resource: ConceptNet

*Sixing Wu, Ying Li, Dawei Zhang, Yang Zhou, Zhonghai Wu*


**Language Generation with Multi-Hop Reasoning on Commonsense Knowledge Graph** EMNLP 2020 [paper](https://arxiv.org/pdf/2009.11692.pdf) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2009.11692"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.54" data-style="small_rectangle"  style="float:left"></span> <br/>
- resource: ConceptNet
 (Citations: 2) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2009.11692"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.54" data-style="small_rectangle"  style="float:left"></span> <br/>
*Haozhe Ji, Pei Ke, Shaohan Huang, Furu Wei, Xiaoyan Zhu, Minlie Huang*

### Question Answering (QA)
<br/>

**Dynamic Knowledge Graph Construction for Zero-shot Commonsense Question Answering** arxiv 2019 [paper](https://arxiv.org/pdf/1911.03876) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1911.03876"  style="float:left"></div> <br/>
- resource: COMET
 (Citations: 0) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1911.03876"  style="float:left"></div> <br/>
*Antoine Bosselut, Yejin Choi*

**Adversarial Training for Commonsense Inference** ACL 2020 RepL4NLP workshop [paper](https://arxiv.org/pdf/2005.08156) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.08156"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.repl4nlp-1.8" data-style="small_rectangle"  style="float:left"></span> <br/>

*Lis Pereira, Xiaodong Liu, Fei Cheng, Masayuki Asahara, Ichiro Kobayashi* (Citations: 2) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.08156"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.repl4nlp-1.8" data-style="small_rectangle"  style="float:left"></span> <br/>

**Unsupervised Commonsense Question Answering with Self-Talk** EMNLP 2020 [paper](https://arxiv.org/pdf/2004.05483) [code](https://github.com/vered1986/self_talk) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2004.05483"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.373" data-style="small_rectangle"  style="float:left"></span> <br/>
- resource: ConceptNet, COMET, Google N-grams
 (Citations: 15, 1 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2004.05483"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.373" data-style="small_rectangle"  style="float:left"></span> <br/>
*Vered Shwartz, Peter West, Ronan Le Bras, Chandra Bhagavatula, Yejin Choi*

**Scalable Multi-Hop Relational Reasoning for Knowledge-Aware Question Answering** EMNLP 2020 [paper](https://arxiv.org/pdf/2005.00646) [code](https://github.com/INK-USC/MHGRN) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.00646"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.99" data-style="small_rectangle"  style="float:left"></span> <br/>

*Yanlin Feng, Xinyue Chen, Bill Yuchen Lin, Peifeng Wang, Jun Yan, Xiang Ren* (Citations: 7, 1 influential) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="2005.00646"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.18653/v1/2020.emnlp-main.99" data-style="small_rectangle"  style="float:left"></span> <br/>

### Vision, Robotics, Multimodal, Grounding and Speech

<br/>

**Enabling Robots to Understand Incomplete Natural Language Instructions Using Commonsense Reasoning** ICRA 2020 [paper](https://arxiv.org/pdf/1904.12907) <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1904.12907"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1109/ICRA40945.2020.9197315" data-style="small_rectangle"  style="float:left"></span> <br/>

*Haonan Chen; Hao Tan; Alan Kuntz; Mohit Bansal; Ron Alterovitz* (Citations: 7) <br/> <div data-badge-popover="right" data-badge-type="2" data-hide-no-mentions="true" class="altmetric-embed" data-arxiv-id="1904.12907"  style="float:left"></div>  <span class="__dimensions_badge_embed__" data-doi="10.1109/ICRA40945.2020.9197315" data-style="small_rectangle"  style="float:left"></span> <br/>

**Visual Commonsense R-CNN** CVPR 2020 [paper](https://openaccess.thecvf.com/content_CVPR_2020/papers/Wang_Visual_Commonsense_R-CNN_CVPR_2020_paper.pdf) [code](https://github.com/Wangt-CN/VC-R-CNN)

*Tan Wang, Jianqiang Huang, Hanwang Zhang, Qianru Sun*

[back to table of contents](#toc)
