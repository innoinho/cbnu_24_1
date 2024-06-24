import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# 데이터프레임 생성
kg_df = pd.DataFrame({'source': ['author', 'author'], 
                      'target': ['book', 'book'], 
                      'edge': ['written by', 'composed by']})

# 그래프 생성
G = nx.from_pandas_edgelist(kg_df, 'source', 'target', 
                            edge_attr=True, create_using=nx.MultiDiGraph())

# 그래프를 시각화하기 위한 설정
plt.figure(figsize=(12, 12))
pos = nx.spring_layout(G, k=0.5)  # k regulates the distance between nodes
nx.draw(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues, pos=pos)

# 엣지 라벨 추가
edge_labels = {(u, v): d["edge"] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.show()
