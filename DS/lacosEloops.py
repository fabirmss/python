def verifica_se_pode_dirigir(idades):
  for idade in idades:
    if idade >= 18:
      print(f'{idade} anos de idade, TEM permissão para dirigir')
    else:
      print(f'{idade} anos de idade, NÃO TEM permissão para dirigir')