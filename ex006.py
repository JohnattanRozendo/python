n = int(input('Digite um Nº: '))
d = int(n*2)
t = int(n*3)
rq = float (n**(1/2))
print ('O dobro de {} é: {}' .format(n, d))
print ('O triplo de {} é: {} \nA raiz de {} é: {:.2f}' .format(n, t, n, rq))
# \n - > Serve para quebrar linha... manter a proxima frase junto para n ter espaço ex: \nProxima Frase
# Na mascara {} conseguimos formatar o que será impresso. Exemplo print {} == 3.45465484612 
# print {:.2f} == 3.45 | começando sempre com :. + numero de casas + tipo primitivo
# Outra forma de fazer o calculo da raiz quadrada é usando a função pow (power ou potencia)