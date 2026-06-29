import spacy

nlp = spacy.load("en_core_web_sm")


def extract_relationships(text):

    doc = nlp(text)

    relationships = []

    for sent in doc.sents:

        entities = []

        for chunk in sent.noun_chunks:
            entities.append(chunk.text)

        if len(entities) >= 2:

            source = entities[0]
            target = entities[-1]

            relationships.append((source, target))

    return relationships