import sklearn.feature_extraction.text as txt
def comparison_test():
    sklearn_hashing_trick = txt.HashingVectorizer(n_features=20, binary=True, norm=None)
    one_hot_enconder = txt.CountVectorizer()
    texts = ['Python for data science','Python for machine learning']
    one_hot_enconded = one_hot_enconder.fit_transform(texts)
    hashing = sklearn_hashing_trick.transform(texts)
from example_code import comparison_test
%mprun f comparison_test comparison_test()