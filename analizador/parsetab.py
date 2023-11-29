
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY ARRAY ASIGNACION ASIGNAR BOOLEANO BREAK CADENA CASE CLASE COMA COMILLA_DOBLE COMILLA_DOBLE_CADENA COMILLA_SIMPLE COMILLA_SIMPLE_CADENA COMNT CONTINUE DICT DIFERENTE DIV DIV_ASIGNAR DO DOSPUNTOS ECHO ELSE ELSEIF ENDWHILE ENTERO EOL FLOTANTE FOR FOREACH FUNCION FUNCTION GLOBAL ID IF IGUAL LBRACE LBRACKET LPAREN MAYOR MAYOR_IGUAL MAYOR_MENOR MENOR MENOR_IGUAL MENOR_MAYOR MODULO MULT MULT_ASIGNAR NEW OBJETO OR POT POT_ASIGNAR PUBLIC PUNTO RBRACE RBRACKET READLINE RESTA RESTA_ASIGNAR RETURN RPAREN SET SUMA SUMA_ASIGNAR SWITCH TUPLE VAR VARIABLE_ARRAY VARIABLE_FUNCION VARIABLE_OBJETO WHILEsentencia : asignacion\n                | echo\n                | estructuracontrol\n                | comentario\n                | declaracion_numeros\n                | array\n                | funcion\n                | readline\n                | ingreso_datos\n                | objeto\n                | expresionAritmetica\n  asignacion : VAR ASIGNACION valor EOL\n   echo : ECHO valores EOL\n   \n   valores : valor\n           | valor COMA valores\n   valor : ENTERO\n          | FLOTANTE\n          | BOOLEANO    \n          | CADENA\n          | VAR\n          | VARIABLE_ARRAY\n          | operacion\n          | argumentologico\n  \n   operacion : ENTERO \n            | FLOTANTE\n            | ENTERO operador operacion\n            | FLOTANTE operador operacion\n   \n   estructuracontrol : while\n                     | if\n                     | for\n   \n   while : WHILE LPAREN condicion RPAREN LBRACE lineas RBRACE\n   \n   if : IF LPAREN condicion RPAREN LBRACE lineas RBRACE\n      | if else\n      | if elseif else\n      | if elseif\n   \n   elseif : ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE\n          | ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE elseif\n   \n   else : ELSE LBRACE lineas RBRACE\n   \n   condicion : argumentologico \n             | argumentologico conector_logico condicion\n   \n   vacio : EOL\n   \n   conector_logico : AND\n                   | OR\n   \n   valor_logico : numero\n                | VAR\n   \n   argumentologico : VAR operador_logico VAR\n                   | numero operador_logico numero\n                   | VAR operador_logico numero\n                   | VAR IGUAL BOOLEANO\n                   | VAR IGUAL CADENA\n                   | VAR DIFERENTE BOOLEANO\n                   | VAR DIFERENTE CADENA\n                   | numero operador_logico VAR\n                   | BOOLEANO IGUAL VAR\n                   | CADENA IGUAL VAR\n                   | CADENA IGUAL CADENA\n                   | CADENA DIFERENTE VAR\n                   | CADENA DIFERENTE CADENA\n                   | BOOLEANO\n   \n   numero : ENTERO\n          | FLOTANTE\n   \n   operador_logico : IGUAL\n                 | DIFERENTE\n                 | MENOR\n                 | MAYOR\n                 | MENOR_IGUAL\n                 | MAYOR_IGUAL      \n   \n   comentario : COMNT\n   \n   operador : SUMA \n            | RESTA \n            | MULT \n            | DIV \n            | POT\n   declaracion_numeros : VAR ASIGNACION numero EOLarray : VAR ASIGNACION ARRAY LPAREN elementos RPAREN EOLelementos : lista\n               | diccionariodiccionario : CADENA ASIGNACION MAYOR valor_dic\n                 | CADENA ASIGNACION MAYOR valor COMA diccionariovalor_dic : numero\n           | CADENAlista : palabras\n           | numeros\n           | variablespalabras : CADENA COMA palabras\n              | CADENAnumeros : numero COMA numeros\n             | numerovariables : VAR COMA variables\n               | VARfuncion : FUNCTION tipo_funcion LBRACE final_funcion RBRACEtipo_funcion : FUNCION\n                  | VARIABLE_FUNCIONfinal_funcion : RETURN VAR EOL\n                    | lineas final_funcion\n  cuerpo_funcion : declaracion_numeros final_funcion\n                    | array final_funcion\n                    | estructuracontrol final_funcionreadline : READLINE LPAREN CADENA RPAREN EOL\n   ingreso_datos : VAR ASIGNACION readline\n   \n   objeto : CLASE OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL mas_atributos\n   \n   cuerpo_objeto : PUBLIC VAR EOL\n                 | PUBLIC asignacion\n   \n   mas_objetos : cuerpo_objeto\n               | cuerpo_objeto mas_objetos \n   \n   atributo : VAR RESTA MAYOR ID ASIGNACION CADENA EOL\n   \n   mas_atributos : atributo\n                 | atributo mas_atributos\n   \n   for : FOR LPAREN asignacion argumentologico EOL VAR SUMA SUMA RPAREN LBRACE lineas RBRACE\n                  | FOR LPAREN asignacion argumentologico EOL VAR RESTA RESTA RPAREN LBRACE lineas RBRACE\n   \n   linea : ECHO CADENA EOL \n         | ECHO VAR EOL\n         | VAR ASIGNACION CADENA EOL \n         | estructuracontrol\n         | comentario\n         | declaracion_numeros\n         | array\n   \n   lineas : linea\n          | linea lineas\n   \n   expresionAritmetica : VAR ASIGNACION numero masTerminos EOL\n                       | VAR ASIGNACION VAR masTerminos EOL\n   \n   termino : operador numero\n           | operador VAR\n   \n   masTerminos : termino\n               | termino masTerminos\n   '
    
_lr_action_items = {'VAR':([0,14,15,16,17,18,25,37,38,46,47,48,57,59,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,92,96,97,98,100,120,121,123,124,125,126,129,130,134,136,137,138,141,156,157,166,170,172,173,174,179,180,183,191,192,196,199,200,207,212,219,220,224,225,226,229,236,],[13,32,-28,-29,-30,-68,49,-33,-35,86,86,93,32,-69,-70,-71,-72,-73,106,108,110,111,-62,-63,-64,-65,-66,-67,118,-62,-63,-34,122,86,122,86,145,-12,-74,147,122,159,-114,-115,-116,-117,163,122,168,86,-42,-43,32,-38,-119,185,122,122,189,147,-111,-112,122,-75,32,-113,-31,-32,-36,-37,122,122,227,-109,-110,227,-106,]),'ECHO':([0,15,16,17,18,37,38,78,79,81,98,120,123,124,125,126,130,156,157,170,172,179,180,183,191,196,199,200,207,212,219,220,225,226,],[14,-28,-29,-30,-68,-33,-35,-34,121,121,-74,121,-114,-115,-116,-117,121,-38,-119,121,121,-111,-112,121,-75,-113,-31,-32,-36,-37,121,121,-109,-110,]),'COMNT':([0,15,16,17,18,37,38,78,79,81,98,120,123,124,125,126,130,156,157,170,172,179,180,183,191,196,199,200,207,212,219,220,225,226,],[18,-28,-29,-30,-68,-33,-35,-34,18,18,-74,18,-114,-115,-116,-117,18,-38,-119,18,18,-111,-112,18,-75,-113,-31,-32,-36,-37,18,18,-109,-110,]),'FUNCTION':([0,],[19,]),'READLINE':([0,25,],[20,20,]),'CLASE':([0,],[21,]),'WHILE':([0,15,16,17,18,37,38,78,79,81,98,120,123,124,125,126,130,156,157,170,172,179,180,183,191,196,199,200,207,212,219,220,225,226,],[22,-28,-29,-30,-68,-33,-35,-34,22,22,-74,22,-114,-115,-116,-117,22,-38,-119,22,22,-111,-112,22,-75,-113,-31,-32,-36,-37,22,22,-109,-110,]),'IF':([0,15,16,17,18,37,38,78,79,81,98,120,123,124,125,126,130,156,157,170,172,179,180,183,191,196,199,200,207,212,219,220,225,226,],[23,-28,-29,-30,-68,-33,-35,-34,23,23,-74,23,-114,-115,-116,-117,23,-38,-119,23,23,-111,-112,23,-75,-113,-31,-32,-36,-37,23,23,-109,-110,]),'FOR':([0,15,16,17,18,37,38,78,79,81,98,120,123,124,125,126,130,156,157,170,172,179,180,183,191,196,199,200,207,212,219,220,225,226,],[24,-28,-29,-30,-68,-33,-35,-34,24,24,-74,24,-114,-115,-116,-117,24,-38,-119,24,24,-111,-112,24,-75,-113,-31,-32,-36,-37,24,24,-109,-110,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,37,38,53,56,78,97,98,142,146,156,162,165,191,199,200,207,212,225,226,228,229,231,236,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-28,-29,-30,-68,-33,-35,-100,-13,-34,-12,-74,-121,-120,-38,-91,-99,-75,-31,-32,-36,-37,-109,-110,-101,-107,-108,-106,]),'ASIGNACION':([13,93,122,154,168,185,216,233,],[25,141,160,176,141,198,176,234,]),'ENTERO':([14,25,46,47,57,58,59,60,61,62,63,64,68,69,70,71,72,73,74,75,76,77,80,92,96,97,100,136,137,138,141,160,178,192,],[28,54,89,89,28,102,-69,-70,-71,-72,-73,102,89,-62,-63,-64,-65,-66,-67,89,-62,-63,89,89,89,-12,89,89,-42,-43,28,89,89,54,]),'FLOTANTE':([14,25,46,47,57,58,59,60,61,62,63,64,68,69,70,71,72,73,74,75,76,77,80,92,96,97,100,136,137,138,141,160,178,192,],[29,55,90,90,29,104,-69,-70,-71,-72,-73,104,90,-62,-63,-64,-65,-66,-67,90,-62,-63,90,90,90,-12,90,90,-42,-43,29,90,90,55,]),'BOOLEANO':([14,25,46,47,57,69,70,80,92,97,136,137,138,141,192,],[30,30,87,87,30,113,115,87,87,-12,87,-42,-43,30,30,]),'CADENA':([14,25,44,46,47,57,66,67,69,70,80,92,97,100,121,136,137,138,141,160,177,192,211,234,],[31,31,82,88,88,31,107,109,114,116,88,88,-12,154,158,88,-42,-43,31,181,193,203,216,235,]),'VARIABLE_ARRAY':([14,25,57,141,192,],[33,33,33,33,33,]),'RBRACE':([15,16,17,18,37,38,78,97,98,119,120,123,124,125,126,128,132,133,156,157,164,167,169,179,180,184,186,187,188,191,196,197,199,200,207,212,222,223,225,226,],[-28,-29,-30,-68,-33,-35,-34,-12,-74,156,-118,-114,-115,-116,-117,162,166,-104,-38,-119,-95,-105,-103,-111,-112,-94,-102,199,200,-75,-113,207,-31,-32,-36,-37,225,226,-109,-110,]),'RETURN':([15,16,17,18,37,38,78,81,98,120,123,124,125,126,130,156,157,179,180,191,196,199,200,207,212,225,226,],[-28,-29,-30,-68,-33,-35,-34,129,-74,-118,-114,-115,-116,-117,129,-38,-119,-111,-112,-75,-113,-31,-32,-36,-37,-109,-110,]),'ELSE':([16,37,38,78,156,200,207,212,],[39,-33,39,-34,-38,-32,-36,-37,]),'ELSEIF':([16,37,38,78,156,200,207,212,],[40,-33,-35,-34,-38,-32,40,-37,]),'FUNCION':([19,],[42,]),'VARIABLE_FUNCION':([19,],[43,]),'LPAREN':([20,22,23,24,40,52,213,],[44,46,47,48,80,100,218,]),'OBJETO':([21,208,],[45,213,]),'ARRAY':([25,160,],[52,52,]),'EOL':([26,27,28,29,30,31,32,33,34,35,49,50,51,54,55,87,89,90,94,95,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,131,140,143,144,145,158,159,163,168,175,181,182,221,235,],[56,-14,-16,-17,-18,-19,-20,-21,-22,-23,-20,97,98,-16,-17,-59,-60,-61,142,-124,146,-15,-24,-26,-25,-27,-54,-56,-55,-58,-57,-46,-48,-49,-50,-51,-52,-47,-53,165,173,-125,-122,-123,179,180,184,186,191,196,98,224,236,]),'COMA':([27,28,29,30,31,32,33,34,35,54,55,89,90,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,147,154,155,193,203,205,],[57,-16,-17,-18,-19,-20,-21,-22,-23,-16,-17,-60,-61,-24,-26,-25,-27,-54,-56,-55,-58,-57,-46,-48,-49,-50,-51,-52,-47,-53,174,177,178,177,-19,211,]),'IGUAL':([28,29,30,31,32,36,49,51,54,55,86,87,88,89,90,203,206,],[-60,-61,65,66,69,76,69,76,-60,-61,69,65,66,-60,-61,66,76,]),'DIFERENTE':([28,29,31,32,36,49,51,54,55,86,88,89,90,203,206,],[-60,-61,67,70,77,70,77,-60,-61,70,67,-60,-61,67,77,]),'MENOR':([28,29,32,36,49,51,54,55,86,89,90,206,],[-60,-61,71,71,71,71,-60,-61,71,-60,-61,71,]),'MAYOR':([28,29,32,36,49,51,54,55,86,89,90,176,206,230,],[-60,-61,72,72,72,72,-60,-61,72,-60,-61,192,72,232,]),'MENOR_IGUAL':([28,29,32,36,49,51,54,55,86,89,90,206,],[-60,-61,73,73,73,73,-60,-61,73,-60,-61,73,]),'MAYOR_IGUAL':([28,29,32,36,49,51,54,55,86,89,90,206,],[-60,-61,74,74,74,74,-60,-61,74,-60,-61,74,]),'SUMA':([28,29,49,51,54,55,89,90,95,102,104,144,145,189,201,],[59,59,59,59,59,59,-60,-61,59,59,59,-122,-123,201,209,]),'RESTA':([28,29,49,51,54,55,89,90,95,102,104,144,145,189,202,227,],[60,60,60,60,60,60,-60,-61,60,60,60,-122,-123,202,210,230,]),'MULT':([28,29,49,51,54,55,89,90,95,102,104,144,145,],[61,61,61,61,61,61,-60,-61,61,61,61,-122,-123,]),'DIV':([28,29,49,51,54,55,89,90,95,102,104,144,145,],[62,62,62,62,62,62,-60,-61,62,62,62,-122,-123,]),'POT':([28,29,49,51,54,55,89,90,95,102,104,144,145,],[63,63,63,63,63,63,-60,-61,63,63,63,-122,-123,]),'LBRACE':([39,41,42,43,45,135,139,161,214,215,],[79,81,-92,-93,83,170,172,183,219,220,]),'RPAREN':([54,55,82,84,85,87,89,90,91,106,107,108,109,110,111,112,113,114,115,116,117,118,127,147,148,149,150,151,152,153,154,155,171,190,193,194,195,203,204,206,209,210,217,218,],[-60,-61,131,135,-39,-59,-60,-61,139,-54,-56,-55,-58,-57,-46,-48,-49,-50,-51,-52,-47,-53,161,-90,175,-76,-77,-82,-83,-84,-86,-88,-40,-89,-86,-85,-87,-81,-78,-80,214,215,-79,221,]),'PUBLIC':([83,97,133,169,186,],[134,-12,134,-103,-102,]),'AND':([85,87,89,90,106,107,108,109,110,111,112,113,114,115,116,117,118,],[137,-59,-60,-61,-54,-56,-55,-58,-57,-46,-48,-49,-50,-51,-52,-47,-53,]),'OR':([85,87,89,90,106,107,108,109,110,111,112,113,114,115,116,117,118,],[138,-59,-60,-61,-54,-56,-55,-58,-57,-46,-48,-49,-50,-51,-52,-47,-53,]),'NEW':([198,],[208,]),'ID':([232,],[233,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,],[1,]),'asignacion':([0,48,134,],[2,92,169,]),'echo':([0,],[3,]),'estructuracontrol':([0,79,81,120,130,170,172,183,219,220,],[4,123,123,123,123,123,123,123,123,123,]),'comentario':([0,79,81,120,130,170,172,183,219,220,],[5,124,124,124,124,124,124,124,124,124,]),'declaracion_numeros':([0,79,81,120,130,170,172,183,219,220,],[6,125,125,125,125,125,125,125,125,125,]),'array':([0,79,81,120,130,170,172,183,219,220,],[7,126,126,126,126,126,126,126,126,126,]),'funcion':([0,],[8,]),'readline':([0,25,],[9,53,]),'ingreso_datos':([0,],[10,]),'objeto':([0,],[11,]),'expresionAritmetica':([0,],[12,]),'while':([0,79,81,120,130,170,172,183,219,220,],[15,15,15,15,15,15,15,15,15,15,]),'if':([0,79,81,120,130,170,172,183,219,220,],[16,16,16,16,16,16,16,16,16,16,]),'for':([0,79,81,120,130,170,172,183,219,220,],[17,17,17,17,17,17,17,17,17,17,]),'valores':([14,57,],[26,101,]),'valor':([14,25,57,141,192,],[27,50,27,50,205,]),'operacion':([14,25,57,58,64,141,192,],[34,34,34,103,105,34,34,]),'argumentologico':([14,25,46,47,57,80,92,136,141,192,],[35,35,85,85,35,85,140,85,35,35,]),'numero':([14,25,46,47,57,68,75,80,92,96,100,136,141,160,178,192,],[36,51,36,36,36,112,117,36,36,144,155,36,36,182,155,206,]),'else':([16,38,],[37,78,]),'elseif':([16,207,],[38,212,]),'tipo_funcion':([19,],[41,]),'operador':([28,29,49,51,54,55,95,102,104,],[58,64,96,96,58,64,96,58,64,]),'operador_logico':([32,36,49,51,86,206,],[68,75,68,75,68,75,]),'condicion':([46,47,80,136,],[84,91,127,171,]),'masTerminos':([49,51,95,],[94,99,143,]),'termino':([49,51,95,],[95,95,95,]),'lineas':([79,81,120,130,170,172,183,219,220,],[119,130,157,130,187,188,197,222,223,]),'linea':([79,81,120,130,170,172,183,219,220,],[120,120,120,120,120,120,120,120,120,]),'final_funcion':([81,130,],[128,164,]),'mas_objetos':([83,133,],[132,167,]),'cuerpo_objeto':([83,133,],[133,133,]),'conector_logico':([85,],[136,]),'elementos':([100,],[148,]),'lista':([100,],[149,]),'diccionario':([100,211,],[150,217,]),'palabras':([100,177,],[151,194,]),'numeros':([100,178,],[152,195,]),'variables':([100,174,],[153,190,]),'valor_dic':([192,],[204,]),'mas_atributos':([224,229,],[228,231,]),'atributo':([224,229,],[229,229,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencia","S'",1,None,None,None),
  ('sentencia -> asignacion','sentencia',1,'p_sentencia','main.py',11),
  ('sentencia -> echo','sentencia',1,'p_sentencia','main.py',12),
  ('sentencia -> estructuracontrol','sentencia',1,'p_sentencia','main.py',13),
  ('sentencia -> comentario','sentencia',1,'p_sentencia','main.py',14),
  ('sentencia -> declaracion_numeros','sentencia',1,'p_sentencia','main.py',15),
  ('sentencia -> array','sentencia',1,'p_sentencia','main.py',16),
  ('sentencia -> funcion','sentencia',1,'p_sentencia','main.py',17),
  ('sentencia -> readline','sentencia',1,'p_sentencia','main.py',18),
  ('sentencia -> ingreso_datos','sentencia',1,'p_sentencia','main.py',19),
  ('sentencia -> objeto','sentencia',1,'p_sentencia','main.py',20),
  ('sentencia -> expresionAritmetica','sentencia',1,'p_sentencia','main.py',21),
  ('asignacion -> VAR ASIGNACION valor EOL','asignacion',4,'p_asignacion','main.py',26),
  ('echo -> ECHO valores EOL','echo',3,'p_echo','main.py',31),
  ('valores -> valor','valores',1,'p_valores','main.py',40),
  ('valores -> valor COMA valores','valores',3,'p_valores','main.py',41),
  ('valor -> ENTERO','valor',1,'p_valor','main.py',45),
  ('valor -> FLOTANTE','valor',1,'p_valor','main.py',46),
  ('valor -> BOOLEANO','valor',1,'p_valor','main.py',47),
  ('valor -> CADENA','valor',1,'p_valor','main.py',48),
  ('valor -> VAR','valor',1,'p_valor','main.py',49),
  ('valor -> VARIABLE_ARRAY','valor',1,'p_valor','main.py',50),
  ('valor -> operacion','valor',1,'p_valor','main.py',51),
  ('valor -> argumentologico','valor',1,'p_valor','main.py',52),
  ('operacion -> ENTERO','operacion',1,'p_operacion','main.py',57),
  ('operacion -> FLOTANTE','operacion',1,'p_operacion','main.py',58),
  ('operacion -> ENTERO operador operacion','operacion',3,'p_operacion','main.py',59),
  ('operacion -> FLOTANTE operador operacion','operacion',3,'p_operacion','main.py',60),
  ('estructuracontrol -> while','estructuracontrol',1,'p_estructuracontrol','main.py',65),
  ('estructuracontrol -> if','estructuracontrol',1,'p_estructuracontrol','main.py',66),
  ('estructuracontrol -> for','estructuracontrol',1,'p_estructuracontrol','main.py',67),
  ('while -> WHILE LPAREN condicion RPAREN LBRACE lineas RBRACE','while',7,'p_while','main.py',72),
  ('if -> IF LPAREN condicion RPAREN LBRACE lineas RBRACE','if',7,'p_if','main.py',77),
  ('if -> if else','if',2,'p_if','main.py',78),
  ('if -> if elseif else','if',3,'p_if','main.py',79),
  ('if -> if elseif','if',2,'p_if','main.py',80),
  ('elseif -> ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE','elseif',7,'p_elseif','main.py',85),
  ('elseif -> ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE elseif','elseif',8,'p_elseif','main.py',86),
  ('else -> ELSE LBRACE lineas RBRACE','else',4,'p_else','main.py',91),
  ('condicion -> argumentologico','condicion',1,'p_condicion','main.py',96),
  ('condicion -> argumentologico conector_logico condicion','condicion',3,'p_condicion','main.py',97),
  ('vacio -> EOL','vacio',1,'p_vacio','main.py',101),
  ('conector_logico -> AND','conector_logico',1,'p_conector_logico','main.py',111),
  ('conector_logico -> OR','conector_logico',1,'p_conector_logico','main.py',112),
  ('valor_logico -> numero','valor_logico',1,'p_valor_logico','main.py',117),
  ('valor_logico -> VAR','valor_logico',1,'p_valor_logico','main.py',118),
  ('argumentologico -> VAR operador_logico VAR','argumentologico',3,'p_argumentologico','main.py',123),
  ('argumentologico -> numero operador_logico numero','argumentologico',3,'p_argumentologico','main.py',124),
  ('argumentologico -> VAR operador_logico numero','argumentologico',3,'p_argumentologico','main.py',125),
  ('argumentologico -> VAR IGUAL BOOLEANO','argumentologico',3,'p_argumentologico','main.py',126),
  ('argumentologico -> VAR IGUAL CADENA','argumentologico',3,'p_argumentologico','main.py',127),
  ('argumentologico -> VAR DIFERENTE BOOLEANO','argumentologico',3,'p_argumentologico','main.py',128),
  ('argumentologico -> VAR DIFERENTE CADENA','argumentologico',3,'p_argumentologico','main.py',129),
  ('argumentologico -> numero operador_logico VAR','argumentologico',3,'p_argumentologico','main.py',130),
  ('argumentologico -> BOOLEANO IGUAL VAR','argumentologico',3,'p_argumentologico','main.py',131),
  ('argumentologico -> CADENA IGUAL VAR','argumentologico',3,'p_argumentologico','main.py',132),
  ('argumentologico -> CADENA IGUAL CADENA','argumentologico',3,'p_argumentologico','main.py',133),
  ('argumentologico -> CADENA DIFERENTE VAR','argumentologico',3,'p_argumentologico','main.py',134),
  ('argumentologico -> CADENA DIFERENTE CADENA','argumentologico',3,'p_argumentologico','main.py',135),
  ('argumentologico -> BOOLEANO','argumentologico',1,'p_argumentologico','main.py',136),
  ('numero -> ENTERO','numero',1,'p_numero','main.py',141),
  ('numero -> FLOTANTE','numero',1,'p_numero','main.py',142),
  ('operador_logico -> IGUAL','operador_logico',1,'p_operador_logico','main.py',147),
  ('operador_logico -> DIFERENTE','operador_logico',1,'p_operador_logico','main.py',148),
  ('operador_logico -> MENOR','operador_logico',1,'p_operador_logico','main.py',149),
  ('operador_logico -> MAYOR','operador_logico',1,'p_operador_logico','main.py',150),
  ('operador_logico -> MENOR_IGUAL','operador_logico',1,'p_operador_logico','main.py',151),
  ('operador_logico -> MAYOR_IGUAL','operador_logico',1,'p_operador_logico','main.py',152),
  ('comentario -> COMNT','comentario',1,'p_comentario','main.py',158),
  ('operador -> SUMA','operador',1,'p_operador','main.py',162),
  ('operador -> RESTA','operador',1,'p_operador','main.py',163),
  ('operador -> MULT','operador',1,'p_operador','main.py',164),
  ('operador -> DIV','operador',1,'p_operador','main.py',165),
  ('operador -> POT','operador',1,'p_operador','main.py',166),
  ('declaracion_numeros -> VAR ASIGNACION numero EOL','declaracion_numeros',4,'p_declaracion_numeros','main.py',176),
  ('array -> VAR ASIGNACION ARRAY LPAREN elementos RPAREN EOL','array',7,'p_array','main.py',179),
  ('elementos -> lista','elementos',1,'p_elementos','main.py',182),
  ('elementos -> diccionario','elementos',1,'p_elementos','main.py',183),
  ('diccionario -> CADENA ASIGNACION MAYOR valor_dic','diccionario',4,'p_diccionario','main.py',186),
  ('diccionario -> CADENA ASIGNACION MAYOR valor COMA diccionario','diccionario',6,'p_diccionario','main.py',187),
  ('valor_dic -> numero','valor_dic',1,'p_valor_dic','main.py',190),
  ('valor_dic -> CADENA','valor_dic',1,'p_valor_dic','main.py',191),
  ('lista -> palabras','lista',1,'p_lista','main.py',194),
  ('lista -> numeros','lista',1,'p_lista','main.py',195),
  ('lista -> variables','lista',1,'p_lista','main.py',196),
  ('palabras -> CADENA COMA palabras','palabras',3,'p_palabras','main.py',199),
  ('palabras -> CADENA','palabras',1,'p_palabras','main.py',200),
  ('numeros -> numero COMA numeros','numeros',3,'p_numeros','main.py',203),
  ('numeros -> numero','numeros',1,'p_numeros','main.py',204),
  ('variables -> VAR COMA variables','variables',3,'p_variables','main.py',207),
  ('variables -> VAR','variables',1,'p_variables','main.py',208),
  ('funcion -> FUNCTION tipo_funcion LBRACE final_funcion RBRACE','funcion',5,'p_funcion','main.py',211),
  ('tipo_funcion -> FUNCION','tipo_funcion',1,'p_tipo_funcion','main.py',214),
  ('tipo_funcion -> VARIABLE_FUNCION','tipo_funcion',1,'p_tipo_funcion','main.py',215),
  ('final_funcion -> RETURN VAR EOL','final_funcion',3,'p_final_funcion','main.py',218),
  ('final_funcion -> lineas final_funcion','final_funcion',2,'p_final_funcion','main.py',219),
  ('cuerpo_funcion -> declaracion_numeros final_funcion','cuerpo_funcion',2,'p_cuerpo_funcion','main.py',223),
  ('cuerpo_funcion -> array final_funcion','cuerpo_funcion',2,'p_cuerpo_funcion','main.py',224),
  ('cuerpo_funcion -> estructuracontrol final_funcion','cuerpo_funcion',2,'p_cuerpo_funcion','main.py',225),
  ('readline -> READLINE LPAREN CADENA RPAREN EOL','readline',5,'p_readline','main.py',234),
  ('ingreso_datos -> VAR ASIGNACION readline','ingreso_datos',3,'p_ingreso_datos','main.py',238),
  ('objeto -> CLASE OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL mas_atributos','objeto',13,'p_objeto','main.py',244),
  ('cuerpo_objeto -> PUBLIC VAR EOL','cuerpo_objeto',3,'p_cuerpo_objeto','main.py',249),
  ('cuerpo_objeto -> PUBLIC asignacion','cuerpo_objeto',2,'p_cuerpo_objeto','main.py',250),
  ('mas_objetos -> cuerpo_objeto','mas_objetos',1,'p_mas_objetos','main.py',255),
  ('mas_objetos -> cuerpo_objeto mas_objetos','mas_objetos',2,'p_mas_objetos','main.py',256),
  ('atributo -> VAR RESTA MAYOR ID ASIGNACION CADENA EOL','atributo',7,'p_atributo','main.py',261),
  ('mas_atributos -> atributo','mas_atributos',1,'p_mas_atributos','main.py',266),
  ('mas_atributos -> atributo mas_atributos','mas_atributos',2,'p_mas_atributos','main.py',267),
  ('for -> FOR LPAREN asignacion argumentologico EOL VAR SUMA SUMA RPAREN LBRACE lineas RBRACE','for',12,'p_for','main.py',272),
  ('for -> FOR LPAREN asignacion argumentologico EOL VAR RESTA RESTA RPAREN LBRACE lineas RBRACE','for',12,'p_for','main.py',273),
  ('linea -> ECHO CADENA EOL','linea',3,'p_linea','main.py',278),
  ('linea -> ECHO VAR EOL','linea',3,'p_linea','main.py',279),
  ('linea -> VAR ASIGNACION CADENA EOL','linea',4,'p_linea','main.py',280),
  ('linea -> estructuracontrol','linea',1,'p_linea','main.py',281),
  ('linea -> comentario','linea',1,'p_linea','main.py',282),
  ('linea -> declaracion_numeros','linea',1,'p_linea','main.py',283),
  ('linea -> array','linea',1,'p_linea','main.py',284),
  ('lineas -> linea','lineas',1,'p_lineas','main.py',289),
  ('lineas -> linea lineas','lineas',2,'p_lineas','main.py',290),
  ('expresionAritmetica -> VAR ASIGNACION numero masTerminos EOL','expresionAritmetica',5,'p_expresionAritmetica','main.py',295),
  ('expresionAritmetica -> VAR ASIGNACION VAR masTerminos EOL','expresionAritmetica',5,'p_expresionAritmetica','main.py',296),
  ('termino -> operador numero','termino',2,'p_termino','main.py',301),
  ('termino -> operador VAR','termino',2,'p_termino','main.py',302),
  ('masTerminos -> termino','masTerminos',1,'p_masTerminos','main.py',306),
  ('masTerminos -> termino masTerminos','masTerminos',2,'p_masTerminos','main.py',307),
]
