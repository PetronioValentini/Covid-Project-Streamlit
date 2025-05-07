import streamlit as st
from utils.data_loader import page_config, load_data

def main():
    page_config()
    
    st.markdown("<h1 style='text-align: center;'>Covid-19 DataFrame</h1>", unsafe_allow_html=True)
    
    dt = load_data()
    st.write(dt)
    
    
    

if __name__ == "__main__":
    main()
