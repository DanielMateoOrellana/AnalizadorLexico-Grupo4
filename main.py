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