def tpl_sort(tpl):
    if all(isinstance(x, int) for x in tpl):
        return tuple(sorted(tpl))
    else:
        return tpl


tpl = (6, 3, -1, 8, 4, 10, -5)
print(tpl_sort(tpl))