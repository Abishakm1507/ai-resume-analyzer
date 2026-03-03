from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils.skill_extractor import SKILL_DATABASE


def calculate_ats_score(resume_text, job_description):
    """
    Calculates ATS score using TF-IDF and cosine similarity.
    Returns percentage score.
    """
    vectorizer = TfidfVectorizer()

    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = similarity[0][0] * 100

    return round(score, 2)

def calculate_skill_gap(resume_skills, job_description):
    """
    Compare job description skills with resume skills
    and return missing ones.
    """

    job_desc_lower = job_description.lower()

    # Flatten resume skills
    resume_skill_list = []
    for category in resume_skills.values():
        resume_skill_list.extend(category)

    # Get full skill list from database
    all_skills = []
    for skills in SKILL_DATABASE.values():
        all_skills.extend(skills)

    missing_skills = []

    for skill in all_skills:
        if skill in job_desc_lower and skill not in resume_skill_list:
            missing_skills.append(skill)

    return missing_skills

def calculate_skill_match_percentage(resume_skills, job_description):
    """
    Calculates percentage of job description skills matched in resume.
    """

    job_desc_lower = job_description.lower()

    resume_skill_list = []
    for category in resume_skills.values():
        resume_skill_list.extend(category)

    from utils.skill_extractor import SKILL_DATABASE

    all_skills = []
    for skills in SKILL_DATABASE.values():
        all_skills.extend(skills)

    required_skills = [
        skill for skill in all_skills if skill in job_desc_lower
    ]

    if not required_skills:
        return 0

    matched = [
        skill for skill in required_skills
        if skill in resume_skill_list
    ]

    return round((len(matched) / len(required_skills)) * 100, 2)

def generate_suggestions(ats_score, missing_skills):
    suggestions = []

    if ats_score < 50:
        suggestions.append("Your resume has low similarity with the job description. Consider tailoring it more specifically.")

    if missing_skills:
        suggestions.append(f"Consider adding these skills if you have experience: {', '.join(missing_skills)}")

    if ats_score > 80:
        suggestions.append("Your resume is highly aligned with this job description. Great work!")

    return suggestions