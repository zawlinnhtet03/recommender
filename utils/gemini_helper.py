import google.generativeai as genai
import streamlit as st
# from dotenv import load_dotenv
# import os

# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")

# Initialize Gemini AI
api_key = st.secrets["GEMINI_API_KEY"]
genai.configure(api_key=api_key)

def get_laptop_recommendations(preferences):
    """
    Get laptop recommendations using Gemini AI based on user preferences
    """
    # Create the model
    model = genai.GenerativeModel('gemini-pro')

    # Construct the prompt
    prompt = f"""
    Act as an expert laptop recommender. Based on the following preferences, suggest 3-4 specific laptop models:

    Budget Range: ${preferences['price_range'][0]} - ${preferences['price_range'][1]}
    Preferred Brands: {', '.join(preferences['brands']) if isinstance(preferences['brands'], list) else preferences['brands']}
    Primary Use: {preferences['primary_use']}
    Battery Life Priority: {'Yes' if preferences['battery_life'] else 'No'}
    Portability Priority: {'Yes' if preferences['portability'] else 'No'}

    For each recommendation, please provide:
    1. Model name and brief description
    2. Key specifications
    3. Estimated price range
    4. Pros and cons
    5. Best suited for

    Format each recommendation clearly and make sure they truly match the user's requirements.
    """

    try:
        # Generate response
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"Error generating recommendations: {str(e)}")