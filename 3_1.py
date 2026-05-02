class ExpressionSolver:
    def __init__(self, expression):
        self.expression = expression

    def solve(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return f"Error: {e}"

    def display(self):
        print("Expression:", self.expression)
        print("Result:", self.solve())


expr = input("Enter a mathematical expression: ")

solver = ExpressionSolver(expr)

solver.display()
