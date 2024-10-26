import json


def decode_unicode_string(s):
    try:
        return s.encode('latin1').decode('unicode_escape')
    except Exception as e:
        print(f"Ошибка при декодировании строки: {s} - {e}")
        return s


def process_table(table_data):
    for item in table_data:
        for key, value in item.items():
            if key in ['text', 'name']:
                item[key] = decode_unicode_string(value)
            elif isinstance(value, dict):
                process_table([value])
            elif isinstance(value, list):
                process_table(value)


def main(input_file_path, output_file_path):
    # Чтение данных из файла
    with open(input_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Обработка данных
    for table_name, table_data in data.items():
        print(f"Обработка таблицы: {table_name}")
        process_table(table_data)

    # Запись откорректированных данных в новый файл
    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Данные успешно записаны в {output_file_path}")


# Пример использования
if __name__ == "__main__":
    input_file = "output_ui.json"
    output_file = "decoded_data.json"
    main(input_file, output_file)
