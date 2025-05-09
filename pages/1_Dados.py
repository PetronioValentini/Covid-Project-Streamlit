import streamlit as st
from utils.utils import get_country_code, page_config, load_data

def main():
    # Set the page configuration
    page_config()
    
    # Título
    st.markdown("<h1 style='text-align: center;'>Casos Covid-19</h1><br>", unsafe_allow_html=True)
    
    # Carregando os dados
    df = load_data()

    # Adicionando a coluna de bandeira
    df["Bandeira"] = (df["País"].apply(get_country_code))
    df = df.set_index("Bandeira") # Definindo a bandeira como índice

    
    st.sidebar.header("Filtros") # Filtros na barra lateral
    opcoes_continente = sorted(df["Continente"].dropna().unique()) # Opções de continentes disponíveis
    continentes = st.sidebar.multiselect( # Seleção de continentes
        "Selecione o(s) Continente(s):",
        options=opcoes_continente, # Opções de continentes disponíveis
        default=opcoes_continente, # Seleção padrão de todos os continentes
        help="Selecione um ou mais continentes para filtrar os dados.",
    )
    df = df[df["Continente"].isin(continentes)] # Filtrando os dados com base nos continentes selecionados
    

    opcoes_pais = sorted(df["País"].dropna().unique()) # Opções de países disponíveis
    pais = st.sidebar.selectbox( # Seleção de país
        "Selecione um País:",
        options=["Todos"] + opcoes_pais, # Opções de países disponíveis
        help="Selecione um país específico para visualizar os dados.", 
    )

    if pais != "Todos": # Se um país específico for selecionado
        df = df[df["País"] == pais] # Filtrando os dados com base no país selecionado

    # Exibição
    st.write(f"🔎 **{len(df)} registros encontrados.**")

    st.dataframe(  # Exibindo o DataFrame
        df, 
        use_container_width=True, # Definindo a largura do contêiner
        column_config={ # Configuração das colunas
            "Bandeira": st.column_config.ImageColumn( # Coluna de imagem
                help="Bandeira do País",
            )
        }
    )


if __name__ == "__main__":
    main()
