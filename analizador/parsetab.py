
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ARRAY ARRAY ASIGNACION ASIGNAR BOOLEANO BREAK CADENA CASE CLASE COMA COMILLA_DOBLE COMILLA_DOBLE_CADENA COMILLA_SIMPLE COMILLA_SIMPLE_CADENA COMNT CONTINUE DICT DIFERENTE DIV DIV_ASIGNAR DO DOSPUNTOS ECHO ELSE ELSEIF ENDWHILE ENTERO EOL EXTENDS FLOTANTE FOR FOREACH FUNCION FUNCTION GLOBAL ID IF IGUAL INDENT LBRACE LBRACKET LPAREN MAYOR MAYOR_IGUAL MAYOR_MENOR MENOR MENOR_IGUAL MENOR_MAYOR MODULO MULT MULT_ASIGNAR NEW OBJETO OR POT POT_ASIGNAR PUBLIC PUNTO RBRACE RBRACKET READLINE RESTA RESTA_ASIGNAR RETURN RPAREN SALTO SET SUMA SUMA_ASIGNAR SWITCH TUPLE VAR VARIABLE_ARRAY VARIABLE_FUNCION VARIABLE_OBJETO WHILEsentencia : asignacion\n                | echo\n                | estructuracontrol\n                | comentario\n                | declaracion_numeros\n                | array\n                | funcion\n                | readline\n                | ingreso_datos\n                | objeto\n                | expresionAritmetica\n                | echo SALTO\n                \n  asignacion : VAR ASIGNACION valor EOL\n   echo : ECHO valores EOL \n         | ECHO valores EOL SALTO\n   \n   valores : valor\n           | valor COMA valores\n   valor : ENTERO\n          | FLOTANTE\n          | BOOLEANO    \n          | CADENA\n          | VAR\n          | VARIABLE_ARRAY\n          | operacion\n          | argumentologico\n          | array_index\n  diccionario : clave_dic ASIGNACION MAYOR valor_dic\n                 | clave_dic ASIGNACION MAYOR valor_dic COMA diccionarioclave_dic : ENTERO\n                | CADENAvalor_dic : numero\n           | CADENA\n           | VAR\n           | BOOLEANO\n           | array_larray_index : VAR multi_dimensiones multi_dimensiones : LBRACKET clave_dic RBRACKET\n                       | LBRACKET clave_dic RBRACKET multi_dimensiones\n  \n   operacion : ENTERO \n            | FLOTANTE\n            | ENTERO operador operacion\n            | FLOTANTE operador operacion\n   \n   estructuracontrol : while\n                     | if\n                     | for\n   \n   while : WHILE LPAREN condicion RPAREN LBRACE lineas RBRACE\n   \n   if : IF LPAREN condicion RPAREN LBRACE lineas RBRACE\n      | if else\n      | if elseif else\n      | if elseif\n   \n   elseif : ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE\n          | ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE elseif\n   \n   else : ELSE LBRACE lineas RBRACE\n   \n   condicion : argumentologico \n             | argumentologico conector_logico condicion\n   \n   vacio : EOL\n   \n   conector_logico : AND\n                   | OR\n   \n   valor_logico : numero\n                | VAR\n   \n   argumentologico : VAR operador_logico VAR\n                   | numero operador_logico numero\n                   | VAR operador_logico numero\n                   | VAR IGUAL BOOLEANO\n                   | VAR IGUAL CADENA\n                   | VAR DIFERENTE BOOLEANO\n                   | VAR DIFERENTE CADENA\n                   | numero operador_logico VAR\n                   | BOOLEANO IGUAL VAR\n                   | CADENA IGUAL VAR\n                   | CADENA IGUAL CADENA\n                   | CADENA DIFERENTE VAR\n                   | CADENA DIFERENTE CADENA\n                   | BOOLEANO     \n   \n   numero : ENTERO\n          | FLOTANTE\n   \n   operador_logico : IGUAL\n                 | DIFERENTE\n                 | MENOR\n                 | MAYOR\n                 | MENOR_IGUAL\n                 | MAYOR_IGUAL      \n   \n   comentario : COMNT\n   \n   operador : SUMA \n            | RESTA \n            | MULT \n            | DIV \n            | POT\n   declaracion_numeros : VAR ASIGNACION numero EOLarray : VAR ASIGNACION ARRAY LPAREN elementos RPAREN EOLelementos : lista\n               | diccionariolista : palabras\n           | numeros\n           | variables\n           | array_l\n           | boolarray_l : ARRAY LPAREN elementos RPAREN\n             | ARRAY LPAREN elementos RPAREN COMA listapalabras : CADENA\n              | CADENA COMA listanumeros : numero\n             | numero COMA listavariables : VAR\n               | VAR COMA listabool : BOOLEANO\n          | BOOLEANO COMA listafuncion : FUNCTION tipo_funcion LBRACE final_funcion RBRACEtipo_funcion : FUNCION\n                  | VARIABLE_FUNCIONfinal_funcion : RETURN VAR EOL\n                    | lineas final_funcion\n  cuerpo_funcion : declaracion_numeros final_funcion\n                    | array final_funcion\n                    | estructuracontrol final_funcionreadline : READLINE LPAREN CADENA RPAREN EOL\n   ingreso_datos : VAR ASIGNACION readline\n   \n   objeto : CLASE OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL mas_atributos\n          | CLASE OBJETO EXTENDS OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL mas_atributos\n   \n   cuerpo_objeto : PUBLIC VAR EOL\n                 | PUBLIC asignacion\n                 | PUBLIC funcion\n   \n   mas_objetos : cuerpo_objeto\n               | cuerpo_objeto mas_objetos \n   \n   atributo : VAR RESTA MAYOR ID ASIGNACION CADENA EOL\n   \n   mas_atributos : atributo\n                 | atributo mas_atributos\n   \n   for : FOR LPAREN asignacion argumentologico EOL VAR SUMA SUMA RPAREN LBRACE lineas RBRACE\n                  | FOR LPAREN asignacion argumentologico EOL VAR RESTA RESTA RPAREN LBRACE lineas RBRACE\n                  | FOR LPAREN asignacion argumentologico EOL VAR SUMA SUMA RPAREN LBRACE SALTO lineas SALTO RBRACE\n   \n   linea : echo \n         | ECHO CADENA EOL \n         | ECHO VAR EOL\n         | VAR ASIGNACION CADENA EOL \n         | estructuracontrol\n         | comentario\n         | declaracion_numeros\n         | array\n   \n   lineas : linea\n          | linea lineas\n   \n   expresionAritmetica : VAR ASIGNACION numero masTerminos EOL\n                       | VAR ASIGNACION VAR masTerminos EOL\n   \n   termino : operador numero\n           | operador VAR\n   \n   masTerminos : termino\n               | termino masTerminos\n   '
    
_lr_action_items = {'VAR':([0,14,15,16,17,18,26,39,40,48,49,50,58,59,61,62,63,64,65,67,68,69,70,71,72,74,75,76,77,79,80,81,82,83,84,85,97,101,102,103,105,106,129,130,131,133,134,135,136,139,140,144,147,148,149,152,174,175,184,190,192,193,194,195,198,199,200,202,203,206,217,218,222,225,226,227,237,242,244,253,254,258,260,262,264,267,272,273,279,],[13,33,-43,-44,-45,-83,51,-48,-50,91,91,98,-14,33,-84,-85,-86,-87,-88,112,114,116,117,-77,-78,-79,-80,-81,-82,127,-77,-78,-49,132,91,132,91,156,-13,-89,158,-15,132,-131,177,-135,-136,-137,-138,181,132,186,91,-57,-58,33,-53,-140,208,132,132,213,158,158,158,158,158,-132,-133,132,-90,234,-134,239,-46,-47,-51,158,-52,132,132,132,265,-128,-129,265,265,-130,-125,]),'ECHO':([0,15,16,17,18,39,40,58,82,83,85,103,106,129,130,133,134,135,136,140,174,175,190,192,202,203,206,217,222,226,227,237,244,253,254,258,262,264,273,],[14,-43,-44,-45,-83,-48,-50,-14,-49,131,131,-89,-15,131,-131,-135,-136,-137,-138,131,-53,-140,131,131,-132,-133,131,-90,-134,-46,-47,-51,-52,131,131,131,-128,-129,-130,]),'COMNT':([0,15,16,17,18,39,40,58,82,83,85,103,106,129,130,133,134,135,136,140,174,175,190,192,202,203,206,217,222,226,227,237,244,253,254,258,262,264,273,],[18,-43,-44,-45,-83,-48,-50,-14,-49,18,18,-89,-15,18,-131,-135,-136,-137,-138,18,-53,-140,18,18,-132,-133,18,-90,-134,-46,-47,-51,-52,18,18,18,-128,-129,-130,]),'FUNCTION':([0,144,],[19,19,]),'READLINE':([0,26,],[20,20,]),'CLASE':([0,],[21,]),'WHILE':([0,15,16,17,18,39,40,58,82,83,85,103,106,129,130,133,134,135,136,140,174,175,190,192,202,203,206,217,222,226,227,237,244,253,254,258,262,264,273,],[22,-43,-44,-45,-83,-48,-50,-14,-49,22,22,-89,-15,22,-131,-135,-136,-137,-138,22,-53,-140,22,22,-132,-133,22,-90,-134,-46,-47,-51,-52,22,22,22,-128,-129,-130,]),'IF':([0,15,16,17,18,39,40,58,82,83,85,103,106,129,130,133,134,135,136,140,174,175,190,192,202,203,206,217,222,226,227,237,244,253,254,258,262,264,273,],[23,-43,-44,-45,-83,-48,-50,-14,-49,23,23,-89,-15,23,-131,-135,-136,-137,-138,23,-53,-140,23,23,-132,-133,23,-90,-134,-46,-47,-51,-52,23,23,23,-128,-129,-130,]),'FOR':([0,15,16,17,18,39,40,58,82,83,85,103,106,129,130,133,134,135,136,140,174,175,190,192,202,203,206,217,222,226,227,237,244,253,254,258,262,264,273,],[24,-43,-44,-45,-83,-48,-50,-14,-49,24,24,-89,-15,24,-131,-135,-136,-137,-138,24,-53,-140,24,24,-132,-133,24,-90,-134,-46,-47,-51,-52,24,24,24,-128,-129,-130,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,15,16,17,18,25,39,40,55,58,82,102,103,106,153,157,174,180,183,217,226,227,237,244,262,264,266,267,271,273,275,279,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-43,-44,-45,-83,-12,-48,-50,-117,-14,-49,-13,-89,-15,-142,-141,-53,-108,-116,-90,-46,-47,-51,-52,-128,-129,-118,-126,-127,-130,-119,-125,]),'SALTO':([3,15,16,17,18,39,40,58,82,103,106,129,130,133,134,135,136,174,175,202,203,217,222,226,227,237,244,253,262,263,264,273,],[25,-43,-44,-45,-83,-48,-50,106,-49,-89,-15,-139,-131,-135,-136,-137,-138,-53,-140,-132,-133,-90,-134,-46,-47,-51,-52,258,-128,269,-129,-130,]),'ASIGNACION':([13,98,124,125,132,168,169,172,186,208,239,276,],[26,152,-29,-30,178,197,-30,-29,152,224,246,277,]),'ENTERO':([14,26,48,49,59,60,61,62,63,64,65,66,70,71,72,74,75,76,77,78,79,80,81,84,97,101,102,105,131,147,148,149,152,178,194,195,198,199,200,218,242,243,],[29,56,94,94,29,108,-84,-85,-86,-87,-88,108,94,-77,-78,-79,-80,-81,-82,124,94,-77,-78,94,94,94,-13,172,29,94,-57,-58,29,94,94,172,94,94,94,94,94,124,]),'FLOTANTE':([14,26,48,49,59,60,61,62,63,64,65,66,70,71,72,74,75,76,77,79,80,81,84,97,101,102,105,131,147,148,149,152,178,194,195,198,199,200,218,242,],[30,57,95,95,30,110,-84,-85,-86,-87,-88,110,95,-77,-78,-79,-80,-81,-82,95,-77,-78,95,95,95,-13,95,30,95,-57,-58,30,95,95,95,95,95,95,95,95,]),'BOOLEANO':([14,26,48,49,59,71,72,84,97,102,105,131,147,148,149,152,194,195,198,199,200,218,242,],[31,31,92,92,31,119,121,92,92,-13,171,31,92,-57,-58,31,171,171,171,171,171,235,171,]),'CADENA':([14,26,46,48,49,59,68,69,71,72,78,84,97,102,105,131,147,148,149,152,178,194,195,198,199,200,218,242,243,277,],[32,32,86,93,93,32,113,115,120,122,125,93,93,-13,169,176,93,-57,-58,32,204,215,169,215,215,215,233,215,125,278,]),'VARIABLE_ARRAY':([14,26,59,131,152,],[34,34,34,34,34,]),'RBRACE':([15,16,17,18,39,40,58,82,102,103,106,128,129,130,133,134,135,136,138,142,143,174,175,180,182,185,187,188,202,203,207,209,210,211,212,217,222,223,226,227,237,244,257,259,262,264,269,273,],[-43,-44,-45,-83,-48,-50,-14,-49,-13,-89,-15,174,-139,-131,-135,-136,-137,-138,180,184,-123,-53,-140,-108,-112,-124,-121,-122,-132,-133,-111,-120,225,226,227,-90,-134,237,-46,-47,-51,-52,262,264,-128,-129,273,-130,]),'RETURN':([15,16,17,18,39,40,58,82,85,103,106,129,130,133,134,135,136,140,174,175,202,203,217,222,226,227,237,244,262,264,273,],[-43,-44,-45,-83,-48,-50,-14,-49,139,-89,-15,-139,-131,-135,-136,-137,-138,139,-53,-140,-132,-133,-90,-134,-46,-47,-51,-52,-128,-129,-130,]),'ELSE':([16,39,40,82,174,227,237,244,],[41,-48,41,-49,-53,-47,-51,-52,]),'ELSEIF':([16,39,40,82,174,227,237,244,],[42,-48,-50,-49,-53,-47,42,-52,]),'FUNCION':([19,],[44,]),'VARIABLE_FUNCION':([19,],[45,]),'LPAREN':([20,22,23,24,42,54,159,245,256,],[46,48,49,50,84,105,195,251,261,]),'OBJETO':([21,88,238,252,],[47,145,245,256,]),'ARRAY':([26,105,178,194,195,198,199,200,218,242,],[54,159,54,159,159,159,159,159,159,159,]),'EOL':([27,28,29,30,31,32,33,34,35,36,37,51,52,53,56,57,73,92,94,95,99,100,104,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,126,127,141,151,154,155,156,173,176,177,181,186,196,201,204,205,255,268,278,],[58,-16,-18,-19,-20,-21,-22,-23,-24,-25,-26,-22,102,103,-18,-19,-36,-74,-75,-76,153,-145,157,-17,-39,-41,-40,-42,-69,-71,-70,-73,-72,-61,-63,-64,-65,-66,-67,-62,-68,183,193,-146,-143,-144,-37,202,203,207,209,217,-38,222,103,260,272,279,]),'COMA':([28,29,30,31,32,33,34,35,36,37,73,94,95,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,126,127,158,163,164,165,166,167,169,170,171,172,173,176,177,201,214,215,219,220,221,230,231,232,233,234,235,236,249,],[59,-18,-19,-20,-21,-22,-23,-24,-25,-26,-36,-75,-76,-39,-41,-40,-42,-69,-71,-70,-73,-72,-61,-63,-64,-65,-66,-67,-62,-68,194,-93,-94,-95,-96,-97,198,199,200,-75,-37,-21,-22,-38,-105,198,-101,-103,-107,242,243,-31,-32,-33,-34,-35,-99,]),'IGUAL':([29,30,31,32,33,38,51,53,56,57,91,92,93,94,95,176,177,],[-75,-76,67,68,71,80,71,80,-75,-76,71,67,68,-75,-76,68,71,]),'DIFERENTE':([29,30,32,33,38,51,53,56,57,91,93,94,95,176,177,],[-75,-76,69,72,81,72,81,-75,-76,72,69,-75,-76,69,72,]),'MENOR':([29,30,33,38,51,53,56,57,91,94,95,177,],[-75,-76,74,74,74,74,-75,-76,74,-75,-76,74,]),'MAYOR':([29,30,33,38,51,53,56,57,91,94,95,177,197,270,],[-75,-76,75,75,75,75,-75,-76,75,-75,-76,75,218,274,]),'MENOR_IGUAL':([29,30,33,38,51,53,56,57,91,94,95,177,],[-75,-76,76,76,76,76,-75,-76,76,-75,-76,76,]),'MAYOR_IGUAL':([29,30,33,38,51,53,56,57,91,94,95,177,],[-75,-76,77,77,77,77,-75,-76,77,-75,-76,77,]),'SUMA':([29,30,51,53,56,57,94,95,100,108,110,155,156,213,228,],[61,61,61,61,61,61,-75,-76,61,61,61,-143,-144,228,240,]),'RESTA':([29,30,51,53,56,57,94,95,100,108,110,155,156,213,229,265,],[62,62,62,62,62,62,-75,-76,62,62,62,-143,-144,229,241,270,]),'MULT':([29,30,51,53,56,57,94,95,100,108,110,155,156,],[63,63,63,63,63,63,-75,-76,63,63,63,-143,-144,]),'DIV':([29,30,51,53,56,57,94,95,100,108,110,155,156,],[64,64,64,64,64,64,-75,-76,64,64,64,-143,-144,]),'POT':([29,30,51,53,56,57,94,95,100,108,110,155,156,],[65,65,65,65,65,65,-75,-76,65,65,65,-143,-144,]),'LBRACKET':([33,51,173,177,],[78,78,78,78,]),'LBRACE':([41,43,44,45,47,145,146,150,179,247,248,],[83,85,-109,-110,87,189,190,192,206,253,254,]),'EXTENDS':([47,],[88,]),'RPAREN':([86,89,90,92,94,95,96,112,113,114,115,116,117,118,119,120,121,122,126,127,137,158,160,161,162,163,164,165,166,167,169,170,171,172,191,214,215,216,219,220,221,230,231,232,233,234,235,236,240,241,249,250,251,261,],[141,146,-54,-74,-75,-76,150,-69,-71,-70,-73,-72,-61,-63,-64,-65,-66,-67,-62,-68,179,-104,196,-91,-92,-93,-94,-95,-96,-97,-100,-102,-106,-75,-55,-105,-100,230,-101,-103,-107,-98,-27,-31,-32,-33,-34,-35,247,248,-99,-28,255,268,]),'PUBLIC':([87,102,143,180,187,188,189,209,],[144,-13,144,-108,-121,-122,144,-120,]),'AND':([90,92,94,95,112,113,114,115,116,117,118,119,120,121,122,126,127,],[148,-74,-75,-76,-69,-71,-70,-73,-72,-61,-63,-64,-65,-66,-67,-62,-68,]),'OR':([90,92,94,95,112,113,114,115,116,117,118,119,120,121,122,126,127,],[149,-74,-75,-76,-69,-71,-70,-73,-72,-61,-63,-64,-65,-66,-67,-62,-68,]),'RBRACKET':([123,124,125,],[173,-29,-30,]),'NEW':([224,246,],[238,252,]),'ID':([274,],[276,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,],[1,]),'asignacion':([0,50,144,],[2,97,187,]),'echo':([0,83,85,129,140,190,192,206,253,254,258,],[3,130,130,130,130,130,130,130,130,130,130,]),'estructuracontrol':([0,83,85,129,140,190,192,206,253,254,258,],[4,133,133,133,133,133,133,133,133,133,133,]),'comentario':([0,83,85,129,140,190,192,206,253,254,258,],[5,134,134,134,134,134,134,134,134,134,134,]),'declaracion_numeros':([0,83,85,129,140,190,192,206,253,254,258,],[6,135,135,135,135,135,135,135,135,135,135,]),'array':([0,83,85,129,140,190,192,206,253,254,258,],[7,136,136,136,136,136,136,136,136,136,136,]),'funcion':([0,144,],[8,188,]),'readline':([0,26,],[9,55,]),'ingreso_datos':([0,],[10,]),'objeto':([0,],[11,]),'expresionAritmetica':([0,],[12,]),'while':([0,83,85,129,140,190,192,206,253,254,258,],[15,15,15,15,15,15,15,15,15,15,15,]),'if':([0,83,85,129,140,190,192,206,253,254,258,],[16,16,16,16,16,16,16,16,16,16,16,]),'for':([0,83,85,129,140,190,192,206,253,254,258,],[17,17,17,17,17,17,17,17,17,17,17,]),'valores':([14,59,131,],[27,107,27,]),'valor':([14,26,59,131,152,],[28,52,28,28,52,]),'operacion':([14,26,59,60,66,131,152,],[35,35,35,109,111,35,35,]),'argumentologico':([14,26,48,49,59,84,97,131,147,152,],[36,36,90,90,36,90,151,36,90,36,]),'array_index':([14,26,59,131,152,],[37,37,37,37,37,]),'numero':([14,26,48,49,59,70,79,84,97,101,105,131,147,152,178,194,195,198,199,200,218,242,],[38,53,38,38,38,118,126,38,38,155,170,38,38,38,205,170,170,170,170,170,232,170,]),'else':([16,40,],[39,82,]),'elseif':([16,237,],[40,244,]),'tipo_funcion':([19,],[43,]),'operador':([29,30,51,53,56,57,100,108,110,],[60,66,101,101,60,66,101,60,66,]),'operador_logico':([33,38,51,53,91,177,],[70,79,70,79,70,70,]),'multi_dimensiones':([33,51,173,177,],[73,73,201,73,]),'condicion':([48,49,84,147,],[89,96,137,191,]),'masTerminos':([51,53,100,],[99,104,154,]),'termino':([51,53,100,],[100,100,100,]),'clave_dic':([78,105,195,243,],[123,168,168,168,]),'lineas':([83,85,129,140,190,192,206,253,254,258,],[128,140,175,140,211,212,223,257,259,263,]),'linea':([83,85,129,140,190,192,206,253,254,258,],[129,129,129,129,129,129,129,129,129,129,]),'final_funcion':([85,140,],[138,182,]),'mas_objetos':([87,143,189,],[142,185,210,]),'cuerpo_objeto':([87,143,189,],[143,143,143,]),'conector_logico':([90,],[147,]),'elementos':([105,195,],[160,216,]),'lista':([105,194,195,198,199,200,242,],[161,214,161,219,220,221,249,]),'diccionario':([105,195,243,],[162,162,250,]),'palabras':([105,194,195,198,199,200,242,],[163,163,163,163,163,163,163,]),'numeros':([105,194,195,198,199,200,242,],[164,164,164,164,164,164,164,]),'variables':([105,194,195,198,199,200,242,],[165,165,165,165,165,165,165,]),'array_l':([105,194,195,198,199,200,218,242,],[166,166,166,166,166,166,236,166,]),'bool':([105,194,195,198,199,200,242,],[167,167,167,167,167,167,167,]),'valor_dic':([218,],[231,]),'mas_atributos':([260,267,272,],[266,271,275,]),'atributo':([260,267,272,],[267,267,267,]),}

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
  ('sentencia -> echo SALTO','sentencia',2,'p_sentencia','main.py',22),
  ('asignacion -> VAR ASIGNACION valor EOL','asignacion',4,'p_asignacion','main.py',28),
  ('echo -> ECHO valores EOL','echo',3,'p_echo','main.py',33),
  ('echo -> ECHO valores EOL SALTO','echo',4,'p_echo','main.py',34),
  ('valores -> valor','valores',1,'p_valores','main.py',43),
  ('valores -> valor COMA valores','valores',3,'p_valores','main.py',44),
  ('valor -> ENTERO','valor',1,'p_valor','main.py',48),
  ('valor -> FLOTANTE','valor',1,'p_valor','main.py',49),
  ('valor -> BOOLEANO','valor',1,'p_valor','main.py',50),
  ('valor -> CADENA','valor',1,'p_valor','main.py',51),
  ('valor -> VAR','valor',1,'p_valor','main.py',52),
  ('valor -> VARIABLE_ARRAY','valor',1,'p_valor','main.py',53),
  ('valor -> operacion','valor',1,'p_valor','main.py',54),
  ('valor -> argumentologico','valor',1,'p_valor','main.py',55),
  ('valor -> array_index','valor',1,'p_valor','main.py',56),
  ('diccionario -> clave_dic ASIGNACION MAYOR valor_dic','diccionario',4,'p_diccionario','main.py',67),
  ('diccionario -> clave_dic ASIGNACION MAYOR valor_dic COMA diccionario','diccionario',6,'p_diccionario','main.py',68),
  ('clave_dic -> ENTERO','clave_dic',1,'p_clave_dic','main.py',71),
  ('clave_dic -> CADENA','clave_dic',1,'p_clave_dic','main.py',72),
  ('valor_dic -> numero','valor_dic',1,'p_valor_dic','main.py',75),
  ('valor_dic -> CADENA','valor_dic',1,'p_valor_dic','main.py',76),
  ('valor_dic -> VAR','valor_dic',1,'p_valor_dic','main.py',77),
  ('valor_dic -> BOOLEANO','valor_dic',1,'p_valor_dic','main.py',78),
  ('valor_dic -> array_l','valor_dic',1,'p_valor_dic','main.py',79),
  ('array_index -> VAR multi_dimensiones','array_index',2,'p_array_index','main.py',82),
  ('multi_dimensiones -> LBRACKET clave_dic RBRACKET','multi_dimensiones',3,'p_mul_dimensiones','main.py',95),
  ('multi_dimensiones -> LBRACKET clave_dic RBRACKET multi_dimensiones','multi_dimensiones',4,'p_mul_dimensiones','main.py',96),
  ('operacion -> ENTERO','operacion',1,'p_operacion','main.py',102),
  ('operacion -> FLOTANTE','operacion',1,'p_operacion','main.py',103),
  ('operacion -> ENTERO operador operacion','operacion',3,'p_operacion','main.py',104),
  ('operacion -> FLOTANTE operador operacion','operacion',3,'p_operacion','main.py',105),
  ('estructuracontrol -> while','estructuracontrol',1,'p_estructuracontrol','main.py',110),
  ('estructuracontrol -> if','estructuracontrol',1,'p_estructuracontrol','main.py',111),
  ('estructuracontrol -> for','estructuracontrol',1,'p_estructuracontrol','main.py',112),
  ('while -> WHILE LPAREN condicion RPAREN LBRACE lineas RBRACE','while',7,'p_while','main.py',117),
  ('if -> IF LPAREN condicion RPAREN LBRACE lineas RBRACE','if',7,'p_if','main.py',122),
  ('if -> if else','if',2,'p_if','main.py',123),
  ('if -> if elseif else','if',3,'p_if','main.py',124),
  ('if -> if elseif','if',2,'p_if','main.py',125),
  ('elseif -> ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE','elseif',7,'p_elseif','main.py',130),
  ('elseif -> ELSEIF LPAREN condicion RPAREN LBRACE lineas RBRACE elseif','elseif',8,'p_elseif','main.py',131),
  ('else -> ELSE LBRACE lineas RBRACE','else',4,'p_else','main.py',136),
  ('condicion -> argumentologico','condicion',1,'p_condicion','main.py',141),
  ('condicion -> argumentologico conector_logico condicion','condicion',3,'p_condicion','main.py',142),
  ('vacio -> EOL','vacio',1,'p_vacio','main.py',146),
  ('conector_logico -> AND','conector_logico',1,'p_conector_logico','main.py',151),
  ('conector_logico -> OR','conector_logico',1,'p_conector_logico','main.py',152),
  ('valor_logico -> numero','valor_logico',1,'p_valor_logico','main.py',157),
  ('valor_logico -> VAR','valor_logico',1,'p_valor_logico','main.py',158),
  ('argumentologico -> VAR operador_logico VAR','argumentologico',3,'p_argumentologico','main.py',171),
  ('argumentologico -> numero operador_logico numero','argumentologico',3,'p_argumentologico','main.py',172),
  ('argumentologico -> VAR operador_logico numero','argumentologico',3,'p_argumentologico','main.py',173),
  ('argumentologico -> VAR IGUAL BOOLEANO','argumentologico',3,'p_argumentologico','main.py',174),
  ('argumentologico -> VAR IGUAL CADENA','argumentologico',3,'p_argumentologico','main.py',175),
  ('argumentologico -> VAR DIFERENTE BOOLEANO','argumentologico',3,'p_argumentologico','main.py',176),
  ('argumentologico -> VAR DIFERENTE CADENA','argumentologico',3,'p_argumentologico','main.py',177),
  ('argumentologico -> numero operador_logico VAR','argumentologico',3,'p_argumentologico','main.py',178),
  ('argumentologico -> BOOLEANO IGUAL VAR','argumentologico',3,'p_argumentologico','main.py',179),
  ('argumentologico -> CADENA IGUAL VAR','argumentologico',3,'p_argumentologico','main.py',180),
  ('argumentologico -> CADENA IGUAL CADENA','argumentologico',3,'p_argumentologico','main.py',181),
  ('argumentologico -> CADENA DIFERENTE VAR','argumentologico',3,'p_argumentologico','main.py',182),
  ('argumentologico -> CADENA DIFERENTE CADENA','argumentologico',3,'p_argumentologico','main.py',183),
  ('argumentologico -> BOOLEANO','argumentologico',1,'p_argumentologico','main.py',184),
  ('numero -> ENTERO','numero',1,'p_numero','main.py',189),
  ('numero -> FLOTANTE','numero',1,'p_numero','main.py',190),
  ('operador_logico -> IGUAL','operador_logico',1,'p_operador_logico','main.py',195),
  ('operador_logico -> DIFERENTE','operador_logico',1,'p_operador_logico','main.py',196),
  ('operador_logico -> MENOR','operador_logico',1,'p_operador_logico','main.py',197),
  ('operador_logico -> MAYOR','operador_logico',1,'p_operador_logico','main.py',198),
  ('operador_logico -> MENOR_IGUAL','operador_logico',1,'p_operador_logico','main.py',199),
  ('operador_logico -> MAYOR_IGUAL','operador_logico',1,'p_operador_logico','main.py',200),
  ('comentario -> COMNT','comentario',1,'p_comentario','main.py',206),
  ('operador -> SUMA','operador',1,'p_operador','main.py',210),
  ('operador -> RESTA','operador',1,'p_operador','main.py',211),
  ('operador -> MULT','operador',1,'p_operador','main.py',212),
  ('operador -> DIV','operador',1,'p_operador','main.py',213),
  ('operador -> POT','operador',1,'p_operador','main.py',214),
  ('declaracion_numeros -> VAR ASIGNACION numero EOL','declaracion_numeros',4,'p_declaracion_numeros','main.py',224),
  ('array -> VAR ASIGNACION ARRAY LPAREN elementos RPAREN EOL','array',7,'p_array','main.py',234),
  ('elementos -> lista','elementos',1,'p_elementos','main.py',237),
  ('elementos -> diccionario','elementos',1,'p_elementos','main.py',238),
  ('lista -> palabras','lista',1,'p_lista','main.py',241),
  ('lista -> numeros','lista',1,'p_lista','main.py',242),
  ('lista -> variables','lista',1,'p_lista','main.py',243),
  ('lista -> array_l','lista',1,'p_lista','main.py',244),
  ('lista -> bool','lista',1,'p_lista','main.py',245),
  ('array_l -> ARRAY LPAREN elementos RPAREN','array_l',4,'p_array_l','main.py',248),
  ('array_l -> ARRAY LPAREN elementos RPAREN COMA lista','array_l',6,'p_array_l','main.py',249),
  ('palabras -> CADENA','palabras',1,'p_palabras','main.py',252),
  ('palabras -> CADENA COMA lista','palabras',3,'p_palabras','main.py',253),
  ('numeros -> numero','numeros',1,'p_numeros','main.py',256),
  ('numeros -> numero COMA lista','numeros',3,'p_numeros','main.py',257),
  ('variables -> VAR','variables',1,'p_variables','main.py',260),
  ('variables -> VAR COMA lista','variables',3,'p_variables','main.py',261),
  ('bool -> BOOLEANO','bool',1,'p_bool','main.py',264),
  ('bool -> BOOLEANO COMA lista','bool',3,'p_bool','main.py',265),
  ('funcion -> FUNCTION tipo_funcion LBRACE final_funcion RBRACE','funcion',5,'p_funcion','main.py',269),
  ('tipo_funcion -> FUNCION','tipo_funcion',1,'p_tipo_funcion','main.py',272),
  ('tipo_funcion -> VARIABLE_FUNCION','tipo_funcion',1,'p_tipo_funcion','main.py',273),
  ('final_funcion -> RETURN VAR EOL','final_funcion',3,'p_final_funcion','main.py',276),
  ('final_funcion -> lineas final_funcion','final_funcion',2,'p_final_funcion','main.py',277),
  ('cuerpo_funcion -> declaracion_numeros final_funcion','cuerpo_funcion',2,'p_cuerpo_funcion','main.py',281),
  ('cuerpo_funcion -> array final_funcion','cuerpo_funcion',2,'p_cuerpo_funcion','main.py',282),
  ('cuerpo_funcion -> estructuracontrol final_funcion','cuerpo_funcion',2,'p_cuerpo_funcion','main.py',283),
  ('readline -> READLINE LPAREN CADENA RPAREN EOL','readline',5,'p_readline','main.py',314),
  ('ingreso_datos -> VAR ASIGNACION readline','ingreso_datos',3,'p_ingreso_datos','main.py',318),
  ('objeto -> CLASE OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL mas_atributos','objeto',13,'p_objeto','main.py',331),
  ('objeto -> CLASE OBJETO EXTENDS OBJETO LBRACE mas_objetos RBRACE VAR ASIGNACION NEW OBJETO LPAREN RPAREN EOL mas_atributos','objeto',15,'p_objeto','main.py',332),
  ('cuerpo_objeto -> PUBLIC VAR EOL','cuerpo_objeto',3,'p_cuerpo_objeto','main.py',343),
  ('cuerpo_objeto -> PUBLIC asignacion','cuerpo_objeto',2,'p_cuerpo_objeto','main.py',344),
  ('cuerpo_objeto -> PUBLIC funcion','cuerpo_objeto',2,'p_cuerpo_objeto','main.py',345),
  ('mas_objetos -> cuerpo_objeto','mas_objetos',1,'p_mas_objetos','main.py',351),
  ('mas_objetos -> cuerpo_objeto mas_objetos','mas_objetos',2,'p_mas_objetos','main.py',352),
  ('atributo -> VAR RESTA MAYOR ID ASIGNACION CADENA EOL','atributo',7,'p_atributo','main.py',357),
  ('mas_atributos -> atributo','mas_atributos',1,'p_mas_atributos','main.py',362),
  ('mas_atributos -> atributo mas_atributos','mas_atributos',2,'p_mas_atributos','main.py',363),
  ('for -> FOR LPAREN asignacion argumentologico EOL VAR SUMA SUMA RPAREN LBRACE lineas RBRACE','for',12,'p_for','main.py',368),
  ('for -> FOR LPAREN asignacion argumentologico EOL VAR RESTA RESTA RPAREN LBRACE lineas RBRACE','for',12,'p_for','main.py',369),
  ('for -> FOR LPAREN asignacion argumentologico EOL VAR SUMA SUMA RPAREN LBRACE SALTO lineas SALTO RBRACE','for',14,'p_for','main.py',370),
  ('linea -> echo','linea',1,'p_linea','main.py',375),
  ('linea -> ECHO CADENA EOL','linea',3,'p_linea','main.py',376),
  ('linea -> ECHO VAR EOL','linea',3,'p_linea','main.py',377),
  ('linea -> VAR ASIGNACION CADENA EOL','linea',4,'p_linea','main.py',378),
  ('linea -> estructuracontrol','linea',1,'p_linea','main.py',379),
  ('linea -> comentario','linea',1,'p_linea','main.py',380),
  ('linea -> declaracion_numeros','linea',1,'p_linea','main.py',381),
  ('linea -> array','linea',1,'p_linea','main.py',382),
  ('lineas -> linea','lineas',1,'p_lineas','main.py',387),
  ('lineas -> linea lineas','lineas',2,'p_lineas','main.py',388),
  ('expresionAritmetica -> VAR ASIGNACION numero masTerminos EOL','expresionAritmetica',5,'p_expresionAritmetica','main.py',393),
  ('expresionAritmetica -> VAR ASIGNACION VAR masTerminos EOL','expresionAritmetica',5,'p_expresionAritmetica','main.py',394),
  ('termino -> operador numero','termino',2,'p_termino','main.py',399),
  ('termino -> operador VAR','termino',2,'p_termino','main.py',400),
  ('masTerminos -> termino','masTerminos',1,'p_masTerminos','main.py',404),
  ('masTerminos -> termino masTerminos','masTerminos',2,'p_masTerminos','main.py',405),
]
