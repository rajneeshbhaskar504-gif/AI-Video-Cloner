import streamlit as st
import os
from datetime import datetime

st.set_page_config(
    page_title="History",
    page_icon="📜",
    layout="wide"
)

st.title("📜 Video History")

st.markdown("---")

history_folder = "outputs"

if not os.path.exists(history_folder):
    os.makedirs(history_folder)

files = sorted(
    os.listdir(history_folder),
    reverse=True
)

if len(files) == 0:
    st.info("No videos found.")
else:

    for file in files:

        path = os.path.join(history_folder, file)

        size = round(
            os.path.getsize(path) / 1024 / 1024,
            2
        )

        created = datetime.fromtimestamp(
            os.path.getctime(path)
        )

        with st.expander(file):

            st.write(f"📅 Created : {created}")
            st.write(f"📦 Size : {size} MB")

            with open(path, "rb") as f:

                st.download_button(
                    "⬇ Download",
                    f,
                    file_name=file,
                    use_container_width=True
                )

st.markdown("---")

if st.button("Refresh History"):
    st.rerun()
