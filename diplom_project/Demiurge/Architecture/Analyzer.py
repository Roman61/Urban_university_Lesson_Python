import ast
import json
import os
from typing import Dict, List, Union
import xml.etree.ElementTree as ET


class ProjectAnalyzer:
    def __init__(self, root_directory: str = None, ignore_list: List[str] = None):
        self.root_directory = root_directory or self.find_project_root()
        self.ignore_list = ignore_list or []
        self.architecture = {}

    def find_project_root(self, start_path: str = '.') -> Union[str, None]:
        root_indicators = ['.venv', 'requirements.txt', 'pyproject.toml', '.git']
        current_path = os.path.abspath(start_path)

        while current_path:
            if any(os.path.exists(os.path.join(current_path, indicator)) for indicator in root_indicators):
                return current_path
            new_path = os.path.dirname(current_path)
            if new_path == current_path:  # Достигли корня
                break
            current_path = new_path
        return None

    def get_architecture(self) -> None:
        project_name = os.path.basename(self.root_directory)
        self.architecture[project_name] = self.traverse_directory(self.root_directory)

    def traverse_directory(self, dir_path: str) -> Dict[str, Union[Dict, Dict[str, dict]]]:
        file_tree = {}
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)

            if item in self.ignore_list:
                continue

            if os.path.isdir(item_path):
                file_tree[item] = self.traverse_directory(item_path)
            else:
                if item.endswith('.py'):
                    file_tree[item] = self.file_analyzer(item_path)
                # Не обрабатываем не-Python файлы, такие как .txt, .md и т.д.

        return file_tree

    def file_analyzer(self, file_path: str) -> dict:
        classes, functions, variables = self.parse_python_file_details(file_path)
        return {
            'classes': classes,
            'functions': functions,
            'variables': variables
        }

    def parse_python_file(self, file_path: str) -> tuple:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                node = ast.parse(f.read(), filename=file_path)

            classes = [n.name for n in node.body if isinstance(n, ast.ClassDef)]
            functions = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]
            variables = [n.targets[0].id for n in node.body
                         if isinstance(n, ast.Assign) and isinstance(n.targets[0], ast.Name)]
            return classes, functions, variables

        except Exception as e:
            print(f"Error parsing file {file_path}: {e}")
            return [], [], []  # Возвращаем пустые списки в случае ошибки

    def parse_python_file_details(self, file_path: str) -> tuple:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                node = ast.parse(f.read(), filename=file_path)

            classes = []
            functions = []
            variables = []

            for item in node.body:
                if isinstance(item, ast.ClassDef):
                    # Собираем информацию о классе
                    class_info = {
                        'name': item.name,
                        'methods': [],
                        'fields': []
                    }

                    # Проходим по телу класса
                    for class_item in item.body:
                        if isinstance(class_item, ast.FunctionDef):
                            # Это метод класса
                            class_info['methods'].append(class_item.name)
                        elif isinstance(class_item, ast.Assign):
                            # Поле класса
                            for target in class_item.targets:
                                if isinstance(target, ast.Name):
                                    class_info['fields'].append(target.id)

                    classes.append(class_info)  # Добавляем информацию о классе

                elif isinstance(item, ast.FunctionDef):
                    # Это функция на уровне модуля
                    functions.append(item.name)
                elif isinstance(item, ast.Assign):
                    # Переменные на уровне модуля
                    for target in item.targets:
                        if isinstance(target, ast.Name):
                            variables.append(target.id)

            return classes, functions, variables

        except Exception as e:
            print(f"Error parsing file {file_path}: {e}")
            return [], [], []  # Возвращаем пустые списки в случае ошибки

    def print_architecture(self, architecture: Dict = None, indent: int = 0) -> None:
        if architecture is None:
            architecture = self.architecture

        indent_str = "│  " * indent
        for folder, content in architecture.items():
            if isinstance(content, dict):
                print(f"{indent_str}├── {folder}/")
                self.print_architecture(content, indent + 1)
            else:  # Это файл с данными
                self._print_file_details(folder, content, indent_str)

    def _print_file_details(self, file_name: str, details: dict, indent_str: str) -> None:
        if details:
            flag = False
            print(f"{indent_str}├── {file_name}")
            for key in ['classes', 'functions', 'variables']:
                if key in details:  # Проверяем на наличие элементов через get
                    flag = True
                    print(f"{indent_str}│  ├── {key.capitalize()}: {', '.join(details[key])}")
            if not flag:
                for key in details:
                    print(f"{indent_str}│  ├── {key}")

    def save_architecture_to_json(self, filename: str) -> None:
        try:
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(self.architecture, json_file, ensure_ascii=False, indent=4)
            print(f"Architecture saved to {filename} in JSON format.")
        except Exception as e:
            print(f"Error saving architecture to JSON: {e}")

    def save_architecture_to_xml(self, filename: str) -> None:
        try:
            def build_xml_tree(data, parent):
                for key, value in data.items():
                    element = ET.SubElement(parent, key)
                    if isinstance(value, dict):
                        build_xml_tree(value, element)
                    else:
                        element.text = str(value)

            root = ET.Element('Architecture')
            build_xml_tree(self.architecture, root)

            tree = ET.ElementTree(root)
            tree.write(filename, encoding='utf-8', xml_declaration=True)
            print(f"Architecture saved to {filename} in XML format.")
        except Exception as e:
            print(f"Error saving architecture to XML: {e}")


# Пример использования
if __name__ == "__main__":
    ignored_items = ['.venv', '.gitignore']
    analyzer = ProjectAnalyzer(ignore_list=ignored_items)
    analyzer.get_architecture()

    # Сохраняем архитектуру в JSON и XML
    # analyzer.save_architecture_to_json('architecture.json')
    # analyzer.save_architecture_to_xml('architecture.xml')

    analyzer.print_architecture()
