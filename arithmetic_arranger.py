#Create a function that receives a list of strings that are arithmetic problems and returns the problems arranged vertically and side-by-side. 
# The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

#def variável

def arithmetic_arranger (problems, solutions = False):
    if len (problems) >5:
        return 'Eror: Too many problems.'

#def arranjo

first_operand = []
second_operand =[]
operator =[]
third_line =[]
fourth_line =[]

for problem in problems :
    symbols = problem.split()
    first_operand.append (symbols [0])
    operator.append (symbols [1])
    second_operand.append (symbols [2])

#def operador

if '*' in operator or '/' in operator:
    return "Error: The operator must be '+' or '-'"

#verf fo e so int

if i in range (len(first_operand)):
    if not(first_operand[i].isdigit() and second_operand[i].isdigit()):
        return 'Error: Number must only contain digits.'

#verif num maior

longest_number = []
for i in range(len(first_operand)):
    longest_number.append(max(len first_operand[i], len(second_operand [i])))
for i in range(len(longest_number)):
    third_line.append ('-'(longest_number[i]+2))

#arranjo

first_line = []
for i in range(len(first_operand):
    if len (first_operand[i])) > len (second_operand[i]):
        first_line.append (''+ first_operand[i])
    else:
        first_line.append('' * len(second_operand[i]) - len(first_operand[i] + 2) + first_operand [i])

second_line = []
for i in range (len(second_operand)):
    if len (second_operand[i]) > len (first_operand[i]):
        second_line.append(operator[i] + '' + second_operand[i])
    else:
        second_line.append(operator[i]+ '' * len(first_operand[i] - len (second_operand[i])+1)+ second_operand[i])

#sol

if solution :
    for i in range(len(first_operand)):
        if operator == '+'
            a = str (int(first_operand[i]) + int (second_operand[i]))
        else:
            a = str (int(first_operand[i]) - int (second_operand[i]))
        if len (a) > max (len(first_operand[i]), len (second_operand[i])):
            fourth_line = ("" + a)
        else:
            fourth_line.append("" * (max(len(first_operand[i]), len (second_operand)) - len (a) + 2) +a)
        arranged_problems = " ".join(first_line) + '\n' + " ".join(second_line) + "\n" + " ".join(third_line) + "\n" + " ".join(fourth_line)
else:
        arranged_problems = " ".join(first_line) + '\n' + " ".join(second_line) + "\n" + " ".join(third_line)

return arranged_problems