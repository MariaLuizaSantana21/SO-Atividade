import os

username = os.getlogin()
hostname = os.uname()[1]
print(f"Olá, {username}! Seja bem-vindo ao sistema {hostname}.")