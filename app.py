import streamlit as st
from utils.editor import VideoEditor

st.set_page_config(
    page_title="AI Social Media Video Creator",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Social Media Video Creator")
st.write("किसी विषय पर नया, मौलिक वीडियो बनाने के लिए विषय लिखें।")

topic = st.text_input("Video Topic")

if st.button("Generate Video"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")
        st.stop()

    editor = VideoEditor()

    with st.spinner("Generating Script..."):
        result = editor.create_video(topic)

    st.success("Video Generated Successfully")

    st.subheader("Script")
    st.write(result["script"])

    st.subheader("Audio")
    st.audio(result["audio"])

    st.subheader("Final Video")

    with open(result["video"], "rb") as f:
        st.video(f.read())

    with open(result["video"], "rb") as f:
        st.download_button(
            "Download Video",
            data=f,
            file_name="final_video.mp4",
            mime="video/mp4"
        )
