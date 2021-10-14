m = float(input('Digite em metros para ser calculado: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm= m * 1000
print('o valor digitado é {}m, em decimetro é {} em centímetros é {}, em milimetros é {}'.format(m, dm, cm, mm))
print('O valor {}m em decâmetros é {}, em hectômetro é {} em kilômetros é {} '.format(m, dam, hm, km))
