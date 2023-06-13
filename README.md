# soy-mas-lab17

## Juego de los dados

Escribiremos el código necesario para crear un juego de los dados.

En la terminal el usuario debe ver lo siguiente:

```bash
----- El juego de los dados -----
1. Quiero Jugar
2. Quiero saber los resultados
3. Salir
```

## Quiero jugar

El juego debe simular una situación en la cuál el usuario lanza 2 dados, obtiene resultados al azar.
Luego es el turno de la computadora que también lanza 2 dados.

Una vez que ambos hayan jugado sus dados, para cada jugador se sumarán ambos dados. Quién haya obtenido la suma más alta será el ganador de la partida.

El programa debe ser capaz de identificar quién ganó la partida, los puntajes parciales de ambos jugadores y contar el número de partidas jugadas hasta el momento

Importante: En cada partida solo deben mostrarse los resultados de la partida recién jugada y el ganador, y NO los resultados totales ni la cantidad de partidas jugadas.
(Recuerda que si no mostrarás esa información, igual debes calcularla cada vez que jueguen)


## Quiero saber los resultados

Cuando el usuario quiere ver los resultados deben mostrarse exactamente los siguientes mensajes reemplazando con los valores donde corresponda:

`Cantidad de partidas jugadas: NUMERO-DE-PARTIDAS`
`Puntaje total usuario: PUNTAJE-USUARIO`
`Puntaje total computadora: PUNTAJE-COMPUTADORA`

### Salir 

Al salir debe ver el siguiente mensaje:

`Gracias por jugar.`
