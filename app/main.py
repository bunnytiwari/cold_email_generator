# import streamlit as st
# from langchain_community.document_loaders import WebBaseLoader
# import base64
# from chains import Chain
# from utils import clean_text


# def add_background_image(image_path):
#     with open(image_path, "rb") as image_file:
#         encoded_image = base64.b64encode(image_file.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/png;base64,{encoded_image}");
#             background-size: cover;
#             background-position: center;
#         }}
#         </style>
#         """,
#         unsafe_allow_html=True
#     )



# def create_streamlit_app(llm, portfolio, clean_text):
#     st.title("📧 Cold Mail Generator")
#     url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-42819?from=job%20search%20funnel")
#     submit_button = st.button("Submit")

#     if submit_button:
#         try:
#             loader = WebBaseLoader([url_input])
#             data = clean_text(loader.load().pop().page_content)
#             portfolio.load_portfolio()
#             jobs = llm.extract_jobs(data)
#             for job in jobs:
#                 skills = job.get('skills', [])
#                 links = portfolio.query_links(skills)
#                 email = llm.write_mail(job, links)
#                 st.code(email, language='markdown')
#         except Exception as e:
#             st.error(f"An Error Occurred: {e}")


# if __name__ == "__main__":
#     chain = Chain()
#     st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
#     # Add background image (replace with your image URL)
#     add_background_image(r"C:\Users\shrad\Downloads\project-genai-cold-email-generator-main\(new)project-genai-cold-email-generator-main - Copy\app\background_2.png")

#     create_streamlit_app(chain,portfolio,clean_text)

import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
import base64
from chains import Chain
from utils import clean_text

def add_background_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_image}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def create_streamlit_app(llm, clean_text):
    st.title("📧 Cold Mail Generator")
    url_input = st.text_input("Enter a URL:", value="https://jobs.nike.com/job/R-42819?from=job%20search%20funnel")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            jobs = llm.extract_jobs(data)
            for job in jobs:
                email = llm.write_mail(job)
                st.code(email, language='markdown')
        except Exception as e:
            st.error(f"An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    # Add background image (replace with your image URL)
    add_background_image(r"C:\Users\shrad\Downloads\project-genai-cold-email-generator-main\(new)project-genai-cold-email-generator-main - Copy\app\background_2.png")

    create_streamlit_app(chain, clean_text)


