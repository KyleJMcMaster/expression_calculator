def calcExpression(expression):
    print("calculating expression: " + str(expression))

    # check if expression is contained within brackets
    if inBrackets(expression):
        expression = expression.strip()[1:-1]
        print(expression)
    term_num = 0
    bracket_count = 0
    terms = ['']
    separators = ['']
    for char in expression:
        if char == ' ':
            pass
        elif char == '(':
            bracket_count += 1
            terms[term_num] += '('
        elif char == ')':
            bracket_count -= 1
            terms[term_num] += ')'
        elif bracket_count == 0 and (char == '-' or char == '+'):
            if terms[term_num][-1] not in ['*', '/', '^']:
                term_num += 1
                terms.append('')
                separators.append(char)
            else:
                terms[term_num] += str(char)
        else:
            terms[term_num] += str(char)

    total = 0
    print(terms)
    print(separators)
    for i in range(len(terms)):
        if separators[i] == '-':
            add = False
        else:
            add = True
        if add:
            total += calcTerm(terms[i])
        else:
            total -= calcTerm(terms[i])

    return total


def calcTerm(term):
    print("calculating term: " + str(term))
    fac_num = 0
    bracket_count = 0
    factors = ['']
    separators = ['']
    for char in term:
        if char == '(':
            bracket_count += 1
            factors[fac_num] += '('
        elif char == ')':
            bracket_count -= 1
            factors[fac_num] += ')'
        elif bracket_count == 0 and (char == '*' or char == '/'):
            fac_num += 1
            factors.append('')
            separators.append(char)
        else:
            factors[fac_num] += str(char)

    print(factors)
    print(separators)


    product = 1.0

    for i in range(len(factors)):
        # default first separator is ''
        if separators[i] == '/':
            multiply = False
        else:
            multiply = True
        if multiply:
            product *= float(calcFactor(factors[i]))
        else:
            product /= float(calcFactor(factors[i]))
    # print(product)
    return product


def calcFactor(factor):
    print("calculating factor: " + str(factor))
    prim_num = 0
    bracket_count = 0
    primaries = ['']
    separators = ['']
    for char in factor:
        if char == '(':
            bracket_count += 1
            primaries[prim_num] += '('
        elif char == ')':
            bracket_count -= 1
            primaries[prim_num] += ')'
        elif bracket_count == 0 and char == '^':
            prim_num += 1
            primaries.append('')
            separators.append(char)
        else:
            primaries[prim_num] += str(char)

    result = float(calcPrimaries(primaries[0]))
    for i in range(1, len(primaries)):
        result **= float(calcPrimaries(primaries[i]))

    return result


def calcPrimaries(primary):
    print("calculating primary: " + str(primary))
    if inBrackets(primary):
        primary = float(calcExpression(primary))

    return primary


def inBrackets(statement):
    if statement[0] == '(':
        bracket_count = 1
        i = 1
        while bracket_count != 0 or i == len(statement)-1:
            if statement[i] == '(':
                bracket_count += 1
            elif statement[i] == ')':
                bracket_count -= 1
            i += 1
        #Check if it made it all the way through before finding a matching pair
        if i != len(statement):
            return False
        else:
            return True


input_statement = input("Enter your statement: ")
print("calc expression: " + str(calcExpression(input_statement)))
