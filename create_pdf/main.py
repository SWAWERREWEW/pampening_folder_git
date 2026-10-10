import weasyprint
import base64
import mimetypes
import os

def image_to_data_url(image_path):
    """
    Конвертирует локальное изображение в строку Data URL (Base64).
    """
    # 1. Проверяем, существует ли файл
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Файл не найден по пути: {image_path}")
        
    # 2. Автоматически определяем MIME-тип (например, image/png или image/jpeg)
    mime_type, _ = mimetypes.guess_type(image_path)
    if not mime_type:
        mime_type = "image/jpg"  # Значение по умолчанию, если тип не определился
        
    # 3. Читаем файл в бинарном режиме и кодируем в Base64
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
        
    # 4. Формируем и возвращаем готовую Data URL строку
    return f"data:{mime_type};base64,{encoded_string}"

link_image = image_to_data_url("some_picture.jpg")
html_content = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
body { font-family: sans-serif; }
</style>
</head>
<body>
<h1>Привет, мир!</h1>
<p>Этот PDF создан из HTML с поддержкой русских букв.</p>
<img src='""" + link_image + """' style="width: 500px; height: auto;"/>
</body>
</html>
"""

weasyprint.HTML(string=html_content).write_pdf("мухахаха.pdf")

