solution = lambda my_string, num1, num2 : my_string[:min(num1, num2)]+my_string[max(num1, num2)]+my_string[min(num1, num2)+1:max(num1, num2)]+my_string[min(num1, num2)]+my_string[max(num1, num2)+1:]
