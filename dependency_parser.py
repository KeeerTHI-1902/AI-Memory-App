import spacy

nlp = spacy.load("en_core_web_sm")

text = """
Python is used in Data Science.
Machine Learning uses Statistics.
Data Science uses Python and SQL.
Statistics helps in Machine Learning.
"""

doc = nlp(text)

for sent in doc.sents:

    print("\nSentence:", sent.text)

    for token in sent:

        print(
            token.text,
            " | ",
            token.dep_,
            " | ",
            token.head.text
        )