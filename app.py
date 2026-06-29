import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Read notes file
with open("data/notes.txt", "r") as file:
    text = file.read()

# Process text
doc = nlp(text)

# Store concepts
concepts = set()

# Extract noun phrases
for chunk in doc.noun_chunks:
    concepts.add(chunk.text)

# Print concepts
print("Concepts Found:\n")

for concept in concepts:
    print(concept)