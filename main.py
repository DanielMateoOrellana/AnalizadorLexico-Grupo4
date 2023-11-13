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
  '''

# ---Declaracion y asignacion de variables---
def p_asignacion(p):
  "asignacion : VAR ASIGNACION valor EOL"


def p_echo(p):
   '''
   echo : ECHO valor EOL
   '''



# VARIABLE_ARRAY NO FUNCIONA PARA ARRAYS DE 1 SOLO ELEMENTO

def p_valor(p):
  '''valor : ENTERO
          | FLOTANTE
          | BOOLEANO    
          | CADENA
          | VAR
          | VARIABLE_ARRAY
          | operacion
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
                   | BOOLEANO
                   | VAR simboloLogico ENTERO
                   | VAR simboloLogico FLOTANTE
                   | VAR IGUAL BOOLEANO
                   | VAR IGUAL CADENA
                   | ENTERO simboloLogico VAR
                   | FLOTANTE simboloLogico VAR
                   | BOOLEANO IGUAL VAR
                   | CADENA IGUAL VAR
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



def p_error(p):
  print("Error de sintaxis")


parser = sint.yacc()

while True:
   try:
       s = input('calc >>> ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   if result != None:
     print(result)