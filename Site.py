import openai
import streamlit as st

# Configurar a API Key
openai.api_key = st.secrets["openai"]["api_key"]

# Configurar interface
st.title("Chatbot com Streamlit")
st.markdown("Digite uma mensagem para o chatbot.")

# Histórico de mensagens
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Você é um assistente útil."}]

# Entrada do usuário
user_input = st.text_input("Você:", key="user_input")

if st.button("Enviar") and user_input.strip():
    # Adiciona mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Gera resposta do modelo
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Ou "gpt-4", dependendo da sua conta
            messages=st.session_state.messages,
        )
        bot_response = response["choices"][0]["message"]["content"]

        # Adiciona resposta do chatbot ao histórico
        st.session_state.messages.append({"role": "assistant", "content": bot_response})

    except Exception as e:
        st.error(f"Erro ao chamar a API OpenAI: {e}")

# Exibir histórico de mensagens
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**Você:** {message['content']}")
    elif message["role"] == "assistant":
        st.markdown(f"**Chatbot:** {message['content']}")
