from spellchecker import SpellChecker


def get_misspelling_score(paragraph):
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