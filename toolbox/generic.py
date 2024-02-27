import spacy
import nltk

class generic:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
    
    def get_token_nbr(self, x):
        doc = self.nlp(x)
        return(len(doc))

    def get_mean_len(self, x):
        doc = self.nlp(x)
        longueur_phrases = [len(sent) for sent in doc.sents]
        longueur_moyenne_phrase = sum(longueur_phrases) / len(longueur_phrases) if longueur_phrases else 0
        return (longueur_moyenne_phrase)