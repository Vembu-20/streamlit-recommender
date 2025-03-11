import streamlit as st
import json

# Load recommendations from JSON file
def load_recommendations():
    with open("recommendations.json", "r") as f:
        return json.load(f)

# Streamlit UI
st.set_page_config(page_title="AI-Powered Recommendations", page_icon="🍽️", layout="centered")

st.title("🍽️ AI-Powered Food Recommendations")
st.write("Discover trending dishes based on popularity & ratings!")

# Load recommendations
recommendations = load_recommendations()

# Display recommendations as a table
st.subheader("📌 Top Recommended Dishes")
for item in recommendations:
    st.markdown(f"""
        **{item['Menu Item']}**  
        ⭐ Average Rating: {item['Avg_Rating']:.1f}  
        📊 Total Orders: {item['Total_Orders']}  
        ---
    """)

# Footer
st.write("🔗 Powered by AI & Data Science 🚀")
