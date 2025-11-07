def soma(a, b):
  return a + b
def teste_unidade():
  assert soma(2, 3) == 5

if __name__ == "__main__":
  print("Executando CodeHealth - simulação")
  teste_unidade()
  print("Teste local OK")
