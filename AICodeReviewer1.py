import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="")

# Styling
st.markdown(
    """
    <style>
    body {
        background-color: #8cc6f9;
        font-family: 'Arial', sans-serif;
        text-transform: capitalize;
    }
    .stButton>button {
        border-radius: 4px;
        background-color: #f4511e;
        border: none;
        color: #FFFFFF;
        text-align: center;
        font-size: 20px;
        padding: 10px;
        width: 200px;
        transition: all 0.5s;
        cursor: pointer;
        margin: 2px;
    }
    .stButton>button:hover {
        background-color: blue;
        color: #FFFFFF;
    }
    .stTextArea>textarea {
        background-color: #f8f8f8;
        border: 1px solid #dcdcdc;
        padding: 15px;
        font-size: 14px;
        width: 100%;
        height: 250px;
    }
    .stAlert {
        background-color: #e6f7ff;
        color: #1e3a8a;
    }
    .stMarkdown h2 {
        color: #2e8b57;
    }
    .response-box {
        background-color: grey;
        border-radius: 8px;
        border: 1px solid #ddd;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        white-space: pre-wrap;
    }
    .spinner {
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')
chat = model.start_chat(history=[])

# UI Title and Instructions
st.title("AI 🐍 SQL & Python Reviewer")
st.markdown("""
Submit your <span style='color:green; font-weight:bold;'>Python</span> or <span style='color:blue; font-weight:bold;'>SQL</span> code/query for review or answers.
""", unsafe_allow_html=True)

st.subheader("Choose Your Input", divider="blue")

# Language selection
language = st.selectbox("Select Language", ("Python", "SQL", "Excel"))

# User input
user_input = st.text_area(f"Enter your {language} code or question here")

# Submit button
if st.button("Submit"):
    if user_input.strip():
        with st.spinner("Processing your request..."):
            try:
                # Generate the appropriate prompt
                if language == "Python":
                    prompt = f"""
You're an expert Python reviewer. If the input is code, review it for bugs and suggest improvements. 
If it's a question, to write a code, give simpliest code with different approch.
when function not required dont use. 

Input:
{user_input}
"""
                elif language == "SQL":
                    prompt = f"""
You're an expert in SQL. If the input is a SQL query, review it and suggest improvements or fixes.
If it's a SQL-related question, provide SQL Query with different approchs.

Input:
{user_input}
"""
                    
                elif language == "Excel":
                    prompt = f"""
You're an Excel Expert with 10 years of experience, if the input is Excel formula, review it and suggest improvements or fixes.
if it's a Excel question , provide a Excel Formulas with different apporchs or direct methods.


Input:
{user_input}
"""    


                # Send prompt to Gemini
                response = chat.send_message(prompt)

                # Display result
                st.markdown("<h2 style='color: green;'>Result:</h2>", unsafe_allow_html=True)
                st.markdown(f"<div class='response-box'>{response.text}</div>", unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter a code snippet or a question to continue.")
