import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Menu Superior", layout="wide")

# CSS personalizado para limitar a largura do conteúdo
st.markdown(
    """
    <style>
        .main-container {
            max-width: 1200px; /* Define a largura máxima do conteúdo */
            margin: 0 auto; /* Centraliza horizontalmente */
            padding: 20px; /* Adiciona espaço interno */
        }
        .menu-container {
            background-color: #C2EDF2;
            padding: 10px 0;
        }
        .form-container {
            margin-top: 20px; /* Espaço entre o menu e o conteúdo */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Contêiner principal
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Barra de navegação
st.markdown('<div class="menu-container">', unsafe_allow_html=True)
selected = option_menu(
    menu_title=None,
    options=["Categorias", "Ofertas", "Cupons", "Mercado Play", "Cadastro", "Contato"],
    icons=["list", "tag", "ticket", "play-circle", "cash", "envelope"],
    menu_icon="menu",
    default_index=0,
    orientation="horizontal",
    styles={
        "nav-link": {"font-size": "16px", "color": "black", "font-weight": "bold", "text-align": "center"},
        "nav-link-selected": {"background-color": "#FFFFFF", "color": "#000000"},
    },
)
st.markdown('</div>', unsafe_allow_html=True)

# Conteúdo da aba selecionada
if selected == "Categorias":
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.title("Categorias")
    st.write("Conteúdo da aba Categorias.")
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Ofertas":
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.title("Ofertas")
    st.write("Conteúdo da aba Ofertas.")
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Cupons":
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.title("Cupons")
    st.write("Conteúdo da aba Cupons.")
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Mercado Play":
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.title("Mercado Play")
    st.write("Conteúdo da aba Mercado Play.")
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Cadastro":
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.title("Cadastro")
    with st.form("form_cadastro"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        senha = st.text_input("Senha", type="password")

        # Botão de submissão
        submit_button = st.form_submit_button("Cadastrar")
    st.markdown('</div>', unsafe_allow_html=True)

    # Ação ao clicar no botão
    if submit_button:
        if nome and email and telefone and senha:  # Verifica se todos os campos estão preenchidos
            st.success(f"Cadastro realizado com sucesso!\nBem-vindo, {nome}!")
        else:
            st.error("Por favor, preencha todos os campos.")

elif selected == "Contato":
    st.markdown('<div class="form-container">', unsafe_allow_html=True)
    st.title("Contato")
    st.write("Conteúdo da aba Contato.")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
