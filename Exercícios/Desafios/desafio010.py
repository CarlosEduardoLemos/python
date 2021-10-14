real = float(input('Quanto dinheiro você tem? R$'))
dolar = real/5.33 
euro = real/6.02
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar EUR{:.2f}'.format(real, euro))
