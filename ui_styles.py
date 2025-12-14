import streamlit as st

def load_css():
    st.markdown("""
        <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)
