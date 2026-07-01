import json

SKILL_FILE = "data/skills.json"

def load_skills():
    with open(SKILL_FILE, "r") as f:
        return json.load(f)

def update_skill(level, score):
    skills = load_skills()

    if score >= 80:
        skills[level] += 2
    elif score >= 50:
        skills[level] += 1
    else:
        skills[level] -= 1

    # clamp
    skills[level] = max(0, skills[level])

    with open(SKILL_FILE, "w") as f:
        json.dump(skills, f)

    return skills

def get_next_level(skills):
    if skills["easy"] > 5:
        return "medium"
    if skills["medium"] > 5:
        return "hard"
    return "easy"