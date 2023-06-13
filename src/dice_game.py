import random
option = 0
wins = 0
loose = 0
even = 0
while option != "3":
  print("----- El juego de los dados -----")
  print("1. Quiero Jugar")
  print("2. Quiero saber los resultados")
  print("3. Salir")

  option = input()
  
  if option == "1":
    # Dados del usuario
    user_dice_one = random.randint(1,6)
    user_dice_two = random.randint(1,6)
    # Suma de la partida del usuario
    user_sum = user_dice_one + user_dice_two

    # Dados del computador
    computer_dice_one = random.randint(1,6)
    computer_dice_two = random.randint(1,6)
    # Suma de la partida del computador
    computer_sum = computer_dice_one + computer_dice_two

    print(f"Tus dados fueron: {user_dice_one} y {user_dice_two}")
    print(f"Los dados del computador fueron: {computer_dice_one} y {computer_dice_two}")

    # Gana el usuario Si la suma del usuario es mayor que el computador
    if user_sum > computer_sum:
      wins += 1 
      print("Ganaste")
    elif user_sum < computer_sum:
      loose += 1
      print("Perdiste")
    # Si son iguales empatan
    else:
      even += 1
      print("Empate")
  elif option == "2":
    print(f"Cantidad de partidas jugadas: {wins + loose + even}")
    print(f"Puntaje total usuario: {wins}")
    print(f"Puntaje total computadora: {loose}")
  
  elif option =="3":
    print("Gracias por jugar.")

  else:
    print("Ingrese una opción válida") 
