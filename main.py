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
                | funcion
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
                   | VAR DIFERENTE BOOLEANO
                   | VAR DIFERENTE CADENA
                   | numero simboloLogico VAR
                   | BOOLEANO IGUAL VAR
                   | CADENA IGUAL VAR
                   | CADENA IGUAL CADENA
                   | CADENA DIFERENTE VAR
                   | CADENA DIFERENTE CADENA
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
  '''declaracion_numeros : VAR ASIGNACION numero EOL'''

def p_array(p):
  '''array : VAR ASIGNACION ARRAY LPAREN elementos RPAREN EOL'''

def p_elementos(p):
  '''elementos : lista
               | diccionario'''

def p_diccionario(p):
  '''diccionario : CADENA ASIGNACION MAYOR valor_dic
                 | CADENA ASIGNACION MAYOR valor COMA diccionario'''

def p_valor_dic(p):
  '''valor_dic : numero
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
  
def p_funcion(p):
  '''funcion : FUNCTION tipo_funcion LBRACE final_funcion RBRACE'''''

def p_tipo_funcion(p):
  '''tipo_funcion : FUNCION
                  | VARIABLE_FUNCION'''

def p_final_funcion(p):
  '''final_funcion : RETURN VAR EOL
                    | cuerpo_funcion
  '''

def p_cuerpo_funcion(p):
  '''cuerpo_funcion : declaracion_numeros final_funcion
                    | array final_funcion
                    | estructuracontrol final_funcion'''


def p_error(p):
  print("Error de sintaxis")

# Aporte Daniel Mateo

def p_ingreso_datos(p):
   '''
    ingreso_datos : VAR ASIGNACION readline EOL
    '''

def p_readline(p):
  '''
  readline : READLINE LPAREN CADENA RPAREN
  '''

def p_objeto(p):
   '''
    objeto : CLASE OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL VARIABLE_OBJETO ASIGNACION CADENA EOL
           | CLASE OBJETO LBRACE mas_objetos PUBLIC VAR EOL RBRACE
           | CLASE OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL
           | CLASE OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL VARIABLE_OBJETO EOL
    '''

def p_cuerpo_objeto(p):
   '''
   cuerpo_objeto : PUBLIC VAR EOL
   '''

def p_mas_objetos(p):
   '''
   mas_objetos : cuerpo_objeto
               | cuerpo_objeto mas_objetos 
   '''
  
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

testRoberto = '''//Hola mundo
$a1 = 2;
$a2 = 2.4;
$a3 = True;
$a4 = False;
$a5 = 'Hola mundo';
$a6 = "Hola mundo";
$a7 = $a3;
$a9 = 2+1-3.4+1*2/1.5**4;
$a10 = $a1 >= 4.2;
$a11 = $a1 == 2.2;
$a12 = $a1 <= 1.2;
$a13 = $a1 < 0.2;
$a14 = $a1 > 4.2;
$a14 = $a1 != 4.2;
$a15 = $a1 == True;
$a16 = $a1 == False;
$a17 = 1 <= 1.2;
$a18 = 1 == 1;
$a19 = 1.1 >= 1.2;
$a20 = 1.3 < 1.2;
$a21 = 1 > 1.2;
$a22 = 1 > 1.2;
$a22 = 1 != 1.2;
$a23 = $a5 == 'Hola mundo';
$a24 = 'Hola PHP' == 'Hola mundo';
$a25 = 'Hola PHP' != 'Hola mundo';
$a26 = "Hey" != 'Hola mundo';
echo $a1;
echo 1;
echo 2.4;
echo 'Hello world';
echo True;
echo False;
echo 'Hola mundo', 1.4, 2, True, False, $a21;'''
lRoberto = testRoberto.split("\n")

for linea in lRoberto:
  result = parser.parse(linea)
  if result != None:
      print(result)

testCristopher = '''$array1 = array("hola","mundo");
$array1 = array(1,2,3);
$array2 = array(1.2, 5.2, 6.5);
$array3 = array($p1 , $p2 , $p3 );
$array4 = array("rojo", "verde", "azul" );
$array5 = array("Hola" => "valor", "Clave" => 35 );
$entero = 45;
$decimal = 53.2;
function longitud($texto) {$entero = 45; $array1 = array(1,2,3); $array5 = array("Hola" => "valor", "Clave" => 35 ); return $entero ;}'''
lCristopher = testCristopher.split("\n")

for linea in lCristopher:
  result = parser.parse(linea)
  if result != None:
      print(result)

testDaniel = '''echo "El valor de pi es: ", pi;
echo "<br>";
$nombre = readline("Ingrese su nombre: ");
$edad = readline("Ingrese su edad: ");
$suma = $edad + 1;
$resta = $edad - 1;
$multiplicacion = $edad * 2;
$division = $edad / 2;
echo "El símbolo de dólar es: \$";
echo "El símbolo de porcentaje es: %";
$persona = new stdClass();
$persona->nombre = $nombre;
$persona->edad = $edad;
echo "El nombre de la persona es: " . $persona->nombre;
echo "La edad de la persona es: " . $persona->edad;'''
