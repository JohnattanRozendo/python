nome = input('Nome do Cliente:')
din = float(input('Digite o valor R$:'))
#compra = (din/5.57)

print('Bem vindo {}. Para o valor R${}, você receberá em Dolar é U$${:.2f}'.format(nome, din, din/5.57))