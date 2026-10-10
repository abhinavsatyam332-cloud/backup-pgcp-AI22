# Decision tree on the diabetes dataset: entropy criterion, depth, rules, importance, saving the tree
# (Slide: Decision Tree Code Examples - implementation\13_5_Decision-tree-diabetes.py)
import graphviz
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay, accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz, export_text, plot_tree

df = pd.read_csv("diabetes.csv")
X = df.drop("Outcome", axis=1)
y = df["Outcome"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101, stratify=y)
# NOTE: decision trees do not need scaling - each split looks at one feature at a time

# ------------------------------------------------------------
# 1) Default tree vs a limited tree
# ------------------------------------------------------------
default = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
print(f"Default tree: depth {default.get_depth()}, test accuracy {default.score(X_test, y_test):.3f}")

model = DecisionTreeClassifier(criterion="entropy", max_depth=4, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(f"Entropy tree, max_depth 4: test accuracy {accuracy_score(y_test, y_pred):.3f}")
print(classification_report(y_test, y_pred, target_names=["No Diabetes", "Diabetes"]))

ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=["No Diabetes", "Diabetes"], cmap="Blues")
plt.title("Confusion Matrix - Decision Tree")
plt.show()

# ------------------------------------------------------------
# 2) Rules and the tree picture
# ------------------------------------------------------------
print(export_text(model, feature_names=list(X.columns)))

plt.figure(figsize=(18, 8))
plot_tree(model, feature_names=X.columns, class_names=["No Diabetes", "Diabetes"],
          filled=True, rounded=True, fontsize=8)
plt.title("Decision Tree (entropy, max_depth = 4)")
plt.show()

# Save a high-quality image with Graphviz (needs the Graphviz program: https://graphviz.org/download/)
dot = export_graphviz(model, out_file=None, feature_names=list(X.columns),
                      class_names=["No Diabetes", "Diabetes"], filled=True, rounded=True)
try:
    graphviz.Source(dot).render("diabetes_tree", format="png", cleanup=True)
    print("Saved diabetes_tree.png")
except graphviz.ExecutableNotFound:
    print("Graphviz program not installed - skipping the PNG export")

# ------------------------------------------------------------
# 3) Feature importance: how much each feature reduced the entropy in total
# ------------------------------------------------------------
importances = pd.DataFrame({"Feature": X.columns, "Importance": model.feature_importances_}) \
    .sort_values("Importance", ascending=False)
print(importances)
sns.barplot(data=importances, x="Importance", y="Feature", color="teal")
plt.title("Feature Importance (information gain)")
plt.show()

# ------------------------------------------------------------
# 4) A tree predicts in STEPS: probability of diabetes vs glucose only
# ------------------------------------------------------------
model_glucose = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
model_glucose.fit(df[["Glucose"]], y)
glucose_range = pd.DataFrame({"Glucose": np.linspace(df["Glucose"].min(), df["Glucose"].max(), 300)})
plt.plot(glucose_range, model_glucose.predict_proba(glucose_range)[:, 1], color="orange", lw=2,
         label="Tree: P(diabetes | glucose)")
plt.scatter(df["Glucose"], y, alpha=0.2, label="Actual (0 / 1)")
plt.xlabel("Glucose")
plt.ylabel("Probability of diabetes")
plt.title("A decision tree gives a step function")
plt.legend()
plt.show()
