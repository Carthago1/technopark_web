from django.db import models
from random import randint

QUESTIONS = [
    {
        'id': question_id,
        'title': f'Question {question_id}',
        'text': f'Text of question {question_id}',
        'answers_number': question_id,
        'tags': [f'tag{i + 1}' for i in range(question_id % 5 + 1)],
        'image_number': str(question_id % 3 + 1),
        'likes_number': question_id,
        'hot_rating': randint(1, 100),
    } for question_id in range(1, 101)
]

ANSWERS = [
    {
        'question_id': question_id,
        'answer_number': question_id,
    } for question_id in range(1, 101)
]

for answer in ANSWERS:
    answers = []
    for answer_id in range(1, answer['answer_number'] + 1):
        answers.append({
            'title': f'Answer {answer_id}',
            'text': f'Text of answer {answer_id}',
            'likes_number': answer_id,
            'image_number': str(answer_id % 3 + 1),
        })
    answer['answer_items'] = answers

USER = {
    'login': 'dr_pepper',
    'email': 'dr_pepper@mail.ru',
    'nick_name': 'Dr. Pepper',
    'image_number': '3',
}

