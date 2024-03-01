import nltk
from nltk.corpus import stopwords
from nltk import ngrams
from nltk.tokenize import word_tokenize
from collections import Counter
import math
nltk.download('punkt')
import spacy
import pandas as pd


def stopword_count(text):
    """
    Calculate the count of stopwords in a given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - int: Count of stopwords.
    """
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    stopword_count = sum(1 for word in words if word.lower() in stop_words)
    return stopword_count

def named_entity_recognition(text):
    """
    Perform Named Entity Recognition (NER) on the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - list: List of named entities and their labels.
    """
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy NLP pipeline
    doc = nlp(text)

    # Extract named entities and their labels
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    return len(entities)

def unique_word_count(text):
    """
    Calculate the count of unique words in a given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - int: Count of unique words.
    """
    words = text.split()
    unique_words = set(words)
    unique_word_count = len(unique_words)
    return unique_word_count

def generate_ngrams(text):
    """
    Generate N-grams from the given text.

    Parameters:
    - text (str): Input text.
    
    Returns:
    - list: List of N-grams.
    """
    words = word_tokenize(text)
    n_grams = list(ngrams(words, 2))
    return len(n_grams)

def read_time_estimate(text, words_per_minute=200):
    """
    Estimate read time for a given text.

    Parameters:
    - text (str): Input text.
    - words_per_minute (int): Average reading speed in words per minute (default is 200).

    Returns:
    - float: Estimated read time in minutes.
    """
    word_count = len(text.split())
    read_time = word_count / words_per_minute
    return read_time

import spacy

def dependency_parse_features(text):
    """
    Extract features from the dependency parse tree of the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - dict: Dictionary of dependency parse features.
    """
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy NLP pipeline
    doc = nlp(text)

    # Initialize feature counters
    num_dependencies = 0
    dep_types = set()

    # Iterate over tokens and extract features from the dependency parse
    for token in doc:
        num_dependencies += len(list(token.children))
        dep_types.add(token.dep_)

    # Calculate average number of dependencies per token
    avg_dependencies_per_token = num_dependencies / len(doc)

    # Create a dictionary of features
    return num_dependencies

def avg_dependencies_per_token(text):
    """
    Extract features from the dependency parse tree of the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - dict: Dictionary of dependency parse features.
    """
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy NLP pipeline
    doc = nlp(text)

    # Initialize feature counters
    num_dependencies = 0
    dep_types = set()

    # Iterate over tokens and extract features from the dependency parse
    for token in doc:
        num_dependencies += len(list(token.children))
        dep_types.add(token.dep_)

    # Calculate average number of dependencies per token
    avg_dependencies_per_token = num_dependencies / len(doc)

    # Create a dictionary of features
    return avg_dependencies_per_token

def unique_dependency_types(text):
    """
    Extract features from the dependency parse tree of the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - dict: Dictionary of dependency parse features.
    """
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy NLP pipeline
    doc = nlp(text)

    # Initialize feature counters
    num_dependencies = 0
    dep_types = set()

    # Iterate over tokens and extract features from the dependency parse
    for token in doc:
        num_dependencies += len(list(token.children))
        dep_types.add(token.dep_)

    # Calculate average number of dependencies per token
    avg_dependencies_per_token = num_dependencies / len(doc)

    # Create a dictionary of features
    
    return len(dep_types)

def noun_verb_ratio(text):
    """
    Calculate the Noun-Verb Ratio for the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - float: Noun-Verb Ratio.
    """
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text with spaCy NLP pipeline
    doc = nlp(text)

    # Initialize counters for nouns and verbs
    noun_count = 0
    verb_count = 0

    # Iterate over tokens and count nouns and verbs
    for token in doc:
        if token.pos_ == 'NOUN':
            noun_count += 1
        elif token.pos_ == 'VERB':
            verb_count += 1

    # Calculate the Noun-Verb Ratio
    if verb_count > 0:
        ratio = noun_count / verb_count
    else:
        ratio = 0.0

    return ratio

def word_entropy(text):
    """
    Calculate the word entropy for the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - float: Word Entropy.
    """
    # Tokenize the text into words
    words = text.split()

    # Calculate the frequency distribution of words
    word_counts = Counter(words)

    # Calculate the total number of words
    total_words = len(words)

    # Calculate word probabilities
    probabilities = [count / total_words for count in word_counts.values()]

    # Calculate word entropy
    entropy = -sum(p * math.log2(p) for p in probabilities)

    return entropy

def read_time_difficulty_estimate(text):
    """
    Estimate the difficulty of reading the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - str: Difficulty level (e.g., 'Easy', 'Moderate', 'Difficult').
    """
    # Tokenize the text into words
    words = text.split()

    # Calculate average word length
    avg_word_length = sum(len(word) for word in words) / len(words)

    # Count unique words
    unique_word_count = len(set(words))

    # Estimate difficulty based on average word length and unique word count
    if avg_word_length <= 4 and unique_word_count <= 50:
        return 'Easy'
    elif avg_word_length <= 6 and unique_word_count <= 100:
        return 0
    else:
        return 1

    
def syllable_count(text):
    """
    Count the number of syllables in the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - int: Syllable count.
    """
    words = nltk.word_tokenize(text)
    syllable_count = sum([nltk.syllable_count(word) for word in words])
    return syllable_count

import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

def positive_score(text):
    """
    Estimate emotion scores (positive and negative sentiment) for the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - dict: Dictionary containing positive and negative emotion scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    # Positive and negative emotion scores
    positive_score = sentiment_scores['pos']
    return positive_score

def negative_score(text):
    """
    Estimate emotion scores (positive and negative sentiment) for the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - dict: Dictionary containing positive and negative emotion scores.
    """
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(text)

    # Positive and negative emotion scores
    negative_score = sentiment_scores['neg']
    return negative_score

def co_reference_features(text):
    """
    Extract co-reference features from the given text.

    Parameters:
    - text (str): Input text.

    Returns:
    - list: List of dictionaries containing co-reference features.
    """
    # Load the English language model with coreference resolution support
    nlp = spacy.load("en_coref_md")

    # Process the text with spaCy NLP pipeline
    doc = nlp(text)

    # Initialize a list to store co-reference features
    co_reference_features_list = []

    # Iterate over sentences and extract co-reference information
    for sent in doc.sents:
        co_reference_info = {'sentence': sent.text, 'co_references': []}

        # Extract co-reference clusters in the sentence
        for cluster in sent._.coref_clusters:
            mentions = [mention.text for mention in cluster.mentions]
            co_reference_info['co_references'].append({
                'representative': cluster.main.text,
                'mentions': mentions
            })

        co_reference_features_list.append(co_reference_info)

    return len(co_reference_features_list)

def get_prediction(essay, xg_reg, gen, reada, qual, comp):
    data = [gen.get_token_nbr(essay), gen.get_mean_len(essay), qual.get_sophisticated_nbr(essay),
            qual.level_of_language(essay), reada.g_fog(essay), reada.ari(essay),
            reada.smog_index(essay), reada.flesch_kincaid(essay), comp.coleman_liau(essay),
            reada.dale_chall_readability(essay), comp.root_ttr(essay), comp.ttr(essay),
            comp.log_ttr(essay), comp.mass_ttr(essay), comp.msttr(essay), comp.mtld(essay),
            negative_score(essay), positive_score(essay), read_time_difficulty_estimate(essay),
            word_entropy(essay), noun_verb_ratio(essay), unique_dependency_types(essay),
            avg_dependencies_per_token(essay), dependency_parse_features(essay),
            read_time_estimate(essay), generate_ngrams(essay),
            unique_word_count(essay), stopword_count(essay)]

    # Reshape the data to match the model's expectations
    data_reshaped = [data]

    columns = ['token_nbr', 'mean_len', 'sophisticated_nbr', 'level_of_language',
               'gunning_fog', 'ari', 'smog_index', 'flesch_kincaid', 'coleman_liau',
               'dale_chall_readability', 'root_ttr', 'ttr', 'log_ttr', 'mass_ttr',
               'msttr', 'mtld', 'negative_score', 'positive_score',
               'read_time_difficulty_estimate', 'word_entropy', 'noun_verb_ratio',
               'unique_dependency_types', 'avg_dependencies_per_token',
               'dependency_parse_features', 'read_time_estimate', 'generate_ngrams',
               'unique_word_count', 'stopword_count']

    df_essay = pd.DataFrame(data_reshaped, columns=columns)
    y_pred_valid = xg_reg.predict(df_essay)
    return y_pred_valid[0]