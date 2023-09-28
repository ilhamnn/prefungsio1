class Satu:
    def minus(x):
        hitung=17-10-x
        print("kurang = ",hitung)
    def mult(x):
        hitung=8*x
        print("kali = ",hitung)
    def div(x):
        hitung=100/x
        print("pembagian = ",hitung)    
    minus(8)
    mult(2)
    div(10)     
    def evaluate_expression(expression_tree):
        if isinstance(expression_tree, tuple):
            left = Satu.evaluate_expression(expression_tree[0])  
            operator = expression_tree[1]
            right = Satu.evaluate_expression(expression_tree[2])  

            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right
            elif operator == '/':
                if right == 0:
                    raise ZeroDivisionError('Division by zero')
                return left / right
        else:
            return expression_tree

# Expression tree
expression_tree = ((2, '+', 3), '*', (5, '-', 1))

# Evaluasi ekspresi tree
result = Satu.evaluate_expression(expression_tree) 
print(result)