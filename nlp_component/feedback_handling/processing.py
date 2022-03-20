import spacy
from spellchecker import SpellChecker
from nltk.corpus import stopwords

# load a large german pipeline
try:
    nlp = spacy.load("de_core_news_lg")
except:  # If not present, we download
    spacy.cli.download("de_core_news_lg")
    nlp = spacy.load("de_core_news_lg")


# preprocessing
def preprocess(user_comment):

    preprocess_user_comment = ' '.join(user_comment.strip().split())
    return preprocess_user_comment


def processing_user_comment(user_comment):
    doc = language_processing(preprocess(user_comment))
    sentences = sentence_segmentation(doc)
    processed_user_comment = []
    for sentence in sentences:
        keywords = keyword_extraction(sentence)
        sentence_text = get_sentence_words(sentence)
        processed_user_comment.append((sentence_text, keywords, sentence.text))
    return processed_user_comment


def spellchecking():
    pass


def language_processing(user_comment):
    doc = nlp(user_comment)
    return doc


def sentence_segmentation(doc):
    sentences = []
    for sentence in doc.sents:
        sentences.append(sentence)
    return sentences


def keyword_extraction(sentence):
    keywords = []
    for token in sentence:
        if token.pos_ == "VERB":
            keywords.append(token.lemma_)
        elif token.pos_ == "NOUN":
            if token.dep_ == "oa" or token.dep_ == "sb" or token.dep_ == "nk":
                keywords.append(token.lemma_)
    return keywords


def get_sentence_words(sentence):
    sentence_text = []
    for token in sentence:
        if not token.is_punct and token.lemma_ not in stopwords.words("german"):
            sentence_text.append(token.lemma_)

    return sentence_text