import streamlit as st
from functions import sidebar
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(
    layout="wide",
    page_title="Settings",
    page_icon="⚙️",
)

sidebar()

st.title("STEP dimensioning")

st.write("-----")

elevation = st.session_state['alt_max'] - st.session_state['alt_min']

st.write(f"Elevation: {elevation} m.")

conv_rate = st.session_state['conversion_rate']
available_energy = (elevation * st.session_state['fluid_mass'] * 9810)*conv_rate/100

st.write(f"Available/Potential Energy: {available_energy} J or {available_energy / 3600} Wh or {available_energy / 3600000} kWh")

time_to_empty = st.session_state['time_to_empty']
st.write(f"Averaged available power: {available_energy / (time_to_empty*3600)} W.")

st.write("-----")

def energy_function(x):
    return x ** 2

x = np.linspace(-5, 5, 1000)
y = energy_function(x)
data = []

fig, x = plt.subplots()
plt.plot(y)
st.pyplot(fig)