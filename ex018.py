from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja: '))
print('O angulo de {} tem..\no Seno {:.2f}\no Cosseno: {:.2f}\na Tangante: {:.2f}'.format(angulo, sin(radians(angulo)), cos(radians(angulo)), tan(radians(angulo))))
