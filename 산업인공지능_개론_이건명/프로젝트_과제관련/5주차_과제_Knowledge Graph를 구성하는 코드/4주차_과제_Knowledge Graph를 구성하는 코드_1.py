import re
import pandas as pd
import bs4
import requests
import spacy
from spacy import displacy
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher
from spacy.tokens import Span

import networkx as nx

import matplotlib.pyplot as plt
from tqdm import tqdm

pd.set_option('display.max_colwidth', 200)
# %matplotlib inline

# wikipedia 문장 데이터: https://github.com/phgunawan/Latihan-ML/blob/master/wiki_sentences_v2.csv
candidate_sentences = pd.read_csv("wiki_sentences_v2.csv")
candidate_sentences.shape

def get_entities(sent):
    ent1 = ""
    ent2 = ""
    prv_tok_dep = ""    # 이전 토큰의 의존성 레이블을 저장할 변수 선언
    prv_tok_text = ""   # 이전 토큰의 텍스트를 저장할 변수 선언
    prefix = ""
    modifier = ""
    for tok in nlp(sent):
        
        if tok.dep_ != "punct":
            if tok.dep_ == "compound":
                prefix = tok.text
                if prv_tok_dep == "compound":
                    prefix = prv_tok_text + " "+ tok.text
            if tok.dep_.endswith("mod") == True:
                modifier = tok.text
                if prv_tok_dep == "compound":
                    modifier = prv_tok_text + " "+ tok.text
                    
            if tok.dep_.find("subj") == True:
                ent1 = modifier +" "+ prefix + " "+ tok.text
                prefix = ""
                modifier = ""
                prv_tok_dep = ""
                prv_tok_text = ""
            if tok.dep_.find("obj") == True:
                ent2 = modifier +" "+ prefix +" "+ tok.text

        prv_tok_dep = tok.dep_
        prv_tok_text = tok.text

    return [ent1.strip(), ent2.strip()]

entity_pairs = []

for i in tqdm(candidate_sentences["sentence"]):
    entity_pairs.append(get_entities(i))

entity_pairs[10:20]

def get_relation(sent):
    doc = nlp(sent)
    matcher = Matcher(nlp.vocab)

    # 패턴 정의
    pattern = [{'DEP':'ROOT'},
               {'DEP':'prep','OP':"?"},
               {'DEP':'agent','OP':"?"}, 
               {'POS':'ADJ','OP':"?"}]

    matcher.add("matching_1", None, pattern)
    
    matches = matcher(doc)
    print('matches :', matches)
    k = len(matches) - 1

    span = doc[matches[k][1]:matches[k][2]]
    
    return(span.text)

get_relation("John completed the task")

relations = [get_relation(i) for i in tqdm(candidate_sentences['sentence'])]

source = [i[0] for i in entity_pairs]
target = [i[1] for i in entity_pairs]
kg_df = pd.DataFrame({'source': source, 'target': target, 'edge': relations})
G = nx.from_pandas_edgelist(kg_df, "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())
plt.figure(figsize=(12,12))
pos = nx.spring_layout(G)
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos=pos)
plt.show()

G=nx.from_pandas_edgelist(kg_df[kg_df['edge']=="written by"], "source", "target", 
                          edge_attr=True, create_using=nx.MultiDiGraph())

plt.figure(figsize=(12,12))

pos = nx.spring_layout(G, k = 0.5)

nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos = pos)

nx.draw_networkx_edge_labels(G, pos, edge_labels="written by")

plt.show()

G=nx.from_pandas_edgelist(kg_df[kg_df['edge']=="composed by"], "source", "target", 
                          edge_attr=True, create_using=nx.MultiDiGraph())

plt.figure(figsize=(12,12))

pos = nx.spring_layout(G, k = 0.5) # k regulates the distance between nodes

nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos = pos)

plt.show()

