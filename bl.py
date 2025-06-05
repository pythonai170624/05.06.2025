
def sum_two(a, b):
    return a+ b

def get_entities(text: str):
    import spacy
    nlp = spacy.load("en_core_web_sm")
    # text = "Taylor Swift performed in Los Angeles on March 3rd, 2023."
    doc = nlp(text)

    # Print all named entities along with their labels
    result = []
    for ent in doc.ents:
        result.append(f" {ent.text} {ent.label_}")

    return result

'''
import spacy

nlp = spacy.load("en_core_web_sm")
text = "Serena Williams had dinner with Tom Hanks in Paris."
doc = nlp(text)

# prints only the entities of type PERSON

for ent in doc.ents:
    if ent.label_ == "PERSON":
        print(ent.text)
'''