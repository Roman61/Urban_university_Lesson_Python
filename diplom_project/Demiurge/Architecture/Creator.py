import os
import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Union


class ProjectCreator:
    def __init__(self, architecture: Dict[str, Union[Dict, List[str]]] = None):
        self.architecture = architecture or {}
        self.current_path = ''

    def load_from_json(self, file_path: str):
        """Загружает архитектуру проекта из JSON файла."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                self.architecture = json.load(f)
                if len(self.architecture.items()) < 2:
                    temp = list(self.architecture.keys())
                    self.architecture = self.architecture[temp[0]]
            print(f"Project architecture loaded from {file_path}")
        except Exception as e:
            print(f"Error loading JSON file: {e}")

    def load_from_xml(self, file_path: str):
        """Загружает архитектуру проекта из XML файла."""
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
            self.architecture = self._xml_to_dict(root)
            print(f"Project architecture loaded from {file_path}")
        except Exception as e:
            print(f"Error loading XML file: {e}")

    def _xml_to_dict(self, element):
        """Рекурсивно преобразует XML элемент в словарь."""
        result = {element.tag: {} if element.attrib else None}
        children = list(element)
        if children:
            dd = {}
            for child in children:
                child_dict = self._xml_to_dict(child)
                dd[child.tag] = child_dict[child.tag]
            result = {element.tag: dd}
        elif element.text:
            text = element.text.strip()
            result[element.tag] = text
        return result

    def create_project_structure(self, root_path: str = ""):
        if '\\' not in root_path:
            self.current_path = self.find_project_root()
            root_path = self.current_path
        """Создает структуру проекта на основе архитектуры."""
        for folder_name, contents in self.architecture.items():
            self._create_directory(root_path, folder_name, contents)

    def _create_directory(self, path, folder_name, contents):
        folder_path = os.path.join(path, folder_name)
        if '.' not in folder_name:
            os.makedirs(folder_path, exist_ok=True)
            for name, detail in contents.items():
                if '.' not in name:
                    self._create_directory(folder_path, name, detail)
                elif '.' in name:
                    self._create_python_file(folder_path, name, detail)
        elif '.' in folder_name:
            self._create_python_file(path, folder_name, contents)

    def _create_python_file(self, path, file_name, details):
        file_path = os.path.join(path, f"{file_name}")

        # Проверяем, существует ли файл
        if os.path.exists(file_path):
            print(f"Файл '{file_path}' уже существует. Игнорируем создание.")
            return

        # Если файл не существует, создаем его
        with open(file_path, 'w', encoding='utf-8') as f:
            if 'classes' in details:
                for class_info in details['classes']:
                    f.write(f"class {class_info['name']}:\n")
                    for method in class_info['methods']:
                        f.write(f"    def {method}(self):\n")
                        f.write("        pass\n\n")
            if 'functions' in details:
                for func in details['functions']:
                    f.write(f"def {func}():\n")
                    f.write("    pass\n\n")
            if 'variables' in details:
                for var in details['variables']:
                    f.write(f"{var} = None\n")

    def find_project_root(self, start_path: str = '.') -> Union[str, None]:
        root_indicators = ['.venv', 'requirements.txt', 'pyproject.toml', '.git']
        self.current_path = os.path.abspath(start_path)

        while self.current_path:
            if any(os.path.exists(os.path.join(self.current_path, indicator)) for indicator in root_indicators):
                return self.current_path
            new_path = os.path.dirname(self.current_path)
            if new_path == self.current_path:  # Достигли корня
                break
            self.current_path = new_path
        return None


if __name__ == "__main__":
    creator = ProjectCreator()
    creator.load_from_json("architecture.json")
    creator.create_project_structure()
