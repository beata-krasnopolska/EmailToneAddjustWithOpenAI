import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

template = """
You are an email assistant that helps users improve their emails. 
The user will provide you with an email text, and you will convert it based on the selected tone and dialect.
The tone can be Formal, Informal, Friendly, or Professional.

Below is the email tone and dialect options:
Tone: {tone}
Dialect: {dialect}
Here is the email text:{email_text}

Please convert the email according to the specified tone and dialect, ensuring that the meaning of the original email is preserved while enhancing its style and clarity.
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email_text"],
    template=template,
)

def load_llm():
    load_dotenv()

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    return llm

llm = load_llm()


st.set_page_config(page_title="Globalize email", page_icon=":robot:")
st.header("Globalize text")

col1, col2 = st.columns(2)

with col1:
    st.markdown("Possibility to improve an email by converting it with help of AI agents (powered by lanhchain and OpenAI)")
    
with col2:
    st.image(image="https://via.placeholder.com/150", width=500, caption="Example of an email")

st.markdown("### Enter your email to convert:")

col1, col2 = st.columns(2)

with col1:
    option_tone = st.selectbox(
        "Select the tone of the email:", ["Formal", "Informal", "Friendly", "Professional"])
    
with col2:
    option_dialect = st.selectbox(
        'What dialect do you want to use?', ['American English', 'British English', 'Australian English']
    )

def get_email_text():
    input_raw_text = st.text_area(label="", placeholder="Email text here...", key="email_input")
    return input_raw_text

email_input = get_email_text()

st.markdown("### Converted email:")

if email_input:
    response = llm.invoke(
        prompt.format(
            tone=option_tone,
            dialect=option_dialect,
            email_text=email_input,
        )
    )

    st.write(response.text)