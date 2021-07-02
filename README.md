# Battleship

Juego de hundir la flota escrito usando numpy. El objetivo del juego es hundir todos los barcos del enemigo, antes de que él consiga hundir los tuyos.

**!El primer jugador en quedarse sin barcos pierde!**

## Instrucciones

* El tablero se compone de 100 posiciones, de los cuales los barcos ocuparán 20. 

* Hay un total de 10 barcos

    * 1 portaaviones que ocupa 4 posiciones
    * 2 acorazados que ocupan 3 espacios cada uno
    * 3 fragatas que ocupan 2 espacios cada una
    * 4 submarinos que ocupan 1 espacio cada uno
  
* Los barcos pueden colocarse hacia el norte, sur, este y oeste siempre que no se salgan del tablero

* No puede haber dos barcos en la misma posición. 

* En cada turno, puedes disparar a una coordenada a la que no hayas disparado antes en el turno del enemigo.
  1) Si das a uno de los barcos del contrincante, te vuelve a tocar
  2) Si fallas, y tu disparo cae al agua, le toca disparar a la maquina
  
## El tablero
El tablero está compuesto de 10 columnas (A-J), y 10 filas (1-10). Cada vez que se coloca un barco, el usuario tiene la opción de colocar de manera aleatoria todos los demás.
```
                    A B C D E F G H I J
                    -------------------
                 1 |1                  |
                 2 |          2 2      |
                 3 |            1   2  |
                 4 |                2  |
                 5 |                   |
                 6 |                   |
                 7 |    3 3 3     4    |
                 8 |  3 3 3   1   4    |
                 9 |              4    |
                10 |  2 2         4   1|
                    -------------------
```
Los numeros presentes en el tablero son los barcos. Los números representan los espacios ocupados por cada uno, de tal manera que los 3 representan los acorazados, los 4 el portaaviones, y así para los 4 tipos de barco. 

Cuando se dispara, sí el impacto da en uno de los barcos del enemigo, este impacto se mostrará con una "X" en el tablero. En caso contrario, se mostrará un guion "-". 

En el siguiente caso, el jugador ha dado a uno de los barcos en la posición H8 del enemigo, pero al disparar a la posición D5 ha fallado.

```
                    A B C D E F G H I J
                    -------------------
                 1 |                   |
                 2 |                   |
                 3 |                   |
                 4 |                   |
                 5 |      -            |
                 6 |                   |
                 7 |                   |
                 8 |              X    |
                 9 |                   |
                10 |                   |
                    -------------------
```

Un tablero en una fase más adelantada del juego puede parecer así

```
                    A B C D E F G H I J
                    -------------------
                 1 |X   -     -       -|
                 2 |-         X       -|
                 3 |-           X   X -|
                 4 |-       -       X -|
                 5 |-   -     -     -  |
                 6 |- -     -   -  -  -|
                 7 |  -   X X         -|
                 8 |    X X -         -|
                 9 |        -         -|
                10 |        -          |
                    -------------------
```
## Recursos utilizados
* Lenguaje utilizado: Python 3.9.5
  * Librerías: 
    * numpy 
    * string
    * re

## Contribuidores
Este proyecto ha sido elaborado por:
 <ol>
  <li>Ana Blanco
    <ul>
      <li>Posicionamiento de barcos</li>
      <li>Impresión gráfica de tableros</li>
    </ul>
  </li>
  <li>Ignacio Gonzalez-Espejo
    <ul>
      <li>Disparar</li>
      <li>Lógica de juego</li>
    </ul> 
  </li>
</ol> 

