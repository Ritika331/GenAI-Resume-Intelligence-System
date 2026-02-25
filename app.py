import streamlit as st
from model.analyzer import analyze_resume
from model.pdf_reader import extract_text_from_pdf
import tempfile


st.set_page_config(page_title="GenAI Resume Intelligence", layout="wide")

st.title("🚀 GenAI Resume Intelligence System")
st.markdown("Analyze your resume against a job description using AI.")


# Upload resume PDF
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

# Job description input
job_description = st.text_area("Enter Job Description")


if st.button("Analyze Resume"):

    if uploaded_file is None:
        st.error("Please upload a resume PDF.")
    elif not job_description.strip():
        st.error("Please enter a job description.")
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.read())
            resume_text = extract_text_from_pdf(tmp.name)

        if resume_text is None:
            st.error("Could not extract text from PDF.")
        else:
            result = analyze_resume(resume_text, job_description)

            score = result["ATS_score"]
            level = result["Match_Level"]
            suggestion = result["Suggestion"]

            st.success("Analysis Complete ✅")

            st.divider()

            # Score Section
            st.subheader("📊 ATS Score")
            st.metric(label="Match Percentage", value=f"{score} %")

            # Color-coded interpretation
            if level == "Low Match":
                st.error(f"🔴 {level}")
            elif level == "Medium Match":
                st.warning(f"🟡 {level}")
            else:
                st.success(f"🟢 {level}")

            st.info(f"💡 Suggestion: {suggestion}")

            st.divider()

            # Skills Section
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("✅ Matched Skills")
                if result["Matched_Skills"]:
                    for skill in result["Matched_Skills"]:
                        st.write(f"✔️ {skill}")
                else:
                    st.write("No matched skills found.")

            with col2:
                st.subheader("❌ Missing Skills")
                if result["Missing_Skills"]:
                    for skill in result["Missing_Skills"]:
                        st.write(f"❗ {skill}")
                else:
                    st.write("No missing skills detected.")