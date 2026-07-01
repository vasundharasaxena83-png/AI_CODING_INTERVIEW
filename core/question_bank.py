import random

QUESTIONS = {
    "easy": [
        {
            "question": "Reverse a string",
            "input": "hello",
            "expected": "olleh"
        },
        {
            "question": "Find sum of array",
            "input": [1, 2, 3],
            "expected": 6
        }
    ],
    "medium": [
        {
            "question": "Check palindrome",
            "input": "madam",
            "expected": True
        },
        {
            "question": "Find max in array",
            "input": [10, 20, 5],
            "expected": 20
        }
    ],
    "hard": [
        {
            "question": "Two Sum problem",
            "input": ([2,7,11,15], 9),
            "expected": [0,1]
        }
    ]
}

def get_question(level):
    return random.choice(QUESTIONS[level])