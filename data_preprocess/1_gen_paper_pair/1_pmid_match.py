from tqdm import tqdm
import re
import pandas as pd

######## building dictionary = {citing_pmcid: {cited_pmid: citation_sentence}} from paper_cation.csv
######## getting paper pmc_id from paper_cancer.txt
######## using pmc_id fing citing-cited pair from dictionary

count_n=0
dictionary = {}
reader = pd.read_csv('./paper_citation.csv', encoding='utf-8', sep='\t', chunksize=10000000, usecols=[2,4,7])
for chunk in reader:
    print('number of processed data:', count_n*100000)
    count_n += 1
    for i in range(len(chunk)):
        citing_pmcid = int(chunk.iloc[i][0])
        citation_sentence = chunk.iloc[i][1]
        cited_pmid = int(chunk.iloc[i][2])
        if cited_pmid!=0:
            if citing_pmcid not in dictionary:
                dictionary[citing_pmcid] = {cited_pmid: citation_sentence}
            else:
                dictionary[citing_pmcid].update({cited_pmid: citation_sentence})

with open('./paper_cancer.txt', 'r', encoding='utf-8') as f_cancer, open('./cancer_citation.txt','w', encoding='utf-8') as fw:
    lines = f_cancer.readlines()
    for line in lines:
        tempt = line.strip().split('\t')
        pmcid = int(re.sub('"', '', tempt[0]))
        title = re.sub('"', '', tempt[1])
        abstract = re.sub('"', '', tempt[2])
        keywords = re.sub('"', '', tempt[3])
        if pmcid in dictionary:
            for citedpmid in dictionary[pmcid].keys():
                citation = str(dictionary[pmcid][citedpmid])
                fw.write(str(pmcid) + '\t' + title + '\t' + abstract + '\t' + keywords + '\t' + citation + '\t' + str(citedpmid) +'\n')

