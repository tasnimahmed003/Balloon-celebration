import streamlit as st
import requests
from duckduckgo_search import DDGS

# ১. ক্লিন ও প্রফেশনাল ডিজাইন
st.set_page_config(page_title="Tasnim's AI", layout="centered")

st.markdown("""
    <style>
    .stApp { background: #0e1117; }
    
    /* হেডার সেকশন */
    .header-container {
        text-align: center;
        background: rgba(255, 165, 0, 0.08); 
        backdrop-filter: blur(20px);
        padding: 35px; 
        border-radius: 20px;
        border: 1px solid rgba(255, 165, 0, 0.2);
        margin-bottom: 40px;
    }
    
    .name-title { 
        color: #ffa500; 
        font-size: 32px; 
        font-weight: 800; 
        text-transform: uppercase; 
        margin: 0; 
        letter-spacing: 2px;
    }
    
    .made-by { 
        color: #ffffff; 
        font-size: 16px; 
        opacity: 0.9; 
        margin-top: 10px;
    }

    /* চ্যাট বাবল ডিজাইন */
    [data-testid="stChatMessage"] { 
        background: rgba(255, 255, 255, 0.04) !important; 
        border-radius: 15px !important; 
        border: 1px solid rgba(255, 165, 0, 0.1) !important;
    }
    
    header, footer {visibility: hidden;}
    </style>
    
    <div class="header-container">
        <div class="name-title">TASNIM AHMED</div>
        <div class="made-by">আমি তাসনিমের তৈরি এআই চ্যাটবট</div>
    </div>
    """, unsafe_allow_html=True)

# ২. রিসার্চ ফাংশন (পর্দার আড়ালে কাজ করবে)
def internet_research(query):
    try:
        with DDGS() as ddgs:
            results = [r['body'] for r in ddgs.text(query, max_results=3)]
            return "\n".join(results)
    except:
        return ""

# ৩. এআই ইঞ্জিন
API_KEY = "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"

def get_ai_response(history):
    user_input = history[-1]["content"]
    search_context = internet_research(user_input)
    
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    
    system_prompt = f"""
    তুমি তাসনিম আহমেদের তৈরি এআই।
    ১. প্রতিবার উত্তরের শুরুতে বলবে: 'আসসালামু আলাইকুম! হাই, আমি তাসনিমের তৈরি চ্যাটবট। তোমাকে কীভাবে সাহায্য করতে পারি?'
    ২. এরপর অত্যন্ত বুদ্ধিমত্তার সাথে সরাসরি প্রশ্নের উত্তর দিবে।
    ৩. তোমার কাছে থাকা এই ইন্টারনেট তথ্য ব্যবহার করো: {search_context}
    ৪. কোনো বাড়তি কথা বা অপ্রাসঙ্গিক কথা বলবে না। 
    ৫. একদম মানুষের মতো স্বাভাবিক ও প্রফেশনাল বাংলা ব্যবহার করো।
    """
    
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [{"role": "system", "content": system_prompt}] + history,
        "temperature": 0.4 
    }
    
    try:
        response = requests.post(url, headers=headers, json=data, timeout=20)
        return response.json()['choices'][0]['message']['content']
    except:
        return "দুঃখিত, আমি এখন উত্তর দিতে পারছি না। আবার চেষ্টা করো।"

# ৪. চ্যাট ইন্টারফেস
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ৫. চ্যাট বক্সের টেক্সট এখন ক্লিন (Message Tasnim AI)
if prompt := st.chat_input("Message Tasnim AI"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        response = get_ai_response(st.session_state.messages)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
