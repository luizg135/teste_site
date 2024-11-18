# import streamlit as st
# from streamlit_option_menu import option_menu

# # Configuração da página
# st.set_page_config(page_title="Menu Superior", layout="wide")

# # Barra de navegação
# selected = option_menu(
#     menu_title=None,  # Ocultar título do menu
#     options=["Categorias", "Ofertas", "Cupons", "Mercado Play", "Cadastro", "Contato"],
#     icons=["list", "tag", "ticket", "play-circle", "cash", "envelope"],  # Ícones opcionais
#     menu_icon="menu",  # Ícone do menu
#     default_index=0,  # Aba inicial
#     orientation="horizontal",  # Orientação horizontal
#     styles={
#         "container": {"padding": "0!important", "background-color": "#C2EDF2"},
#         "nav-link": {"font-size": "16px", "color": "black", "font-weight": "bold", "text-align": "center"},
#         "nav-link-selected": {"background-color": "#FFFFFF", "color": "#000000"},
#     },
# )

# # Conteúdo da aba selecionada
# if selected == "Categorias":
#     st.title("Categorias")
#     st.write("Conteúdo da aba Categorias.")

# elif selected == "Ofertas":
#     st.title("Ofertas")
#     st.write("Conteúdo da aba Ofertas.")

# elif selected == "Cupons":
#     st.title("Cupons")
#     st.write("Conteúdo da aba Cupons.")

# elif selected == "Mercado Play":
#     st.title("Mercado Play")
#     st.write("Conteúdo da aba Mercado Play.")

# elif selected == "Cadastro":
#     st.title("Cadastro")

#     # Campos do formulário
#     with st.form("form_cadastro"):
#         nome = st.text_input("Nome Completo")
#         email = st.text_input("Email")
#         telefone = st.text_input("Telefone")
#         senha = st.text_input("Senha", type="password")

#         # Botão de submissão
#         submit_button = st.form_submit_button("Cadastrar")

#     # Ação ao clicar no botão
#     if submit_button:
#         if nome and email and telefone and senha:  # Verifica se todos os campos estão preenchidos
#             st.success(f"Cadastro realizado com sucesso!\nBem-vindo, {nome}!")
#             # Aqui você pode salvar os dados em uma lista, arquivo ou banco de dados
#             # Exemplo simples: Salvar os dados localmente
#             cadastro = {"Nome": nome, "Email": email, "Telefone": telefone, "Senha": senha}
#             st.write("Dados cadastrados:")
#             st.json(cadastro)
#         else:
#             st.error("Por favor, preencha todos os campos.")

# elif selected == "Contato":
#     st.title("Contato")
#     st.write("Conteúdo da aba Contato.")

import streamlit as st
from streamlit_option_menu import option_menu

# Configuração da página
st.set_page_config(page_title="Menu Superior", layout="wide")

# CSS personalizado para o menu e o novo contêiner
st.markdown(
    """
    <style>
        /* Contêiner para o menu superior */
        .menu-container {
            max-width: 1200px; /* Largura fixa para o menu */
            margin: 0 auto; /* Centraliza o menu horizontalmente */
        }
        
        /* Novo contêiner para o conteúdo */
        .content-container {
            max-width: 1200px; /* Mesma largura do menu */
            margin: 0 auto; /* Centraliza o conteúdo horizontalmente */
            padding: 20px; /* Adiciona espaçamento interno */
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Menu superior
st.markdown('<div class="menu-container">', unsafe_allow_html=True)
selected = option_menu(
    menu_title=None,
    options=["Categorias", "Ofertas", "Cupons", "Mercado Play", "Cadastro", "Contato"],
    icons=["list", "tag", "ticket", "play-circle", "cash", "envelope"],
    menu_icon="menu",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"background-color": "#C2EDF2"},
        "nav-link": {
            "font-size": "16px",
            "color": "black",
            "font-weight": "bold",
            "text-align": "center",
        },
        "nav-link-selected": {"background-color": "#FFFFFF", "color": "#000000"},
    },
)
st.markdown('</div>', unsafe_allow_html=True)

# Novo contêiner para o conteúdo
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
