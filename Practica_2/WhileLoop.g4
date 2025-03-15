grammar WhileLoop;

// Reglas
prog:   stat+ ;

stat:   assign                # asignacion
    |   whileStmt              # bucleWhile
    ;

assign: ID '=' expr ';' ;

whileStmt: 'while' '(' condicion ')' '{' stat* '}' ;

condicion: expr op=('<'|'>'|'<='|'>='|'=='|'!=') expr ;

expr:   expr op=('*'|'/') expr # MulDiv
    |   expr op=('+'|'-') expr # AddSub
    |   ID                     # Id
    |   INT                    # Int
    ;

// Tokens
ID  :   [a-zA-Z]+ ;
INT :   [0-9]+ ;
WS  :   [ \t\r\n]+ -> skip ;
