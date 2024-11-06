#Utilizar o módulo os para navegar pelo sistema de arquivos.
#o Listar diretórios e arquivos.
#o Obter informações sobre arquivos (tamanho, data de modificação).


import os

dir= os.get_exec_path ( env = None )
arquivos=os.ctermid ( ) 
print(dir)
print(arquivos)
for arq in arquivos:
    a=os.ctermid ( )
    print(a)
    inf=os.fpathconf(fd,name) 
    print(inf)






