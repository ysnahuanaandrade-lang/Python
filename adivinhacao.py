# import random

# numero_secreto = 7
# chute = int(input('Escolha um numero de 1 a 10'))
# print(f'Você escolheu o numro: {chute}')

# if chute == numero_secreto:
#     print('Você acertou')
# elif chute > numero_secreto:
#     print('Você errou! Tente um numero menor.')    
# else chute < numero_secreto:
#     print('Você errou! tente um numero maior.')  
# else:
#     print('Você acertou')

numero_secreto = random.randint(1, 20)

print('Tente adivinhar o número que estou pensando... Entre 1 a 20. Você tem 5 tentativas')


for tentativa in range (1,6):
     chute = int(input('Seu palpite: '))

     if chute < numero_secreto:
          print('Você errou! Tente um número maior')
else:
     print(f'Acertou em {tentativas} tentativa(s)!')
          break
else:
    print(f'Acabaram as tentativas. O número era {numero_secreto}')

# while True:
#      chute = int (input('Seu palpite: '))
#      tentativa += 1

#      if chute < numero_secreto: 
#           print('Voê errou! Tente um número maior')
#      elif chute >  numero_secreto:
#           print('Voê errou! Tente um número menor')
#      else: 
#           print(f'Acertou em {tentativas} tentativa(s)!')
#           break