import streamlit as st
import time

# পেজের টাইটেল এবং ডিজাইন
st.set_page_config(page_title="Tasnim's Surprise", page_icon="🎈")

st.title("🎈 Tasnim's Special Python Project")
st.write("Enter the time and watch the magic happen!")

# ইউজার থেকে ইনপুট নেওয়া
seconds = st.number_input("Enter seconds (e.g., 20):", min_value=1, value=20)

if st.button("Start Celebration"):
    st.write(f"Wait for it... The celebration will last for {seconds} seconds!")

    # ২০ সেকেন্ড (বা তোমার দেওয়া সময়) ধরে বেলুন ওড়ানোর লজিক
    start_time = time.time()
    while time.time() - start_time < seconds:
        st.balloons() # এই কমান্ডটি স্ক্রিনে বেলুন ওড়াবে
        time.sleep(1) # প্রতি ১ সেকেন্ড পরপর নতুন করে বেলুন উড়বে

    st.success("Hope you enjoyed the celebration! 🎈")
