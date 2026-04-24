import difflib

def get_chatbot_response():
    # FAQ ডাটাবেস: এখানে বাংলা এবং ইংরেজি উভয় ভার্সন রাখা হয়েছে
    faq_database = {
        # Greetings - English
        "hi": "Hello! How can I assist you?",
        "hello": "Hi there! What can I do for you?",
        "how are you": "I am a bot, but I am doing great! How about you?",
        "who created you": "I was created using Python programming.",
        
        # Greetings - Bangla
        "হাই": "হ্যালো! আমি আপনাকে কীভাবে সাহায্য করতে পারি?",
        "কেমন আছো": "আমি ভালো আছি, আপনি কেমন আছেন?",
        "তোমার নাম কি": "আমি একটি পাইথন চ্যাটবট।",
        "কে তোমাকে বানিয়েছে": "আমাকে পাইথন প্রোগ্রামিং দিয়ে তৈরি করা হয়েছে।",

        # Programming & Tech - English
        "what is python": "Python is a versatile and easy-to-learn programming language.",
        "what is a variable": "A variable is a container for storing data values.",
        "what is html": "HTML is the standard markup language for creating web pages.",
        
        # Programming & Tech - Bangla
        "পাইথন কি": "পাইথন একটি বহুমুখী এবং সহজে শেখা যায় এমন প্রোগ্রামিং ল্যাঙ্গুয়েজ।",
        "ভ্যারিয়েবল কি": "ভ্যারিয়েবল হলো ডেটা জমা রাখার একটি পাত্র বা কন্টেইনার।",
        "কম্পিউটার কি": "কম্পিউটার একটি ইলেকট্রনিক যন্ত্র যা তথ্য প্রক্রিয়াকরণ করে।",

        # General Knowledge - English
        "capital of bangladesh": "The capital of Bangladesh is Dhaka.",
        "largest river in bangladesh": "The Padma, Meghna, and Jamuna are the major rivers.",
        
        # General Knowledge - Bangla
        "বাংলাদেশের রাজধানী কি": "বাংলাদেশের রাজধানী হলো ঢাকা।",
        "সূর্য কোন দিকে ওঠে": "সূর্য পূর্ব দিকে ওঠে।",
        
        # Add more up to 500 in this pattern...
    }

    print("--- Multi-Language FAQ Bot ---")
    print("Type your question (English or Bangla). Type 'exit' to stop.")

    while True:
        user_input = input("\nYou: ").strip().lower()

        if user_input == 'exit' or user_input == 'বন্ধ':
            print("Chatbot: Goodbye! / বিদায়!")
            break

        # প্রশ্নের মিল খোঁজা (Similarity Check)
        questions = list(faq_database.keys())
        matches = difflib.get_close_matches(user_input, questions, n=1, cutoff=0.4)

        if matches:
            best_match = matches[0]
            print(f"Chatbot: {faq_database[best_match]}")
        else:
            # যদি উত্তর না পাওয়া যায়
            print("Chatbot: Sorry, I don't know the answer to that. / দুঃখিত, আমি এর উত্তর জানি না।")

if __name__ == "__main__":
    get_chatbot_response()
