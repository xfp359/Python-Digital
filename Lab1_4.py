# Список пользователей, посетивших сайт
users_visits = ["user1", "user2", "user3", "user1", "user4", "user2", "user5"]

# Создание словаря статистики с начальными значениями
statistics_dict = {"Общее количество": 0, "Уникальные посещения": 0}

# Установка новых значений в словаре
statistics_dict["Общее количество"] = len(users_visits)
statistics_dict["Уникальные посещения"] = len(set(users_visits))
print(statistics_dict)
