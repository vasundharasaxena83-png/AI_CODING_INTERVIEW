QUESTION_PROBABILITY = {
    "Two Sum": {"Amazon": 90, "Google": 70, "Meta": 80},
    "LRU Cache": {"Microsoft": 85, "Amazon": 60},
    "Median of Two Sorted Arrays": {"Google": 90, "Microsoft": 70},
    "N-Queens": {"Meta": 85}
}

def get_probability(question, company):
    return QUESTION_PROBABILITY.get(question, {}).get(company, 20)