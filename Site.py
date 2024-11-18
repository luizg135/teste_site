import streamlit as st
import openai

# Configurar a API Key usando secrets
openai.api_key = st.secrets["openai"]["api_key"]

# Configurando a interface
st.title("Chatbot com Streamlit")
st.markdown("Digite uma mensagem abaixo e o chatbot responderá.")

# Histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Entrada do usuário
user_input = st.text_input("Você:", "", key="input")

# Resposta do chatbot
if st.button("Enviar") and user_input.strip():
    # Adiciona mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Gera resposta do chatbot
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Confirme se está usando um modelo suportado
    messages=[
        {"role": "system", "content": "Você é um assistente útil."},
        {"role": "user", "content": user_input},
    ],
)
bot_response = response['choices'][0]['message']['content']


    # Adiciona resposta ao histórico
    st.session_state.messages.append({"role": "assistant", "content": bot_response})

# Exibindo o histórico do chat
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**Você:** {message['content']}")
    else:
        st.markdown(f"**Chatbot:** {message['content']}")
