# LLM App - LUCY Demo 🤖

Bienvenid@ a **LLM App - LUCY Demo**, un proyecto de demostración de un LLM (Large Language Model)
integrado con Streamlit y LangChain usando la API de OpenAI.  
Esta app permite interactuar con LUCY, un asistente virtual amigable y servicial.

---

## 🔹 Características
- Chat en tiempo real con LUCY usando GPT-3.5-turbo.  
- Historial de conversación persistente en sesión de Streamlit.  
- Respuestas claras y concisas, con manejo de casos donde LUCY no sabe la respuesta.  

---

## 🔹 Requisitos

Python 3.10+ y las siguientes librerías:

requeriments.txt
        streamlit==1.38.0
        langchain==0.2.14
        langchain-core==0.2.36
        langchain-openai==0.1.23
        openai==1.43.0
        python-dotenv==1.0.1

---

## 🔹 Instalación

Clonar el repositorio:

bash
Copiar código
git clone https://github.com/TU_maluramos72/LLM-demo.git
cd LLM-demo

**Crear y activar un entorno virtual (recomendado):

bash
Copiar código
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

---

**Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt

**Configurar API Key de OpenAI en .env:

env
Copiar código
OPENAI_API_KEY=tu_api_key_aqui

---

## 🔹 Uso

Ejecutar la app con Streamlit:

bash
Copiar código
streamlit run app.py
Escribe tu mensaje en el chat y LUCY te responderá.

El historial de conversación se mantiene mientras la sesión esté activa.

---

## 🔹 Notas Importantes
**Uso de la API de OpenAI: cada mensaje consumirá tokens y descontará del saldo de tu cuenta.

