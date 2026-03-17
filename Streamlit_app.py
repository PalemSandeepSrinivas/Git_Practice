import streamlit as st
import os

def main():
    st.title("Git & Deployment Practice App")
    
    st.markdown("""
    Welcome! This app is a sandbox to practice:
    - Committing code to Git
    - Deploying to Streamlit Cloud
    - Managing Environment Secrets
    """)

    # --- Secrets Management ---
    st.header("Secrets Check")
    
    # The key we expect to find in the secrets manager
    SECRET_KEY = "MY_SECRET_TOKEN"

    # Streamlit Cloud exposes secrets via the st.secrets dictionary
    if SECRET_KEY in st.secrets:
        st.success(f"Success! Secret '{SECRET_KEY}' was read securely.")
        st.info(f"Value: {st.secrets[SECRET_KEY]}")
    else:
        st.warning(f"Secret '{SECRET_KEY}' not found. Please add it to Streamlit Cloud 'Secrets' settings.")

if __name__ == "__main__":
    print("Developer: This message is printed to the console, not the Streamlit app. Check your terminal for this output.")
    main()