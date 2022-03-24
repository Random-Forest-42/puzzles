from copy import deepcopy
import sys, os
import numpy
import random
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


# goal = 8
goal = 448
# goal = 33
input_numbers = [2, 2, 5, 5, 25]
input_numbers = [5, 6, 10, 10, 11, 50]
# input_numbers = [2, 2, 3, 5, 25, 100]
# input_numbers = [1, 2, 3, 1]

n = len(input_numbers)



def operate(inputs, a, b):
    outcomes = []
    outcomes.append(
        {
            "letter": (a, "+", b),
            "inputs": inputs + [a+b],
                "result": a+b,
        }
    )
    outcomes.append(
        {
            "letter": (a, "*", b),
            "inputs": inputs + [a*b],
                "result": a*b,
        }
    )
    if a > b:
        outcomes.append(
            {
                "letter": (a, "-", b),
                "inputs": inputs + [a-b],
                "result": a-b,
            }
        )
    elif b > a:
        outcomes.append(
            {
                "letter": (b, "-", a),
                "inputs": inputs + [b-a],
                "result": b-a,
            }
        )
    if a%b == 0:
        outcomes.append(
            {
                "letter": (a, "/", b),
                "inputs": inputs + [a/b],
                "result": a/b,
            }
        )
    elif b%a == 0:
        outcomes.append(
            {
                "letter": (b, "/", a),
                "inputs": inputs + [b/a],
                "result": b/a,
            }
        )
    return outcomes


words = []

def get_all_posible_letters(inputs):
    posible_letters = []
    for i, a in enumerate(inputs):
        c_inputs = deepcopy(inputs)
        c_inputs.pop(i)
        for j, b in enumerate(c_inputs):
            c2_inputs = deepcopy(c_inputs)
            c2_inputs.pop(j)
            outcomes = operate(c2_inputs, a, b)
            posible_letters.append(outcomes)
    return posible_letters

l1 = get_all_posible_letters(input_numbers)

def iterate_step(l, step_number):
    for l_a in l:
        for l in l_a:
            if l["result"] == goal:
                print(l)
                break
            l[f"step_{step_number}"] = get_all_posible_letters[l["inputs"]]

# l2 = iterate_step(l1)

goal_found = False
for l_a in l1:
    if not goal_found:
        for l in l_a:
            if l["result"] == goal:
                print(l)
                break
            if not goal_found:
                l["step_2"] = get_all_posible_letters(l["inputs"])
                for l_a2 in l["step_2"]:
                    if not goal_found:
                        for l_2 in l_a2:
                            if l_2["result"] == goal:
                                goal_found = True
                                print("--------")
                                print(l["letter"])
                                print(l_2["letter"])
                                print("--------")
                                break
                            l["step_3"] = get_all_posible_letters(l_2["inputs"])
                            for l_a3 in l["step_3"]:
                                if not goal_found:
                                    for l_3 in l_a3:
                                        if l_3["result"] == goal:
                                            goal_found = True
                                            print("--------")
                                            print(l["letter"])
                                            print(l_2["letter"])
                                            print(l_3["letter"])
                                            print("--------")
                                            break
                                        l["step_4"] = get_all_posible_letters(l_3["inputs"])
                                        for l_a4 in l["step_3"]:
                                            if not goal_found:
                                                for l_4 in l_a4:
                                                    if l_4["result"] == goal:
                                                        goal_found = True
                                                        print("--------")
                                                        print(l["letter"])
                                                        print(l_2["letter"])
                                                        print(l_3["letter"])
                                                        print(l_4["letter"])
                                                        print("--------")
                                                        break
                                                    l["step_5"] = get_all_posible_letters(l_4["inputs"])
                                                    for l_a5 in l["step_4"]:
                                                        if not goal_found:
                                                            for l_5 in l_a5:
                                                                if l_5["result"] == goal:
                                                                    goal_found = True
                                                                    print("--------")
                                                                    print(l["letter"])
                                                                    print(l_2["letter"])
                                                                    print(l_3["letter"])
                                                                    print(l_4["letter"])
                                                                    print(l_5["letter"])
                                                                    print("--------")
                                                                    break





