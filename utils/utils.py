import streamlit as st
import pandas as pd
import pycountry

def page_config():
    """
    Set the page configuration for the Streamlit app.
    """
    st.set_page_config(
        page_title="Covid 19 DataFrame Display",
        initial_sidebar_state="expanded",
        layout="wide",
        page_icon="🦠"
    )
    
@st.cache_data
def load_data():
    """
    Load the Covid-19 data from a CSV file and return it as a DataFrame.
    """
    df = pd.read_csv("data/covid.csv")

    df_covid = df.rename(
        columns={
        "Country/Region": "País",
        "Continent": "Continente",
        "Population": "População",
        "TotalCases": "Total de Casos",
        "NewCases": "Novos Casos",
        "TotalDeaths": "Total de Mortes",
        "NewDeaths": "Novas Mortes",
        "TotalRecovered": "Total de Recuperados",
        "NewRecovered": "Novas Recuperações",
        "ActiveCases": "Casos Ativos",
        "Serious,Critical": "Casos Críticos",
        "Tot Cases/1M pop": "Casos por 1M",
        "Deaths/1M pop": "Mortes por 1M",
        "TotalTests": "Total de Testes",
        "Tests/1M pop": "Testes por 1M",
        "WHO Region": "Região OMS",
        }
    )

    return df_covid


def get_country_code(country_name):
    """
    Get the ISO 3166-1 alpha-2 country code for a given country name.
    """
    try:
        code = pycountry.countries.lookup(country_name).alpha_2.lower()
        if code:
            return f"https://flagcdn.com/w40/{code}.png"
    except LookupError:
        return "https://flagcdn.com/w40/un.png"
    



