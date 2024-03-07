import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Home",
    page_icon="👋",
)

st.title("STEP dimensioning")

if "alt_min" not in st.session_state:
    st.session_state["alt_min"] = 0
st.number_input("Min altitude", value=st.session_state["alt_min"], key="alt_min")

st.write(st.session_state["alt_min"])
