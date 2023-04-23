# Ejercicio 1: Factorial de un número

def factor(num):
    if num < 0:
        return "Error. Este número es negativo"
    elif num == 0:
        return 1
    else:
      factor_var = 1
      for i in range(1, num+1):
          factor_var = factor_var * i
    return factor_var
num = int(input("Ingrese un número mayor o igual a 0: \n"))
print(factor(num))
