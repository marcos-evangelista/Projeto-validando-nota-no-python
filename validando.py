#Esse codigo foi atualizado, pois o if foi trocado por while.
#Caso a nota seja maior que 10, irá informar que a nota foi digitada errada!
#Fará que o usuário, fique em um loop, até que digite a nota correta!!!
nome= str(input('Digite seu nome:'))
a = int (input('\n {nome} digite a nota do primeiro bimestre: '.format(nome=nome))) #Entrada da nota
while a > 10: #Verificando se a nota é maior que 10
    a=int (input('A nota do primeiro bimestre está errada! {nome}Digite novamente:'.format(nome=nome)))#Caso a nota >10 informo o erro

b = int (input ('\n {nome} digite a nota do segundo bimestre: '.format(nome=nome)))#Entrada da nota
while b > 10: #Verificando se a nota é maior que 10
     b=int (input('{nome} a nota do segundo bimestre está errada!Corrigir nota  Digite novamente:'.format(nome=nome)))#Se for informar erro

c = int(input('\n{nome} digite a nota do terceiro bimestre:  '.format(nome=nome))) #Entrada da nota
while c > 10:  #Verificando se a nota é maior que 10
    c=int (input('{nome} nota do terceiro bimestre está errada! Digite novamente:'.format(nome=nome)))#Se for informar erro

d = int(input('\nAgora {nome} digite a nota do quarto bimestre:  '.format(nome=nome)))#Entrada da nota
while d > 10:
    d=int (input('A nota do quarto bimestre está errada! {nome} Digite novamente:'.format(nome=nome)))#Se for informar erro

media = (a+b+c+d)/4
print('A média é: {}'.format(media)) #Irá imprimir na tela a média

if media >=7<10:


    print ('Parabéns! {nome} Você foi aprovado(a)! média {media}'.format(nome=nome,media=media))
elif media <6:
    print ('Infelizmente você foi reprovado(a)!{nome} a sua média foi média {media}'.format(nome=nome,media=media))
else:
    print('{nome} você está de recuperação e terá que fazer a prova novamente!'.format(nome=nome))