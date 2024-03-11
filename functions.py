import streamlit as st


def sidebar():

    if "alt_min" not in st.session_state:
        st.session_state["alt_min"] = 0
    if "alt_max" not in st.session_state:
        st.session_state["alt_max"] = 0
    if "fluid_mass" not in st.session_state:
        st.session_state["fluid_mass"] = 0
    if "conversion_rate" not in st.session_state:
        st.session_state["conversion_rate"] = 0
    if "time_to_empty" not in st.session_state:
        st.session_state["time_to_empty"] = 0
    

    st.session_state["alt_min"] = st.sidebar.slider('Alt min (m)', max_value=1000)
   

    st.session_state["alt_max"] = st.sidebar.slider('Alt max (m)', max_value=1000)

    st.session_state["fluid_mass"] = st.sidebar.number_input('Fluid mass (T)')



