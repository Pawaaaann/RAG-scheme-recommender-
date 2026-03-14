import streamlit as st
import requests
import re
import os

API_URL = os.getenv("SCHEME_ADVISOR_API_URL", "https://rag-scheme-advisor.onrender.com/recommend")

st.set_page_config(
    page_title="AI Government Scheme Advisor",
    page_icon="🇮🇳",
    layout="wide"
)

st.title("🇮🇳 AI Government Scheme Advisor")
st.write("Find the best government schemes based on your profile.")

# -------------------------
# Page Layout
# -------------------------

left, right = st.columns([1,2])

# -------------------------
# LEFT SIDE → USER INPUT
# -------------------------

with left:

    st.subheader("👤 Your Details")

    age = st.number_input("Age", 18, 100, 18)

    income = st.number_input("Annual Income (₹)", 0)

    state = st.selectbox(
        "State",
        [
            "Tamil Nadu",
            "Karnataka",
            "Kerala",
            "Delhi",
            "Maharashtra",
            "Gujarat"
        ]
    )

    occupation = st.selectbox(
        "Occupation",
        [
            "Student",
            "Farmer",
            "Entrepreneur",
            "Worker",
            "Unemployed Youth"
        ]
    )

    question = st.text_input(
        "What schemes do you need?",
        placeholder="education schemes"
    )

    search = st.button("🔍 Find Best Schemes")


# -------------------------
# RIGHT SIDE → RESULTS
# -------------------------

with right:

    st.subheader("📋 Recommended Schemes")

    if search:

        payload = {
            "age": age,
            "income": income,
            "state": state,
            "occupation": occupation,
            "question": question
        }

        response = requests.post(API_URL, json=payload)

        if response.status_code == 200:

            result = response.json()["recommendation"]

            # Split schemes
            schemes = re.split(r"Scheme Name:", result)

            for scheme in schemes[1:]:

                lines = scheme.split("\n")

                name = lines[0].strip()

                text = "\n".join(lines[1:])

                with st.container():

                    st.markdown(
                        f"""
                        ### 🏛 {name}

                        {text}
                        """
                    )

                    st.divider()

        else:
            st.error("Unable to fetch schemes")