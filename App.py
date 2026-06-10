import streamlit as st
import joblib

# Load model
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

emotion_map = {
    0: ("😢", "Sadness"),
    1: ("😡", "Anger"),
    2: ("❤️", "Love"),
    3: ("😲", "Surprise"),
    4: ("😨", "Fear"),
    5: ("😊", "Joy")
}

st.set_page_config(
    page_title="Emotion Detection AI",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.main {
    background-color: #0E1117;
}

.title {
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:white;
}

.subtitle {
    text-align:center;
    color:#A0A0A0;
    margin-bottom:30px;
}

.result-card {
    padding:20px;
    border-radius:15px;
    background:#1E1E1E;
    text-align:center;
    border:1px solid #333;
}

.big-emoji {
    font-size:70px;
}

.emotion-text {
    font-size:28px;
    font-weight:bold;
    color:#00FFAA;
}
</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="title">🧠 Emotion Detection AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict emotions from text using Machine Learning & NLP</div>',
    unsafe_allow_html=True
)

user_text = st.text_area(
    "✍️ Enter your text",
    height=150,
    placeholder="Example: I am feeling very happy today..."
)

if st.button("🔍 Analyze Emotion", use_container_width=True):

    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:

        transformed_text = vectorizer.transform([user_text])

        prediction = model.predict(transformed_text)[0]

        emoji, emotion = emotion_map[prediction]

        st.markdown(
            f"""
            <div class="result-card">
                <div class="big-emoji">{emoji}</div>
                <div class="emotion-text">{emotion}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        try:
            confidence = max(
                model.predict_proba(transformed_text)[0]
            ) * 100

            st.write("")
            st.progress(int(confidence))
            st.success(
                f"Confidence Score: {confidence:.2f}%"
            )

        except:
            pass

st.write("---")
st.caption(
    "Built by Vinay Kumar | Streamlit • Scikit-Learn • NLP"
)