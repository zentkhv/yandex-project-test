"""Модуль для отладки."""

# Глобальные пакеты
# import json
# import sys

# Локальные пакеты
from src import model


if __name__ == "__main__":
    # test_dict = {1: 1, 2: 2, 3: 3}
    #
    # for key, value in test_dict.items():
    #     print(f"{key}: {value}")
    #
    # json_dict = json.dumps(test_dict, ensure_ascii=False, indent=4)
    # print(json_dict)

    columns = ["Имя", "Возраст"]
    data = [{"Имя": "Михаил", "Возраст": 18}, {"Имя": "Александр", "Возраст": 20}]
    frame = model.frame(columns=columns, data=data)
    print(frame)
