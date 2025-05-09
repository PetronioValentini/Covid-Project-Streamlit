import streamlit as st
import pandas as pd
import altair as alt
from utils.utils import page_config, load_data

def main():
    # Set the page configuration
    page_config()
    
    # Título
    st.markdown("<h1 style='text-align: center;'>Top 10 Paises com Maiores Índices de Morte por Covid</h1><br>", unsafe_allow_html=True)
    
    # Carregando os dados
    df = load_data() 

    # Data Frame
    top10 = df.sort_values("Total de Mortes", ascending=False).head(10) # Selecionando os 10 países com mais mortes

    # Criar o gráfico de barras com Altair
    chart = alt.Chart(top10).mark_bar().encode(
        x=alt.X("País", title="País", axis=alt.Axis(labelAngle=0)),  # Eixo x: Países
        y=alt.Y("Total de Mortes", title="Total de Mortes"),  # Eixo y: Total de Mortes
        color=alt.Color("País", legend=None)        # Define uma cor diferente para cada país

    )

    # Exibir o gráfico no Streamlit
    st.altair_chart(
        chart, # Exibindo o gráfico
        use_container_width=True,  # Definindo a largura do contêiner

    )




if __name__ == "__main__":
    main()
