import streamlit as st
import time

# 1. Page Setup
st.set_page_config(page_title="Tasnim's Portfolio", page_icon="🎈", layout="wide")

# 2. Name and Identity
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>MD TASNIM</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 20px;'>Student of Computer Science and Technology</p>", unsafe_allow_html=True)

# 3. Profile Picture Section (Tomar chobir name boshiye dewa hoyeche)
col1, col2, col3 = st.columns([1, 1.5, 1])
with col2:
    try:
        # Ekhane tumi je name-ti diyechile sheta boshiye dewa holo
        st.image("PhotoRoom-20250120_181402-03-01.jpg", width=350, caption="Develop By Tasnim", use_container_width=True)
    except:
        st.info("GitHub-e chobi-ti (PhotoRoom-20250120_181402-03-01.jpg) upload korun.")

st.write("---")

# 4. Multi-Celebration Timer
st.subheader("🎉 Multi-Celebration Magic (Balloons + Snow)")
seconds = st.number_input("Koto second celebration cholbe?", min_value=1, max_value=60, value=20)

# 5. Celebration Logic
if st.button("Start Grand Celebration 🚀"):
    st.balloons()
    st.success(f"Celebration shuru hoyeche! It will last for {seconds} seconds.")
    
    start_time = time.time()
    while time.time() - start_time < seconds:
        st.balloons() # Balloon urbe
        st.snow()     # Tusharpat hobe
        time.sleep(1)
    
    st.balloons()
    st.write("Magic shesh! Dhonnobad.")
