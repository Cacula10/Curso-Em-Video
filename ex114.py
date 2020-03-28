import socket

try:
    ip = socket.gethostbyname('pudim.com.br')
except socket.gaierror:
    print('O site "Pudim" está Fora do Ar')
else:
    print('O site "Pudim" está no Ar')
finally:
    print('Consulte-nos sempre !')