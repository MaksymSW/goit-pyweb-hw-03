"""
Перша частина для потоків
    Напишіть програму обробки директорії "Хлам", яка копіює файли з заданої директорії (та всіх її піддиректорій) до цільової директорії,
    сортуючи їх за розширеннями. Програма повинна використовувати багатопотоковість для ефективної обробки великих обсягів файлів та піддиректорій.
    Програма приймає два аргументи командного рядка:
        шлях до директорії з файлами для обробки.
        шлях до директорії, де будуть розміщені відсортовані файли. За замовчуванням використовується директорія dist.
    Вона має рекурсивно обходити всі піддиректорії джерельної директорії. 
"""

from pathlib import Path
from threading import Thread

class Sort_file():
    def __init__(self,source_folder_path,target_folder_path):
        self.source_folder_path = source_folder_path
        self.target_folder_path = target_folder_path
        

    def file_sort(self):
        self.files_by_extension = {}
        source_folder = Path(source_folder_path)
        target_folder = Path(target_folder_path)

        for file_path in source_folder.rglob('*'):
            if file_path.is_file():
                extension = file_path.suffix.lower()
                if extension in self.files_by_extension:
                    self.files_by_extension[extension].append(file_path)
                else:
                    self.files_by_extension[extension] = [file_path]

        for extension, files in self.files_by_extension.items():
            extension_folder = target_folder / extension[1:] 
            extension_folder.mkdir(parents=True, exist_ok=True)  
            for file_path in files:        
                new_file_path = extension_folder / file_path.name
                file_path.replace(new_file_path)

    

if __name__ == "__main__":
    
    source_folder_path = input("Введите путь к исходной папке: ").strip()
    target_folder_path = input("Введите путь к целевой папке: ").strip()
    
    sort_file = Sort_file(source_folder_path, target_folder_path)   
    thread = Thread(target=sort_file.file_sort)   
    thread.start()
    thread.join()
                
                
                    
                
                




        
        

