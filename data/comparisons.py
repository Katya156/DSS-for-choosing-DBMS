from itertools import combinations
from data.dbms_values import dbms_values

def saaty_scale(diff):
    """Преобразует разность оценок в шкалу Саати."""
    mapping = {
        0: 1,
        1: 3,
        2: 5,
        3: 7,
        4: 9
    }
    if diff >= 0:
        return mapping.get(diff, 9)
    else:
        return 1 / mapping.get(abs(diff), 9)

def convert_to_pairwise_dict(df):
    result = {}
    for criterion in df.columns:
        comparisons = {}
        for a, b in combinations(df.index, 2):
            score_a = df.loc[a, criterion]
            score_b = df.loc[b, criterion]
            diff = int(round(score_a - score_b))
            comparisons[(a, b)] = saaty_scale(diff)
        result[criterion] = comparisons
    return result

pairwise_dict = convert_to_pairwise_dict(dbms_values)
