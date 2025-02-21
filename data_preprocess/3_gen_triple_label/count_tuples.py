import time,random 
import pandas as pd
import json
import re
from tqdm import tqdm
from flashtext import KeywordProcessor
import time
import csv
from queue import Queue
from threading import Lock, Thread

import sys

#先进先出队列

    
import threading


def get_tuples():
    tuples = []
    head_tuples = []
    tail_tuples = []
    # with open('./matched_triple.csv', encoding='utf-8') as f:
    with open('./sldb_complete_triple.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in tqdm(reader):
            head = row[0]
            relation = row[1]
            tail = row[2]
            tuples.append([head, relation, tail])
            head_tuples.append(head)
            tail_tuples.append(tail)
    return tuples, head_tuples, tail_tuples

if __name__ == '__main__':
    tuples, head_tuples, tail_tuples = get_tuples()
    # context_information = context_information[:]
    # context_information = " the cancer stem cell evidence for its origin as an injured autoreactive t cell	this review explores similarities between lymphocytes and cancer cells, and proposes a new model for the genesis of human cancer. we suggest that the development of cancer requires infection(s) during which antigenic determinants from pathogens mimicking self-antigens are co-presented to the immune system, leading to breaking t cell tolerance. some level of autoimmunity is normal and necessary for effective pathogen eradication. however, autoreactive t cells must be eliminated by apoptosis when the immune response is terminated. apoptosis can be deficient in the event of a weakened immune system, the causes of which are multifactorial. some autoreactive t cells suffer genomic damage in this process, but manage to survive. the resulting cancer stem cell still retains some functions of an inflammatory t cell, so it seeks out sites of inflammation inside the body. due to its defective constitutive production of inflammatory cytokines and other growth factors, a stroma is built at the site of inflammation similar to the temporary stroma built during wound healing. the cancer cells grow inside this stroma, forming a tumor that provides their vascular supply and protects them from cellular immune response.as cancer stem cells have plasticity comparable to normal stem cells, interactions with surrounding normal tissues cause them to give rise to all the various types of cancers, resembling differentiated tissue types. metastases form at an advanced stage of the disease, with the proliferation of sites of inflammation inside the body following a similar mechanism. immunosuppressive cancer therapies inadvertently re-invigorate pathogenic microorganisms and parasitic infections common to cancer, leading to a vicious circle of infection, autoimmunity and malignancy that ultimately dooms cancer patients. based on this new understanding, we recommend a systemic approach to the development of cancer therapies that supports rather than antagonizes the immune system.	hnk 1 antibody detects an antigen expressed on neuroectodermal cells	the hnk-1 antibody known to define a subpopulation of human lymphocytes with natural killer and killer cell activities was shown to detect a common neuroectodermal antigen. most tumor lines and paraffin-embedded tumors and normal tissues of neuroectodermal origin were specifically stained by hnk-1. lines and tissues of other derivations were negative except a trophoblastic tumor line and a percentage of ewing\'s sarcomas, whose histogenesis is poorly understood. these data indicate that hnk-1 antibody could be of interest in clinical histopathology but cannot be considered as specific for a lymphocyte subset.	] and a variety of other solid tumors including astrocytoma, neuroblastoma, retinoblastoma, carcinoid tumors, etc"
    # context_information = [context_information]

    threadnums = 10

    head_tuples = list(set(head_tuples))
    tail_tuples = list(set(tail_tuples))

    htsd = {}
    for hk,r,tk in tuples:
        key = hk +"---"+tk
        htsd[key] = htsd.get(key,0) + 1
    
    counts = 0
    for k,v in htsd.items():
        if v> 1:
            counts += 1
    print(counts ,len(htsd))
