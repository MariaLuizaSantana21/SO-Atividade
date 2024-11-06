


import os



esco=input("Digiteo comando: ")

try:
    esc=os.subprocess.run(esco)
except FileNotFoundError:
  print("Comando não encontrado.")






