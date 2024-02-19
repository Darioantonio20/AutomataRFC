# Autómata Finito Determinista (DFA) - Proyecto
## Autor: Darío Antonio Gutiérrez Álvarez - 221245

Este proyecto implementa un Autómata Finito Determinista (DFA) en Python. El DFA acepta cadenas que siguen un patrón específico.

## Uso

1. Ejecute el programa.
2. Cuando se le solicite, introduzca una cadena de texto.
3. El programa creará una instancia de la clase `Automaton` y verificará si el DFA acepta la cadena de entrada.
4. Si el DFA acepta la cadena, el programa imprimirá un mensaje indicando que la cadena es correcta según el DFA.
5. Si el DFA no acepta la cadena, el programa imprimirá un mensaje indicando que la cadena es incorrecta.

## Equivalente en Expresión Regular

El DFA definido en este programa es equivalente a la siguiente expresión regular:


Esta expresión regular coincide con las cadenas que:

- Comienzan con 'G' o 'g'
- Opcionalmente seguidas por 'U' o 'u'
- Opcionalmente seguidas por 'A' o 'a'
- Opcionalmente seguidas por 'D' o 'd'
- Y luego terminan


# Curp/RFC con mis 4 iniciales  ->  GUAD
#Expresión regular              ->  ^[gG][uU]?[aA]?[dD]?$