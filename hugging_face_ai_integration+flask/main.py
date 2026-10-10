import asyncio
import json
import os
from dataclasses import asdict
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
from huggingface_hub import AsyncInferenceClient

# Загрузка переменных окружения
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

HF_TOKEN = os.getenv("HF_TOKEN")

# На бесплатном тарифе Hugging Face выделяет всего $0.10 в месяц на баланс для таких запросов.
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B" 
# Замените старую строку с DeepSeek на одну из этих:

# Вариант 1: Отличная и очень быстрая модель от Alibaba
MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"

# Вариант 2: Надежная модель от Meta (Facebook)
MODEL_NAME = "meta-llama/Llama-3.1-8B-Instruct"

# Вариант 3: Маленькая, но умная модель от Microsoft
MODEL_NAME = "microsoft/Phi-3.5-mini-instruct"

app = FastAPI()

# Асинхронная функция запроса к Hugging Face
async def ask_free_ai(prompt: str):
    client = AsyncInferenceClient(token=HF_TOKEN)
    print(f"Отправляем запрос к {MODEL_NAME}...")
    json_filename = "huggingface_response.json"
    
    try:
        response = await client.chat_completion(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        
        # Сохранение сырого ответа в JSON
        raw_json_data = json.dumps(asdict(response), indent=4, ensure_ascii=False)
        with open(json_filename, "w", encoding="utf-8") as f:
            f.write(raw_json_data)
        print(f" Успех! Сырой JSON-ответ сохранен в файл: {json_filename}")
        
        answer_AI = response.choices[0].message.content
        print(f"\nОтвет ИИ в консоли:\n{answer_AI}")
        return answer_AI
        
    except Exception as e:
        error_msg = f"Произошла ошибка при запросе: {e}"
        print(error_msg)
        return error_msg

# Интегрированная логика обработки слов и ИИ
@app.get("/api/process")
async def process_word(word: str):
    word_clean = word.strip()
    word_lower = word_clean.lower()
    
    # 1. Сначала проверяем жесткие команды
    if word_lower == "свет":
        return {"message": "Вы включили виртуальный свет! 💡"}
    elif word_lower == "создать":
        return {"message": "Файл успешно создан на сервере! 📂"}
    
    # 2. Если это не команда, отправляем текст как промпт в Hugging Face AI!
    ai_response = await ask_free_ai(word_clean)
    return {"message": ai_response}

# Главная страница с исправленным JavaScript
@app.get("/", response_class=HTMLResponse)
async def main_page():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Интерактивный ввод с ИИ</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 50px; text-align: center; background: #f4f4f9; }
            input { padding: 10px; width: 400px; font-size: 16px; border: 1px solid #ccc; border-radius: 4px; }
            button { padding: 10px 20px; font-size: 16px; background: #007bff; color: white; border: none; border-radius: 4px; cursor: pointer; }
            button:hover { background: #0056b3; }
            #output { margin-top: 20px; font-size: 16px; color: #333; text-align: left; max-width: 600px; margin-left: auto; margin-right: auto; white-space: pre-wrap; background: white; padding: 15px; border-radius: 5px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        </style>
    </head>
    <body>
        <h2>Введите команду или задайте вопрос ИИ</h2>
        <input type="text" id="wordInput" placeholder="Например: свет или Как дела?">
        <button onclick="sendWord()">Отправить</button>
        <div id="output">Здесь появится ответ...</div>

        <script>
            // Исправлено на async function! Браузер больше не будет ругаться
            async function sendWord() {
                const wordInput = document.getElementById('wordInput');
                const outputDiv = document.getElementById('output');
                const word = wordInput.value;
                if (!word) return;
                
                outputDiv.innerText = "Думаю... 🤖⏳";
                
                try {
                    const response = await fetch(`/api/process?word=${encodeURIComponent(word)}`);
                    const data = await response.json();
                    outputDiv.innerText = data.message;
                } catch (error) {
                    outputDiv.innerText = "Ошибка соединения с сервером ❌";
                }
            }
        </script>
    </body>
    </html>
    """

