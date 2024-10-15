
import os
import time
directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filespath = os.path.join(root, file)
        filetime = os.path.getmtime(filespath)
        formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(filetime))
        filesize = os.path.getsize(filespath)
        parent_dir = os.path.dirname(filespath)
        print(
            f'''Обнаружен файл: {file}, Путь: {filespath}, Размер: {filesize} байт, Время изменения: {formatted_time},
            Родительская директория: {parent_dir}''')