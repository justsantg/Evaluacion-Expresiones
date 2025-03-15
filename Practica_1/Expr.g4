grammar Expr;

// Reglas principales
// 'prog' acepta una o más sentencias (stat)
prog:   stat+ ;

// 'stat' permite dos tipos de sentencias: 
// 1. Expresión seguida de ';' (printExpr)
// 2. Asignación de un valor a una variable (assign)
stat:   expr ';'               # printExpr
    |   ID '=' expr ';'        # assign
    ;

// 'expr' define las reglas para operaciones matemáticas y valores:
// - Multiplicación y división tienen mayor prioridad (MulDiv)
// - Suma y resta (AddSub)
// - Expresiones entre paréntesis (Parens)
// - Identificadores como variables (Id)
// - Números enteros (Int)
expr:   expr op=('*'|'/') expr # MulDiv
    |   expr op=('+'|'-') expr # AddSub
    |   '(' expr ')'           # Parens
    |   ID                     # Id
    |   INT                    # Int
    ;

// Definición de tokens
ID  :   [a-zA-Z]+ ;   // Identificadores: secuencias de letras
INT :   [0-9]+ ;       // Números enteros: secuencias de dígitos
WS  :   [ \t\r\n]+ -> skip ; // Espacios en blanco: ignorados
