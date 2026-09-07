from function import calculate_times,calculate_pm,split,eval_bracket,power,calculate_factorial
import sys
def main():
    allowed_syntax = ["(",")","-","+","*","/","^","!"]
    print("calculate anything")
    print("type end to end the program")
    print()
    while True:
        while True:
            valid = True
            calculate = input("calculate: ")
            if calculate == "end":
                print("thanks for using!!!!")
                sys.exit(0)
            if calculate == "":
                print("input something.")
                continue
            i = 0
            while i < len(calculate):
                try:
                    if not (calculate[i].isdigit() or calculate[i] == "." or calculate[i] in allowed_syntax):
                        if calculate[i:i+3] in ["log","sin","cos","tan"] :
                            i+=3
                            continue
                        if calculate[i:i+4] == "sqrt":
                            i+=4
                            continue
                        valid = False
                        break
                except IndexError:
                    valid = False
                    break
                i += 1
            if not valid:
                print("invalid syntax")
            else:
                break
        u = eval_bracket(calculate)
        if not u:
            print("math error!imaginary number")
            continue
        elif u == "empty":
            print("error! empty bracket")
            continue
        else:
            y = split(u)
            k = calculate_factorial(y)
            if k == "Error! negative factorial":
                print("Error! negative factorial")
            elif k == "Value Error: answer too large":
                print("Value Error: answer too large")
            x = power(k)
            q = calculate_times(x)
            if q == ["Syntax Error"]:
                print(q)
                continue
            final = calculate_pm(q)
            answer = str(final[0])
            try:
                answer = int(answer)
            except ValueError:
                answer = float(answer)
            print(answer)


if __name__ == "__main__":
    main()
    sys.exit(0)
