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

# 노드 중요성에 따라 노드 크기 설정
node_size = [5000 * len(list(G.neighbors(node))) for node in G.nodes]

# 랜덤 레이아웃 생성
pos = nx.random_layout(G)

# 그래프 그리기
plt.figure(figsize=(10, 10))
nx.draw(G, pos=pos, with_labels=True, node_size=node_size, node_color="skyblue", font_size=12, font_weight="bold", width=2, edge_color="gray", arrows=False)  # arrows=False로 화살표 제거

# 관계에 대한 주석 설명 추가
for edge in G.edges():
    plt.annotate("", xy=pos[edge[0]], xytext=pos[edge[1]], arrowprops=dict(facecolor='black', arrowstyle="-"))

plt.show()


