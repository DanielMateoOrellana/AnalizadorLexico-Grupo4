import ply.yacc as sint
from lexico import tokens
# Roberto: Declaración de Variables, Comentarios, Identificadores, Strings.
#Primera regla

#--------------------------
# Aporte Roberto Patiño
#--------------------------
# ---Definicion de sentencias---
def p_sentencia(p):
  '''sentencia : asignacion
                | echo
                | estructuracontrol
                | comentario
                | declaracion_numeros
                | array
  '''

# ---Declaracion y asignacion de variables---
def p_asignacion(p):
  "asignacion : VAR ASIGNACION valor EOL"

# ---Sentencia echo para imprimir valores---
def p_echo(p):
   '''
   echo : ECHO valores EOL
   '''



# VARIABLE_ARRAY NO FUNCIONA PARA ARRAYS DE 1 SOLO ELEMENTO

def p_valores(p):
   '''
   valores : valor
           | valor COMA valores
   '''

def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | BOOLEANO    
          | CADENA
          | VAR
          | VARIABLE_ARRAY
          | operacion
          | argumentologico
  '''

def p_operacion(p):
   '''
   operacion : ENTERO 
            | FLOTANTE
            | ENTERO operador operacion
            | FLOTANTE operador operacion
   '''

def p_estructuracontrol(p):
   '''
   estructuracontrol : while
                     | if
   '''
# TODO: DA ERROR SI NO SE COLOCAN ESPACIOS. POR EJEMPLO while() Da error
# while (variable simbolo variable) tambien da error, pero si funciona si se coloca espacios antes y despues de variable
def p_while(p):
   '''
   while : WHILE LPAREN argumentologico RPAREN
   '''

def p_if(p):
   '''
   if : IF LPAREN argumentologico RPAREN
   '''

def p_argumentologico(p):
   '''
   argumentologico : VAR simboloLogico VAR
                   | numero simboloLogico numero
                   | VAR simboloLogico numero
                   | VAR IGUAL BOOLEANO
                   | VAR IGUAL CADENA
                   | numero simboloLogico VAR
                   | BOOLEANO IGUAL VAR
                   | CADENA IGUAL VAR
                   | CADENA IGUAL CADENA
                   | BOOLEANO
   '''
  
def p_numero(p):
   '''
   numero : ENTERO
          | FLOTANTE
   '''

def p_simboloLogico(p):
   '''
   simboloLogico : IGUAL
                 | DIFERENTE
                 | MENOR
                 | MAYOR
                 | MENOR_IGUAL
                 | MAYOR_IGUAL      
   '''


def p_comentario(p):
   '''
   comentario : COMNT
   '''
def p_operador(p):
   '''
   operador : SUMA 
            | RESTA 
            | MULT 
            | DIV 
            | POT
   '''
#--------------------------
# Fin de Aporte Roberto Patiño
#--------------------------

# Aporte Cristopher Arroba
def p_numero(p):
  '''numero : ENTERO
            | FLOTANTE'''

def p_declaracion_numeros(p):
  '''declaracion_numeros : VAR ASIGNACION numero'''

def p_array(p):
  '''array : VAR ASIGNACION ARRAY LPAREN elementos RPAREN '''

def p_elementos(p):
  '''elementos : lista
               | diccionario'''

def p_diccionario(p):
  '''diccionario : CADENA ASIGNACION MAYOR valor
                 | CADENA ASIGNACION MAYOR valor COMA diccionario'''

def p_valor(p):
  '''valor : numero
           | CADENA'''

def p_lista(p):
  '''lista : palabras
           | numeros
           | variables'''

def p_palabras(p):
  '''palabras : CADENA COMA palabras
              | CADENA'''

def p_numeros(p):
  '''numeros : numero COMA numeros
             | numero'''

def p_variables(p):
  '''variables : VAR COMA variables
               | VAR'''

def p_error(p):
  print("Error de sintaxis")


parser = sint.yacc()

# while True:
#    try:
#        s = input('calc >>> ')
#    except EOFError:
#        break
#    if not s: continue
#    result = parser.parse(s)
#    if result != None:
#      print(result)

testRoberto = '''
   //Hola mundo
   $a1 = 2;
'''

result = parser.parse(testRoberto)
if result != None:
   print(result)