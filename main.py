#proyecto 1 de teoria computacional
#Andrea Paniagua 18733
#Andre Salazar 18764
#Javier Alvarez 18051
from graphviz import Digraph
from libs import *
from thomson import *
from subconjuntos import *
import sys
#seteamos el ambiente
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz/bin'
print("Proyecto 1 \n")
print("Implementación de los algoritmos básicos de autómatas finitos y expresiones regulares \n")
exp = input("Ingrese la expresión regular: \n")
exxpr = exp[:0] + '(' + exp[0:]
expr = exxpr[:-1] + exxpr[-1] + ')'
count = 0

for item in range(len(expr)):
    if expr[item] == '(' or expr[item] == ')':
        count += 1
    
    
if count % 2 == 0:
    print("\nCadena aceptada\n")
else:
    sys.exit('Cadena Erronea')


pos_exp, alfa = postfix(expr)
print("\nEspresion posfix: \n", pos_exp)
print("\nAlfabeto: ", alfa)
#print(pos_exp)
#print(alfa)
thom_resultado, thom_trans = thomson(pos_exp, alfa)
print("\nTransiciones Thompson: \n", thom_resultado)
print("\nNodos inicial-final: \n", thom_trans)
grafo(thom_resultado, thom_trans, "thomson")
#print(thom_trans)
# print(thom_resultado)
sub_estados, sub_end, = subconjuntos(thom_resultado, thom_trans)
print("\nTabla de estados: ")
print(sub_estados)
print("\nEstados de inicio/fin: ")
print(sub_end)
grafo(sub_estados, sub_end, "subconjuntos")

#ingreso de cadena
cadena = input("Ingrese la cadena de caracteres para probar la simulación: \n")
res_t = simulacion(thom_resultado, cadena, thom_trans, alfa, 0)
res_s = simulacion(sub_estados, cadena, sub_end, alfa)
#condiciones de simulación
if res_s == 0:
    print("La cadena no pertenece a Thomson")

if res_s == 1:
    print("La cadena si pertenece a Thomson")

if res_s == 0:
    print("La cadena no pertenece a subconjuntos")
if res_s == 1:
    print("La cadena si pertenece a subconjuntos")