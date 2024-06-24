import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random
import spacy

# 데이터셋 로드
df = pd.read_csv('wiki_sentences_v2.csv')

# 영어 자연어 처리 모델 로드
nlp = spacy.load("en_core_web_sm")

# 그래프 생성
G = nx.DiGraph()  # 방향 그래프로 설정

# 랜덤으로 선택할 단어의 수
num_words_to_select = 5

# 무작위로 단어 선택하고, 해당 단어를 기준으로 유사한 단어를 찾아 그래프에 추가
for _ in range(num_words_to_select):
    
    # 데이터셋에서 무작위로 문장 선택
    sentence = random.choice(df['sentence'])
    doc = nlp(sentence)
    
    # 무작위로 단어 선택
    word = random.choice([token.text for token in doc if token.pos_ in ['NOUN', 'PROPN']])
    
    # 단어와 관련된 유사한 단어 찾기
    similar_words = []
    for token in doc:
        if token.text != word and token.text in nlp.vocab and token.is_alpha:
            similar_words.append(token.text)
            if len(similar_words) >= 5:
                break
    
    # 그래프에 노드 및 엣지 추가
    G.add_node(word)
    for similar_word in similar_words:
        G.add_node(similar_word)
        G.add_edge(word, similar_word)

# 그래프를 시각화하기 위한 설정
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.5)  # k regulates the distance between nodes
nx.draw(G, pos=pos, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, arrows=True)  # arrows=True로 화살표 설정

plt.show()
