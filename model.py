from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load pretrained embedding model from Hugging Face
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def calculate_similarity(resume_text, job_description):
    
    # Convert texts to embeddings
    resume_embedding = model.encode([resume_text])
    job_embedding = model.encode([job_description])
    
    # Calculate cosine similarity
    similarity = cosine_similarity(resume_embedding, job_embedding)
    
    # Convert to percentage
    score = similarity[0][0] * 100
    
    return round(score, 2)


if __name__ == "__main__":
    
    resume = "Python developer with experience in machine learning and NLP."
    
    job = "Looking for a machine learning engineer skilled in Python and NLP."
    
    score = calculate_similarity(resume, job)
    
    print("ATS Match Score:", score, "%")