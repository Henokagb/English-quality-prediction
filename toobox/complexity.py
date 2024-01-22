from wordfreq import word_frequency
from textblob import TextBlob
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk import word_tokenize
nltk.download('averaged_perceptron_tagger')
from spellchecker import SpellChecker

#word_frequency("Data", "en")

def lexical_density(text):
    blob = TextBlob(text)
    words = blob.words
    content_words = [word.lower() for word in words if word.lower() not in stopwords.words('english')]
    lexical_density = len(content_words) / len(words)
    return lexical_density


def calculate_pos_ratios(paragraph):
    words = word_tokenize(paragraph)
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.isalpha() and word.lower() not in stop_words]
    pos_tags = nltk.pos_tag(words)
    total_words = len(words)
    adjective_count = sum(1 for word, pos in pos_tags if pos in ['JJ'] or pos in ['JJR'] or pos in ['JJS'])
    noun_count = sum(1 for word, pos in pos_tags if pos in ['NN']  or pos in ['NNS'])
    verb_count = sum(1 for word, pos in pos_tags if pos in ['VB'] or pos in ['VBD'] or pos in ['VBG'] or pos in ['VBN'] or pos in ['VBP'] or pos in ['VBZ'])
    adjective_ratio = adjective_count / total_words if total_words > 0 else 0
    noun_ratio = noun_count / total_words if total_words > 0 else 0
    verb_ratio = verb_count / total_words if total_words > 0 else 0

    return adjective_ratio, noun_ratio, verb_ratio