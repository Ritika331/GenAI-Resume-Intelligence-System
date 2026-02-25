from sentence_transformers import SentenceTransformer

# Load model once when module is imported
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")


def get_embedding(text):
    """
    Convert text into embedding vector
    """
    return model.encode([text])