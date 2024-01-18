def find_common_participants(group1, group2, delimiter=','):
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    common_participants = sorted(participants1.intersection(participants2))

    return common_participants

# Пример использования функции:
group1 = "Иванов,Петров,Сидоров,Смирнов"
group2 = "Петров,Сидоров,Козлов,Кузнецов"

result = find_common_participants(group1, group2)

if result:
    print(f"Общие участники: {result}")
else:
    print("Общих участников не найдено.")
