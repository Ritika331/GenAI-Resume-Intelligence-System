from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pretrained embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def extract_skills(text):
    """
    Simple skill extraction using keyword matching.
    Later we can improve this.
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

    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_description])

    similarity = cosine_similarity(resume_embedding, job_embedding)
    score = round(similarity[0][0] * 100, 2)

    return score


def analyze_resume(resume_text, job_description):

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


if __name__ == "__main__":

    resume = """
    Python developer with experience in machine learning and NLP.
    Skilled in PyTorch and data analysis.
    """

    job = """
    Looking for ML engineer skilled in Python, NLP,
    deep learning and TensorFlow.
    """

    result = analyze_resume(resume, job)

    print("ATS Score:", result["ATS_score"], "%")
    print("Matched Skills:", result["Matched_Skills"])
    print("Missing Skills:", result["Missing_Skills"])