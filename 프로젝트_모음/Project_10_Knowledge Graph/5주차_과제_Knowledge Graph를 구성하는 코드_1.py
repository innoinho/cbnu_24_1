import pandas as pd
import spacy
import networkx as nx
import matplotlib.pyplot as plt

# 영어 토크나이저, 태거, 파서, 개체명 인식기, 워드 벡터를 로드합니다.
nlp = spacy.load("en_core_web_sm")

# 데이터셋을 로드합니다.
df = pd.read_csv('wiki_sentences_v2.csv')

# 방향성 그래프를 생성합니다.
G = nx.DiGraph()

# 관계를 추출하는 함수를 정의합니다.
def extract_relationships(sentence):
    doc = nlp(sentence)
    relationships = []
    for ent in doc.ents:
        # 주어를 첫 번째 개체로, 목적어를 마지막 개체로 가정합니다.
        subject = doc.ents[0]
        object = doc.ents[-1]
        # 주어와 목적어를 연결하는 동사를 찾기 위해 토큰을 반복합니다.
        for token in doc:
            if token.dep_ == 'ROOT' and token.pos_ == 'VERB':
                relationships.append((subject, token, object))
    return relationships

# 각 문장을 처리하고 그래프에 엣지를 추가합니다.
for index, row in df.iterrows():
    sentence_relationships = extract_relationships(row['sentence'])
    for rel in sentence_relationships:
        # 각 관계에 대해 그래프에 엣지를 추가합니다.
        G.add_edge(str(rel[0]), str(rel[2]), label=str(rel[1]))

# matplotlib.pyplot를 사용하여 방향성 그래프를 그립니다.
pos = nx.spring_layout(G)
plt.figure(figsize=(12, 12))
nx.draw(G, pos=pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=15, width=2, alpha=0.6, edge_color="gray")
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
