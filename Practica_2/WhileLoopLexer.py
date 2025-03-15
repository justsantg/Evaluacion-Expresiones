# Generated from WhileLoop.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\26")
        buf.write("f\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\23\6\23W\n")
        buf.write("\23\r\23\16\23X\3\24\6\24\\\n\24\r\24\16\24]\3\25\6\25")
        buf.write("a\n\25\r\25\16\25b\3\25\3\25\2\2\26\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37")
        buf.write("\21!\22#\23%\24\'\25)\26\3\2\5\4\2C\\c|\3\2\62;\5\2\13")
        buf.write("\f\17\17\"\"\2h\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\3+\3\2")
        buf.write("\2\2\5-\3\2\2\2\7/\3\2\2\2\t\65\3\2\2\2\13\67\3\2\2\2")
        buf.write("\r9\3\2\2\2\17;\3\2\2\2\21=\3\2\2\2\23?\3\2\2\2\25A\3")
        buf.write("\2\2\2\27D\3\2\2\2\31G\3\2\2\2\33J\3\2\2\2\35M\3\2\2\2")
        buf.write("\37O\3\2\2\2!Q\3\2\2\2#S\3\2\2\2%V\3\2\2\2\'[\3\2\2\2")
        buf.write(")`\3\2\2\2+,\7?\2\2,\4\3\2\2\2-.\7=\2\2.\6\3\2\2\2/\60")
        buf.write("\7y\2\2\60\61\7j\2\2\61\62\7k\2\2\62\63\7n\2\2\63\64\7")
        buf.write("g\2\2\64\b\3\2\2\2\65\66\7*\2\2\66\n\3\2\2\2\678\7+\2")
        buf.write("\28\f\3\2\2\29:\7}\2\2:\16\3\2\2\2;<\7\177\2\2<\20\3\2")
        buf.write("\2\2=>\7>\2\2>\22\3\2\2\2?@\7@\2\2@\24\3\2\2\2AB\7>\2")
        buf.write("\2BC\7?\2\2C\26\3\2\2\2DE\7@\2\2EF\7?\2\2F\30\3\2\2\2")
        buf.write("GH\7?\2\2HI\7?\2\2I\32\3\2\2\2JK\7#\2\2KL\7?\2\2L\34\3")
        buf.write("\2\2\2MN\7,\2\2N\36\3\2\2\2OP\7\61\2\2P \3\2\2\2QR\7-")
        buf.write("\2\2R\"\3\2\2\2ST\7/\2\2T$\3\2\2\2UW\t\2\2\2VU\3\2\2\2")
        buf.write("WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2Y&\3\2\2\2Z\\\t\3\2\2[Z")
        buf.write("\3\2\2\2\\]\3\2\2\2][\3\2\2\2]^\3\2\2\2^(\3\2\2\2_a\t")
        buf.write("\4\2\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2cd\3\2\2")
        buf.write("\2de\b\25\2\2e*\3\2\2\2\6\2X]b\3\b\2\2")
        return buf.getvalue()


class WhileLoopLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    ID = 18
    INT = 19
    WS = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "';'", "'while'", "'('", "')'", "'{'", "'}'", "'<'", 
            "'>'", "'<='", "'>='", "'=='", "'!='", "'*'", "'/'", "'+'", 
            "'-'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "ID", "INT", "WS" ]

    grammarFileName = "WhileLoop.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


