import streamlit as st
import yaml
from src.utils.pdf import extract_text_from_pdf
from src.utils.llm import parse_resume, review_resume
from resume_formatter import format_resume

def main():
    st.title(":page_facing_up: Resume Parser and Reviewer")
    st.sidebar.image("src/images/banner.png")
    st.sidebar.markdown("""
        :brain: ResumeAI is an advanced tool that leverages the power of Large Language Models (LLMs) to analyze and improve resumes.
    """)

    with st.sidebar:
        uploaded_file = st.file_uploader("Upload your resume (PDF)", type="pdf")
        job_description = st.text_area("Enter job description (optional)").strip()

        if st.button("Run Analysis", use_container_width=True):
            if uploaded_file is not None:
                resume_text = extract_text_from_pdf(uploaded_file)
                with st.spinner("Parsing resume... [Step 1 of 2]"):
                    resume_yaml = parse_resume(resume_text)
                with st.spinner("Reviewing resume... [Step 2 of 2]"):
                    review_response = review_resume(resume_yaml, job_description)

                resume_data = yaml.safe_load(resume_yaml)
                review_data = yaml.safe_load(review_response)

                st.session_state.resume_data = resume_data
                st.session_state.review_data = review_data
                st.session_state.current_section = 0
                st.session_state.sections = list(resume_data.keys())

    if 'resume_data' in st.session_state and 'review_data' in st.session_state:
        display_analysis()
    else:
        st.info("Please upload a resume and run the analysis to view results.")

def display_analysis():
    col1, col2, col3 = st.columns([3, 1, 3])
    with col1:
        if st.button("⬅️", use_container_width=True) and st.session_state.current_section > 0:
            st.session_state.current_section -= 1
    with col2:
        page_number = f"{st.session_state.current_section + 1}/{len(st.session_state.sections)}"
        st.button(f"**{page_number}**", use_container_width=True)
    with col3:
        if st.button("➡️", use_container_width=True) and st.session_state.current_section < len(st.session_state.sections) - 1:
            st.session_state.current_section += 1

    current_section = st.session_state.sections[st.session_state.current_section]