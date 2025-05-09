import streamlit as st
from utils.utils import page_config
import webbrowser

def main():
      
    page_config() # Set the page configuration

    # Título
    st.title("DataFrame da Covid-19 🦠")

    # Corpo
    st.markdown(
    """
    ### Sobre este Aplicativo

    Este painel interativo apresenta um **conjunto de dados global sobre a pandemia de Covid-19**, com informações por país, incluindo:

    - Total de casos confirmados, mortes, recuperações e casos ativos  
    - Novos casos, mortes e recuperações (atualizações diárias)  
    - Indicadores derivados, como:
        - **Casos e mortes por 1 milhão de habitantes**  
        - **Testes realizados e testes por 1 milhão de habitantes**
        - **Taxa de mortalidade e taxa de recuperação**
        - **Casos críticos e casos ativos**
    - População total e continente de cada país
    - Dados de vacinação (total de vacinas administradas e porcentagem da população vacinada)
    - Comparações semanais de casos e aumento percentual  
    - Região da OMS associada a cada país

    O objetivo é **explorar tendências e fazer comparações por país** usando uma interface simples e interativa construída com Streamlit.

    Use a barra lateral para navegar entre as páginas e clique no botão abaixo para acessar o conjunto de dados original no Kaggle.
    """
    )

    
    btn = st.button("Covid Kaggle Dataset")
    if btn:
        webbrowser.open_new_tab("https://www.kaggle.com/datasets/imdevskp/corona-virus-report/data")
    
    
    #Sidebar
    st.sidebar.markdown("Desenvolvido por [Petrônio](https://github.com/petroniovalentini) para fins de aprendizado.")
    
    


if __name__ == "__main__":
    main()
