import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Menu Superior", layout="wide")

# Barra de navegação
selected = option_menu(
    menu_title=None,  # Ocultar título do menu
    options=["Categorias", "Ofertas", "Cupons", "Mercado Play", "Vender", "Contato"],
    icons=["list", "tag", "ticket", "play-circle", "cash", "envelope"],  # Ícones opcionais
    menu_icon="menu",  # Ícone do menu
    default_index=0,  # Aba inicial
    orientation="horizontal",  # Orientação horizontal
    styles={
        "container": {"padding": "0!important", "background-color": "#C2EDF2"},
        "nav-link": {"font-size": "16px", "color": "black", "font-weight": "bold", "text-align": "center"},
        "nav-link-selected": {"background-color": "#FFFFFF", "color": "#000000"},
    },
)

# Exibindo o conteúdo de acordo com a aba selecionada
if selected == "Categorias":
    st.title("Categorias")
    st.write("Conteúdo da aba Categorias.")
elif selected == "Ofertas":
    st.title("Ofertas")
    st.write("Conteúdo da aba Ofertas.")
elif selected == "Cupons":
    st.title("Cupons")
    st.write("Conteúdo da aba Cupons.")
elif selected == "Supermercado":
    st.title("Supermercado")
    st.write("Conteúdo da aba Supermercado.")
elif selected == "Moda":
    st.title("Moda")
    st.write("Conteúdo da aba Moda.")
elif selected == "Mercado Play":
    st.title("Mercado Play")
    st.write("Conteúdo da aba Mercado Play.")
elif selected == "Vender":
    st.title("Vender")
    st.write("Conteúdo da aba Vender.")
elif selected == "Contato":
    st.title("Contato")
    st.write("Conteúdo da aba Contato.")
