lista = [ 10, 20, 14, 8 , 7, 42, 90, 87, 65]

for num in lista:
    if num == 87:
        print(num)
        break
    else:
        continue

for num in lista:
    if num == 12:
        print(num)
        break
    else:
        continue # Não encontrando o número 12, continua rodando o código buscando


cont = 0

while(cont < 10):
  print('Contador: ' + str(cont))
  print(cont + 1)
  
  cont+=1