import ply.yacc as sint
from lexico import tokens
# Roberto: Declaración de Variables, Comentarios, Identificadores, Strings.
#Primera regla
valid = True
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
                | readline
                | ingreso_datos
                | objeto
                | expresionAritmetica
                | echo SALTO
                
  '''

# ---Declaracion y asignacion de variables---
def p_asignacion(p):
  "asignacion : VAR ASIGNACION valor EOL"

# ---Sentencia echo para imprimir valores---
def p_echo(p):
   '''
   echo : ECHO valores EOL 
         | ECHO valores EOL SALTO
   '''





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
          | array_index
  '''

###################################################################
############## Regla semantica 1: Roberto Patiño ##################
#Esta regla se usa para acceder a los elementos de un diccionario #
#por clave, teniendo en cuenta que las claves pueden ser numeros  #
#o cadenas, y las mismas se acceden usando corchetes siguiendo    #
#esta notacion: $diccionario["clave"]                             #
###################################################################
def p_diccionario(p):
  '''diccionario : clave_dic ASIGNACION MAYOR valor_dic
                 | clave_dic ASIGNACION MAYOR valor_dic COMA diccionario'''

def p_clave_dic(p):
  '''clave_dic : ENTERO
                | CADENA'''

def p_valor_dic(p):
  '''valor_dic : numero
           | CADENA
           | VAR
           | BOOLEANO
           | array_l'''

def p_array_index(p):
  '''array_index : VAR multi_dimensiones '''
  
################### Fin de regla semantica 1: Roberto Patiño############


###################################################################
############## Regla semantica 1: Cristopher Arroba ###############
#Los arrays pueden ser multidimensionales, es decir, pueden       #
#contener otros arrays.                                           #
#Los elementos de un array multidimensional pueden ser accedidos  #
#utilizando múltiples índices.                                    #  
###################################################################
def p_mul_dimensiones(p):
  '''multi_dimensiones : LBRACKET clave_dic RBRACKET
                       | LBRACKET clave_dic RBRACKET multi_dimensiones
  '''
################### Fin de regla semantica 1: Cristopher Arroba############

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
                     | for
   '''

def p_while(p):
   '''
   while : WHILE LPAREN condicion RPAREN LBRACE lineas RBRACE
   '''

def p_if(p):
   '''
   if : IF LPAREN condicion RPAREN LBRACE lineas RBRACE
      | if else
      | if elseif else
      | if elseif
   '''

def p_elseif(p):
   '''
   elseif : ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE
          | ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE elseif
   '''

def p_else(p):
   '''
   else : ELSE LBRACE lineas RBRACE
   '''

def p_condicion(p):
   '''
   condicion : argumentologico 
             | argumentologico conector_logico condicion
   '''
def p_vacio(p):
   '''
   vacio : EOL
   '''

def p_conector_logico(p):
   '''
   conector_logico : AND
                   | OR
   '''

def p_valor_logico(p):
   '''
   valor_logico : numero
                | VAR
   '''


###################################################################
############## Regla semantica 2: Roberto Patiño ##################
#Esta regla se usa en conjunto con las sentencias condicionales   #
#y estructuras iterativas como while para validar que su argumento#
#siempre sea algo booleano.                                       #
###################################################################

def p_argumentologico(p):
   '''
   argumentologico : VAR operador_logico VAR
                   | numero operador_logico numero
                   | VAR operador_logico numero
                   | VAR IGUAL BOOLEANO
                   | VAR IGUAL CADENA
                   | VAR DIFERENTE BOOLEANO
                   | VAR DIFERENTE CADENA
                   | numero operador_logico VAR
                   | BOOLEANO IGUAL VAR
                   | CADENA IGUAL VAR
                   | CADENA IGUAL CADENA
                   | CADENA DIFERENTE VAR
                   | CADENA DIFERENTE CADENA
                   | BOOLEANO
                   | VAR operador_logico VAR mul_dimensiones
                   | VAR mul_dimensiones operador_logico VAR
                   | VAR mul_dimensiones operador_logico numero
                   | VAR mul_dimensiones operador_logico CADENA
                   | VAR operador_logico VAR mul_dimensiones
                   | numero operador_logico VAR mul_dimensiones
                   | CADENA operador_logico VAR mul_dimensiones
   '''
################### Fin de regla semantica 2: Roberto Patiño############
def p_numero(p):
   '''
   numero : ENTERO
          | FLOTANTE
   '''

def p_operador_logico(p):
   '''
   operador_logico : IGUAL
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


def p_declaracion_numeros(p):
  '''declaracion_numeros : VAR ASIGNACION numero EOL'''


###################################################################
############## Regla semantica 2: Cristopher Arroba ###############
# Al igual que con los arrays en general, los diccionarios pueden #
# contener valores de diferentes tipos, como cadenas, números,    #
# booleanos, objetos, otros arrays, etc.                          #  
###################################################################
def p_array(p):
  '''array : VAR ASIGNACION ARRAY LPAREN elementos RPAREN EOL'''

def p_elementos(p):
  '''elementos : lista
               | diccionario'''

def p_lista(p):
  '''lista : palabras
           | numeros
           | variables
           | array_l
           | bool'''
  
def p_array_l(p):
  '''array_l : ARRAY LPAREN elementos RPAREN
             | ARRAY LPAREN elementos RPAREN COMA lista'''

def p_palabras(p):
  '''palabras : CADENA
              | CADENA COMA lista'''

def p_numeros(p):
  '''numeros : numero
             | numero COMA lista'''

def p_variables(p):
  '''variables : VAR
               | VAR COMA lista'''

def p_bool(p):
  '''bool : BOOLEANO
          | BOOLEANO COMA lista'''
################### Fin de regla semantica 2: Cristopher Arroba############

def p_funcion(p):
  '''funcion : FUNCTION tipo_funcion LBRACE final_funcion RBRACE'''''

def p_tipo_funcion(p):
  '''tipo_funcion : FUNCION
                  | VARIABLE_FUNCION'''

def p_final_funcion(p):
  '''final_funcion : RETURN VAR EOL
                    | lineas final_funcion
  '''

def p_cuerpo_funcion(p):
  '''cuerpo_funcion : declaracion_numeros final_funcion
                    | array final_funcion
                    | estructuracontrol final_funcion'''


def p_error(p):
    mensaje = ""
    if p:
        if p.type == 'EOL':
            mensaje = f"Error en la línea {p.lineno}: Las sentencias solo pueden terminar con un punto y coma"
        else:
            mensaje = f"Error de sintaxis en la línea {p.lineno}: Token inesperado '{p.value}'"
            # Verificación adicional para detectar si el token siguiente es un operador
            index = p.lexpos + len(p.value) -1
            if index < len(p.lexer.lexdata):
                next_char = p.lexer.lexdata[index]
                if next_char in '+-*/=':
                    mensaje = f". El caracter '{next_char}' después del operador '{p.lexer.lexdata[index-1]}' no es válido"
        print(mensaje)
        output_file = open("gui/assets/code_output.txt", "a")
        output_file.write(mensaje + "\n")
        output_file.close()
    else:
        print("Error de sintaxis: entrada inesperada al final del archivo ")
        mensaje = "Error: entrada inesperada al final del archivo, asegurese de finalizar cada sentencia con punto y coma"
        output_file = open("gui/assets/code_output.txt", "a")
        output_file.write(mensaje + "\n")
        output_file.close()

# def p_error(p):
#    print("Error de sintaxis")






# Aporte Daniel Mateo

def p_readline(p):
  '''readline : READLINE LPAREN CADENA RPAREN EOL'''

def p_ingreso_datos(p):
   '''
   ingreso_datos : VAR ASIGNACION readline
   '''


def p_objeto(p):
   '''
   objeto : CLASE OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL mas_atributos
   '''

def p_cuerpo_objeto(p):
   '''
   cuerpo_objeto : PUBLIC VAR EOL
                 | PUBLIC asignacion
   '''

def p_mas_objetos(p):
   '''
   mas_objetos : cuerpo_objeto
               | cuerpo_objeto mas_objetos 
   '''

def p_atributo(p):
   '''
   atributo : VAR RESTA MAYOR ID ASIGNACION CADENA EOL
   '''

def p_mas_atributos(p):
   '''
   mas_atributos : atributo
                 | atributo mas_atributos
   '''

def p_for(p):
   '''
   for : FOR LPAREN asignacion argumentologico EOL VAR SUMA SUMA RPAREN LBRACE lineas RBRACE
                  | FOR LPAREN asignacion argumentologico EOL VAR RESTA RESTA RPAREN LBRACE lineas RBRACE
                  | FOR LPAREN asignacion argumentologico EOL VAR SUMA SUMA RPAREN LBRACE SALTO lineas SALTO RBRACE
   '''

def p_linea(p):
   '''
   linea : echo 
         | ECHO CADENA EOL 
         | ECHO VAR EOL
         | VAR ASIGNACION CADENA EOL 
         | estructuracontrol
         | comentario
         | declaracion_numeros
         | array
   '''

def p_lineas(p):
   '''
   lineas : linea
          | linea lineas
   '''

def p_expresionAritmetica(p):
   '''
   expresionAritmetica : VAR ASIGNACION numero masTerminos EOL
                       | VAR ASIGNACION VAR masTerminos EOL
   '''

def p_termino(p):
   '''
   termino : operador numero
           | operador VAR
   '''
def p_masTerminos(p):
   '''
   masTerminos : termino
               | termino masTerminos
   '''

parser = sint.yacc()


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
echo 'Hola mundo', 1.4, 2, True, False, $a21 ;
echo 'Hola mundo', 1.4, 2, True, False, $a [4]["cadena"][3] ;
echo $a [4]["cadena"][3];
if ($a1> $a2 and $a1>$a2 or $a1 > $a2 or "hola mundo" == $a3 ){ $asd = "Hola"; }
if($a1<=$a2){ $asd = "Hola"; }else{ $asd = "Hola"; }
if($a1<=$a2){ $asd = "Hola"; }elseif($a>3 or 1!=$num){ $asd = "Hola"; }else{ $asd = "Hola"; }
if($a1<=$a2){ $asd = "Hola"; }elseif($a>3 or 1!=$num){ $asd = "Hola"; }elseif($a<3 or 1==$num){ $asd = "Hola"; }else{ $asd = "Hola"; }
while ( $a3 == "Hola" and $costo <= 27.8 and $bool == True ){ $asd = "Hola"; }'''
lRoberto = testRoberto.split("\n")
print("---PRUEBA ROBERTO PATINO---")
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
$array6 = array("Hola" => "valor" );
$array7 = array(1);
$array8 = array($p1 );
$array9 = array($p1 , $p2 , $p3 , array($p1 , $p2 , $p3 ), array("Hola" => "valor" , "Clave" => 35 ) );
$array10 = array(1.2, $p1 , $p2 , $p3 , array($p1 , True , $p3 ,array(2 => 5 , "Clave" => array("Hola" => $p1 , "Clave" => False))), array(2 => 5));
$entero = 45;
$decimal = 53.2;
function longitud($texto) {$entero = 45; $array1 = array(1,2,3); if($a1<=$a2){ $asd = "Hola"; }elseif($a>3 or 1!=$num){ $asd = "Hola"; }elseif($a<3 or 1==$num){ $asd = "Hola"; }else{ $asd = "Hola"; } $array5 = array("Hola" => "valor", "Clave" => 35 ); return $entero ;}
function longitud($texto) {$entero = 45; for ($i=5;$i<6;$i++) {echo "Hola"; echo "Chao"; for ( $i = 5; $i <6;$i++) {if ($a1> $a2 and $a1>$a2 or $a1 > $a2 or "hola mundo" == $a3 ){ $asd = "Hola"; }}} return $entero;}
function longitud($texto) {while ( $a3 == "Hola" and $costo <= 27.8 and $bool == True ){ $asd = "Hola"; if($a1<=$a2){ $asd = "Hola"; }else{ $asd = "Hola";}} $entero = 45; for ( $i = 5; $i <6;$i++) { echo "Hola"; echo "Chao"; for ( $i = 5; $i <6;$i++) { echo "Hola"; echo "Chao"; }} return $entero;}'''

lCristopher = testCristopher.split("\n")
print("\n--- Prueba Cristopher ---\n")
for linea in lCristopher:
  result = parser.parse(linea)
  if result != None:
      print(result)

print("\n--- Prueba Daniel ---\n")

testDaniel = '''class Producto {public $nombre; public $precio = 5; public $nombre;} $producto1 = new Producto(); $producto1 -> nombre = "asd"; $producto1 -> nombre = "asd";
class Persona {public $nombre; public $apellido = "Mateo" ;} $persona1 = new Persona(); $persona1 -> nombre = "Daniel"; $producto1 -> nombre = "Alfredo";
class Producto {public $nombre;} $producto1 = new Producto(); $producto1 -> nombre = "asd"; $producto1 -> nombre = "asd";
class Producto {public $precio = 5; public $nombre; } $producto1 = new Producto(); $producto1 -> nombre = "asd";
$edad = readline("Escribe tu edad");
$nombre = readline("Escribe tu nombre");
for ($i=5;$i<6;$i++) {echo "Hola"; echo "Chao"; for ( $i = 5; $i <6;$i++) { echo "Hola"; echo "Chao"; }}
for ($i=5;$i<6;$i++) {echo "Hola"; echo "Chao"; for ( $i = 5; $i <6;$i++) { for ( $i = 5; $i <6;$i++) { echo "Hola"; echo "Chao"; }}}
for ($i=5;$i<6;$i++) {echo "Hola"; echo "Chao"; for ( $i = 5; $i <6;$i++) {if ($a1> $a2 and $a1>$a2 or $a1 > $a2 or "hola mundo" == $a3 ){ $asd = "Hola"; }}}
if ($a1> $a2 and $a1>$a2 or $a1 > $a2 or "hola mundo" == $a3 ){ $asd = "Hola"; }
if($a1<=$a2){ $asd = "Hola"; }else{ $asd = "Hola"; }
if($a1<=$a2){ $asd = "Hola"; }elseif($a>3 or 1!=$num){ $asd = "Hola"; }else{ $asd = "Hola"; }
if($a1<=$a2){ $asd = "Hola"; }else{ $asd = "Hola"; for ($i=5;$i<6;$i++) {echo "Hola"; echo "Chao"; for ( $i = 5; $i <6;$i++) { echo "Hola"; echo "Chao"; }}}
if($a1<=$a2){ $asd = "Hola"; }elseif($a>3 or 1!=$num){ $asd = "Hola"; }elseif($a<3 or 1==$num){ $asd = "Hola"; }else{ $asd = "Hola"; }
while ( $a3 == "Hola" and $costo <= 27.8 and $bool == True ){ $asd = "Hola"; if($a1<=$a2){ $asd = "Hola"; }else{ $asd = "Hola";}}
$a = $b + $a;
$a = $a + 15 +$b + $x + $y + 15; 
$a1 = 2;
$a = 15 + 17;
$asd = $ab + $bc * 5;
$edad = $edad1 + $edad2;
$total = 10 + 10;
$totalIVA = 20 * 0.12;'''


lDaniel = testDaniel.split("\n")

for linea in lDaniel:
  result = parser.parse(linea)
  if result != None:
      print(result)


##############################################################
##############################################################
# INICIO DE TESTS PARA LA ENTREGA FINAL ######################
##############################################################
##############################################################


###### ALGORITMO DE PRUEBA CRISTOPHER #####
testFinalCristopher = '''$numeros = array(1, 2, 3, 4, 5);
$persona = array("nombre" => "Juan","edad" => 25,"activo" => True);
echo "Elementos del array numérico: ";
$indice = 0;
echo $numeros [0];
echo $persona ["nombre"];
$array9 = array($p1 , $p2 , $p3 , array($p1 , $p2 , $p3 ), array("Hola" => "valor" , "Clave" => 35 ) );
echo 'Hola mundo', 1.4, 2, True, False, $a [4]["cadena"][3] ;
echo $a [4]["cadena"][3];
while ($indice < $numeros) {echo $numeros ["indice"];}
echo "Elementos del diccionario asociativo: ";
function sumar($a, $b) {return $a;}
echo "Resultado de la función sumar:", $resultado;
class Persona {public $nombre = "Vacio"; public $edad; } $persona1 = new Persona(); $persona -> edad = "20";
if ($juan>=18) { echo "Juan es mayor de edad";}else{ echo "Juan es menor de edad"; }'''

###### ALGORITMO DE PRUEBA ROBERTO #####

testFinalRoberto = '''//Creando un diccionario
$diccionario = array("Peras" => "Agotado" , "Manzanas" => 0.25, "Cebolla"=>0.30, "Apio"=>"Agotado","Helado"=>0.30 );
echo $diccionario ["Peras"], $diccionario ["Manzanas"];
if($diccionario ["Peras"]=="Agotado"){echo "No hay peras disponibles en stock";}'''



archivo = open("gui/assets/code_input.txt","r")
line_number = 1
for linea in archivo:
    result = parser.parse(linea)
    if result is not None:
        print("### LÍNEA VÁLIDA ###")
    print("Linea ejecutada: ", line_number)
    line_number += 1



