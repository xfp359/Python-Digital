import json

def calculate_sum_of_products(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    sum_of_products = 0.0

    # Проходим по каждому словарю в списке
    for item in data:
        product = item["score"] * item["weight"]
        sum_of_products += product

    sum_of_products = round(sum_of_products, 3)
    print(f"Сумма произведений: {sum_of_products}")

    return sum_of_products

# Пример использования
json_file_path = "/path/to/your/file.json"
result = calculate_sum_of_products(json_file_path)
