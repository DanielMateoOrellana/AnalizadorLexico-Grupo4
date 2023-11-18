import ply.lex as lex

#--------------------------
# Aporte Roberto Patiño
#--------------------------
# ---Palabras reservadas---
reservadas = {
    'if': 'IF',
    'and': 'AND',
    'or' : 'OR',
    'while': 'WHILE',
    'else': 'ELSE',
    'case': 'CASE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'do': 'DO',
    'echo': 'ECHO',
    'elseif': 'ELSEIF',
    'endwhile': 'ENDWHILE',
    'for': 'FOR',
    'foreach': 'FOREACH',
    'function': 'FUNCTION',
    'global': 'GLOBAL',
    'return': 'RETURN',
    'switch': 'SWITCH',
    'array': 'ARRAY',
    'class' : 'CLASE',
    'new': 'NEW',
    'public': 'PUBLIC',
    'readline': 'READLINE'
}
# Secuencia de tokens
tokens = (
    # Roberto ------------------
    'ID',
    'ASIGNACION',
    'VAR',
    'COMNT',
    'EOL',
    'ENTERO',
    'FLOTANTE',
    'BOOLEANO',
    'CADENA',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COMA',
    'PUNTO',
    'DOSPUNTOS',
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
    # Daniel -------------------
    # Operadores
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POT',
    # Tipos de datos avanzados
    'DICT',
    'TUPLE',
    'SET',
    # Cristopher ---------------
    'VARIABLE_ARRAY',
    'VARIABLE_FUNCION',
    'VARIABLE_OBJETO',
    'ARRAY',
    'FUNCION',
    'OBJETO') + tuple(reservadas.values())

# ---Expresiones regulares simples para simbolos o caracteres especiales---

# Asignacion
t_ASIGNACION = r'\='
t_COMA = r'\,'
t_DOSPUNTOS = r'\:'
# Simbolos aritmeticos
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_POT = r'\*\*'
t_PUNTO = r'\.'

# Simbolos de comparacion
t_IGUAL = r'\=='
t_DIFERENTE = r'\!='
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_MENOR_IGUAL = r'\<='
t_MAYOR_IGUAL = r'\>='

# Simbolos para delimitar bloques
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EOL = r'\;'


#---Definicion de funciones---
# Aporte Cristopher -------
# Variable Array
def t_VARIABLE_ARRAY(t):
  r'array\((((\d+)(,\s\d)+)|("\w+"(,\s"\w+")*)|(\$\w+(,\s\$\w+)*))\)'
  return t


# Variable Funcion
def t_VARIABLE_FUNCION(t):
  r'[a-z]\w*\(\$\w+(,\s\$\w+)*\)'
  return t


# Variable Objeto
def t_VARIABLE_OBJETO(t):
  r'\$[a-z]\w*->[a-z]\w*'
  return t


# Funcion
def t_FUNCION(t):
  r'[a-z]\w*\(\)'
  return t

# Booleanos
def t_BOOLEANO(t):
  r'True|False'
  t.value = bool(t.value)
  return t



# Objeto
def t_OBJETO(t):
  r'[A-Z][a-z]*'
  return t


# Comentarios
def t_COMNT(t):
  r'\/\/.*|\/\*(\*(?!\/)|[^*])*\*\/'
  t.type = reservadas.get(t.value, 'COMNT')
  return t
  
# Diccionarios
def t_DICT(t):
  r'array\("\w+"\s=>\s(("\w+")|(\d+))(,\s"\w+"\s=>\s("\w+"|\d+))*\)'
  return t


# Identificadores
def t_ID(t):
  r'[a-z_]\w*'
  t.type = reservadas.get(t.value, 'ID')
  return t


# Definicion de variables
def t_VAR(t):
  r'\$([a-zA-z]|_)+\w*[^\$\s\;\+\-\/\*\>\<\>=\<=\=]*'
  t.type = reservadas.get(t.value, 'VAR')
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





# Aporte Daniel -------

# ---- Tipos de datos avanzados ----


# Listas
def t_ARRAY(t):
  r'\[(((\d+)(,\s?\d)+)|("\w+"(,\s?"\w+")*)|(\$\w+(,\s?\$\w+)*))\]'
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

codigo_prueba_daniel = '''[3,4,5,6] array("nombre" => "Juan", "edad" => 30, "ciudad" => "Madrid") (4,5,6) ; x = 3 + - * / 
  $diccionario = array(
    "gato" => "animal doméstico",
    "perro" => "animal doméstico",
    "pez" => "animal acuático"
);'''
# test_tokens(codigo_prueba_daniel)

# Prueba Roberto
print("\n---- Prueba Roberto ----\n")

test_tokens('''
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
            ''')

# Prueba Cristopher
print("\n---- Prueba Cristopher ----\n")
codigo_prueba_cristopher = '''
array(1, 2, 3, 4)
array($persona1, $persona2, $persona3)
array("rojo", "verde", "azul")

promedio($numeros)
suma($a, $b, $c)
promedio_total($numeros)
suma_total($a, $b, $c)

$this->nombre
$juan->apellido
$juan5->apellido

[1, 2, 3, 4, 5]
[$persona1, $persona2, $persona3]
["rojo", "verde", "azul"]

promedio()
promedio_total()

Persona
Casa
Carro
Oficina

'''
# test_tokens(codigo_prueba_cristopher)
