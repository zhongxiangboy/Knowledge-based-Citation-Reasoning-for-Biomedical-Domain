
import time,random
from turtle import tilt 
import pandas as pd
import json
import re
from tqdm import tqdm
from flashtext import KeywordProcessor
import time
import csv

#先进先出队列

    
import threading

def write_dbs(i):
    print(i)

def extractKW(one_str, kw_list):
    '''
    关键词抽取
    '''
    keywords_found = keyword_processor.extract_keywords(one_str)
    return keywords_found

def get_context_information():
    title_information = []
    abstract_information = []
    citation_information = []
    keyword_information = []
    journal_information = []

    with open('./cancer_corpus_jt.json', 'r', encoding='utf-8') as fj:
        json_data = json.load(fj)
        

        # for key in list(json_data.keys())[:20]:
        for key in tqdm( list(json_data.keys()) ):
            pair_list = json_data[key]
            j = 0
            for pair in pair_list:

                citing_title = pair['citing_title']
                cited_title = pair['cited_title']

                citing_a = pair['citing_abstract']
                citing_abstract = re.sub('<.{1,50}>', '', citing_a)

                cited_a = pair['cited_abstract']
                cited_abstract = re.sub('<.{1,50}>', '', cited_a)

                citing_keywords = pair['citing_keywords']
                cited_keywords = pair['cited_keywords']
                
                citing_jt = pair['citing_jt']
                cited_jt = pair['cited_jt']

                citation = pair['citation_sentence']

                title = citing_title + '\t' + cited_title
                abstract = citing_abstract + '\t' + cited_abstract
                keyword = citing_keywords + '\t' + cited_keywords
                journal = citing_jt + '\t' + cited_jt

                title_information.append(title)
                abstract_information.append(abstract)
                keyword_information.append(keyword)
                citation_information.append(citation)
                journal_information.append(journal)
    return title_information, abstract_information, keyword_information, citation_information, journal_information


def get_tuples():
    tuples = []
    head_tuples = []
    tail_tuples = []

    with open('./Triple_base/Triple_chem_phenotype.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in tqdm(reader):
            head = row[0].lower()
            relation = row[1]
            tail = row[2].lower()
            tuples.append([head, relation, tail])
            head_tuples.append(head)
            tail_tuples.append(tail)

    # with open('./sldb_complete_triple.csv', encoding='utf-8') as f:
    #     reader = csv.reader(f)
    #     header = next(reader)
    #     for row in tqdm(reader):
    #         head = row[0].lower()
    #         relation = row[1]
    #         tail = row[2].lower()
    #         tuples.append([head, relation, tail])
    #         head_tuples.append(head)
    #         tail_tuples.append(tail)

    return tuples, head_tuples, tail_tuples

if __name__ == '__main__':
    tuples, head_tuples, tail_tuples = get_tuples()
    title_information, abstract_information, keyword_information, citation_information, journal_information = get_context_information()

    threadnums = 10

    head_tuples = list(set(head_tuples))
    if 'was' in head_tuples:
        head_tuples.remove('was')
    tail_tuples = list(set(tail_tuples))
    if 'was' in tail_tuples:
        tail_tuples.remove('was')

    htsd = {}
    for hk,r,tk in tuples:
        key = hk +"---"+tk
        v = "\t".join([hk,r,tk])
        htsd[key] = htsd.get(key,[])
        htsd[key].append(v)
    # htsd = {hk +"---"+tk: "\t".join([hk,r,tk]) for hk,r,tk in tuples}
    # context_information = context_information[:2000]

    print("head keyword_processor...")
    keyword_processor = KeywordProcessor(case_sensitive=False)
    keyword_processor.add_keywords_from_list(head_tuples)

    print("extract_keywords...")
    head_kws = []
    for text in tqdm(citation_information):
        hk = keyword_processor.extract_keywords(text)
        hk = list(set(hk))
        head_kws.append(hk)
    
    print("tail keyword_processor...")
    keyword_processor = KeywordProcessor(case_sensitive=False)
    keyword_processor.add_keywords_from_list(tail_tuples)

    print("extract_keywords...")
    tail_kws = []
    for text in tqdm(citation_information):
        tk = keyword_processor.extract_keywords(text)
        tk = list(set(tk))
        tail_kws.append(tk)
    
    fw = open('./citation_match_triple_chemical_disease.txt', 'w', encoding='utf-8')
    fw2 = open('./citation_no_triple_match_chemical_disease.txt', 'w', encoding='utf-8')

    for ii in range(len(citation_information)):
        hks, tks = head_kws[ii], tail_kws[ii]
        title = title_information[ii]
        abstract = abstract_information[ii]
        keyword = keyword_information[ii]
        citation = citation_information[ii]
        journal = journal_information[ii]
        allhrt = []
        # print(hks)
        for hk in hks:
            for tk in tks:
                ht = hk + "---" + tk
                if not ht in htsd:
                    continue
                allhrt += htsd[ht]
                # print(ht)
        if allhrt:
            fw.write(title + '\t' + abstract + '\t' + keyword + '\t' + citation+ '\t' + journal + "*****" + "||||".join(allhrt) + "\n")
            # break
        else:
            fw2.write(title + '\t' + abstract + '\t' + keyword + '\t' + citation + "\n")

    fw.close()
    fw2.close

    """
    for i in range(7):
        t = threading.Thread(target=write_dbs, args=(i,))
        t.start()
    
    print("allDone")
    """
