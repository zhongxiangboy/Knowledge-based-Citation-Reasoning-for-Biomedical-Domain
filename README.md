# Knowledge-based-Citation-Reasoning-for-Biomedical-Domain
This work aims to explain or help understand the citation relationship between two papers by constructing a visual knowledge graph. 

For example, if article A studies a disease X, and article B explores a drug Y, and while drug Y has a therapeutic effect on disease X, then we would like to extract a triple like (drug X, therapy, disease Y) and construct a knowledge graph, which in turn helps to explain the citation associations between article A and article B


Data used

For a pair of citing-cited papers, we would like to explain the citation relationship between them with one or more triple. To obtain annotated data satisfying the above style:
  1. We first acquired the PMC dataset (https://www.ncbi.nlm.nih.gov/pmc/tools/textmining/) containing 2.4 million publications and limited the domain to cancer, obtaining 53043 cancer-related papers.
  2. Subsequently, applying the conditions that the abstract cannot be empty and at least one reference can be found in PMC, we obtained 11,620 citing-cited paper pairs.
  3. For each pair, we extracted the citation sentences about the cited papers from the citing papers, and with the help of knowledge bases such as CTD (https://ctdbase.org/), KG4SL (https://github.com/JieZheng-ShanghaiTech/KG4SL), and COSMIC (https://cancer.sanger.ac.uk/cosmic), we derived the triple labels from the citation sentences based on a distant supervision approach.
