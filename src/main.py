import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

def print_author():
    # Читаем значение из переменной окружения AUTHOR
    author = os.getenv('AUTHOR')
    
    # Проверяем, что переменная найдена
    if author is None:
        author = "Неизвестный автор"
    
    print(f"Автор проекта: {author}")

print_author()
