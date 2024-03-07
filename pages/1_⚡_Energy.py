import streamlit as st

st.set_page_config(page_title="Energy wise", page_icon="⚡")

st.title("Energy oriented page")

alt_min = st.session_state["alt_min"]

st.write("Alt min:")
st.write(alt_min)
