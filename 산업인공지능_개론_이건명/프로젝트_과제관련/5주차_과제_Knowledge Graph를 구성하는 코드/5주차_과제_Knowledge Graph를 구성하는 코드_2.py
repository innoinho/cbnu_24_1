import pandas as pd
import spacy
import networkx as nx
import matplotlib.pyplot as plt
import random

# 영어 자연어 처리 모델 로드
nlp = spacy.load("en_core_web_sm")

# 데이터셋 로드
df = pd.read_csv('wiki_sentences_v2.csv')

# 랜덤으로 선택할 단어의 수
num_words_to_select = 5

# 데이터셋에서 랜덤으로 단어 선택
random_words = random.sample(df['sentence'].str.split().sum(), num_words_to_select)

# 그래프 생성
G = nx.Graph()

# 선택된 단어들 간의 관계 추출 및 그래프에 추가
for word in random_words:
    # 단어가 포함된 문장 선택
    sentence = df[df['sentence'].str.contains(word)]['sentence'].iloc[0]
    doc = nlp(sentence)
    entities = [token.text for token in doc if token.pos_ in ['NOUN', 'PROPN'] and token.text != word]  # 선택된 단어 제외하고 명사, 고유명사 추출
    # 랜덤으로 선택한 단어와 추출한 단어들 간의 관계를 그래프에 추가
    for entity in entities:
        G.add_edge(word, entity)

# 그래프 그리기
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G)  # 그래프 레이아웃 설정
nx.draw(G, pos=pos, with_labels=True, node_size=500, node_color="skyblue", font_size=12, font_weight="bold", edge_color="gray")

# 관계에 대한 주석 설명 추가
for edge in G.edges():
    plt.annotate("관계", xy=pos[edge[0]], xytext=pos[edge[1]], arrowprops=dict(facecolor='black', arrowstyle="->"))

plt.title("랜덤으로 선택된 단어 간의 관계를 단순하게 표현한 그래프")
plt.show()


