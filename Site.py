import streamlit as st
from streamlit_option_menu import option_menu
import gspread
from google.oauth2.service_account import Credentials

# Configuração da página
st.set_page_config(page_title="Menu Superior", layout="wide")

# Configurar autenticação com Google Sheets
def connect_to_gsheets():
    credentials = Credentials.from_service_account_info(
        st.secrets["google_service_account"]
    )
    client = gspread.authorize(credentials)
    # Abra a planilha pelo nome ou URL
    sheet = client.open("Cadastramento").sheet1
    return sheet

# Função para salvar dados na planilha
def save_to_gsheet(data):
    sheet = connect_to_gsheets()
    sheet.append_row(data)

# Barra de navegação
selected = option_menu(
    menu_title=None,  # Ocultar título do menu
    options=["Categorias", "Ofertas", "Cupons", "Mercado Play", "Cadastro", "Contato"],
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

# Conteúdo da aba selecionada
if selected == "Cadastro":
    st.title("Cadastro")

    # Campos do formulário
    with st.form("form_cadastro"):
        nome = st.text_input("Nome Completo")
        email = st.text_input("Email")
        telefone = st.text_input("Telefone")
        senha = st.text_input("Senha", type="password")

        # Botão de submissão
        submit_button = st.form_submit_button("Cadastrar")

    # Ação ao clicar no botão
    if submit_button:
        if nome and email and telefone and senha:  # Verifica se todos os campos estão preenchidos
            st.success(f"Cadastro realizado com sucesso!\nBem-vindo, {nome}!")

            # Dados para salvar na planilha
            data = [nome, email, telefone, senha]
            try:
                save_to_gsheet(data)
                st.success("Dados enviados para o Google Sheets!")
            except Exception as e:
                st.error(f"Erro ao salvar os dados: {e}")
        else:
            st.error("Por favor, preencha todos os campos.")
