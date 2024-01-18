import csv
import json

def convert_csv_to_json(csv_file_path, json_file_path=None):
    # Открываем CSV файл и создаем DictReader
    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        data_list = []

        # Проходим по каждой строке CSV файла
        for row in csv_reader:
            data_list.append(row)

    # Преобразуем список словарей в JSON строку с отступами
    json_data = json.dumps(data_list, indent=4)

    # Если указан путь для сохранения JSON файла, сохраняем
    if json_file_path:
        with open(json_file_path, 'w') as json_file:
            json_file.write(json_data)

    print(json_data)

    return json_data

# Пример использования
csv_file_path = "путь_к_вашему_файлу.csv"
json_file_path = "путь_к_вашему_файлу.json"
convert_csv_to_json(csv_file_path, json_file_path)
