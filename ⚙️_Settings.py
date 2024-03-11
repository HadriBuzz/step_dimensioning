import streamlit as st
from functions import sidebar

st.set_page_config(
    layout="wide",
    page_title="Settings",
    page_icon="⚙️",
)

sidebar()

st.title("STEP dimensioning")

elevation = st.session_state['alt_max'] - st.session_state['alt_min']

st.write(f"Elevation: {elevation} m.")

available_energy = elevation * st.session_state['fluid_mass'] * 9.81

st.write(f"Potential Energy: {available_energy} J.")

st.write(f"Available Energy: {available_energy / 3600} Wh or {available_energy / 3600000} kWh")
