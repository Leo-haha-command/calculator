import re
import sys
import math
#TODO: add squrt parser
def eval_bracket(in_All):
    start = in_All.rfind("(")
    end = in_All.find(")",start+1)
    if start == -1 or end == -1:
        return in_All
    content = in_All[start+1:end]
    if content == "":
        return "empty" #because i just want the value inside the blanket
    y = split(content)
    k = calculate_factorial(y)
    x = power(k)
    q = calculate_times(x)
    if q == ["Syntax Error"]:
        return q
    e = calculate_pm(q)
    if start >= 4 and in_All[start-4:start] == "sqrt":
        value = square_root(float(e[0]))
        if value == "imaginary" :
            return False
        new = in_All[:start-4] + str(value) + in_All[end+1:]
    elif start >= 3 and in_All[start-3:start] == "log":
        if float(e[0]) <= 0:
            return False
        value = log(float(e[0]))
        new = in_All[:start-3] + str(value) + in_All[end+1:]
    elif start >= 3 and in_All[start-3:start] == "sin":
        value = sin(float(e[0]))
        new = in_All[:start-3] + str(value) + in_All[end+1:]
    elif start >= 3 and in_All[start-3:start] == "cos":
        value = cos(float(e[0]))
        new = in_All[:start-3] + str(value) + in_All[end+1:]
    elif start >= 3 and in_All[start-3:start] == "tan":
        value = sin(float(e[0])) /cos(float(e[0]))
        new = in_All[:start-3] + str(value) + in_All[end+1:]
    else:
        result = e[0]
        new = in_All[:start] + str(result) + in_All[end+1:]
    return eval_bracket(new)


def calculate_times(in_calculation):
    num = 1
    x = check_double(in_calculation)
    if x is not None:
        return x
    while num < len(in_calculation):
        operator = in_calculation[num]
        if operator == "*":
            in_calculation[num-1:num+2] = [str(float(in_calculation[num-1]) *float(in_calculation[num+1]))]
            num -= 1
        elif operator == "/":
            in_calculation[num-1:num+2] = [str(float(in_calculation[num-1]) / float(in_calculation[num+1]))]
            num -= 1
        num += 1
    return in_calculation


def calculate_pm(plus):
    uy = 1

    while uy < len(plus):
        operator = plus[uy]
        if operator == "+":
            plus[uy-1:uy+2] = [str(float(plus[uy-1]) + float(plus[uy+1]))]
            uy -= 1
        elif operator == "-":
            plus[uy-1:uy+2] = [str(float(plus[uy-1]) - float(plus[uy+1]))]
            uy -= 1
        uy += 1
    return plus

def split(expr):
    token = re.split(r'(\+|\-|\*|\/|\^|\!)', expr)
    tokens = [t for t in token if t != ""]
    if (tokens[0] == "-" or tokens[0] == "+") and is_number(tokens[1]):
        tokens[1] = tokens[0] + tokens[1]
        tokens.pop(0)
    outcome = pm_detect(tokens)
    i = 0
    while i < len(outcome):
        if outcome[i] == "-" and outcome[i-1] in ["*" , "/" , "(" , ")","^"]:
            outcome[i+1] = "-" + outcome[i+1]
            outcome.pop(i)
        else:
            i += 1
    return outcome
def check_double(calculation):
    times_minus = ["/","*"]
    i = 0
    while i < len(calculation):
        if i+1 < len(calculation):
            current = calculation[i]
            next = calculation[i+1]
            if (current in times_minus and next in times_minus ):
                return ["Syntax Error"]
        i += 1
    return None
def is_number(int):
    try:
        float(int)
        return True
    except ValueError:
        return False

def pm_detect(text):
    i=0
    while i < len(text) - 1:  # Stops before the last item so text[i+1] never errors out
        if text[i] == '-' and text[i+1] == '-':
            text[i+1] = "+"
            text.pop(i)       # Safely removes text[i]; do NOT increment i so we can check the new pair
            continue
        elif text[i] == "+" and text[i+1] == "-":
            text[i+1] = "-"
            text.pop(i)
            continue
        elif text[i] == "-" and text[i+1] == "+":
            text[i+1] = "-"
            text.pop(i)
            continue
        elif text[i] == "+" and text[i+1] == "+":
            text[i+1] = "+"
            text.pop(i)
            continue
        else:
            i += 1
    return text

    return y
def power(input,i=0):
    if '^' not in input:
        return input
    if input[i] == "^":
        input[i+1] = str(float(input[i-1]) ** float(input[i+1]))
        del input[i]
        del input[i-1]
        return power(input,i-1)
        #the list is updated so if i = 2 the "third" place would be the answer
        # and the list change so 3-> 1 place which is i-1 =2-1
    else:
        return power(input,i+1)
        #the list is not updated so keeps track the next slot

def square_root(expr): 

    if expr < 0:
        return "imaginary"
    guess = float(expr) /2
    tolerance = 1e-10
    return root(expr, guess,tolerance)
def root(input,guess, tolerance):
    if abs(guess*guess-input)<tolerance:
        return guess
    else:
        guess = (float(input/guess) + float(guess))/2
        return root(input,guess,tolerance )

def log(input):
    answer = math.log10(input)
    return answer
def factorial(input):
    n = int(input)
    if n < 0:
        return "Error! negative factorial"
    elif n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    # Check if result is too large (scientific notation risk)
    return result

def calculate_factorial(input, i=0):
    # Base case: no '!' left in the list
    if "!" not in input:
        # Check for scientific notation (safety net)
        for token in input:
            if isinstance(token, str) and ('e' in token or 'E' in token):
                return ["Value Error: answer too large"]
        return input

    # If a '!' token
    if input[i] == '!':
        if input[i-1] == ")":
            input[i-1] = eval_bracket(input)
        # Ensure there is a number before it
        if i == 0 or not is_number(input[i - 1]):
            return ["Syntax Error: misplaced '!' (sorry only support format like [value]!)"]

        # Compute factorial of the number before '!'
        result = factorial(float(input[i - 1]))
        if len(str(result)) > 15:  # More than 15 digits = too big for display
                result = "Error: Factorial too large"
        # Check if factorial returned an error string
        if isinstance(result, str) and "Error" in result:
            return [result]  # Pass the error up

        # Replace [number, '!'] with [result]
        input[i - 1:i + 1] = [str(result)]

        # Step back one index to check the new element
        return calculate_factorial(input, i - 1)

    else:
        ## no deletion so move on keeping the i pointer to next token
        return calculate_factorial(input, i + 1)

def sin(input):
    rad = math.radians(input) % math.pi
    result = 0
    power = 1
    term = 0
    sign =1
    for i in range(10):
        term = rad**power / float(factorial(power))
        result += sign*term
        sign *= -1
        power += 2
    if abs(result) < 1e-12:
        return 0.0
    if abs(abs(result) - 1) < 1e-12:
        return 1.0 if result > 0 else -1.0
    return result
def cos(input):
    rad = math.radians(input) % math.pi
    result = 0
    power = 0
    term = 0
    sign =1
    for i in range(10):
        term = rad**power / float(factorial(power))
        result += sign * term
        sign *= -1
        power += 2
    if abs(result) < 1e-12:
        return 0.0
    if abs(abs(result) - 1) < 1e-12:
        return 1.0 if result > 0 else -1.0
    return result

def is_int(answer):
    try:
        answer = int(answer)
        return answer
    except ValueError:
        answer = float(answer)
        return answer