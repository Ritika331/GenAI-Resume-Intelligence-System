from model.analyzer import analyze_resume


def run_analysis():
    print("=== GenAI Resume Intelligence System ===\n")

    resume = input("Enter Resume Text:\n")
    print("\n")
    job = input("Enter Job Description:\n")
    print("\nAnalyzing...\n")

    result = analyze_resume(resume, job)

    print("ATS Score:", result["ATS_score"], "%")
    print("Matched Skills:", result["Matched_Skills"])
    print("Missing Skills:", result["Missing_Skills"])


if __name__ == "__main__":
    run_analysis()