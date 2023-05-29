pessoas ={'nome': ['Letícia', 'Salomao', 'Ana Paula', 'Salim'],
          'sexo': ['f','m','f','m']
          }
for i in range(len(pessoas['nome'])):
  if pessoas['sexo'][i] == 'f':
    saudacao = 'bem-vinda'
  else:
    saudacao = 'bem-vindo'
  print(saudacao, pessoas['nome'][i])