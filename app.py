import streamlit as st
from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent,Task
from lyzr_automata.pipelines.linear_sync_pipeline import LinearSyncPipeline
from PIL import Image
import os

# Set the OpenAI API key
os.environ["OPENAI_API_KEY"] = st.secrets["apikey"]

st.set_page_config(
    page_title="Idea Generator Agent",
    layout="centered",  # or "wide"
    initial_sidebar_state="auto",
    page_icon="./logo/lyzr-logo-cut.png",
)

st.markdown(
    """
    <style>
    .app-header { visibility: hidden; }
    .css-18e3th9 { padding-top: 0; padding-bottom: 0; }
    .css-1d391kg { padding-top: 1rem; padding-right: 1rem; padding-bottom: 1rem; padding-left: 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

image = Image.open("./logo/lyzr-logo.png")
st.image(image, width=150)

# App title and introduction
st.title("Idea Generator")
st.markdown("### Welcome to the Lyzr Idea Generator!")
st.markdown("Enter relevant information or keywords to generate ideas.")

open_ai_text_completion_model = OpenAIModel(
    api_key=st.secrets["apikey"],
    parameters={
        "model": "gpt-4-turbo-preview",
        "temperature": 0.2,
        "max_tokens": 1500,
    },
)
idea = st.text_input("Enter here")

idea_generator = Agent(
    role='Expert Idea Generator',
    prompt_persona=f'You are an Expert IDEATION CONSULTANT. Your task is to generate relevant ideas based on the given {idea}.'
)

task1 = Task(
			name="Generate Ideas",
			model=open_ai_text_completion_model,
			agent=idea_generator,
			instructions=f"""
 Your task is to GENERATE CREATIVE and RELEVANT responses for a given {idea}.

Adhere to this step-by-step guide to ensure you deliver EXCELLENT RESULTS:

1. CAREFULLY READ and COMPREHEND the provided {idea} to FULLY UNDERSTAND its ESSENCE.

2. ANALYZE the CONTEXT of the given {idea}, ensuring your responses are TAILORED and FUNCTIONAL for the user's specific needs.

3. BRAINSTORM a LIST of 5-10 ORIGINAL and APPLICABLE ideas that are in harmony with the given {idea}. Present these ideas PROMINENTLY as a LIST, with BRIEF yet INFORMATIVE descriptions of 1-2 sentences for each.

4. ENSURE that your list of brainstormed ideas is the FOCAL POINT of your response.

5. WRITE with CLARITY and CONCISENESS to maintain the reader's ENGAGEMENT and INTEREST throughout your response.

""",
	)

if st.button("Generate"):
    output = LinearSyncPipeline(
        name="Idea Generation Pipeline",
        completion_message="pipeline completed",
        tasks=[task1],
    ).run()

    
    st.markdown(output[0]['task_output'])
# Footer or any additional information
with st.expander("ℹ️ - About this App"):
    st.markdown(
        """Experience the seamless integration of Lyzr'Automata. For any inquiries or issues, please contact Lyzr."""
    )
    st.link_button("Lyzr", url="https://www.lyzr.ai/", use_container_width=True)
    st.link_button(
        "Book a Demo", url="https://www.lyzr.ai/book-demo/", use_container_width=True
    )
    st.link_button(
        "Discord", url="https://discord.gg/nm7zSyEFA2", use_container_width=True
    )
    st.link_button(
        "Slack",
        url="https://join.slack.com/t/genaiforenterprise/shared_invite/zt-2a7fr38f7-_QDOY1W1WSlSiYNAEncLGw",
        use_container_width=True,
    )