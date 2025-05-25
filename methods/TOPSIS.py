import numpy as np
from data.dbms_values import dbms_values
from topsispy import topsis as tps

def entropy_weights(decision_matrix):
    """
    Расчет весов критериев методом энтропии.
    decision_matrix: numpy array формы (m, n), где m — альтернативы, n — критерии
    """
    # Нормализация данных по столбцам
    P = decision_matrix / decision_matrix.sum(axis=0)
    # Замена 0 на маленькое значение, чтобы избежать log(0)
    P = np.where(P == 0, 1e-12, P)

    # Вычисление энтропии
    m, n = decision_matrix.shape
    k = 1 / np.log(m)
    E = -k * np.sum(P * np.log(P), axis=0)

    # Степень отклонения
    d = 1 - E

    # Вес = нормализация степени отклонения
    weights = d / d.sum()
    return weights

def topsis(criteria, names):
    """
    Метод TOPSIS.
    data: numpy array формы (m, n)
    weights: веса критериев (длина n)
    benefit_criteria: список булевых значений, True — критерий на максимум, False — на минимум
    """
    data = dbms_values[dbms_values.index.isin(names)][list(criteria.keys())]
    # Веса критериев (считаем методом энтропии)
    weights = entropy_weights(np.array(data))

    # Логика критериев: 1 — критерий на максимум, -1 — на минимум
    benefit_criteria = []
    for i in data.columns:
        if i not in ['К7.3. Максимальный размер адресуемой памяти', 'К8.1. Максимальная стоимость лицензии', 'К8.2. Рейтинг СУБД']:
            benefit_criteria.append(1)
        else:
            benefit_criteria.append(-1)

    # Применение метода TOPSIS
    best_rank, scores = tps(data.values, weights, benefit_criteria)

    # Преобразуем веса критериев в словарь, где ключи — это имена критериев, а значения — их веса
    weights_dict = {data.columns[i]: weights[i] for i in range(len(data.columns))}

    # Преобразуем рейтинг в словарь, где ключи — это альтернативы, а значения — их оценки
    scores_dict = {data.index[i]: scores[i] for i in range(len(data.index))}

    scores_dict = dict(sorted(scores_dict.items(), key=lambda x: -x[1]))
    print("Веса критериев (энтропия):", weights_dict)
    print("Оценки TOPSIS:", scores_dict)

    return scores_dict