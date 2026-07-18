import streamlit as st
import os

st.set_page_config(
    page_title="Settings",
    page_icon="⚙️",
    layout="wide"
)

st.title("⚙️ Settings")

st.markdown("---")

st.subheader("AI Settings")

gemini_key = st.text_input(
    "Gemini API Key",
    type="password"
)

language = st.selectbox(
    "Default Language",
    [
        "Hindi",
        "English"
    ]
)

voice = st.selectbox(
    "AI Voice",
    [
        "Female",
        "Male"
    ]
)

quality = st.selectbox(
    "Video Quality",
    [
        "720p",
        "1080p"
    ]
)

st.markdown("---")

if st.button("Save Settings", use_container_width=True):

    with open(".env", "w", encoding="utf-8") as f:
        f.write(f"GEMINI_API_KEY={gemini_key}\n")

    st.success("Settings Saved Successfully ✅")

st.markdown("---")

if os.path.exists(".env"):
    st
