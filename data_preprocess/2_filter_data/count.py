import matplotlib.pyplot as plt
from matplotlib import pyplot

def draw_list(my_list, title, sep):
    Xlable = "length"
    Ylable = "Count"
    Xmin = min(my_list)
    Xmax = max(my_list)
    Ymin = 0
    plt.hist(my_list, sep)
    plt.xlabel(Xlable)
    plt.xlim(Xmin,Xmax)
    plt.ylabel(Ylable)
    plt.ylim(Ymin,100000)
    plt.title(title)
    plt.show()

with open('./final_corpus.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    len_citing_title = []
    len_citing_abstract = []
    len_citing_keywords = []
    len_citation_sentence = []
    len_cited_title = []
    len_cited_abstract = []
    len_cited_keywords = []
    for line in lines:
        tempt = line.strip().split('\t')
        citing_title = tempt[1]
        citing_abstract = tempt[2]
        citing_keywords = tempt[3]
        citation_sentence = tempt[4]
        cited_pmid = tempt[5]
        cited_title = tempt[6]
        cited_abstract = tempt[7]
        cited_keywords = tempt[8]
        # print(citation_sentence)

        len_citing_title.append(len(citing_title))
        len_citing_abstract.append(len(citing_abstract))

        len_citation_sentence.append(len(citation_sentence))
        len_cited_title.append(len(cited_title))
        len_cited_abstract.append(len(citing_abstract))

    draw_list(len_citing_title, 'citing_title', 20)
    draw_list(len_citing_abstract, 'citing_abstract', 100)
    draw_list(len_cited_title, 'cited_title', 20)
    draw_list(len_cited_abstract, 'cited_abstract', 100)
    draw_list(len_citation_sentence, 'citation_sentence', 20)

