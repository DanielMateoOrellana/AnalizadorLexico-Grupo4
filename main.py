import ply.lex as lex

#--------------------------
# Aporte Roberto Patiño
#--------------------------
# ---Palabras reservadas---
reservadas = {'if':'IF', 'while': 'WHILE', 'else': 'ELSE', 'case' : 'CASE', 
              'break': 'BREAK', 'continue': 'CONTINUE', 'do': 'DO', 'echo': 'ECHO', 
              'elseif': 'ELSEIF', 'endwhile': 'ENDWHILE', 'for': 'FOR', 'foreach': 
              'FOREACH', 'function': 'FUNCTION', 'global': 'GLOBAL', 
              'return': 'RETURN', 'switch': 'SWITCH'}
# Secuencia de tokens
tokens = (
    'ID',
    'COMNT',
    'EOL',
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

# ---Expresiones regulares simples para simbolos o caracteres especiales---
# Simbolos aritmeticos
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_POT = r'\*\*'

# Simbolos de comparacion
t_IGUAL = r'\=='
t_DIFERENTE = r'\!='
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MENOR_IGUAL = r'\>='
t_MAYOR_IGUAL = r'\>='

# Simbolos para delimitar bloques
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_EOL = r'\;'


#---Definicion de funciones---

# Comentarios
def t_COMNT(t):
  r'\/\/.*|\/\*(\*(?!\/)|[^*])*\*\/'
  t.type = reservadas.get(t.value, 'COMNT')
  return t

# Identificadores
def t_ID(t):
  r'\$([a-zA-z]|_)+\w*[^\$\s]*'
  t.type = reservadas.get(t.value, 'ID')
  return t

# ---Tipos de datos basicos---

# Flotantes
def t_FLOTANTE(t):
  r'\d+\.\d+'
  t.value = float(t.value)
  return t

# Enteros
def t_ENTERO(t):
  r'\d+'
  t.value = int(t.value)
  return t

# Cadenas 
def t_CADENA(t):
  r'"([^"\n]|(\\"))*"|\'([^\'\n]|(\\\'))*\''
  t.value = str(t.value)
  return t

# Booleanos
def t_BOOLEANO(t):
  r'^(true|false)$'
  t.value = int(t.value)
  return t


# Manejo de errores
def t_error(t):
  print(
      f"{t.type.upper()}: No se reconoce el caracter {t.value[0]} en la línea {t.lineno}"
  )
  t.lexer.skip(1)

# Expresión regular para reconocer saltos de línea
def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)


# Ignorar espacios, tabulaciones
t_ignore = ' \t'


# Construye el lexer
lexer = lex.lex()

# #################################################################
# # Funcion para validar que los tokens sean validos (Reutilizable)
# #################################################################
def test_tokens(code):
  lexer.input(code)
  for token in lexer:
    print(token)

test_tokens('''
            //hola mundo
            /*
            Hola
            mundo
            */
            $mivar = 12;
            $stringComillasDobles = "Hola mundo";
            $stringComillasSimples = 'Hola mundo';
            12>=4;
            {}
            ''')
