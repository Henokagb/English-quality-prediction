import spacy
from spellchecker import SpellChecker
import nltk

class quality:
    def __init__(self):
            self.nlp = spacy.load("en_core_web_sm")
    
    def get_misspelling_score(self, paragraph):
        to_remove = [',', '.', ':', ';', '!', '?']
        cleaned_paragraph = ''.join([i for i in paragraph if i not in to_remove])
        spell = SpellChecker(language='en')
        words = cleaned_paragraph.split()
        misspelled_words = spell.unknown(words)
        misspelled_count = len(misspelled_words)
        total_words = len(words)
        if total_words == 0:
            return 0
        else:
            misspelling_score = (misspelled_count / total_words) * 100
            return misspelling_score


    def get_sophisticated_nbr(self, x):
        doc = self.nlp(x)
        nombre_mots_sophistiques = sum(1 for token in doc if len(token.text) > 6)
        return(nombre_mots_sophistiques)

    def level_of_language(self, x):
        doc = self.nlp(x)
        longueur_phrases = [len(sent) for sent in doc.sents]
        longueur_moyenne_phrase = sum(longueur_phrases) / len(longueur_phrases) if longueur_phrases else 0
        nombre_mots_sophistiques = sum(1 for token in doc if len(token.text) > 6)
        niveau = "Élevé" if longueur_moyenne_phrase > 20 and nombre_mots_sophistiques > 10 else "Bas"
        return(niveau)
 