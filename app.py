import streamlit as st

st.set_page_config(
    page_title="AI Video Cloner",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Social Media Video Cloner")
st.write("वीडियो का लिंक पेस्ट करें और AI नया ओरिजिनल वीडियो बनाने में मदद करेगा।")

video_url = st.text_input(
    "YouTube / Instagram / Facebook Video URL"
)

if st.button("Analyze Video"):
    if video_url:
        st.success("✅ Video URL प्राप्त हो गया।")
        st.write("URL:", video_url)
    else:
        st.error("❌ पहले वीडियो का लिंक डालें।")
