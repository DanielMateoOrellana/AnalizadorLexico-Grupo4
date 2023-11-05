import ply.lex as lex

#--------------------------
# Aporte Roberto Patiño
#--------------------------
# Palabras reservadas
reservadas = {'if':'IF', 'while': 'WHILE', 'else': 'ELSE', 'case' : 'CASE', 
              'break': 'BREAK', 'continue': 'CONTINUE', 'do': 'DO', 'echo': 'ECHO', 
              'elseif': 'ELSEIF', 'endwhile': 'ENDWHILE', 'for': 'FOR', 'foreach': 
              'FOREACH', 'function': 'FUNCTION', 'global': 'GLOBAL', 
              'return': 'RETURN', 'switch': 'SWITCH'}
# Secuencia de tokens
tokens = (
    'ID',
    'ENTERO',
    'FLOTANTE',
    'BOOLEANO',
    'CADENA',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POT',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMA',
    'PUNTO',
    'IGUAL',
    'MENOR',
    'MAYOR',
    'MENOR_IGUAL',
    'MAYOR_IGUAL',
    'DIFERENTE',
    'MENOR_MAYOR',
    'MAYOR_MENOR',
    'ASIGNAR',
    'SUMA_ASIGNAR',
    'RESTA_ASIGNAR',
    'MULT_ASIGNAR',
    'DIV_ASIGNAR',
    'POT_ASIGNAR',
    'MODULO',
    'COMILLA_DOBLE',
    'COMILLA_SIMPLE',
    'COMILLA_DOBLE_CADENA',
    'COMILLA_SIMPLE_CADENA',
)+tuple(reservadas.values())

