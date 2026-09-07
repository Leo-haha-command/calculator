from flask import Flask, request, render_template
from function import eval_bracket, split, power, calculate_times, calculate_pm, calculate_factorial,is_int

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        expr = request.form.get("expression", "")

        try:
            u = eval_bracket(expr)

            if not u:
                result = "math error! imaginary number"
            elif u == "empty":
                result = "error! empty bracket"
            else:
                y = split(u)
                ##split the token first from string to list
                k = calculate_factorial(y)
                ##go for factorial
                if k == "Error! negative factorial":
                    result = "Error! negative factorial"
                elif k == "Value Error: answer too large":
                    result = "Value Error: answer too large"
                else:
                    ##go through the process
                    x = power(k)
                    q = calculate_times(x)
                    if q == ["Syntax Error"]:
                        result = "Syntax Error"
                    else:
                        final = calculate_pm(q)
                        if isinstance(final, list) and len(final) > 0:
                            result = round(float(final[0]),15)
                        else:
                            result = is_int(final)

        except ValueError:
            result = "invalid syntax"
        except ZeroDivisionError:
            result = "division by zero"
        except IndexError:
                    result = "not completed expression"
        except Exception as e:
            result = f"unknown error: {e}"
    return render_template("index.html", result=result)