import numpy as np


def cosine_similarity(x, y):
    # Ensure length of x and y are the same
    if len(x) != len(y):
        return None

    # Compute the dot product between x and y
    dot_product = np.dot(x, y)

    # Compute the L2 norms (magnitudes) of x and y
    magnitude_x = np.sqrt(np.sum(x ** 2))
    magnitude_y = np.sqrt(np.sum(y ** 2))

    # Compute the cosine similarity
    cosine_similarity = dot_product / (magnitude_x * magnitude_y)

    return cosine_similarity

sent1 = " this is demo sentence"
sent1 = sent1.strip()
sent1arr = sent1.split(" ")

sent2 = "this is anohter sentence"
sent2.strip()
sent2arr = sent2.split(" ")

lst = []
x = []
y = []

for i in sent1arr:
    if i not  in lst:
        lst.append(i)

for i in sent2arr:
    if i not  in lst:
        lst.append(i)

ind = 0
for i in lst:
    if i in sent1arr:
        x[ind] = 1
        ind +=1
ind = 0
for i in lst:
    if i in sent2arr:
        y[ind] = 1
        ind +=1

cosine_similarity(x,y)
