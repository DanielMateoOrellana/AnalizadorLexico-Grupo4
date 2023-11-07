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
    'ASIGNACION',
    'VAR',
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
    'VARIABLE_ARRAY',
    'VARIABLE_FUNCION',
    'VARIABLE_OBJETO',
    'ARRAY',
    'FUNCION', 
    'OBJETO',
    'LIST',
    'DICT',
    'TUPLE',
    'SET',
    'VARIABLE_ARRAY',
    'VARIABLE_FUNCION',
    'VARIABLE_OBJETO',
    'ARRAY',
    'FUNCION', 
    'OBJETO'
)+tuple(reservadas.values())

# ---Expresiones regulares simples para simbolos o caracteres especiales---
# Asignacion
t_ASIGNACION = r'\='
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
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EOL = r'\;'


#---Definicion de funciones---

# Comentarios
def t_COMNT(t):
  r'\/\/.*|\/\*(\*(?!\/)|[^*])*\*\/'
  t.type = reservadas.get(t.value, 'COMNT')
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
  r'True|False'
  if t.value =='True':
    t.value = True
  else:
    t.value = False
  return t

# Aporte Daniel -------

  # ---- Tipos de datos avanzados ----
  
  # Listas
  def t_LIST(t):
    r'\[[^\]]*\]'
    return t
  
  # Diccionarios
  def t_DICT(t):
    r'\{[^\}]*\}'
    return t
    
  # Tuplas
  def t_TUPLE(t):
    r'\([^\)]*\)'
    return t
   
  # Set 
  def t_SET(t):
    r'\{[^\}]*\}'
    return t

# Aporte Cristopher --------

# Variable Array
def t_VARIABLE_ARRAY(t):
  r'^array\((((\d+)(, \d)+)|("\w+"(, "\w+")*)|(\$\w+(, \$\w+)*))\)$'
  return t

# Variable Funcion
def t_VARIABLE_FUNCION(t):
  r'^[a-z]\w*\(\$\w+(, \$\w+)*\)$'
  return t
# Variable Objeto
def t_VARIABLE_OBJETO(t):
  r'^\$[a-z]\w*->[a-z]\w*$'
  return t
# Array
def t_ARRAY(t):
  r'^\[(((\d+)(, \d)+)|("\w+"(, "\w+")*)|(\$\w+(, \$\w+)*))\]$'
  return t
# Funcion
def t_FUNCION(t):
  r'^[a-z]\w*\(\)$'
  return t
# Objeto
def t_OBJETO(t):
  r'^[A-Z][a-z]*$'
  return t

# Identificadores
def t_ID(t):
    r'[a-z_]\w*'
    t.type = reservadas.get(t.value, 'ID')
    return t

# Definicion de variables
def t_VAR(t):
  r'\$[a-zA-Z_][a-zA-Z0-9_]*'
  t.type = reservadas.get(t.value, 'VAR')
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

# Prueba Daniel
print("\n---- Prueba Daniel ----\n")

codigo_prueba_daniel = "[3,4,5,6] {asd: asd} (4,5,6) ; x = 3 + - * /"
test_tokens(codigo_prueba_daniel)

# Prueba Roberto
print("\n---- Prueba Roberto ----\n")

test_tokens('''
            if
            //hola mundo
            /*
            Hola
            mundo
            */
            $mivar = 12;
            $var2 = true;
            $var3 = false;
            $stringComillasDobles = "Hola mundo";
            $stringComillasSimples = 'Hola mundo';
            12>=4;
            {}
            ''')

# Prueba Cristopher
print("\n---- Prueba Cristopher ----\n")

codigo_prueba_cristopher = '''
            //hola mundo
            /*
            Hola
            mundo
            */
            $mivar1 = (12.5+12)*7-(2/1)+3**2;

            $mivarBool1 = True;
            $mivarBool2 = False;

            $mivarBool3 = $mivar1 > 12;
            $mivarBool4 = 4>=10.5;
            $mivarBool5 = 5.5==5.5;
            $mivarBool6 = 7<5;
            $mivarBool7 = 1<=1.5;

            $stringComillasDobles = "Hola mundo";
            $stringComillasSimples = 'Hola mundo';

            if($mivarBool1 == False){
              while(True){
                $mivar1 = $mivar1 + 1;
                if($mivar1 > 10){
                  break;
                }
              }
            }elseif($mivarBool2 == True){
              $mivar1 = $mivar1 - 1;
            }else{
              $mivar1 = 0;
            }
'''

test_tokens(codigo_prueba_cristopher)
