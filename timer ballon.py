import streamlit as st
import requests
from duckduckgo_search import DDGS

# ১. ডিজাইন সেটআপ
st.set_page_config(page_title="Tasnim's AI", layout="centered")

st.markdown("""
    <style>
    .stApp { background: #0e1117; }
    .header-container {
        text-align: center;
        background: rgba(255, 165, 0, 0.1); 
        backdrop-filter: blur(20px);
        padding: 30px; border-radius: 20px;
        border: 1px solid rgba(255, 165, 0, 0.3);
        margin-bottom: 35px;
    }
    .name-title { color: #ffa500; font-size: 30px; font-weight: 800; text-transform: uppercase; margin: 0; }
    .made-by { color: #ffffff; font-size: 15px; opacity: 0.8; margin-top: 10px; }
    [data-testid="stChatMessage"] { background: rgba(255, 255, 255, 0.05) !important; border-radius: 15px !important; }
    header, footer {visibility: hidden;}
    </style>
    
    <div class="header-container">
        <div class="name-title">TASNIM AHMED</div>
        <div class="made-by">আমি তাসনিমের তৈরি এআই চ্যাটবট</div>
    </div>
    """, unsafe_allow_html=True)

# ২. ইন্টারনেট রিসার্চ ফাংশন
def internet_search(query):
    try:
        with DDGS() as ddgs:
            results = [r['body'] for r in ddgs.text(query, max_results=3)]
            return "\n".join(results)
    except:
        return ""

# ৩. এআই প্রসেসিং
API_KEY = "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"

def get_ai_response(history):
    user_input = history[-1]["content"]
    search_data = internet_search(user_input)
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    # প্রফেশনাল ইনস্ট্রাকশন
    system_prompt = f"""
    তুমি তাসনিম আহমেদের তৈরি এআই। তোমার নাম 'Tasnim's AI'। 
    ১. কেউ মেসেজ দিলে শুরুতেই বলবে: 'আসসালামু আলাইকুম! হাই, আমি তাসনিমের তৈরি চ্যাটবট। তোমাকে কীভাবে সাহায্য করতে পারি?'
    ২. এরপর ব্যবহারকারীর প্রশ্নের সঠিক উত্তর দিবে।
    ৩. ইন্টারনেটের লেটেস্ট তথ্য এখানে আছে: {search_data}
    ৪. উল্টাপাল্টা বা অপ্রাসঙ্গিক কথা বলবে না। একদম টু-দ্য-পয়েন্ট এবং প্রফেশনাল উত্তর দিবে।
    ৫. সুন্দর সাবলীল বাংলা ব্যবহার করবে।
    """
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "system", "content": system_prompt}] + history,
        "temperature": 0.5
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=15)
        return response.json()['choices'][0]['message']['content']
    except:
        return "দুঃখিত, আমি এখন উত্তর দিতে পারছি না। আবার চেষ্টা করো।"

# ৪. চ্যাট ইন্টারফেস
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("যেকোনো কিছু জিজ্ঞেস করো..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("রিসার্চ করছি..."):
            response = get_ai_response(st.session_state.messages)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})
