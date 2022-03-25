from copy import deepcopy

'''
INPUT:
    1 numero objetivo
        ej: 650
    6 numeros para realizar operaciones
        ej: 2, 2, 5, 5, 25
conseguir en maximo 5 operaciones el numero objetivo
reglas:
    un numero solo se puede usar una vez
    el resultado de una operacion se puede utilizar una sola vez
    operaciones permitidas: +, -, %, x
        se pueden repetir
    no se puede trabajar con numeros negativos ni decimales
'''

# kids
goal = 30
input_numbers = [4,5,5,7,8,9]
# medium
# goal = 280
# input_numbers = [1,2,6,6,11,100]
# hard
# goal = 525
# input_numbers = [8,8,10,12,12,25]


def get_letters(a,b):
    possible_letters = []
    possible_letters.append({
        "letter": (a, "+", b),
        "result": a+b,
    })
    possible_letters.append({
        "letter": (a, "*", b),
        "result": a*b,
    })
    if a > b:
        possible_letters.append({
            "letter": (a, "-", b),
            "result": a-b,
        })
    elif b > a:
        possible_letters.append({
            "letter": (b, "-", a),
            "result": b-a,
        })
    if a%b == 0:
        possible_letters.append({
            "letter": (a, "/", b),
            "result": a/b,
        })
    elif b%a == 0:
        possible_letters.append({
            "letter": (b, "/", a),
            "result": b/a,
        })
    return possible_letters

def one_step(trees, goal):
    new_trees = []
    result_found = False
    for t in trees:
        input = t["input"]
        letras = t["letters"]
        for i, a in enumerate(input):
            for j, b in enumerate(input[i+1:]):
                new_inputs = deepcopy(input)
                new_inputs.pop(i+j+1)
                new_inputs.pop(i)
                possible_letters = get_letters(a,b)
                for pl in possible_letters:
                    result = pl["result"]
                    if result == goal:
                        if not result_found:
                            print(letras + [pl["letter"]])
                        result_found = True
                    new_trees.append({
                        "input": new_inputs + [result],
                        "letters": letras + [pl["letter"]],
                        "result": result
                    })
    return new_trees, result_found


def find_result(goal, input_numbers):
    result_found = False
    print(f"goal: {goal}")
    trees = [{
        "input": input_numbers,
        "letters": [],
        "result": 0,
    }]

    max_steps = 5
    for i in range(max_steps):
        if not result_found:
            print(f"profundidad {i+1}")
            trees, result_found = one_step(trees, goal)

    if not result_found:
        print("no se ha encontrado solucion")

find_result(goal, input_numbers)
