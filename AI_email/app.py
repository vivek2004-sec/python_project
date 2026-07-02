import streamlit as st
import ollama

st.set_page_config(
    page_title='Local AI Email Assistant',
    page_icon="✉️",
    layout="centered"
)

st.title("✉️ Local AI Email Responder")

tone = st.selectbox(
    "Select Email Tone",
    ["Professional", "Friendly", "Apologetic", "Direct"]
)

user_input = st.text_area(
    "Enter your rough notes here:",
    height=150
)

if st.button("Generate Professional Email"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Drafting your Email..."):
            system_prompt = f"""
            You are an expert corporate communicator.
            Rewrite the notes into a well-structured email.
            Tone: {tone}.
            No explanations, just the email.
            """
            try:                                          # ✅ inside with block
                response = ollama.chat(                  # ✅ fixed typo resposne → response
                    model="llama3",
                    messages=[
                        {
                            "role": "system",
                            "content": system_prompt
                        },
                        {
                            "role": "user",
                            "content": user_input
                        }
                    ]
                )
                st.info(response["message"]["content"])  # ✅ fixed typo
            except Exception as e:
                st.error(f"Error: {e}. Is Ollama running?")  # ✅ fixed "Ia" → "Is"