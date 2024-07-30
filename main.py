import spacy
from spacy import displacy

# Load the spacy model
nlp = spacy.load("en_core_web_sm")


def parse_sentence(sentence):
    # Process the sentence using spacy
    doc = nlp(sentence)

    # Print the dependency parsing results
    for token in doc:
        print(f"{token.text:10} {token.dep_:10} {token.head.text:10} {token.head.dep_:10}")

    displacy.serve(doc, style="dep")


if __name__ == "__main__":
    # Example sentence
    sentence = "The quick brown fox jumps over the lazy dog."

    # Parse and display the dependency structure
    parse_sentence(sentence)

