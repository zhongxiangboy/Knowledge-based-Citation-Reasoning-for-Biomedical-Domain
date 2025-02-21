    
from os import openpty, write
from typing import Mapping
from flashtext import KeywordProcessor
import re
import random
def extractKW(one_str, kw_list):
    '''
    关键词抽取
    '''
    keyword_processor = KeywordProcessor()
    for one_kw in kw_list:
        keyword_processor.add_keyword(one_kw)
    keywords_found = keyword_processor.extract_keywords(one_str)
    return keywords_found

# with open('./kg4sl_paper_info_match_allkws.txt', encoding='utf-8') as f:

def check_and_write(input, output):
    with open(input, 'r', encoding='utf-8') as f, open(output, 'a', encoding='utf-8') as fw:
        lines= f.readlines()
        k=0
        for line in list(set(lines[:])):
            line = line.strip()
            context,hrts = line.split("*****")
            write_str = ''
            for hrt in hrts.split("||||"):
                h,r,t = hrt.split("\t")
                if len(set(extractKW(one_str=context, kw_list=[h,t]))) ==2:
                    write_str += h + '\t' + r + '\t' + t + '||||'
            if len(write_str) != 0:
                k += 1
                fw.write(context.strip()+ "*****" + write_str[:-4] + '\n')
        print("data remained: ", k)

if __name__=='__main__':
    check_and_write('./citation_match_triple.txt', './citation_matched_triple.txt')
            