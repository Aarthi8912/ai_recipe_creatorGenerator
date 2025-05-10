import streamlit as st
import cohere

# Initialize Cohere client
co = cohere.Client('api_key')  # Replace with your actual API key

st.set_page_config(page_title="Recipe Generator", page_icon="🍲")

st.title("🥘 AI Recipe Generator")
st.write("Enter ingredients and get a recipe powered by Cohere!")

# User input
ingredients = st.text_input("Enter ingredients (comma-separated):", "")

if st.button("Generate Recipe"):
    if ingredients.strip() == "":
        st.warning("Please enter some ingredients.")
    else:
        with st.spinner("Generating recipe..."):
            response = co.chat(
                model='command-r-plus',
                message=ingredients
            )

        st.subheader("🍽️ Your Recipe:")
        st.write(response.text.strip())
