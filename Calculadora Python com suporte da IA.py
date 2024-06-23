# Calculadora Python com suporte da IA de Replid 

import math

def calculadora_python_soma (num1, num2):
  resultado = num1 + num2
  return resultado

def calculadora_python_subtracao (num1, num2):
   resultado = num1 - num2
   return resultado

def calculadora_python_multiplicacao (num1, num2):
   resultado = num1 * num2
   return resultado

def calculadora_python_divisao (num1, num2):
  resultado = num1 / num2
  return resultado

def calculadora_python_potencia (num1, num2):
  resultado = num1 ** num2
  return resultado

def calculadora_python_raiz (num1, num2):
  resultado = num1 ** (1/num2)
  return resultado

def calculadora_python_porcentagem (num1, num2):
  resultado = num1 * (num2/100)
  return resultado

def main():
  
  while True:
    
    try: 
      num1 = float(input("Digite o primeiro número: "))
      num2 = float(input("Digite o segundo número: "))
      operacao = input("Digite a operação desejada (+, -, *, /, **, %, raiz): ")
     
      if operacao == "+":
        resultado = calculadora_python_soma(num1, num2)
      elif operacao == "-":
        resultado = calculadora_python_subtracao(num1, num2)  
      elif operacao == "*":
        resultado = calculadora_python_multiplicacao (num1, num2)
      elif operacao == "/":
        resultado = calculadora_python_divisao(num1, num2) 
      elif operacao == "**":
        resultado = calculadora_python_potencia(num1, num2)
      elif operacao == "%":
        resultado = calculadora_python_porcentagem(num1, num2)
      elif operacao == "raiz":
        resultado = calculadora_python_raiz(num1, num2)
        
      else: 
        print("Operação inválida. Tente novamente.")
        continue
      print("Resultado: ", resultado)
      continuar = input("Deseja continuar? (sim/não): ")
      
      if continuar.lower() != "sim": 
        
        break
    except ValueError:
      print("Entrada inválida. Tente novamente.")

if __name__ == "__main__":
  main()