import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Menu Superior", layout="wide")

# CSS personalizado para ajustar o menu superior
st.markdown(
    """
    <style>
        /* Ajusta o menu superior para ocupar toda a largura da página */
        .menu-container {
            width: 100%; /* Ocupa toda a largura */
            background-color: #C2EDF2; /* Cor de fundo do menu */
            padding: 10px 0; /* Espaçamento vertical no menu */
            display: flex; /* Garante que o conteúdo se alinha corretamente */
            justify-content: center; /* Centraliza os itens dentro do menu */
        }
        
        /* Centraliza o conteúdo dentro do menu */
        .menu-content {
            max-width: 1200px; /* Limita a largura do conteúdo dentro do menu */
            width: 100%; /* Garante que ocupe todo o espaço disponível */
            display: flex; /* Torna o conteúdo flexível */
            justify-content: space-between; /* Espaça uniformemente os itens */
        }
        
        /* Novo contêiner para o restante do conteúdo da página */
        .content-container {
            max-width: 1200px; /* Largura fixa para o conteúdo */
            margin: 0 auto; /* Centraliza o conteúdo horizontalmente */
            padding: 20px; /* Adiciona espaçamento interno */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Menu superior
st.markdown('<div class="menu-container">', unsafe_allow_html=True)
st.markdown('<div class="menu-content">', unsafe_allow_html=True)

# Configuração do menu superior com as opções
selected = option_menu(
    menu_title=None,
    options=["Categorias", "Ofertas", "Cupons", "Mercado Play", "Cadastro", "Contato"],
    icons=["list", "tag", "ticket", "play-circle", "cash", "envelope"],
    menu_icon="menu",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"background-color": "transparent"},
        "nav-link": {
            "font-size": "16px",
            "color": "black",
            "font-weight": "bold",
            "text-align": "center",
        },
        "nav-link-selected": {"background-color": "#FFFFFF", "color": "#000000"},
    },
)
st.markdown('</div>', unsafe_allow_html=True)  # Fecha o menu-content
st.markdown('</div>', unsafe_allow_html=True)  # Fecha o menu-container

# Novo contêiner para o restante do conteúdo
st.markdown('<div class="content-container">', unsafe_allow_html=True)

# Conteúdo da aba selecionada
if selected == "Categorias":
    st.title("Categorias")
    st.write("Conteúdo da aba Categorias.")

elif selected == "Ofertas":
    st.title("Ofertas")
    st.write("Conteúdo da aba Ofertas.")

elif selected == "Cupons":
    st.title("Cupons")
    st.write("Conteúdo da aba Cupons.")

elif selected == "Mercado Play":
    st.title("Mercado Play")
    st.write("Conteúdo da aba Mercado Play.")

elif selected == "Cadastro":
    st.title("Cadastro")
    with st.form("form_cadastro"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        senha = st.text_input("Senha", type="password")

        # Botão de submissão
        submit_button = st.form_submit_button("Cadastrar")
    if submit_button:
        if nome and email and telefone and senha:  # Verifica se todos os campos estão preenchidos
            st.success(f"Cadastro realizado com sucesso!\nBem-vindo, {nome}!")
        else:
            st.error("Por favor, preencha todos os campos.")

elif selected == "Contato":
    st.title("Contato")
    st.write("Conteúdo da aba Contato.")

# Fecha o contêiner de conteúdo
st.markdown('</div>', unsafe_allow_html=True)
