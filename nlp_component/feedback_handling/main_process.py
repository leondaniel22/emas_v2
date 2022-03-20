from .processing import *
from .grouping import *
from ..models import *


def process_user_comment(user_comment, error_appearance):
    """start to process a new user comment"""
    processed_user_comment = processing_user_comment(user_comment=user_comment)
    add_to_groups(processed_user_comment=processed_user_comment, content=user_comment, error_appearance=error_appearance)


def get_group_represent(group_id):
    current_avg_similarity = 0
    sentences = Sentence.objects.filter(group_id=group_id)
    current_sentence = sentences[0]
    if len(sentences) > 1:
        for sentence_1 in sentences:
            keywords_1 = [keyword.lemma for keyword in Keyword.objects.filter(sentence=sentence_1)]
            similarity_sum = 0
            for sentence_2 in sentences:
                if not sentence_1 == sentence_2:
                    keywords_2 = [keyword.lemma for keyword in Keyword.objects.filter(sentence=sentence_2)]
                    similarity_sum += sentence_similarity(sentence_1.name, sentence_2.name, keywords_1, keywords_1)

            avg_similarity = len(sentences)-1
            if similarity_sum/avg_similarity > current_avg_similarity:
                current_avg_similarity = avg_similarity
                current_sentence = sentence_1
    return current_sentence.name




