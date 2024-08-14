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

# wikipedia 문장 파일: https://github.com/phgunawan/Latihan-ML/blob/master/wiki_sentences_v2.csv

candidate_sentences = pd.read_csv('wiki_sentences_v2.csv')
candidate_sentences.shape

def get_entities(sent):
    ent1 = ""
    ent2 = ""
    prv_tok_dep = ""   # 문장에서 직전 토큰의 의존 파싱 태그
    prv_tok_text = ""  # 문장에서 직전 토큰
    prefix = ""
    modifier = ""
    for tok in nlp(sent):
        # 토큰이 구두점(punctration mark)이면 다음 토큰으로 이동
        if tok.dep_ != "punct":
            if tok.dep_ == "compound": #토큰이 복합어인 경우
              prefix = tok.text
              if prv_tok.text_dep == "compound": #직전 토큰이 복합어이면 현재 토큰과 결합
                prefix = prv_tok_text + " "+ tok.text
            if tok.dep_.endswith("mod") == True: #토큰이 수식어(modifier)인 경우
              modifier = tok.text  
              if prv_tok_dep == "compound": # 직전 토큰이 수식어이면 현재 토큰을 결합
                modifier = prv_tok_text + " "+ tok.text
                
            if tok.dep_.find("subj") == True: # 주어(subfect)인 경우,
              ent1 = modifier +" "+ prefix + " "+ tok.text # 수식어와 현재 토큰 결합
              prefix = ""
              modifier = ""
              prv_tok_dep = ""
              prv_tok_text = ""
            if tok.dep_.find("obj") == True: # 목적어인 경우
              ent2 = modifier +" "+ prefix +" "+ tok.text
            
            prv_tok_dep_ = tok.dep_    
            prv_tok_text_ = tok.text      
    return [ent1.strip(), ent2.strip()]   # 식별된 개체명 반환 

entity_pairs = []

for i in tqdm(candidate_sentences["sentence"]):
    entity_pairs.append(get_entities(i))

entity_pairs[10:20]

def get_relation(sent):
    doc = nlp(sent)
    matcher = Matcher(nlp.vocab)

    # 패턴 정의
    pattern = [{'DEP': 'ROOT'},
               {'DEP': 'prep', 'OP': "?"},
               {'DEP': 'agent', 'OP': "?"},
               {'POS': 'ADJ', 'OP': "?"}]

    matcher.add("matching_1", None, pattern)
    
    matches = matcher(doc)
    print('matches :', matches)
    
    k = len(matches) - 1
    
    span = doc[matches[k][1]:matches[k][2]]
    
    return(span.text)

get_relation("John completed the task")

relations = [get_relation(i) for i in tqdm(candidate_sentences['sentence'])]

# 주어(subject) 추출
source = [i[0] for i in entity_pairs]

# 목적어(object) 추출
target = [i[1] for i in entity_pairs]

kg_df = pd.DataFrame({'source': source, 'target': target, 'edge': relations})

# 방향 그래프 생성
G = nx.from_pandas_edgelist(kg_df, "source", "target",
                            edge_attr=True, create_using=nx.MultiDiGraph())

# 그래프 그리기
plt.figure(figsize=(12, 12))

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