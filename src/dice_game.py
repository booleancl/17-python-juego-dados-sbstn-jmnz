import random
option = 0
total_user = 0
total_computer = 0
plays = 0

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
    total_user += user_sum 

    # Dados del computador
    computer_dice_one = random.randint(1,6)
    computer_dice_two = random.randint(1,6)
    # Suma de la partida del computador
    computer_sum = computer_dice_one + computer_dice_two
    total_computer += computer_sum

    print(f"Tus dados fueron: {user_dice_one} y {user_dice_two}")
    print(f"Los dados del computador fueron: {computer_dice_one} y {computer_dice_two}")

    plays += 1

    # Gana el usuario Si la suma del usuario es mayor que el computador
    if user_sum > computer_sum:
      print("Ganaste")
    elif user_sum < computer_sum:
      print("Perdiste")
    # Si son iguales empatan
    else:
      print("Empate")
  elif option == "2":
    print(f"Cantidad de partidas jugadas: {plays}")
    print(f"Puntaje total usuario: {total_user}")
    print(f"Puntaje total computadora: {total_computer}")
  
  elif option =="3":
    print("Gracias por jugar.")

  else:
    print("Ingrese una opción válida") 
