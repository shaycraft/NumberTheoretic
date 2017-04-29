def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    dp, xp, yp = extended_euclid(b, a % b)
    d = dp
    x = yp
    y = xp - int(a/b) * yp
    #print "DEBUG: {0} = {1}*{2} + {3}*{4}".format(d, a, x, b, y)
    return d, x, y


def modular_linear_equation_solver(a, b, n): # solves for x -> ax = b mod n
    solutions = []
    d, xp, yp = extended_euclid(a, n)
    if b % d == 0:
        x0 = xp * int(b/d) % n
        for i in range(0, d):
            solutions.append((x0 + i * int(n/d)) % n)
    return solutions