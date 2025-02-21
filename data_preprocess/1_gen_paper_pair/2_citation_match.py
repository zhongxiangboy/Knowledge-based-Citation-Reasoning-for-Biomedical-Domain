from tqdm import tqdm
import re
import pandas as pd

########### use citation_sentence id finging citation sentence string from sentence.csv

count_n=0
dictionary = {}

lines = open('./cancer_citation.txt', 'r', encoding='utf-8').readlines()
print(len(lines))
for line in lines:
    tempt = line.strip().split('\t')
    pmcid= tempt[0]
    title = tempt[1]
    abstract = tempt[2]
    keywords = tempt[3]
    citation = int(tempt[4])
    citedpmid = tempt[5]
    if citation != 0:
        dictionary[citation] = ''


reader = pd.read_csv('./sentence.csv', encoding='utf-8', sep='\t', chunksize=10000000, usecols=[0, 9])
for chunk in reader:
    print('number of processed data:', count_n*100000)
    count_n += 1
    for i in range(len(chunk)):
        sentence_id = int(chunk.iloc[i][0])
        sentence = chunk.iloc[i][1]
        if sentence_id in dictionary:
            dictionary[sentence_id] = sentence


fw = open('./cancer_corpus.txt', 'w', encoding='utf-8')
for line in lines:
    tempt = line.strip().split('\t')
    pmcid= tempt[0]
    title = tempt[1]
    abstract = tempt[2]
    keywords = tempt[3]
    citation = int(tempt[4])
    citedpmid = tempt[5]
    citation_sentence = dictionary[citation]
    fw.write(pmcid + '\t' + title + '\t' + abstract + '\t' + keywords + '\t' + citation_sentence + '\t' + citedpmid +'\n')
