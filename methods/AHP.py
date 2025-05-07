import ahpy
from data.comparisons import pairwise_dict

def ahp(criteria_in, criteria_out, names):
    # подсчет весов внутренних и внешних критериев
    criteria_out = ahpy.Compare('Criteria', criteria_out)
    criteria_out_weights = criteria_out.target_weights

    criteria_in = ahpy.Compare('Criteria', criteria_in)
    criteria_in_weights = criteria_in.target_weights

    for i in criteria_out_weights:
        for j in criteria_in_weights:
            if j.startswith(f'{i.split()[0]}'):
                criteria_in_weights[j] *= criteria_out_weights[i]

    print(f'Итоговые веса критериев: {criteria_in_weights}')
    alternatives = {key: 0 for key in pairwise_dict if key in criteria_in_weights}
    for i in alternatives:
        alternative = ahpy.Compare(i, pairwise_dict[i])
        alternatives[i] = alternative.target_weights

    print(f'Веса альтернатив по каждому критерию: {alternatives}')
    res = {j: 0 for i in alternatives for j in alternatives[i] if j in names}
    for i in alternatives:
        for j in alternatives[i]:
            if j in names:
                alternatives[i][j] *= criteria_in_weights[i]
                res[j] += alternatives[i][j]
    res = dict(sorted(res.items(), key = lambda x: -x[1]))
    print(f'Итоговые веса альтернатив с учетом весов критериев: {res}')
    return res