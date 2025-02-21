### select title : 25-200
### select abstract : 500_3000
### select citation sentence:50-

import numpy as np
import json
import matplotlib.pyplot as plt
import pandas as pd


with open('./courpus_with_jt.txt', 'r', encoding='utf-8') as f, open('./cancer_corpus_jt.json', 'w') as fw:
    lines = f.readlines()
    count_x = 0
    print(len(lines))
    corpus_dic = {}
    corpus_result = {}
    for line in lines:
        tempt = line.strip().split('\t')
        citing_pmcid = int(tempt[0])
        citing_title = tempt[1]
        citing_abstract = tempt[2]
        citing_keywords = tempt[3]
        citing_jt = tempt[4]
        citation_sentence = tempt[5]
        cited_pmid = tempt[6]
        cited_title = tempt[7]
        cited_abstract = tempt[8]
        cited_keywords = tempt[9]
        cited_jt = tempt[10]
        if len(citation_sentence) > 50:
            count_x+=1
            if citing_pmcid not in corpus_dic:
                corpus_dic[citing_pmcid] = [
                    {'citing_title': citing_title, 'citing_abstract': citing_abstract, 'citing_keywords': citing_keywords, 'citing_jt': citing_jt,
                     'citation_sentence': citation_sentence, 'cited_title': cited_title, 'cited_abstract': cited_abstract,
                     'cited_keywords': cited_keywords, 'cited_jt': cited_jt}]
            else:
                corpus_dic[citing_pmcid].append(
                    {'citing_title': citing_title, 'citing_abstract': citing_abstract, 'citing_keywords': citing_keywords, 'citing_jt': citing_jt,
                     'citation_sentence': citation_sentence, 'cited_title': cited_title, 'cited_abstract': cited_abstract,
                     'cited_keywords': cited_keywords, 'cited_jt': cited_jt})

    #     if len(citation_sentence)>50:
    #         if citing_pmcid not in corpus_dic:
    #             corpus_dic[citing_pmcid] = [{'citing_title': citing_title, 'citing_abstract': citing_abstract, 'citing_keywords': citing_keywords, 'citation_sentence': citation_sentence, 'cited_title': cited_title, 'cited_abstract': cited_abstract, 'cited_keywords': cited_keywords}]
    #         else:
    #             corpus_dic[citing_pmcid].append({'citing_title': citing_title, 'citing_abstract': citing_abstract, 'citing_keywords': citing_keywords, 'citation_sentence': citation_sentence, 'cited_title': cited_title, 'cited_abstract': cited_abstract, 'cited_keywords': cited_keywords})


    # for i in corpus_dic.keys():
    #     if len(corpus_dic[i]) >=5:
    #         corpus_result[i] = corpus_dic[i]
    # json.dump(corpus_result, fw)

    json.dump(corpus_dic, fw)
    print(count_x)