# Dr. Tapia Bot

Este es un bot de Telegram asistido por OpenAI para ayudar en consultas sobre cirugía plástica.

## 🚀 Instalación

### 1️⃣ Clonar el repositorio
```sh
git clone https://github.com/panacea-icono/dr_tapia_bot.git
cd dr_tapia_bot
```

### 2️⃣ Crear y activar un entorno virtual
```sh
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Instalar dependencias
```sh
pip install -r requirements.txt
```

### 4️⃣ Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto y agrega:
```
TELEGRAM_TOKEN=tu_token_de_telegram
OPENAI_API_KEY=tu_api_key_de_openai
```

### 5️⃣ Ejecutar el bot
```sh
python dr_tapia_bot.py
```

## 📌 Funcionalidades
- Responde preguntas sobre cirugía plástica.
- Integración con OpenAI para respuestas basadas en IA.
- Modo Webhook y Polling disponibles.

## 📜 Licencia
Este proyecto está bajo la licencia MIT.

