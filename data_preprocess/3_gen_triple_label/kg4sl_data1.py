import pandas as pd
import json
import re
from tqdm import tqdm
from flashtext import KeywordProcessor
import time
from pandas.core.frame import DataFrame

def extractKW(one_str, kw_list):
    '''
    关键词抽取
    '''
    keyword_processor = KeywordProcessor()
    for one_kw in kw_list:
        keyword_processor.add_keyword(one_kw)
    keywords_found = keyword_processor.extract_keywords(one_str)
    return keywords_found

context_information = []
strings = ''
head_list = []
tail_list = []
with open('./cancer_corpus.json', 'r', encoding='utf-8') as fj, open('./kg4sl_paper_info_match.txt', 'a', encoding='utf-8') as fw:
    json_data = json.load(fj)
    file = pd.read_csv('./matched_triple.csv', encoding="utf-8")

    for key in json_data.keys():
        pair_list = json_data[key]
        j = 0
        for pair in pair_list:

            citing_title = pair['citing_title']
            cited_title = pair['cited_title']

            citing_a = pair['citing_abstract']
            citing_abstract = re.sub('<.{1,50}>', '', citing_a)

            cited_a = pair['cited_abstract']
            cited_abstract = re.sub('<.{1,50}>', '', cited_a)

            citation = pair['citation_sentence']

            context = citing_title + '\t' + citing_abstract + '\t' + cited_title + '\t' + cited_abstract + '\t' + citation

            context_information.append(context)

            if j == 0:
                strings += citing_title + ' '
                strings += citing_abstract + ' '
            strings += cited_title + ' '
            strings += cited_abstract + ' '
            strings += citation + ' '
            j += 1



    for i in tqdm(range(1, len(file))):
        head = file.iloc[i][0]
        relation = file.iloc[i][1]
        tail = file.iloc[i][2]
        head_list.append(head)
        tail_list.append(tail)
        # kwlist.append(tail)
    # print(len(set(head_list))) ###14468
    # print(len(set(tail_list))) ###39586

    start_time = time.time()
    head_result = list(set(extractKW(strings, list(set(head_list)))))
    end_time = time.time()
    print("head时: {:.2f}秒".format(end_time - start_time))
    print('number of matched head:', len(head_result))

    start_time = time.time()
    tail_result = list(set(extractKW(strings, list(set(tail_list)))))
    end_time = time.time()
    print("head时: {:.2f}秒".format(end_time - start_time))
    print('number of matched tail:', len(tail_result))

    heads = DataFrame({'head_name': head_result})
    tails = DataFrame({'tail_name': tail_result})
    temp_result = pd.merge(heads, file, how='inner', on=['head_name'])
    merge_result = pd.merge(tails, temp_result, how='inner', on=['tail_name'])
    print('number of occurred tripple', len(merge_result))
    print('number of corpus', len(context_information))
    # merge_result.to_csv('matched_triple.csv')
    # triple_file = pd.read_csv('./matched_triple.csv', encoding='utf-8')

    for n in tqdm(range(len(merge_result))):
        head_h = merge_result['head_name'][n]
        relation_r = merge_result['edge_type'][n]
        tail_t = merge_result['tail_name'][n]
        kwlist = [head_h, tail_t]

        for context in context_information:
            citing_title, citing_abstract, cited_title, cited_abstract, citation = context.split('\t')

            paper_information = citing_title + ' ' + citing_abstract + ' ' + cited_title + ' ' + cited_abstract

            # result = extractKW(paper_information, kwlist)
            # if len(set(result)) == 2:
            #     fw.write(context + '\t' + head_h + '\t' + relation_r + '\t' + tail_t + '\n')

            # if head_h in paper_information.split(' ') and tail_t in paper_information.split(' '):
            #         fw.write(context + '\t' + head_h + '\t' + relation_r + '\t' + tail_t + '\n')

            if head_h in citation and tail_t in citation:
                fw.write(context + '\t' + head_h + '\t' + relation_r + '\t' + tail_t + '\n')