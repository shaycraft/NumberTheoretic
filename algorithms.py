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


def modular_exponentiation(a, b, n):
    c = 0
    d = 1
   #print 'DEBUG: bin(b) = ' + str(bin(b))
    for i in range(0, len(bin(b))-1)[::-1]:
        c = c << 1
        d = d * d % n
        if (b >> i) & 1 == 1:
            c = c + 1
            d = d * a %n
    return d

