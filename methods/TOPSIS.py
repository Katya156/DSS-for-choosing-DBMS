import numpy as np
from info.expert_values import expert_values

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
    decision_matrix: numpy array формы (m, n)
    weights: веса критериев (длина n)
    benefit_criteria: список булевых значений, True — критерий на максимум, False — на минимум
    """
    data = expert_values[expert_values.index.isin(names)][list(criteria.keys())]
    # Веса критериев (считаем методом энтропии)
    weights = entropy_weights(np.array(data))

    # Логика критериев: True — критерий на максимум, False — на минимум
    # Например: [цена (min), производительность (max), энергопотребление (min)]
    benefit_criteria = []
    for i in data.columns:
        if i not in ['К7.3. Максимальный размер адресуемой памяти', 'К8.1. Максимальная стоимость лицензии', 'К8.2. Рейтинг СУБД']:
            benefit_criteria.append(True)
        else:
            benefit_criteria.append(False)

    # Шаг 1: Нормализация
    norm_matrix = data / np.sqrt((data ** 2).sum(axis=0))

    # Шаг 2: Умножение на веса
    weighted_matrix = norm_matrix * weights

    # Шаг 3: Определение идеальных и антиидеальных точек
    ideal = np.max(weighted_matrix, axis=0) * benefit_criteria + \
            np.min(weighted_matrix, axis=0) * (~np.array(benefit_criteria))

    anti_ideal = np.min(weighted_matrix, axis=0) * benefit_criteria + \
                 np.max(weighted_matrix, axis=0) * (~np.array(benefit_criteria))

    # Шаг 4: Расчет расстояний до идеальной и антиидеальной точек
    d_pos = np.linalg.norm(weighted_matrix - ideal, axis=1)
    d_neg = np.linalg.norm(weighted_matrix - anti_ideal, axis=1)

    # Шаг 5: Расчет близости к идеалу
    scores = d_neg / (d_pos + d_neg)

    # Критерии: 1 — прибыльный (чем выше — лучше), 0 — затратный (чем меньше — лучше)

    # Преобразуем веса критериев в словарь, где ключи — это имена критериев, а значения — их веса
    weights_dict = {data.columns[i]: weights[i] for i in range(len(data.columns))}

    # Преобразуем рейтинг в словарь, где ключи — это альтернативы, а значения — их оценки
    scores_dict = {data.index[i]: scores[i] for i in range(len(data.index))}

    scores_dict = dict(sorted(scores_dict.items(), key=lambda x: -x[1]))
    print("Веса критериев (энтропия):", weights_dict)
    print("Оценки TOPSIS:", scores_dict)

    return scores_dict