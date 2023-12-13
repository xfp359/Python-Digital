def missing_element(lst):
  total_sum = sum(x for x in lst if x is not None)
  total_count = len(lst)
  average = total_sum / (total_count - 1)
  missing_element = average * total_count - total_sum
  for i in range(len(lst)):
      if lst[i] is None:
          lst[i] = missing_element
          break  # Найден пропущенный элемент, прекращаем цикл

  return lst

numbers = [1, 2, None, 4, 5]
result = missing_element(numbers)
print(f"Список с заменённым пропущенным элементом: {result}")