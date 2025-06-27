import streamlit as st
import pandas as pd
from pathlib import Path

# Set page config
st.set_page_config(page_title="Smart Wireless Earbuds ", layout="wide")

# =============================================
# BACKGROUND VIDEO SECTION
# =============================================

# Video HTML/CSS (place at the beginning to load first)
video_html = """
<style>
#background-video 
{
    position: fixed;
    right: 0;
    bottom: 0;
    min-width: 100%; 
    min-height: 100%;
    width: auto;
    height: auto;
    z-index: -100;
    background-size: cover;
    opacity: 0.3;  /* Adjust transparency */
}

.content {
    position: relative;
    z-index: 1;
    background-color: rgba(0,0,0,0.7);  /* Semi-transparent overlay */
    padding: 2rem;
    border-radius: 10px;
}
</style>

<video autoplay muted loop id="background-video">
    <source src="ear.mp4" type="video/mp4">
</video>
"""

st.markdown(video_html, unsafe_allow_html=True)
# =============================================

# Main content wrapped in a div with our content class
st.markdown('<div class="content">', unsafe_allow_html=True)

# Dashboard Title
st.title("🎧 Smart Wireless Earbuds Specifications Dashboard")
st.write("Collect and analyze specifications and features of smart wireless earbuds.")
st.markdown("---")

# =============================================
# YOUR EXISTING DASHBOARD CODE
# =============================================
# Data Collection Section
st.header("📋 Enter Earbuds Specifications")
with st.form(key='specs_form'):
    connectivity_technology = st.text_input("**Connectivity Technology**", "Wireless")
    wireless_communication_technology = st.text_input("**Wireless Communication Technology**", "Bluetooth")
    
    charging_time = st.slider("**Charging Time (Minutes)**", min_value=0, max_value=180, value=90)
    water_resistance_level = st.text_input("**Water Resistance Level**", "Water Resistant")
    controller_type = st.text_input("**Controller Type**", "Google Assistant, Siri")
    
    battery_life = st.slider("**Battery Life (Hours)**", min_value=0, max_value=100, value=50)
    bluetooth_range = st.slider("**Bluetooth Range (Metres)**", min_value=0, max_value=100, value=10)
    audio_latency = st.slider("**Audio Latency (Milliseconds)**", min_value=0, max_value=200, value=50)
    audio_driver_size = st.slider("**Audio Driver Size (Millimetres)**", min_value=0, max_value=20, value=12)
    
    noise_cancellation = st.selectbox("**Noise Cancellation**", ["Yes", "No"])
    country_of_origin = st.text_input("**Country of Origin**", "")
    
    submit_button = st.form_submit_button(label='Submit Specifications')
# =============================================

if submit_button:
    specs_data = {
        "Connectivity Technology": [connectivity_technology],
        "Wireless Communication Technology": [wireless_communication_technology],
        "Charging Time (Minutes)": [charging_time],
        "Water Resistance Level": [water_resistance_level],
        "Controller Type": [controller_type],
        "Battery Life (Hours)": [battery_life],
        "Bluetooth Range (Metres)": [bluetooth_range],
        "Audio Latency (Milliseconds)": [audio_latency],
        "Audio Driver Size (Millimetres)": [audio_driver_size],
        "Noise Cancellation": [noise_cancellation],
        "Country of Origin": [country_of_origin]
    }
    
    df = pd.DataFrame(specs_data)
    st.success("Specifications Submitted Successfully! 🎉")

    # Score calculation logic
    max_score = 10
    battery_score = (battery_life / 50) * 3
    bluetooth_score = (bluetooth_range / 100) * 3
    latency_score = ((200 - audio_latency) / 200) * 2
    driver_score = (audio_driver_size / 20) * 2
    noise_cancellation_score = 1 if noise_cancellation == "Yes" else 0

    health_score = min(battery_score + bluetooth_score + latency_score + driver_score + noise_cancellation_score, max_score)
    progress_value = health_score / max_score

    st.dataframe(df)
    st.progress(progress_value)
    st.subheader(f"🌟 Health Score: {health_score:.2f}/{max_score}")

# Close the content div
st.markdown('</div>', unsafe_allow_html=True)

