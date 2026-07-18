import streamlit as st
import os
from datetime import datetime

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Video Cloner Dashboard")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🎬 Videos Created",
        value="0"
    )

with col2:
    st.metric(
        label="📥 Downloads",
        value="0"
    )

with col3:
    st.metric(
        label="🗂 Projects",
        value="0"
    )

st.markdown("---")

st.subheader("Recent Activity")

st.info("No project created yet.")

st.markdown("---")

st.subheader("System Information")

st.write(f"Current Time : {datetime.now()}")

folders = [
    "outputs",
    "uploads",
    "temp"
]

for folder in folders:

    if not os.path.exists(folder):
        os.makedirs(folder)

st.success("System Ready ✅")

st.markdown("---")

if st.button("Refresh Dashboard"):
    st.rerun()
