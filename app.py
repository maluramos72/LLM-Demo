import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Verificar API Key
if not os.getenv("OPENAI_API_KEY"):
    st.error("⚠️ No se encontró la API key de OpenAI")
    st.stop()

# Configuración de la página
st.set_page_config(page_title="LLM App - LUCY Demo", page_icon="🤖")
st.title("LLM App - LUCY Demo 🤖")
st.write("¡Bienvenid@ a LLM App LUCY!")

# Inicializar historial
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Función corregida para obtener respuesta
def get_response(query, chat_history):
    template = """Eres LUCY, una asistente virtual amigable y servicial.
    Responde a la consulta del usuario de manera concisa y clara.   
    Si no sabes la respuesta, di "Lo siento, no sé la respuesta a eso."
    
    Consulta: {query}
    Historial de chat: {chat_history}
    Respuesta:"""
    
    prompt = ChatPromptTemplate.from_template(template)
    
    try:
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",  
            temperature=0,
            api_key=os.getenv("OPENAI_API_KEY")
        )
        chain = prompt | llm | StrOutputParser()
        
        return chain.stream({
            "query": query, 
            "chat_history": chat_history
        })
    except Exception as e:
        st.error(f"Error con la API de OpenAI: {str(e)}")
        return None

# Mostrar conversación existente
for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Input de usuario
usr_qry = st.chat_input("Tu Mensaje")
if usr_qry is not None and usr_qry.strip() != "":
    # Agregar mensaje del usuario
    st.session_state.chat_history.append(HumanMessage(usr_qry))
    
    # Mostrar mensaje del usuario
    with st.chat_message("user"):
        st.markdown(usr_qry)

    # Mostrar respuesta de AI con streaming
    with st.chat_message("assistant"):
        try:
            ai_stream = get_response(usr_qry, st.session_state.chat_history)
            if ai_stream:
                # CLAVE: Usar st.write_stream para capturar la respuesta completa
                ai_response = st.write_stream(ai_stream)
                # Agregar la respuesta completa al historial
                st.session_state.chat_history.append(AIMessage(ai_response))
            else:
                st.error("No se pudo obtener respuesta de LUCY")
        except Exception as e:
            st.error(f"Error: {str(e)}")
            if "quota" in str(e).lower() or "429" in str(e):
                st.warning("🚨 **Tu API key de OpenAI se quedó sin créditos**")

# Sidebar con información
with st.sidebar:
    st.header("LUCY - Asistente Virtual")
    st.write("Estado del sistema:")
    
    # Verificar estado de la API
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        st.success("✅ API Key configurada")
        st.write(f"Key: {api_key[:12]}...{api_key[-4:]}")
    else:
        st.error("❌ API Key no encontrada")
    
    st.write("")
    st.write("**Características:**")
    st.write("- 🎯 Respuestas concisas")
    st.write("- 💬 Memoria de conversación") 
    st.write("- ⚡ Streaming en tiempo real")
    
    if st.button("🗑️ Limpiar Chat"):
        st.session_state.chat_history = []
        st.rerun()
    
    st.write("")
    st.caption("💡 Si ves errores de quota, necesitas agregar créditos a tu cuenta de OpenAI")