Comandos utilizados:
- cd Practica_2/
- nano WhileLoop.g4
- antlr4 WhileLoop.g4
- antlr4 -Dlanguage=Python3 WhileLoop.g4
- javac -cp ".:$ANTLR_JAR" WhileLoop*.java
- echo "x = 0; while (x < 5) { x = x + 1; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig WhileLoop prog -tokens
- echo "x = 0; while (x < 5) { x = x + 1; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig WhileLoop prog -tree

Tokens:
[@0,0:0='x',<ID>,1:0]
[@1,2:2='=',<'='>,1:2]
[@2,4:4='0',<INT>,1:4]
[@3,5:5=';',<';'>,1:5]
[@4,7:11='while',<'while'>,1:7]
[@5,13:13='(',<'('>,1:13]
[@6,14:14='x',<ID>,1:14]
[@7,16:16='<',<'<'>,1:16]
[@8,18:18='5',<INT>,1:18]
[@9,19:19=')',<')'>,1:19]
[@10,21:21='{',<'{'>,1:21]
[@11,23:23='x',<ID>,1:23]
[@12,25:25='=',<'='>,1:25]
[@13,27:27='x',<ID>,1:27]
[@14,29:29='+',<'+'>,1:29]
[@15,31:31='1',<INT>,1:31]
[@16,32:32=';',<';'>,1:32]
[@17,34:34='}',<'}'>,1:34]
[@18,36:35='<EOF>',<EOF>,2:0]

Arbol sintactico generado:

echo "x = 0; while (x < 5) { x = x + 1; }" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig WhileLoop prog -tree
(prog (stat (assign x = (expr 0) ;)) (stat (whileStmt while ( (condicion (expr x) < (expr 5)) ) { (stat (assign x = (expr (expr x) + (expr 1)) ;)) })))

Preguntas del cuestionario:
1. Respuesta correcta/ A: "WHILE, (, ID, <, INT, ), {, ID, =, ID, +, INT, }"
    - Se generan estos tokens porque la gramática incluye las palabras clave como while, identifica los identificadores (ID) para las variables, los operadores aritméticos y los símbolos de puntuación
2. Respuesta correcta/ C: "while es el nodo raíz y su condición y cuerpo son nodos secundarios"
    - El nodo raíz es while, y de él cuelgan dos ramas: una para la condición (como x < 5) y otra para el cuerpo (las instrucciones dentro de las llaves)
3. Respuesta correcta/ B: "Se genera un error de sintaxis"
    -Si las llaves {} están definidas en la gramática para delimitar el cuerpo del while, omitirlas provocará un error, ya que el analizador esperará encontrarlas para reconocer correctamente el bloque de código.
    