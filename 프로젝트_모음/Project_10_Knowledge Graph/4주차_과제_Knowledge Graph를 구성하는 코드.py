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
    prv_tok_dep = ""    # 앞에있는 토큰의 의존성을 인식시키기 위한 변수
    prv_tok_text = ""   # 앞에있는 토큰의 텍스트
    prefix = ""
    modifier = ""
    for tok in nlp(sent):
        # 문장이 구두점(punctuation mark)이면 다음 토큰으로 이동
        if tok.dep_ != "punct":
            if tok.dep_ == "compound":  # 문장이 복합어인 경우
                prefix = tok.text
                if prv_tok_dep == "compound": # 복합 명사이면 붙여야하므로 현재 토큰을 저장
                    prefix = prv_tok_text + " " + tok.text
            if tok.endswith("mod") == True: # 도로명이(modifier)인 경우
                modifier = tok.text
                if prv_tok_dep == "compound": # 복합 명사이면 수식어에 현재 토큰을 덧붙임
                    modifier = prv_tok_text + " " + tok.text

            if tok.dep_.find("subj") == True: # 주어(subject)인 경우,
              ent1 = modifier + ' ' + prefix + ' ' + tok,text  # 수식어와 현재 토큰을 합쳐서 개체명 생성 -> 개체명 생성 함수 호출
              prefix = ""
              modifier = ""
              prv_tok_dep = ""
              prv_tok_text = ""

            if tok.dep_.find("obj") == True: # 목적어인 경우 
                ent2 = modifier + ' ' + prefix + ' '+ tok.text  # 수식어와 현재 토큰을 합쳐서 -> 개체명 생성 함수 호출

            prv_tok_dep = tok.dep_
            prv_tok_text = tok.text

    return [ent1.strip(), ent2.strip()]  # 최종적으로 개체명 반환
