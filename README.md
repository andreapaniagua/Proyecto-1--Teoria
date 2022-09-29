# Proyecto-1--Teoria
## Andrea Paniagua, Javier Alvarez, André salazar

El proyecto consiste en la implementación de los algoritmos básicos para construcción de autómatas finitos a
partir de expresiones regulares. El programa aceptará como entrada una expresión regular r y una cadena w. A
partir de la expresión regular r se construirá un AFN, se transformará el AFN a AFD; y se generará un AFD
directamente. Ambos AFD’s deberán minimizarse. Con dichos autómatas se determinará si la cadena w pertenece o
no a L(r).
Objetivos
• Generales
- Implementación de los algoritmos básicos de autómatas finitos y expresiones regulares.
• Específicos
- Implementación de algoritmo de Construcción de Thompson.
- Implementación de algoritmo de Construcción de Subconjuntos.
- Implementación de algoritmo de Construcción de AFD a partir una expresión regular r.
- Implementación de un algoritmo para minimización de AFD’s.
- Implementación de simulación de un AFN.
- Implementación de simulación de un AFD.


## Entrada

Solamente se ingresarán textualmente una expresión regular r y una cadena w. Por ejemplo, se ingresa
la expresión regular r=(b|b)*abb(a|b)* y la cadena w=babbaaaaa. El símbolo que represente a ε será
designado por el programador o programadora (debe ser algo razonable, no una letra o un número con
altas probabilidades de ser usado en otro aspecto del proyecto).



## Correrlo

Instalar graphviz y en consola correr

```
python3 main.py
```
