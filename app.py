import streamlit as st


url = st.secrets["URL"]
st.components.v1.iframe(url, width=800, height=600)
