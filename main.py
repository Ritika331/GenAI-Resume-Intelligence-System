from model.analyzer import analyze_resume
from model.pdf_reader import extract_text_from_pdf


def run_analysis():
    print("=== GenAI Resume Intelligence System ===\n")

    choice = input("Type '1' to paste resume text OR '2' to provide PDF file path: ")

    if choice == "1":
        resume = input("\nEnter Resume Text:\n")

    elif choice == "2":
        pdf_path = input("\nEnter full PDF file path:\n")
        resume = extract_text_from_pdf(pdf_path)

        if resume is None:
            print("Failed to extract text from PDF.")
            return

    else:
        print("Invalid choice.")
        return

    job = input("\nEnter Job Description:\n")

    print("\nAnalyzing...\n")

    result = analyze_resume(resume, job)

    print("ATS Score:", result["ATS_score"], "%")
    print("Matched Skills:", result["Matched_Skills"])
    print("Missing Skills:", result["Missing_Skills"])


if __name__ == "__main__":
    run_analysis()