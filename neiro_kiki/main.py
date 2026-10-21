import asyncio
import json
import os
from huggingface_hub import AsyncInferenceClient
from fastapi import FastAPI
app = FastAPI()

import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

HF_TOKEN = os.getenv("HF_TOKEN")

# Выбираем одну из лучших открытых моделей на сегодня
MODEL_NAME = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B" 
"""
Практический совет: если получите ошибку доступа, попробуйте заменить модель на одну из гарантированно бесплатных:
Qwen/Qwen2.5-7B-Instruct
meta-llama/Llama-3.1-8B-Instruct
microsoft/Phi-3.5-mini-instruct
"""


async def ask_free_ai(prompt: str):
    # Инициализируем асинхронного клиента
    client = AsyncInferenceClient(token=HF_TOKEN)
    
    print(f"Отправляем запрос к {MODEL_NAME}...")
    
    # Имя файла для сохранения сырых данных
    json_filename = "huggingface_response.json"
    
    try:
        # Отправляем асинхронный POST-запрос
        # Используем встроенный метод chat_completion (он возвращает структурированный объект)
        response = await client.chat_completion(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        
        # --- БЛОК СОХРАНЕНИЯ В JSON ---
        # Переводим объект ответа в словарь Python, а затем в красивый текстовый JSON
        from dataclasses import asdict
        raw_json_data = json.dumps(asdict(response), indent=4, ensure_ascii=False)
        
        # Записываем сырой JSON на жесткий диск в папку с кодом
        with open(json_filename, "w", encoding="utf-8") as f:
            f.write(raw_json_data)
        print(f" Успех! Сырой JSON-ответ сохранен в файл: {json_filename}")
        
        # --- ВЫВОД ЧИСТОГО ТЕКСТА В КОНСОЛЬ ---
        print("\nОтвет ИИ в консоли:")
        # Достаем текст из структуры ответа
        answer_AI = response.choices[0].message.content
        print(answer_AI)
        return answer_AI
        
    except Exception as e:
        print(f"Произошла ошибка при запросе: {e}")
        
    # --- ФУНКЦИЯ АВТОМАТИЧЕСКОГО УДАЛЕНИЯ (ЗАКОМЕНТИРОВАНА) ---
    # Если вы захотите, чтобы файл удалялся сам после работы программы,
    # просто уберите решетки (#) с трех строк ниже:
    # 
    # if os.path.exists(json_filename):
    #     os.remove(json_filename)
    #     print(f" Файл {json_filename} был автоматически удален.")


def read_json():
    import json

    # Имя нашего сохраненного файла
    json_filename = "huggingface_response.json"

    try:
        # 1. Открываем файл и загружаем JSON в словарь Python
        with open(json_filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    
        # 2. Достаем метаданные из блока "usage"
        prompt_tokens = data["usage"]["prompt_tokens"]
        completion_tokens = data["usage"]["completion_tokens"]
        total_tokens = data["usage"]["total_tokens"]
        
        # 3. Достаем название модели
        model_name = data["model"]
        
        # Выводим красивый аналитический отчет в консоль
        print("📊 АНАЛИЗ ПОЛУЧЕННОГО JSON-ФАЙЛА 📊")
        print("-" * 40)
        print(f"🤖 Использованная модель: {model_name}")
        print(f"📥 Токенов в вашем вопросе: {prompt_tokens}")
        print(f"📤 Токенов в ответе ИИ:    {completion_tokens}")
        print(f"🧮 Всего потрачено токенов: {total_tokens}")
        print("-" * 40)
        
        # Симулируем расчет стоимости (как если бы мы платили за коммерческий API)
        # Предположим, цена $2 за 1 миллион токенов
        fake_cost = (total_tokens / 1_000_000) * 2
        print(f"💰 Условная стоимость запроса: ${fake_cost:.6f} (для вас — бесплатно!)")

    except FileNotFoundError:
        print(f"❌ Ошибка: Файл {json_filename} не найден в этой папке.")
    except KeyError as e:
        print(f"❌ Ошибка структуры: В JSON нет ключа {e}")

"""
# Запуск асинхронного движка
if __name__ == "__main__":
    import sys
    try: command = sys.argv[1]
    except IndexError: command = None
    
    if command == "read_json":
        read_json()
        exit()
    else:
        asyncio.run(ask_free_ai("Здравствуйте. Вы умеете говорить по-русски?"))
"""

@app.get("/generate")
async def read_root():
    prompt = "Здравствуйте. Вы умеете говорить по-русски?"
    ai_result = await ask_free_ai(prompt)
    return {"result": ai_result}
