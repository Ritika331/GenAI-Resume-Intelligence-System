from sklearn.metrics.pairwise import cosine_similarity
from model.embedding import get_embedding


def extract_skills(text):
    """
    Simple keyword-based skill extraction
    """
    skills_list = [
        "python", "machine learning", "deep learning",
        "nlp", "data analysis", "tensorflow",
        "pytorch", "sql", "communication"
    ]

    text = text.lower()
    found_skills = [skill for skill in skills_list if skill in text]

    return found_skills


def calculate_similarity(resume_text, job_description):
    """
    Calculate cosine similarity score
    """
    resume_embedding = get_embedding(resume_text)
    job_embedding = get_embedding(job_description)

    similarity = cosine_similarity(resume_embedding, job_embedding)
    score = round(similarity[0][0] * 100, 2)

    return score


def analyze_resume(resume_text, job_description):
    """
    Complete resume analysis
    """
    score = calculate_similarity(resume_text, job_description)

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched_skills = list(set(resume_skills) & set(job_skills))
    missing_skills = list(set(job_skills) - set(resume_skills))

    return {
        "ATS_score": score,
        "Matched_Skills": matched_skills,
        "Missing_Skills": missing_skills
    }