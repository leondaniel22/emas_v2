import spacy
from spacy.tokenizer import Tokenizer
import numpy as np
import wn
from ..models import *
from scipy import spatial


# load a small german pipeline
try:
    nlp = spacy.load("de_core_news_md")
except:  # If not present, we download
    spacy.cli.download("de_core_news_md")
    nlp = spacy.load("de_core_news_md")



def word_similarity(w1, w2):
    """determine similarity of two words using a semantic net and the spacy-similarity-function"""
    similarity = 0
    if not wn.lexicons():
        wn.download("odenet")

    if w1 == w2:
        similarity = 1
    else:
        for synset in wn.synsets(w1):
            if w2 in synset.lemmas():
                similarity = 1
        for synset in wn.synsets(w2):
            if w1 in synset.lemmas():
                similarity = 1
        if similarity == 0:
            similarity = nlp(w1).similarity(nlp(w2))
            pass

    return similarity


def get_sentence_vectors(sentence1, sentence2, keywords1, keywords2):
    """create sentence vectors from two sentencens and their word similarities"""
    union_set = set(sentence1).union(set(sentence2))
    print(union_set)
    vector1 = []
    vector2 = []
    for element in union_set:
        similarity1 = 0
        similarity2 = 0
        for word1 in sentence1:
            if word_similarity(element, word1) > similarity1:
                similarity1 = word_similarity(element, word1)
                print(element, word1, word_similarity(element, word1))
        for word2 in sentence2:
            if word_similarity(element, word2) > similarity2:
                similarity2 = word_similarity(element, word2)
        if element not in keywords1+keywords2:
            similarity1 *= 0.2
            similarity2 *= 0.2
        else:
            for token in nlp(element):
                if not token.pos_ == "NOUN":
                    similarity1 *= 0.8
                    similarity2 *= 0.8

        vector1.append(similarity1)
        vector2.append(similarity2)

    return vector1, vector2


def cosine_similarity(vector1, vector2):
    """determine cosine similarity of two vectors"""
    print(vector1, vector2)
    return 1 - spatial.distance.cosine(vector1, vector2)


def sentence_similarity(sentence1, sentence2, keywords1, keywords2):
    """determine the similarity of two sentences"""
    vector1, vector2 = get_sentence_vectors(sentence1, sentence2, keywords1, keywords2)
    similarity = cosine_similarity(vector1, vector2)
    return similarity


def get_mean(similarities):
    """calculate mean of a list of similarities"""
    return np.mean(similarities)


def add_to_groups(processed_user_comment, content, error_appearance):
    """add a new user comment to a group for each sentence of the user comment"""

    user_comment = UserComment(content=content, error_appearance=error_appearance)
    user_comment.save()
    tokenizer = Tokenizer(nlp.vocab)
    threshold = Threshold.objects.all()[0]
    groups = CommentGroup.objects.all()
    already_taken = []

    for element in processed_user_comment:

        user_comment_sentence = None
        new_keyword = None
        semantic_group = None
        new_sentence, new_keywords, original_sentence = element
        current_similarity = 0
        group_id = -1
        for group in groups:
            group_sentences = Sentence.objects.filter(group=group.pk)
            similarities = []
            for group_sentence in group_sentences:
                group_keywords = Keyword.objects.filter(sentence=group_sentence.pk)
                group_sentence = [token.text for token in tokenizer(group_sentence.content)]
                print(new_sentence, group_sentences)
                similarity = sentence_similarity(new_sentence, group_sentence, new_keywords, [keyword.lemma for keyword in group_keywords])
                similarities.append(similarity)
                print(similarity)
                print("________________")
                if get_mean(similarities) > current_similarity:
                    current_similarity = get_mean(similarities)
                    group_id = group.pk

            if not current_similarity > threshold.value:
                group_id = -1

        if group_id == -1 or group_id in already_taken:
            semantic_group = CommentGroup(error_appearance=error_appearance)
            semantic_group.save()
            already_taken.append(semantic_group.pk)
        else:
            semantic_group = CommentGroup.objects.get(pk=group_id)
            already_taken.append(group_id)

        user_comment_sentence = Sentence(name=original_sentence, content=" ".join(new_sentence), user_comment=user_comment, group=semantic_group)
        print(user_comment_sentence)
        user_comment_sentence.save()
        for keyword in new_keywords:
            new_keyword = Keyword(lemma=keyword)
            new_keyword.save()
            new_keyword.sentence.add(user_comment_sentence)



