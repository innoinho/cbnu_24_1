import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

iris = load_iris()
decision_tree = DecisionTreeClassifier(criterion="entropy", random_state=0, max_depth=3)
decision_tree = decision_tree.fit(iris.data, iris.target)

plt.figure()
plot_tree(decision_tree, filled=True)
plt.show()
