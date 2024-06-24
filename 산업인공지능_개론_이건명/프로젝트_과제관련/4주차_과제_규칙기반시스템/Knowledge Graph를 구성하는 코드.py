import re
import pandas as pd
from bs4 import BeautifulSoup
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

# Wikipedia 문서 파일 경로: https://github.com/dipanjanS/practical-machine-learning-with-python/blob/master/notebooks/Ch08_Analyzing_Movie_Content/wiki_sentences_v2.csv
candidate_sentences = pd.read_csv("wiki_sentences_v2.csv")
candidate_sentences.shape

def get_entities(sent):
    ent1 = ""
    ent2 = ""
    prv_tok_dep = ""  # 직전 토큰의 의존 파싱 태그
    prv_tok_text = ""  # 직전 토큰
    prefix = ""
    modifier = ""

    for tok in nlp(sent):
        if tok.dep_ != "punct":
            if tok.dep_ == "compound":
                prefix = tok.text
                if prv_tok_dep == "compound":
                    prefix = prv_tok_text + " " + tok.text
            if tok.dep_.endswith("mod"):
                modifier = tok.text
            if prv_tok_dep == "compound":
                modifier = prv_tok_text + " " + tok.text

            if tok.dep_.find("subj") == 0:
                ent1 = modifier + " " + prefix + " " + tok.text
                prefix = ""
                modifier = ""
            if tok.dep_.find("obj") == 0:
                ent2 = modifier + " " + prefix + " " + tok.text
        prv_tok_dep = tok.dep_
        prv_tok_text = tok.text

    return [ent1.strip(), ent2.strip()]


entity_pairs = []

for sentence in tqdm(candidate_sentences['sentence']):
    entity_pairs.append(get_entities(sentence))



def get_relations(sent):
    doc = nlp(sent)
    matcher = Matcher(nlp.vocab)

    # 패턴 정의
    pattern = [
        {'DEP': 'ROOT'},
        {'DEP': 'prep', 'OP': '?'},
        {'DEP': 'agent', 'OP': '?'},
        {'POS': 'ADJ', 'OP': '*'}
    ]

    matcher.add("matching_1", None, pattern)

    matches = matcher(doc)
    print('matches:', matches)
    
    k = len(matches) - 1
    
    span = doc[matches[k][1]:matches[k][2]]
    
    return span.text

# 주어 (subject) 추출
source = [i[0] for i in entity_pairs]

# 목적어 (object) 추출
target = [i[1] for i in entity_pairs]

# 방향 그래프 생성
G = nx.from_pandas_edgelist(kg_df, 'source', 'target', 
                            edge_attr=True, create_using=nx.MultiDiGraph())

# 그래프 그리기
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G)  # 레이아웃 설정
nx.draw(G, with_labels=True, node_color='skyblue', edge_cmap=plt.cm.Blues, pos=pos)
plt.show()


# 데이터프레임 생성
kg_df = pd.DataFrame({'source': source, 'target': target, 'edge': relations})


# 그래프 생성
G = nx.Graph()

# 노드 추가
G.add_node("source")
G.add_node("target")

# 엣지 추가
G.add_edge("source", "target", edgetype="written by")

# 그래프 그리기
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.5)
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_color=plt.cm.Blues, pos=pos)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d["edgetype"] for u, v, d in G.edges(data=True)})
plt.show()

# Pandas 데이터프레임에서 엣지 리스트를 가져와서 그래프 생성
G = nx.from_pandas_edgelist(kg_df[kg_df['edge'] == "composed by"], "source", "target", edge_attr=True, create_using=nx.MultiDiGraph())

# 그래프를 시각화하기 위한 설정
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.5)  # k regulates the distance between nodes
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos=pos)
plt.show()






