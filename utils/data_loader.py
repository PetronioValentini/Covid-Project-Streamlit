import streamlit as st
import pandas as pd

def page_config():
    """
    Set the page configuration for the Streamlit app.
    """
    st.set_page_config(
        page_title="Covid 19 DataFrame Display",
        initial_sidebar_state="expanded",
    )
    
@st.cache_data
def load_data():
    """
    Load the Covid-19 data from a CSV file and return it as a DataFrame.
    """
    df_covid = pd.read_csv("data/prontuarios_gerados.csv", index_col=0)
    return df_covid


    
    
    

