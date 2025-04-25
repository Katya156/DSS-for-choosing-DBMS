import sys
import os


# Получить путь к файлам в папке 'data', которую мы добавили
def resource_path(relative_path):
    try:
        # Для bundled .exe
        base_path = sys._MEIPASS
    except Exception:
        # Для обычного запуска
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
