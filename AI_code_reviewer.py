import streamlit as st
import google.generativeai as genai

# Open and read the API key from a file

# Maka a folder ex. Gemini AP key and inside that create a txt file paste your API key inside it

f = open("Gemini AP key/key.txt")
key = f.read()

f.close()  

#or
# You can directly paste your Api key inside the genai.configure , replace key with your api key

# genai.configure(api_key="Paste your Api Key")


genai.configure(api_key=key)

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
       font-size: 28px;
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
    .stTextArea textarea:focus {
        border-color: #4CAF50;
    }
    .stAlert {
        background-color: #e6f7ff;
        color: #1e3a8a;
    }
    .stMarkdown h2 {
        color: #2e8b57;
    }
    .response-box {
        background-color: #f3ff3;
        border-radius: 8px;
        border: 1px solid #ddd;
        padding: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .spinner {
        text-align: center;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Title and description
st.title("AI 🐍 CODE REVIEWER")
st.markdown("""
Submit your <span style='color:green; font-weight:bold;'>Python</span> code for an AI-powered review using Google's Gemini AI. 
Get feedback on potential bugs, improvements, and see suggested fixes.
""", unsafe_allow_html=True)

# Dropdown for model selection
model_options = {
    "Gemini-1.5-Flash": "gemini-1.5-flash",
    "Gemini-pro": "gemini-pro"
}
selected_model = st.selectbox("Choose AI Model for Review", list(model_options.keys()))

st.subheader("Enter Your Code", divider="blue")

user_prompt = st.text_area("Paste your code here")

if st.button("Review code"):
    if user_prompt:
        with st.spinner(f"Reviewing your code using {selected_model}... Please wait. 🕑"):
            try:
                # Initialize the selected model
                model = genai.GenerativeModel(model_options[selected_model])
                chat = model.start_chat(history=[])

                # Send code to the model for review
                response = chat.send_message(
                    f"Please review the following Python code for errors or improvements:\n\n{user_prompt}\n\nProvide feedback and suggest fixes if necessary."
                )

                # Display the response from the selected AI model
                st.markdown("<h2 style='color: green;'>Corrected Code and Review:</h2>", unsafe_allow_html=True)
                st.markdown(f"<div class='response-box'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.error("Please enter some code to review.")
