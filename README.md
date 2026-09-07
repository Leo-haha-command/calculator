# calculator
# Project title: A Scientific Calculator

#### Video Demo: https://youtu.be/q8lpowgM374

#### Description:
This is a web-based calculator built with Python, Flask, and basic HTML/CSS. The main goal of this project was to challenge myself to build a math string parser completely from scratch.

I deliberately chose **NOT** to use Python's built-in `eval()` function or any standard shortcut libraries to handle the logic. Everything from breaking down the string to resolving parentheses and calculating operator priority was coded manually based on the data structure concepts I learned from Week 1 to Week 6 in CS50x.

### How It Works & Core Logic

1. **Splitting the Input (`re`)**
   I used Python's `re.split` to break the math string down into a clean list of individual tokens (numbers and operators like `+`, `-`, `*`, `/`, `^`). This allowed me to focus my core code on the actual math logic rather than getting stuck on basic string cutting.

2. **Handling Brackets & Priority (Recursion)**
   To handle math order correctly, my code runs a recursive function (`find_bracket`) that searches for the innermost parentheses from right to left (`rfind`). Once it isolates a single block inside brackets, it evaluates the math in proper order: first exponents (`^`), then multiplication and division (`*`, `/`), and finally addition and subtraction (`+`, `-`).

3. **Newton's Method for Square Roots (Babylonian Method)**
   Instead of using `math.sqrt`, I implemented a recursive square root approximator using Newton's Method. The algorithm starts with an initial guess of `x/2` and iteratively updates it using the formula `guess = (guess + x/guess) / 2` until the difference between `guess²` and `x` is smaller than `1e-10`. This converges very quickly and gives high-precision results without importing any math module.
   *Derivation*: This is equivalent to finding the root of `f(t) = t² - x` via Newton–Raphson iteration. Each step moves the tangent line of the curve at the current guess to intersect the x-axis, and that intersection becomes the next guess—regardless of whether the guess was too high or too low, the method always moves closer to the true root.

4. **Logarithm Handling**
   I used the standard `math.log10` library for the log function. Writing a high-precision log algorithm completely from scratch would take much more processing time and could slow down the Flask server, so using the standard library here was a practical engineering choice for speed.

5. **Sine, Cosine, and Tangent via Taylor Polynomials**
   Instead of using `math.sin` or `math.cos`, I implemented these functions using their Taylor series expansions around `x = 0`:
   - `sin(x) = x - x³/3! + x⁵/5! - x⁷/7! + ...`
   - `cos(x) = 1 - x²/2! + x⁴/4! - x⁶/6! + ...`
   - `tan(x) = sin(x) / cos(x)`, with a safety check to avoid division by zero.
   I used 8 iterations in the loop, which gives near-double-precision accuracy for most inputs without relying on any external math library for trigonometric logic.

6. **Factorial Support**
   The calculator supports postfix factorial notation (e.g., `5!`). The `calculate_factorial` function handles edge cases such as `0! = 1` and displays clear error messages for negative numbers or inputs that would cause overflow.

7. **What I Learned & How This Project Started**
   This project began as a small daily exercise to practice `while` loops and recursion in Python. As I added more features, I realized I was building something much larger than a simple practice script.
   Interestingly, I didn't know about `eval()` when I started—I wrote the parser and tokenizer from scratch. Later, when I discovered `eval()`, I decided to keep my own implementation, because that was the more interesting and challenging path.
   That decision led me to explore numerical methods: I learned about Newton's Method for square roots and Taylor series for trigonometric functions (and 3Blue1Brown's videos were incredibly helpful in understanding them).
   Today, every part of this codebase is something I fully understand and can explain in depth.

### Edge Cases Handled
- **Negative numbers:** The parser correctly handles unary minus signs like `-5` or `-(3+2)`.
- **Double Signs:** `pm_detect` cleans up overlapping signs (e.g., `--` → `+`, `+-` → `-`) before calculations.
- **Math Errors:** Division by zero and negative square roots are caught gracefully and display clear error messages without crashing the server.
- **Empty Brackets:** Inputs like `()` are detected and return an "empty bracket" error.

### What to Improve
- **Functionality:** I can add more features like curve sketching or program (formula) installation to the calculator.
- **Style:** I can also add better UI to make the website much prettier and more professional.

### Acknowledgements
1. CS50x for teaching me the C and Python knowledge.
2. GitHub for providing the platform to host this project.
3. 3Blue1Brown for explaining the methods to approximate sin/cos/tan via Taylor series.


## How to use
1. cd calculator
2. flask run (or python file.py )(for the terminal version(for testing))