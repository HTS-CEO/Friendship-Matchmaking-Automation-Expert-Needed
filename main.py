import streamlit as st
import pandas as pd
import random

questions = [
    "Do you prefer indoor or outdoor activities?",
    "Are you a morning person or night owl?",
    "Do you enjoy reading books?",
    "Do you like traveling?",
    "Are you more introverted or extroverted?"
]

options = {
    "Do you prefer indoor or outdoor activities?": ["Indoor", "Outdoor"],
    "Are you a morning person or night owl?": ["Morning", "Night"],
    "Do you enjoy reading books?": ["Yes", "No"],
    "Do you like traveling?": ["Yes", "No"],
    "Are you more introverted or extroverted?": ["Introverted", "Extroverted"]
}

answer_scores = {
    "Indoor": 1, "Outdoor": 2,
    "Morning": 1, "Night": 2,
    "Yes": 2, "No": 1,
    "Introverted": 1, "Extroverted": 2
}

st.title("Friendship Matchmaking System")

st.header("Fill out the questionnaire")
user_name = st.text_input("Enter your name:")

responses = {}
for q in questions:
    responses[q] = st.radio(q, options[q])

if st.button("Submit"):
    user_score = sum(answer_scores[responses[q]] for q in questions)
    
    existing_users = pd.DataFrame({
        "Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Score": [random.randint(5, 10) for _ in range(5)]
    })
    
    new_user = pd.DataFrame({"Name": [user_name], "Score": [user_score]})
    all_users = pd.concat([existing_users, new_user], ignore_index=True)

    matches = all_users[(all_users["Score"] >= user_score - 5) & (all_users["Score"] <= user_score + 5)]
    
    st.subheader("Your Matches:")
    st.write(matches)
    
    if len(matches) > 1:
        match_name = matches[matches["Name"] != user_name].iloc[0]["Name"]
        email_content = f"""
        Subject: Meet Your New Friend - {match_name}!
        
        Hi {user_name},
        
        We've found a great match for you! Based on your responses, {match_name} shares similar interests. 
        
        Feel free to reach out and start a conversation!
        
        Best,  
        Friendship Matching Team
        """
        st.subheader("Sample Email:")
        st.code(email_content)

