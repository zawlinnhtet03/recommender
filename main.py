import streamlit as st
import pandas as pd
from utils.gemini_helper import get_laptop_recommendations
import time

# Page configuration
st.set_page_config(
    page_title="AI Laptop Recommender",
    page_icon="💻",
    layout="wide"
)

# Load custom CSS
with open("styles/main.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
st.markdown("<h1 class='main-title'>AI Laptop Recommender 💻</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Get personalized laptop recommendations powered by Gemini AI</p>", unsafe_allow_html=True)

# Initialize session state
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None

# Sidebar for user inputs
with st.sidebar:
    st.markdown("<h2 class='sidebar-title'>Your Preferences</h2>", unsafe_allow_html=True)
    
    # Brand selection
    brands = ['Any', 'Dell', 'HP', 'Lenovo', 'Apple', 'ASUS', 'Acer', 'MSI', 'Samsung']
    selected_brands = st.multiselect(
        "Preferred Brands",
        brands,
        default=['Any']
    )

    # Price range
    st.markdown("<h3 class='sidebar-subtitle'>Price Range</h3>", unsafe_allow_html=True)
    price_range = st.slider(
        "Select your budget ($)",
        min_value=300,
        max_value=5000,
        value=(500, 2000),
        step=100
    )

    # Primary use case
    use_cases = [
        'General Purpose',
        'Gaming',
        'Content Creation',
        'Programming/Development',
        'Business/Professional',
        'Student',
        'Video Editing',
        '3D Modeling/CAD'
    ]
    primary_use = st.selectbox(
        "Primary Use Case",
        use_cases
    )

    # Additional preferences
    st.markdown("<h3 class='sidebar-subtitle'>Additional Preferences</h3>", unsafe_allow_html=True)
    battery_life = st.checkbox("Long Battery Life Priority")
    portability = st.checkbox("Portability Priority")
    
    # Get recommendations button
    if st.button("Get Recommendations", type="primary"):
        with st.spinner("🤖 AI is analyzing your preferences..."):
            # Prepare the prompt
            preferences = {
                "brands": "Any" if "Any" in selected_brands else selected_brands,
                "price_range": price_range,
                "primary_use": primary_use,
                "battery_life": battery_life,
                "portability": portability
            }
            
            try:
                st.session_state.recommendations = get_laptop_recommendations(preferences)
                st.success("✨ Recommendations generated successfully!")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Main content area
if st.session_state.recommendations:
    st.markdown("<h2 class='section-title'>Your Personalized Recommendations</h2>", unsafe_allow_html=True)
    
    # Display recommendations
    recommendations = st.session_state.recommendations.split("\n\n")
    
    for idx, rec in enumerate(recommendations, 1):
        if rec.strip():
            with st.expander(f"#{idx}", expanded=True):
                st.markdown(rec)
    
    # Additional tips
    st.markdown("---")
    st.markdown("<h3 class='tips-title'>💡 Pro Tips</h3>", unsafe_allow_html=True)
    st.markdown("""
    - Compare prices across different retailers
    - Check user reviews before making a final decision
    - Consider warranty options
    - Look for student discounts if applicable
    """)
else:
    # Welcome message
    st.markdown("""
    <div class='welcome-box'>
        <h2>👋 Welcome to AI Laptop Recommender!</h2>
        <p>Get personalized laptop recommendations in 3 simple steps:</p>
        <ol>
            <li>Select your preferred brands</li>
            <li>Set your budget range</li>
            <li>Choose your primary use case</li>
        </ol>
        <p>Use the sidebar to input your preferences and click 'Get Recommendations'!</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class='footer'>
    <p>Powered by Gemini AI 🤖 | Made with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)