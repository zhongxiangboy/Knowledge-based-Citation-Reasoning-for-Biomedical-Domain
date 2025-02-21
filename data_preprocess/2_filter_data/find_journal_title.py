import pandas as pd

count_n = 0
dictionary = {}
reader = pd.read_csv('../match/paper.csv', encoding='utf-8', sep='\t', chunksize=10000000, usecols=[11, 14, 18, 24, 25])
for chunk in reader:
    print('number of processed data:', count_n*100000)
    count_n += 1
    for i in range(len(chunk)):
        cited_pmid = int(chunk.iloc[i][1])
        journal_title = chunk.iloc[i][0]
        if cited_pmid!=0:
            dictionary[cited_pmid] = journal_title
print("paper in dicitonary: " + str(len(dictionary)))

cancer = {}
cancer_paper = pd.read_csv('../match/paper_cancer.csv', names=["jt", "pmcid"])
for i_cancer in range(len(cancer_paper)):
    pmc_id = cancer_paper.iloc[i_cancer][1]
    caner_paper_title = cancer_paper.iloc[i_cancer][0]
    cancer[int(pmc_id)] = caner_paper_title

with open('./final_corpus.txt', 'r', encoding='utf-8') as fr, open('./courpus_with_jt.txt', 'w', encoding='utf-8') as fw:
    lines = fr.readlines()
    for line in lines:
        citing_pmcid, citing_title, citing_abstract, citing_keywords, citation_sentence, cited_pmid, cited_title, cited_abstract, cited_keywords = line.strip().split('\t')
        citing_jt = cancer[int(citing_pmcid)]
        if int(cited_pmid) in dictionary:
            cited_jt = dictionary[int(cited_pmid)]
            fw.write(str(citing_pmcid) + '\t' + citing_title + '\t' + citing_abstract + '\t' + citing_keywords + '\t' + str(citing_jt) + '\t' + citation_sentence + '\t' + str(cited_pmid) + '\t' + cited_title + '\t' + cited_abstract + '\t' + cited_keywords + '\t' + str(cited_jt) + '\n')
