"""Тестовый модуль"""
import pandas as pd

def frame(columns: list, data: dict):
    """Метод для создания фрейма"""
    result = pd.DataFrame(
        columns=columns,
        data=data
    )
    return result