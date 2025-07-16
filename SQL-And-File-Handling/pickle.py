import pickle as pk

data_dictionary = {
    'books': 12,
    'articles': 100,
    'subjects': ['math',
                    'programming',
                    'data science']}
with open('readings.pk', 'wb') as f:
    pk.dump(data_dictionary, f)