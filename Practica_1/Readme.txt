Comandos utilizados:
- cd Practica_1/
- nano Expr.g4
- antlr4 Expr.g4
- antlr4 -Dlanguage=Python3 Expr.g4
- javac -cp ".:$ANTLR_JAR" Expr*.java
- echo "a = 10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Expr prog -tokens
- echo "a = 10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Expr prog -tree

Token Generado:
b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Expr prog -tokens
[@0,0:0='a',<ID>,1:0]
[@1,2:2='=',<'='>,1:2]
[@2,4:5='10',<INT>,1:4]
[@3,6:6=';',<';'>,1:6]
[@4,8:8='b',<ID>,1:8]
[@5,10:10='=',<'='>,1:10]
[@6,12:12='5',<INT>,1:12]
[@7,14:14='+',<'+'>,1:14]
[@8,16:16='a',<ID>,1:16]
[@9,18:18='*',<'*'>,1:18]
[@10,20:20='2',<INT>,1:20]
[@11,21:21=';',<';'>,1:21]
[@12,23:23='c',<ID>,1:23]
[@13,25:25='=',<'='>,1:25]
[@14,27:27='(',<'('>,1:27]
[@15,28:28='b',<ID>,1:28]
[@16,30:30='-',<'-'>,1:30]
[@17,32:32='3',<INT>,1:32]
[@18,33:33=')',<')'>,1:33]
[@19,35:35='/',<'/'>,1:35]
[@20,37:37='2',<INT>,1:37]
[@21,38:38=';',<';'>,1:38]
[@22,40:39='<EOF>',<EOF>,2:0]

Arbol sintactico generado:

$ echo "a = 10; b = 5 + a * 2; c = (b - 3) / 2;" | java -cp ".:$ANTLR_JAR" org.antlr.v4.gui.TestRig Expr prog -tree
(prog (stat a = (expr 10) ;) (stat b = (expr (expr 5) + (expr (expr a) * (expr 2))) ;) (stat c = (expr (expr ( (expr (expr b) - (expr 3)) )) / (expr 2)) ;))

Preguntas del cuestionario
1. Respuesta correcta/ B " Como operadores aritméticos específicos": 
    Los operadores se reconocen como tokens especificos definidos como simbolos matematicos, mientras que antlr4 no los trata como identificadores si no como operadores aritmeticos cambiandolos en el analisis lexico como <'+'> o <'*'>
2. Respuesta correcta/ D "* se evalúa antes que +, organizando el árbol en función de la precedencia. ": 
    El árbol generado por ANTLR4 sigue la jerarquía de operaciones:

    - Primero evalúa la multiplicación a * 2.
    - Luego, la suma 5 + (a * 2).
    - Finalmente, asigna el resultado a b.
3. Respuesta correcta/ D "Todas las anteriores": 
    Visualizar los tokens y el árbol de análisis ayuda a entender cómo el compilador interpreta el código, a optimizarlo y a comprobar que la gramática funciona correctamente