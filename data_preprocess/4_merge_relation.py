import json
import re
import random
def select_relation(list_input):
    out_put = []
    relation = ''
    level1 = ['treats', 'causes', 'palliates', 'therapeutic', 'affects cotreatment']
    level2 = ['downregulates', 'upregulates','sl', 'decreases expression', 'increases expression', 'decreases reaction', 'increases reaction', 'decreases phenotype', 'increases phenotype', 'decreases reaction', 'increases reaction']
    level3 = ['regulates']
    level4 = ['associates', 'covaries', 'expresses', 'presents', 'participates', 'includes', 'interacts', 'resembles']
    for i in list_input:
        i = i.lower()
        if "_" in i:
            i = i[:i.index('_')]
        if '^' in i:
            i = re.sub('\^', ' ', i)
        tempt = i.split('|')
        for t in tempt:
            out_put.append(t)
    out_put = list(set(out_put))

    for tempt in level1:
        if tempt in out_put:
            relation = tempt
    if relation == '':
        for tempt in level2:
            if tempt in out_put:
                relation = tempt
    if relation == '':
        for tempt in level3:
            if tempt in out_put:
                relation = tempt
    if relation == '':
        for tempt in level4:
            if tempt in out_put:
                relation = tempt

    if 'binds' in out_put:
        if relation == '':
            relation += '|binds'
        else:
            relation = 'binds'
    if 'localizes' in out_put:
        if relation == '':
            relation += '|localizes'
        else:
            relation = 'localizes'
    if relation == '':
        x = list(set(out_put))
        random.shuffle(x)
        relation = x[0]
    return relation


def write_train_json(read):

    new_data = {}

    with open(read, 'r') as f:
        read_data = json.load(f)
        n = 0
        fw_data = open('./new.json', 'w', encoding='utf-8')

        for i in range(len(read_data)):
            i = str(i)
            citing_title = read_data[i]['citing_title']
            citing_abstract = read_data[i]['citing_abstract']
            citing_k = read_data[i]['citing_keywords']
            citing_jt = read_data[i]['citing_jt']

            cited_title = read_data[i]['cited_title']
            cited_abstract = read_data[i]['cited_abstract']
            cited_k = read_data[i]['cited_keywords']
            cited_jt = read_data[i]['cited_jt']

            triples = read_data[i]['triple_label']
            citation_sentence = read_data[i]['citation_sentence']


            if len(citing_abstract) != 0 and len(cited_abstract) != 0 and len(triples) != 0:
                tempt = triples.strip().split('\t')
                relation_dict = {}
                triple_label = ''
                for t in tempt:
                    if len(t[1:-1].split(',')) == 3:
                        head, relation, tail = t[1:-1].split(',')
                        tempt_key = '(' + head + ',' + tail + ')'
                        if tempt_key not in relation_dict:
                            relation_dict[tempt_key] = relation
                        else:
                            relation_dict[tempt_key] = relation_dict[tempt_key] + ' '+ relation

                for ht in relation_dict.keys():
                    relation_list = relation_dict[ht].split(' ')
                    relation_list = list(set(relation_list))
                    print(relation_list)
                    relation = select_relation(relation_list)
                    print(relation)

                    h, t = ht[1:-1].split(',')
                    triple = '(' + h + ',' + relation + ',' + t + ')'
                    triple_label += triple + '\t'


                new_data[n] = {
                    'citing_title': citing_title,
                    'citing_abstract': citing_abstract,
                    'citing_keywords': citing_k,
                    'citing_jt': citing_jt,
                    'cited_title': cited_title,
                    'cited_abstract': cited_abstract,
                    'cited_keywords': cited_k,
                    'cited_jt': cited_jt,
                    'citation_sentence': citation_sentence,
                    'triple_label': triple_label[:-1]
                }
                n += 1

        json.dump(new_data, fw_data, indent=4)


if __name__ == '__main__':

    write_train_json('./ht_in_citation.json')