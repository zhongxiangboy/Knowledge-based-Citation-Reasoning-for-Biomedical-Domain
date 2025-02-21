from tqdm import tqdm
import re
import pandas as pd

####### using cited_pmid fing cited paper information from paper.csv

count_n = 0
dictionary = {}
reader = pd.read_csv('./paper.csv', encoding='utf-8', sep='\t', chunksize=10000000, usecols=[11, 14, 18, 24, 25])
for chunk in reader:
    print('number of processed data:', count_n*100000)
    count_n += 1
    for i in range(len(chunk)):
        cited_pmid = int(chunk.iloc[i][1])
        title = chunk.iloc[i][2]
        abstract = chunk.iloc[i][3]
        keywords = chunk.iloc[i][4]
        journal_title = chunk.iloc[i][0]
        if cited_pmid!=0:
            dictionary[cited_pmid] = {'title': title, 'abstract': abstract, 'keywords': keywords, 'jt': journal_title}
print("paper in dicitonary: " + str(len(dictionary)))

cancer = {}
cancer_paper = pd.read_csv('./paper_cancer.csv', names=["jt", "pmcid"])
for i_cancer in range(len(cancer_paper)):
    pmc_id = cancer_paper.iloc[i_cancer][1]
    caner_paper_title = cancer_paper.iloc[i_cancer][0]
    cancer[int(pmc_id)] = caner_paper_title


with open('./cancer_corpus.txt', 'r', encoding='utf-8') as f_cancer, open('./final_corpus.txt','w', encoding='utf-8') as fw:
    lines = f_cancer.readlines()
    count_c = 0
    print("number of citing record:" + str(len(lines)))
    for line in lines:
        tempt = line.strip().split('\t')
        citing_pmcid = tempt[0]
        citing_title = tempt[1]
        citing_abstract = tempt[2]
        citing_keywords = tempt[3]
        citing_jt = cancer[int(citing_pmcid)]
        citation_sentence = tempt[4]
        cited_pmid = tempt[5]
        try:
            int(cited_pmid)
            if int(cited_pmid) in dictionary:
                cited_title = dictionary[int(cited_pmid)]['title']
                cited_abstract = dictionary[int(cited_pmid)]['abstract']
                cited_keywords = dictionary[int(cited_pmid)]['keywords']
                cited_jt = dictionary[int(cited_pmid)]['jt']
                fw.write(citing_pmcid + '\t' + citing_title + '\t' + citing_abstract + '\t' + citing_keywords + '\t' + citing_jt + '\t' + citation_sentence + '\t' + str(cited_pmid) + '\t' + cited_title + '\t' + cited_abstract + '\t' + cited_keywords + '\t' + cited_jt + '\n')
            else:
                count_c+=1
        except:
            print('this line with error: ' + line)

    print("number of cited paper which can not been found in dictionary:"+ str(count_c))
