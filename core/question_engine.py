import random
from core.faang_bank import FAANG_QUESTIONS

def get_question(company, level):
    return random.choice(FAANG_QUESTIONS[company][level])