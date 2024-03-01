from wordfreq import word_frequency
from textblob import TextBlob
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import word_tokenize
from spellchecker import SpellChecker
from lexical_diversity import lex_div as ld
import spacy
import textstat
#word_frequency("Data", "en")

class complexity:
    def lexical_density(self, text):
        blob = TextBlob(text)
        words = blob.words
        content_words = [word.lower() for word in words if word.lower() not in stopwords.words('english')]
        lexical_density = len(content_words) / len(words)
        return lexical_density

    def calculate_pos_ratios(self, paragraph):
        words = word_tokenize(paragraph)
        stop_words = set(stopwords.words('english'))
        words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
        pos_tags = nltk.pos_tag(words)
        total_words = len(words)
        adjective_count = sum(1 for word, pos in pos_tags if pos in ['JJ'] or pos in ['JJR'] or pos in ['JJS'])
        noun_count = sum(1 for word, pos in pos_tags if pos in ['NN']  or pos in ['NNS'])
        verb_count = sum(1 for word, pos in pos_tags if pos in ['VB'] or pos in ['VBD'] or pos in ['VBG'] or pos in ['VBN'] or pos in ['VBP'] or 
        pos in ['VBZ'])
        adjective_ratio = adjective_count / total_words if total_words > 0 else 0
        noun_ratio = noun_count / total_words if total_words > 0 else 0
        verb_ratio = verb_count / total_words if total_words > 0 else 0

        return adjective_ratio, noun_ratio, verb_ratio

    def root_ttr(self, text):
        flt = ld.flemmatize(text)
        return ld.root_ttr(flt)

    def ttr(self, text):
        flt = ld.flemmatize(text)
        return ld.ttr(flt)

    def log_ttr(self, text):
        flt = ld.flemmatize(text)
        return ld.log_ttr(flt)

    def mass_ttr(self, text):
        flt = ld.flemmatize(text)
        return ld.maas_ttr(flt)

    def msttr(self, text):
        flt = ld.flemmatize(text)
        return ld.msttr(flt)

    def mtld(self, text):
        flt = ld.flemmatize(text)
        return ld.mtld(flt)

    def coleman_liau(self, text):
        return textstat.coleman_liau_index(text)

    def lexical_score(self, x):
        nlp = spacy.load("en_core_web_sm")
        word = "computer"
        synsets = wordnet.synsets(word)
        lexical_field = set()
        for synset in synsets:
            for lemma in synset.lemmas():
                lexical_field.add(lemma.name())
        result = list(lexical_field)
        for i in range(len(result)):
            result[i] = result[i].replace('_', ' ')
        doc = nlp(x)
        res = [str(i) for i in doc]
        count = 0
        for i in range(len(res)):
            if res[i] in result:
                count += 1
        return count


    def generate_lexical_field(self, word):
        synsets = wordnet.synsets(word)
        lexical_field = set()
        for synset in synsets:
            for lemma in synset.lemmas():
                lexical_field.add(lemma.name())
        result = list(lexical_field)
        for i in range(len(result)):
            result[i] = result[i].replace('_', ' ')
        return result