import streamlit as st
import openai

# Configure sua chave da API OpenAI
openai.api_key = "SUA_API_OPENAI"

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
        model="gpt-3.5-turbo",  # Ou outro modelo desejado
        messages=st.session_state.messages
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
