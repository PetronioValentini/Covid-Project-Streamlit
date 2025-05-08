import streamlit as st
from utils.data_loader import page_config, load_data

def main():
    page_config()
    
    st.markdown("<h1 style='text-align: center;'>Prontuários Gerados</h1>", unsafe_allow_html=True)
    
    dt = load_data()
    dt.reset_index(drop=True, inplace=True)
    st.dataframe(dt, use_container_width=True)
    print(dt.columns.tolist())
    
    
    

if __name__ == "__main__":
    main()
