def sl_ss (L) :
    result_set = []
    valid_obj = (list, tuple, set)
    def int_extract (text) :
        for k in text:
            if isinstance(k, int):
                result_set.append(k)
            elif isinstance(k, valid_obj):
                int_extract(k)
        return None
    for i in L:
        if isinstance(i, int):
            result_set.append(i)
        elif isinstance(i, valid_obj):
            int_extract(i)
    unique_set = sorted(set(result_set))
    if len(unique_set) < 2:
        return None
    return (unique_set[1], unique_set[-2])
print(sl_ss([17, 89, [178, 374, (34, 103)], {67, 99}]))