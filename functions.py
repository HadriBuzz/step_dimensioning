import streamlit as st


def sidebar():
    if "alt_min" not in st.session_state:
        st.session_state["alt_min"] = 0

    st.session_state["alt_min"] = st.sidebar.number_input('Alt min')