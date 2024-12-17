from Arquivo.consulta import *
from Arquivo.scraping import *
from Arquivo.tratamento import *
from Arquivo.banco_de_dados import *

print("   >> Iniciando Programa <<  ")
user = getpass.getuser()
horario = datetime.datetime.now()
with open(r"log_sist.txt", 'a') as arquivo:
    arquivo.write(f"ROBO COMPLEMENTAR DA FOLHA DE PONTO| Iniciado | {user} | {horario} \n")

arquivo.close()
rr = Romeu()
rr.acessando()
rr.login()
rr.dentro()
mm = Mudar()
mm.save()
bb = Banco()
bb.horas()

print("OBRIGADO POR UTILIZAR O ROBÔ, ATÉ MÊS QUEM VEM")


user = getpass.getuser()
horario = datetime.datetime.now()
with open(r"log_sist.txt", 'a') as arquivo:
    arquivo.write(f"ROBO FOLHA COMPLEMENTAR DA DE PONTO | Finalizando | {user} | {horario} \n")

arquivo.close()

print("   >>> Finalizando Programa <<<  ")
