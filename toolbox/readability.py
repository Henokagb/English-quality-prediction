import textstat
import spacy


class readability:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
    
    #The Flesch Reading Ease gives a text a score between 1 and 100, with 100 being the highest readability score
    def f_reading_ease(self, text):
        return textstat.flesch_reading_ease(text)

    #The Gunning Fog formula generates a grade level between 0 and 20. It estimates the education level required to understand the text.
    def g_fog(self, text):
         return textstat.gunning_fog(text)

    def ari(self, text):
        return textstat.automated_readability_index(text)

    def smog_index(self, text):
        return textstat.smog_index(text)

    def flesch_kincaid(self, text):
        return textstat.flesch_kincaid_grade(text)


    def dale_chall_readability(self, text):
        return textstat.dale_chall_readability_score(text)