import streamlit as st
from functions import sidebar

st.set_page_config(
    layout="wide",
    page_title="Settings",
    page_icon="⚙️",
)
sidebar()
st.title("STEP dimensioning")


st.number_input("Min altitude", value=st.session_state["alt_min"], key="alt_min")

st.write(st.session_state["alt_min"])
