def _rpn(cache, s):
    n1 = cache.pop()
    n2 = cache.pop()
    if s == "+":
        cache.append(n2 + n1)
    elif s == "/":
        cache.append(n2 / n1)

def rpn_calc(exp):
    exp_list = exp.split()
    cache = []
    for s in exp_list:
        if s in "+-*/":
           _rpn(cache, s)
        else:
            cache.append(int(s))
    return cache[0]