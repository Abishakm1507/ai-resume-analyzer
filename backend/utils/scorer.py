from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


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
    Finds missing skills by comparing job description keywords.
    """

    job_desc_lower = job_description.lower()

    missing_skills = []

    # Flatten resume skill list
    resume_skill_list = []
    for category in resume_skills.values():
        resume_skill_list.extend(category)

    for skill in resume_skill_list:
        if skill not in job_desc_lower:
            missing_skills.append(skill)

    return missing_skills