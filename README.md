# commonsense-papers
Must-read papers on commonsense knowledge and others resources and tutorials

Contributed by [ADAPTers](https://adapt.seiee.sjtu.edu.cn/) (major efforts by Zhiling Zhang([@blmoistawinde](https://github.com/blmoistawinde)), Siyu Ren, Hongru Huang, Zelin Zhou, Yanzhu Guo)

Our list may not be complete. We will keep adding papers and improving it. Any suggestions and PRs are welcomed!

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

## Statistics

**Research Keywords**

Non-stopping words in title, indicating the hot topics in this field.

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
      <td>9</td>
    </tr>
    <tr>
      <th>language</th>
      <td>8</td>
    </tr>
    <tr>
      <th>question</th>
      <td>5</td>
    </tr>
    <tr>
      <th>graph</th>
      <td>5</td>
    </tr>
    <tr>
      <th>natural</th>
      <td>3</td>
    </tr>
    <tr>
      <th>model</th>
      <td>3</td>
    </tr>
    <tr>
      <th>generation</th>
      <td>3</td>
    </tr>
    <tr>
      <th>answering</th>
      <td>3</td>
    </tr>
    <tr>
      <th>inference</th>
      <td>3</td>
    </tr>
    <tr>
      <th>transformer</th>
      <td>2</td>
    </tr>
  </tbody>
</table>

<br/>

**Researchers**

Most active researchers in this field

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Yejin Choi</th>
      <td>11</td>
    </tr>
    <tr>
      <th>Chandra Bhagavatula</th>
      <td>7</td>
    </tr>
    <tr>
      <th>Bill Yuchen Lin</th>
      <td>5</td>
    </tr>
    <tr>
      <th>Antoine Bosselut</th>
      <td>5</td>
    </tr>
    <tr>
      <th>Ronan Le Bras</th>
      <td>4</td>
    </tr>
    <tr>
      <th>Dan Roth</th>
      <td>4</td>
    </tr>
    <tr>
      <th>Xiang Ren</th>
      <td>3</td>
    </tr>
    <tr>
      <th>Hannah Rashkin</th>
      <td>3</td>
    </tr>
    <tr>
      <th>Chaitanya Malaviya</th>
      <td>3</td>
    </tr>
    <tr>
      <th>Vered Shwartz</th>
      <td>3</td>
    </tr>
  </tbody>
</table>

## Tutorial and Survey

**Recent Advances in Natural Language Inference: A Survey of Benchmarks, Resources, and Approaches** arxiv 2019 [paper](https://arxiv.org/pdf/1904.01172)

*Shane Storks, Qiaozi Gao, Joyce Y. Chai*

**T6: Commonsense Reasoning for Natural Language Processing.** ACL 2020. [slides and video](https://slideslive.com/38931667/t6-commonsense-reasoning-for-natural-language-processing) 

*Antoine Bosselut, Dan Roth, Maarten Sap, Vered Shwartz, Yejin Choi*

[back to table of contents](#toc)

## Resources and Evaluation

### Commonsense Knowledge Bases/Models
<br/>

**CYC: Toward programs with common sense** [data(OpenCyc)](https://github.com/asanchez75/opencyc) [homepage](https://www.cyc.com/)

**ConceptNet 5.5: an open multilingual graph of general knowledge** AAAI 2017. [paper](https://arxiv.org/pdf/1612.03975) [homepage](https://conceptnet.io/)

*Robyn Speer, Joshua Chin, Catherine Havasi*

**ATOMIC: An Atlas of Machine Commonsense for If-Then Reasoning** AAAI 2019. [paper](https://arxiv.org/pdf/1811.00146.pdf) [homepage](https://homes.cs.washington.edu/~msap/atomic/)

*Maarten Sap, Ronan LeBras, Emily Allaway, Chandra Bhagavatula, Nicholas Lourie, Hannah Rashkin, Brendan Roof, Noah A. Smith, Yejin Choi*

**COMET: Commonsense Transformers for Automatic Knowledge Graph Construction** ACL 2019 [paper](https://arxiv.org/abs/1906.05317) [homepage](https://mosaickg.apps.allenai.org/) [code](https://github.com/atcbosselut/comet-commonsense)

*Antoine Bosselut, Hannah Rashkin, Maarten Sap, Chaitanya Malaviya, Asli Celikyilmaz, Yejin Choi*

**ASER: A Large-scale Eventuality Knowledge Graph.** WWW 2020 [paper](https://arxiv.org/pdf/1905.00270) [homepage](https://hkust-knowcomp.github.io/ASER/) [code](https://github.com/HKUST-KnowComp/ASER)

*Hongming Zhang, Xin Liu, Haojie Pan, Yangqiu Song, Cane Wing-Ki Leung*

**Commonsense Properties from Query Logs and Question Answering Forums** (quasimodo) CIKM 2019 [paper](https://arxiv.org/pdf/1905.10989.pdf) [homepage](https://www.mpi-inf.mpg.de/departments/databases-and-information-systems/research/yago-naga/commonsense/quasimodo/) [code](https://github.com/Aunsiels/CSK)

*Julien Romero, Simon Razniewski, Koninika Pal, Jeff Z. Pan, Archit Sakhadeo, Gerhard Weikum*

**TransOMCS: From Linguistic Graphs to Commonsense Knowledge**  IJCAI 2020 [paper](https://arxiv.org/pdf/2005.00206) [homepage](https://hkust-knowcomp.github.io/ASER/) [code](https://github.com/HKUST-KnowComp/TransOMCS)

*Hongming Zhang, Daniel Khashabi, Yangqiu Song, Dan Roth*

**Paragraph-Level Commonsense Transformers with Recurrent Memory** (PARA-COMeT) arxiv 2020 [paper](https://arxiv.org/pdf/2010.01486)

*Saadia Gabriel, Chandra Bhagavatula, Vered Shwartz, Ronan Le Bras, Maxwell Forbes, Yejin Choi*

**COMET-ATOMIC 2020: On Symbolic and Neural Commonsense Knowledge Graphs** arxiv 2020 [paper](https://arxiv.org/pdf/2010.05953.pdf)

*Jena D. Hwang, Chandra Bhagavatula, Ronan Le Bras, Jeff Da, Keisuke Sakaguchi, Antoine Bosselut, Yejin Choi*

**CommonGen: A Constrained Text Generation Challenge for Generative Commonsense Reasoning** EMNLP 2020 Findings [paper](https://arxiv.org/pdf/1911.03705) [homepage](https://inklab.usc.edu/CommonGen/index.html)

*Bill Yuchen Lin, Wangchunshu Zhou, Ming Shen, Pei Zhou, Chandra Bhagavatula, Yejin Choi, Xiang Ren*

### Related Knowledge Bases
<br/>

**WordNet: A Lexical Database for English** Communications of the ACM Vol. 38, No. 11: 39-41. 1995. [homepage] (https://wordnet.princeton.edu/)

*George A. Miller*

**Toward an Architecture for Never-Ending Language Learning** (NELL). AAAI 2010 [paper](http://rtw.ml.cmu.edu/papers/carlson-aaai10.pdf) [homepage](http://rtw.ml.cmu.edu/rtw/) 

*Andrew Carlson, Justin Betteridge, Bryan Kisiel, Burr Settles, Estevam R. Hruschka Jr., and Tom M. Mitchell*

**DBpedia – A Large-scale, Multilingual Knowledge Base Extracted from Wikipedia**. Semantic Web 1 (2012) [paper](http://svn.aksw.org/papers/2013/SWJ_DBpedia/public.pdf) [homepage](https://wiki.dbpedia.org/)

*Jens Lehmann, Robert Isele, Max Jakob, Anja Jentzsch, Dimitris Kontokostas, Pablo N. Mendes, Sebastian Hellmann, Mohamed Morsey, Patrick van Kleef, Sören Auer, Christian Bizer*

### Datasets and Benchmarks
<br/>

**CommonSenseqa: A question answering challenge targeting commonsense knowledge** NAACL 2019 [paper](https://arxiv.org/abs/1811.00937) [homepage](https://www.tau-nlp.org/commonsenseqa) [code](https://github.com/jonathanherzig/commonsenseqa)

*Alon Talmor, Jonathan Herzig, Nicholas Lourie, Jonathan Berant*

**From Recognition to Cognition: Visual Commonsense Reasoning** CVPR 2019 [paper](http://openaccess.thecvf.com/content_CVPR_2019/papers/Zellers_From_Recognition_to_Cognition_Visual_Commonsense_Reasoning_CVPR_2019_paper.pdf) [code](https://github.com/rowanz/r2c/) [homepage](http://visualcommonsense.com/)

*Rowan Zellers, Yonatan Bisk, Ali Farhadi, Yejin Choi*

**oLMpics -- On what Language Model Pre-training Captures** arxiv 2019 [paper](https://arxiv.org/pdf/1912.13283.pdf) [code](https://github.com/alontalmor/oLMpics) [homepage](https://github.com/alontalmor/oLMpics)

*Alon Talmor, Yanai Elazar, Yoav Goldberg, Jonathan Berant*

**ABDUCTIVE COMMONSENSE REASONING** (ART) ICLR 2020 [paper](https://arxiv.org/pdf/1908.05739) [homepage](http://abductivecommonsense.xyz/)

*Chandra Bhagavatula, Ronan Le Bras, Chaitanya Malaviya, Keisuke Sakaguchi, Ari Holtzman, Hannah Rashkin, Doug Downey, Scott Wen-tau Yih, Yejin Choi*

**PIQA: Reasoning about Physical Commonsense in Natural Language** AAAI 2020 [paper](https://arxiv.org/pdf/1911.11641.pdf) [homepage](https://yonatanbisk.com/piqa/)

*Yonatan Bisk, Rowan Zellers, Ronan Le Bras, Jianfeng Gao, Yejin Choi*

**Reasoning about Goals, Steps, and Temporal Ordering with WikiHow** EMNLP 2020 [paper](https://arxiv.org/pdf/2009.07690) [code](https://github.com/zharry29/wikihow-goal-step)

*Qing Lyu, Li Zhang, Chris Callison-Burch*

**Birds have four legs?! NumerSense: Probing Numerical Commonsense Knowledge of Pre-trained Language Models** EMNLP 2020 [paper](https://arxiv.org/pdf/2005.00683.pdf) [homepage](https://inklab.usc.edu/NumerSense/)

*Bill Yuchen Lin, Seyeon Lee, Rahul Khanna and Xiang Ren*

[back to table of contents](#toc)

### Evaluation and Probing

**Joint Reasoning for Multi-Faceted Commonsense Knowledge** AKBC 2020 [paper](https://arxiv.org/pdf/2001.04170.pdf) [homepage](https://dice.mpi-inf.mpg.de/)

*Yohan Chalier, Simon Razniewski, Gerhard Weikum*

**Does BERT Solve Commonsense Task via Commonsense Knowledge?** arxiv 2020 [paper](https://arxiv.org/pdf/2008.03945)

*Leyang Cui, Sijie Cheng, Yu Wu, Yue Zhang*

[back to table of contents](#toc)

## Knowledge Mining (Knowledge Base Completion)

**Automatic Extraction of Commonsense LocatedNear Knowledge** ACL 2018 [paper](https://arxiv.org/pdf/1711.04204) [code](https://github.com/adapt-sjtu/commonsense-locatednear)

*Frank F. Xu, Bill Yuchen Lin, Kenny Q. Zhu*

**Commonsense Knowledge Mining from Pretrained Models** EMNLP 2019 [paper](https://www.aclweb.org/anthology/D19-1109.pdf)

*Joe Davison, Joshua Feldman, Alexander Rush*

**Language Models as Knowledge Bases?** EMNLP 2019 [paper](https://arxiv.org/pdf/1909.01066.pdf) [code](https://github.com/facebookresearch/LAMA)

*Fabio Petroni, Tim Rocktäschel, Patrick Lewis, Anton Bakhtin, Yuxiang Wu, Alexander H. Miller, Sebastian Riedel*

**Commonsense Knowledge Base Completion with Structural and Semantic Context** AAAI 2020 [paper](https://arxiv.org/pdf/1910.02915) [code](https://github.com/allenai/commonsense-kg-completion)

*Chaitanya Malaviya, Chandra Bhagavatula, Antoine Bosselut, Yejin Choi*

**Temporal Common Sense Acquisition with Minimal Supervision** ACL 2020 [paper](https://arxiv.org/pdf/2005.04304.pdf)

*Ben Zhou, Qiang Ning, Daniel Khashabi, Dan Roth*

[back to table of contents](#toc)

## Applications

### natural language inference (NLI) and commonsense reasoning (CSR)
<br/>

**Neural natural language inference models enhanced with external knowledge** ACL 2018 [paper](https://arxiv.org/abs/1711.04289) [code](https://github.com/lukecq1231/kim)
- resource: WordNet

*Qian Chen, Xiaodan Zhu, Zhen-Hua Ling, Diana Inkpen, Si Wei*

**Contrastive Self-Supervised Learning for Commonsense Reasoning** ACL 2020 [paper](https://arxiv.org/pdf/2005.00669.pdf) [code](https://github.com/SAP-samples/acl2020-commonsense/)

*Tassilo Klein, Moin Nabi*

**Do Language Embeddings Capture Scales?** EMNLP Findings 2020 [paper](https://arxiv.org/pdf/2010.05345) [code](https://github.com/google-research-datasets/numbert)

*Xikun Zhang, Deepak Ramachandran, Ian Tenney, Yanai Elazar, Dan Roth*

**Differentiable Open-Ended Commonsense Reasoning** arxiv 2020 [paper](https://arxiv.org/pdf/2010.14439)

*Bill Yuchen Lin, Haitian Sun, Bhuwan Dhingra, Manzil Zaheer, Xiang Ren, William W. Cohen*

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


**Language Generation with Multi-Hop Reasoning on Commonsense Knowledge Graph** EMNLP 2020 [paper](https://arxiv.org/pdf/2009.11692.pdf)
- resource: ConceptNet

*Haozhe Ji, Pei Ke, Shaohan Huang, Furu Wei, Xiaoyan Zhu, Minlie Huang*

### Question Answering (QA)
<br/>

**Dynamic Knowledge Graph Construction for Zero-shot Commonsense Question Answering** arxiv 2019 [paper](https://arxiv.org/pdf/1911.03876)
- resource: COMET

*Antoine Bosselut, Yejin Choi*

**Adversarial Training for Commonsense Inference** ACL2020 RepL4NLP workshop [paper](https://arxiv.org/pdf/2005.08156)

*Lis Pereira, Xiaodong Liu, Fei Cheng, Masayuki Asahara, Ichiro Kobayashi*

**Unsupervised Commonsense Question Answering with Self-Talk** EMNLP 2020 [paper](https://arxiv.org/pdf/2004.05483) [code](https://github.com/vered1986/self_talk)
- resource: ConceptNet, COMET, Google N-grams

*Vered Shwartz, Peter West, Ronan Le Bras, Chandra Bhagavatula, Yejin Choi*

**Scalable Multi-Hop Relational Reasoning for Knowledge-Aware Question Answering** EMNLP 2020 [paper](https://arxiv.org/pdf/2005.00646) [code](https://github.com/INK-USC/MHGRN)

*Yanlin Feng, Xinyue Chen, Bill Yuchen Lin, Peifeng Wang, Jun Yan, Xiang Ren*

[back to table of contents](#toc)
