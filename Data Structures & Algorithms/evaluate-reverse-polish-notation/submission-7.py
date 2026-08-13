class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operation = []
        add = "+"
        subtract = "-"
        multiply = "*"
        divide = "/"
        for token in tokens:
            if token == add:
                operation.append(operation.pop() + operation.pop())
            elif token == subtract:
                a = operation.pop()
                b = operation.pop()
                operation.append(b-a)
            elif token == multiply:
                operation.append(operation.pop() * operation.pop())
            elif token == divide:
                a = operation.pop()
                b = operation.pop()
                operation.append(int(b/a))
            else:
                operation.append(int(token))

        return operation.pop()