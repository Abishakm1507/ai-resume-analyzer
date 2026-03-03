# Predefined skill database (expand gradually)
SKILL_DATABASE = {
    "programming_languages": [
        "python", "java", "c++", "javascript", "sql"
    ],
    "frameworks": [
        "flask", "django", "react", "tensorflow", "pytorch"
    ],
    "ml_skills": [
        "machine learning", "deep learning",
        "nlp", "data analysis", "computer vision"
    ],
    "tools": [
        "git", "docker", "aws", "pandas", "numpy", "scikit-learn"
    ]
}


def extract_skills(text):
    """
    Extracts skills from resume text using predefined database.
    Returns categorized skill dictionary.
    """
    found_skills = {}

    for category, skills in SKILL_DATABASE.items():
        matched = []
        for skill in skills:
            if skill in text:
                matched.append(skill)

        if matched:
            found_skills[category] = matched

    return found_skills