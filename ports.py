import socket
s = socket.socket()
portas = [80,443,1194,53,22,21]
ip = input("Digite o ip do alvo: ")
for p in portas:
    if(s.connect_ex((ip,p)) == 0):
        print ("Porta "+str(p)+" aberta")
    else:
        print ("Porta "+str(p)+" fechada")     

