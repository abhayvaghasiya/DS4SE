import pandas as pd
from gensim import corpora
from gensim.models import LdaModel


df = pd.read_excel('/Users/abhayvaghasiya/Desktop/DS4SE_2/DSSE-Group-7/Assignment_2/Week 2/yarn_document_term_matrix.xlsx')


terms = df.columns[1:]


dictionary = corpora.Dictionary([terms.tolist()])


corpus = []
for i, row in df.iterrows():
    bow = [(dictionary.token2id[term], freq) for term, freq in zip(terms, row[1:]) if freq > 0]
    corpus.append(bow)

# Run LDA
num_topics = 8  # Initial number of topics
lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=15, alpha=0.01, eta=0.01)

# Display topics
topics = lda_model.print_topics(num_words=20)
for topic in topics:
    print(topic)

