from model.analyzer import analyze_resume


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