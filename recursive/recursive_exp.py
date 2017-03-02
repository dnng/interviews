def exp(b, e):
    if e == 1:
        return b
    if e%2:
        return b * exp(b*b, e/2)
    else:
        return exp(b*b, e/2)

