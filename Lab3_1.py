def find_item_index(product_list, item_to_find):
  try:
      index = product_list.index(item_to_find)
      return index
  except ValueError:
      return None

# Пример использования функции:
products = ["яблоко", "груша", "апельсин", "банан", "яблоко"]
item = "яблоко"

result = find_item_index(products, item)

if result is not None:
  print(f"Индекс первого вхождения товара '{item}': {result}")
else:
  print(f"Товар '{item}' не найден в списке.")
