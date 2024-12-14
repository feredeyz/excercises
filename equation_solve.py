import re

def has_numbers(string):
    return any(char.isdigit() for char in str(string))


def solve_eq_alg(eq: str):
    eq = eq.split(' ')
    x = []
    wo_x = []
    for n in eq:
        if n in ("+", "-", "="):
            continue
        if "=" in n:
            n = n[1:]
        if 'x' in n:
            if ("+" in n or "-" in n) and has_numbers(n):
                x.append(n[:-1])
                continue

            idx = eq.index(n)
            if idx == 0:
                x.append(n[:-1])
                continue
            for k in range(idx, 0, -1):
                if eq[k] in ("+", "-", "*", "/"):
                    x.append(eq[k] + n[:-1])
                    continue
            
            wo_x.append(n)

    for n in eq:
        if n in ("+", "-", "="):
            continue
        if 'x' not in n:
            if ("+" in n or "-" in n) and has_numbers(n):
                wo_x.append(n)
                continue

            idx = eq.index(n)

            if "=" in n:
                n = n[1:]
                eq[idx] = n

            if idx == 0:
                wo_x.append(n)
                continue
            for k in range(idx, 0, -1):
                if eq[k] in ("+", "-", "*", "/"):
                    wo_x.append(eq[k] + n)
                    continue
            
            wo_x.append(n)

    return x, wo_x, ''.join(x), ''.join(wo_x)

    a = eval(''.join(x))
    b = eval(''.join(wo_x))

    if a == 0 and b != 0:
        return ()
    elif a == 0 and b == 0:
        return ('inf')
    elif a != 0 and b != 0:
        return b / a

def solve_eq_reg(eq):
    wo_x = re.findall(r'(?<!x)[+-]?\s*\d+(?!\s*\w)', eq)
    x = re.findall(r'[+-]?\s*\d*x', eq)

    res_x = ''
    res_wo_x = ''
    for n in wo_x:
        n = n.strip()
        if n[0] not in ('+', '-', '*', '/'):
            n = "+" + n
        res_wo_x += n

    for n in x:
        n = n.strip()[:-1]
        if n[0] not in ('+', '-', '*', '/'):
            n = "+" + n
        res_x += n

    a = eval(res_x)
    b = eval(res_wo_x)

    if a == 0 and b == 0:
        return ('inf')
    elif a == 0 and b != 0:
        return ()
    elif a != 0 and b != 0:
        return b / a
        



    


def main():
    eq = input('Введите уравнение: ')
    print(solve_eq_reg(eq))

if __name__ == "__main__":
    main()

# 2x +1 + 2 +3x = 0