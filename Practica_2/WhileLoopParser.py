# Generated from WhileLoop.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write(">\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\6\2\20\n\2\r\2\16\2\21\3\3\3\3\5\3\26\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5#\n\5\f\5\16\5&\13")
        buf.write("\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\5\7\61\n\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\7\7\79\n\7\f\7\16\7<\13\7\3\7\2\3\f")
        buf.write("\b\2\4\6\b\n\f\2\5\3\2\n\17\3\2\20\21\3\2\22\23\2=\2\17")
        buf.write("\3\2\2\2\4\25\3\2\2\2\6\27\3\2\2\2\b\34\3\2\2\2\n)\3\2")
        buf.write("\2\2\f\60\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3")
        buf.write("\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\3\3\2\2\2\23\26")
        buf.write("\5\6\4\2\24\26\5\b\5\2\25\23\3\2\2\2\25\24\3\2\2\2\26")
        buf.write("\5\3\2\2\2\27\30\7\24\2\2\30\31\7\3\2\2\31\32\5\f\7\2")
        buf.write("\32\33\7\4\2\2\33\7\3\2\2\2\34\35\7\5\2\2\35\36\7\6\2")
        buf.write("\2\36\37\5\n\6\2\37 \7\7\2\2 $\7\b\2\2!#\5\4\3\2\"!\3")
        buf.write("\2\2\2#&\3\2\2\2$\"\3\2\2\2$%\3\2\2\2%\'\3\2\2\2&$\3\2")
        buf.write("\2\2\'(\7\t\2\2(\t\3\2\2\2)*\5\f\7\2*+\t\2\2\2+,\5\f\7")
        buf.write("\2,\13\3\2\2\2-.\b\7\1\2.\61\7\24\2\2/\61\7\25\2\2\60")
        buf.write("-\3\2\2\2\60/\3\2\2\2\61:\3\2\2\2\62\63\f\6\2\2\63\64")
        buf.write("\t\3\2\2\649\5\f\7\7\65\66\f\5\2\2\66\67\t\4\2\2\679\5")
        buf.write("\f\7\68\62\3\2\2\28\65\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3")
        buf.write("\2\2\2;\r\3\2\2\2<:\3\2\2\2\b\21\25$\608:")
        return buf.getvalue()


class WhileLoopParser ( Parser ):

    grammarFileName = "WhileLoop.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'while'", "'('", "')'", 
                     "'{'", "'}'", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'!='", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "INT", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_assign = 2
    RULE_whileStmt = 3
    RULE_condicion = 4
    RULE_expr = 5

    ruleNames =  [ "prog", "stat", "assign", "whileStmt", "condicion", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    ID=18
    INT=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.StatContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.StatContext,i)


        def getRuleIndex(self):
            return WhileLoopParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = WhileLoopParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.stat()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==WhileLoopParser.T__2 or _la==WhileLoopParser.ID):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLoopParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AsignacionContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLoopParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assign(self):
            return self.getTypedRuleContext(WhileLoopParser.AssignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)


    class BucleWhileContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLoopParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def whileStmt(self):
            return self.getTypedRuleContext(WhileLoopParser.WhileStmtContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBucleWhile" ):
                listener.enterBucleWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBucleWhile" ):
                listener.exitBucleWhile(self)



    def stat(self):

        localctx = WhileLoopParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 19
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileLoopParser.ID]:
                localctx = WhileLoopParser.AsignacionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 17
                self.assign()
                pass
            elif token in [WhileLoopParser.T__2]:
                localctx = WhileLoopParser.BucleWhileContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.whileStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(WhileLoopParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(WhileLoopParser.ExprContext,0)


        def getRuleIndex(self):
            return WhileLoopParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = WhileLoopParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(WhileLoopParser.ID)
            self.state = 22
            self.match(WhileLoopParser.T__0)
            self.state = 23
            self.expr(0)
            self.state = 24
            self.match(WhileLoopParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condicion(self):
            return self.getTypedRuleContext(WhileLoopParser.CondicionContext,0)


        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.StatContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.StatContext,i)


        def getRuleIndex(self):
            return WhileLoopParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)




    def whileStmt(self):

        localctx = WhileLoopParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_whileStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(WhileLoopParser.T__2)
            self.state = 27
            self.match(WhileLoopParser.T__3)
            self.state = 28
            self.condicion()
            self.state = 29
            self.match(WhileLoopParser.T__4)
            self.state = 30
            self.match(WhileLoopParser.T__5)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==WhileLoopParser.T__2 or _la==WhileLoopParser.ID:
                self.state = 31
                self.stat()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 37
            self.match(WhileLoopParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.op = None # Token

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.ExprContext,i)


        def getRuleIndex(self):
            return WhileLoopParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)




    def condicion(self):

        localctx = WhileLoopParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.expr(0)
            self.state = 40
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << WhileLoopParser.T__7) | (1 << WhileLoopParser.T__8) | (1 << WhileLoopParser.T__9) | (1 << WhileLoopParser.T__10) | (1 << WhileLoopParser.T__11) | (1 << WhileLoopParser.T__12))) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 41
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return WhileLoopParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLoopParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLoopParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(WhileLoopParser.ExprContext)
            else:
                return self.getTypedRuleContext(WhileLoopParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLoopParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(WhileLoopParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a WhileLoopParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(WhileLoopParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = WhileLoopParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [WhileLoopParser.ID]:
                localctx = WhileLoopParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 44
                self.match(WhileLoopParser.ID)
                pass
            elif token in [WhileLoopParser.INT]:
                localctx = WhileLoopParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(WhileLoopParser.INT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 56
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 54
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = WhileLoopParser.MulDivContext(self, WhileLoopParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 48
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 49
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileLoopParser.T__13 or _la==WhileLoopParser.T__14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 50
                        self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = WhileLoopParser.AddSubContext(self, WhileLoopParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 51
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==WhileLoopParser.T__15 or _la==WhileLoopParser.T__16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        self.expr(4)
                        pass

             
                self.state = 58
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




