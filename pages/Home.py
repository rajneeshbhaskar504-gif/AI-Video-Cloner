import streamlit as st

st.set_page_config(
    page_title="AI Video Cloner",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Social Media Video Cloner")

st.markdown("---")

topic = st.text_input(
    "Enter Video Topic",
    placeholder="Example: Chandrayaan 3 Explained"
)

style = st.selectbox(
    "Video Style",
    [
        "Movie Explain",
        "Documentary",
        "News",
        "Story",
        "Education"
    ]
)

duration = st.slider(
    "Video Duration (Minutes)",
    1,
    20,
    5
)

if st.button("Generate AI Video", use_container_width=True):

    st.success("Request Submitted Successfully")

    st.write("### Topic")
    st.write(topic)

    st.write("### Style")
    st.write(style)

    st.write("### Duration")
    st.write(f"{duration} Minutes")
