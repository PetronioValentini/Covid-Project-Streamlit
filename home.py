import streamlit as st
from utils.data_loader import page_config
import webbrowser

def main():
      
    page_config() # Set the page configuration

    # Title
    st.title("Covid-19 DataFrame 🦠")
    
    # Body
    st.markdown(
    """
    ### About this App

    This interactive dashboard presents a **global dataset on the Covid-19 pandemic**, with information per country, including:

    - Total confirmed cases, deaths, recoveries, and active cases  
    - New cases, deaths, and recoveries (daily updates)  
    - Derived indicators such as:
        - **Deaths per 100 cases**
        - **Recoveries per 100 cases**
        - **Deaths per 100 recoveries**
    - Weekly case count comparisons and percentage increase  
    - WHO Region associated with each country

    The goal is to **explore trends and make country-level comparisons** using a simple and interactive interface built with Streamlit.

    Use the sidebar to navigate between pages, and click the button below to access the original dataset on Kaggle.
    """
    )
    
    btn = st.button("Covid Kaggle Dataset")
    if btn:
        webbrowser.open_new_tab("https://www.kaggle.com/datasets/imdevskp/corona-virus-report/data")
    
    
    #Sidebar
    st.sidebar.markdown("Desenvolvido por [Petrônio](https://github.com/petroniovalentini)")
    


if __name__ == "__main__":
    main()
