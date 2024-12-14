import re

def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))

class Parser:
    def __init__(self, expr):
        self.expr = expr.replace(' ', '')
        self.p1 = r"[+-]?\d*[a-z](\^\d)*"
        self.p2 = r'(?<!\^)[-+]?\s*\d+(?!x)'
        self.monomials = {}
    
    def parse(self):
        free = re.finditer(self.p2, self.expr)
        free= sum([int(x.group(0)) for x in list(free)])
        print(free)
        via_x = [i.group(0) for i in re.finditer(self.p1, self.expr)]

        for x in via_x:
            unique = ''.join([i.group(0) for i in re.finditer(r'[a-z]\^\d+', x)])
            if unique == '':
                unique = "x^1"
            power = unique[:-2]
            if not power:
                power = 1
            if not self.monomials.get(unique):
                self.monomials[unique] = []
            coeff = re.match(r'[-+]?\d*', x).group(0)
            if has_numbers(coeff):
                self.monomials[unique].append(int(coeff))
            else:
                self.monomials[unique].append(int(coeff + "1"))
            

        polynomial = ''
        for x in self.monomials:
            polynomial += str(sum(self.monomials[x])) + x
        if str(free)[0] not in ("-", "+"):
            return polynomial + "+" + str(free)
        else:
            return polynomial + str(free)
        
       
p = Parser('2x^1 +1 -x^2 - 2x -1')
print(p.parse())