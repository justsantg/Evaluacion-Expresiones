// Generated from WhileLoop.g4 by ANTLR 4.9.3
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link WhileLoopParser}.
 */
public interface WhileLoopListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link WhileLoopParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(WhileLoopParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link WhileLoopParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(WhileLoopParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by the {@code asignacion}
	 * labeled alternative in {@link WhileLoopParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterAsignacion(WhileLoopParser.AsignacionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code asignacion}
	 * labeled alternative in {@link WhileLoopParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitAsignacion(WhileLoopParser.AsignacionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code bucleWhile}
	 * labeled alternative in {@link WhileLoopParser#stat}.
	 * @param ctx the parse tree
	 */
	void enterBucleWhile(WhileLoopParser.BucleWhileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code bucleWhile}
	 * labeled alternative in {@link WhileLoopParser#stat}.
	 * @param ctx the parse tree
	 */
	void exitBucleWhile(WhileLoopParser.BucleWhileContext ctx);
	/**
	 * Enter a parse tree produced by {@link WhileLoopParser#assign}.
	 * @param ctx the parse tree
	 */
	void enterAssign(WhileLoopParser.AssignContext ctx);
	/**
	 * Exit a parse tree produced by {@link WhileLoopParser#assign}.
	 * @param ctx the parse tree
	 */
	void exitAssign(WhileLoopParser.AssignContext ctx);
	/**
	 * Enter a parse tree produced by {@link WhileLoopParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void enterWhileStmt(WhileLoopParser.WhileStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link WhileLoopParser#whileStmt}.
	 * @param ctx the parse tree
	 */
	void exitWhileStmt(WhileLoopParser.WhileStmtContext ctx);
	/**
	 * Enter a parse tree produced by {@link WhileLoopParser#condicion}.
	 * @param ctx the parse tree
	 */
	void enterCondicion(WhileLoopParser.CondicionContext ctx);
	/**
	 * Exit a parse tree produced by {@link WhileLoopParser#condicion}.
	 * @param ctx the parse tree
	 */
	void exitCondicion(WhileLoopParser.CondicionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link WhileLoopParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMulDiv(WhileLoopParser.MulDivContext ctx);
	/**
	 * Exit a parse tree produced by the {@code MulDiv}
	 * labeled alternative in {@link WhileLoopParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMulDiv(WhileLoopParser.MulDivContext ctx);
	/**
	 * Enter a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link WhileLoopParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAddSub(WhileLoopParser.AddSubContext ctx);
	/**
	 * Exit a parse tree produced by the {@code AddSub}
	 * labeled alternative in {@link WhileLoopParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAddSub(WhileLoopParser.AddSubContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Id}
	 * labeled alternative in {@link WhileLoopParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterId(WhileLoopParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Id}
	 * labeled alternative in {@link WhileLoopParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitId(WhileLoopParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code Int}
	 * labeled alternative in {@link WhileLoopParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterInt(WhileLoopParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code Int}
	 * labeled alternative in {@link WhileLoopParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitInt(WhileLoopParser.IntContext ctx);
}