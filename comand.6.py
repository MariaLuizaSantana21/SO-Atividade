#Criar um script que renomeia um conjunto de 
# arquivos de acordo com um padrão.
#Automatizar a criação de backups de arquivos.

import os

diretorio = input("Digite o caminho completo de um diretório: ")
try: 
  arquivos = os.listdir(diretorio)
  print(f"Arquivos encontrados em {diretorio}:")
  for arquivo in arquivos:
    print(arquivo)
except FileNotFoundError:
  print("Diretório não encontrado.")
except FileNotFoundError:
  print("Diretório não encontrado.")





