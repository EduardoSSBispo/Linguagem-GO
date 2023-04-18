import ply.yacc as yacc
from AnaliseLexica import *
import AnaliseAbstrata as sa

precedence = (
  ('left', 'CONJUNCAO', 'DISJUNCAO', 'DIFERENTE'),
  ('nonassoc', 'MAIORQUE', 'MENORQUE', 'IGUAL', 'MAIORIGUAL', 'MENORIGUAL', 'MODULO'),
  ('left', 'ATRIBUICAO', 'ATRIBUICAOSOMA', 'ATRIBUICAOSUB', 'ATRIBUICAOMULT', 'ATRIBUICAODIV', 'ATRIBUICAOMOD', 'ATRIBUICAOPONTO'),
  ('left', 'SOMA', 'SUBTRACAO'),
  ('left', 'ASTERISCO', 'DIVISAO'),
  ('left', 'LPAREN', 'LCHAVE', 'LCOLCHETE', 'RPAREN', 'RCHAVE', 'RCOLCHETE')
)

def p_programa(p):
  '''programa : declaration 
              | programa declaration'''
  if (len(p) == 3):
    p[0] = [p[1]] + p[2]
  else:
    p[0] = [p[1]]
  
def p_declaration(p):
  '''declaration : declarationvar PVIRGULA 
                 | declarationfunc'''
  pass
  
def p_declarationvar(p):
  '''declarationvar : VAR declara 
                    | CONST declara 
                    | ID ATRIBUICAO expbinaria'''
  pass
  
def p_declara(p):
  '''declara : ID tipo 
             | ID tipo ATRIBUICAO expbinaria'''
  pass
  
def p_declarationfunc(p):
  '''declarationfunc : FUNC ID assinatura corpo'''
  pass
  
def p_assinatura(p):
  '''assinatura : LPAREN listaparam RPAREN tipo
                | LPAREN listaparam RPAREN
                | LPAREN RPAREN tipo
                | LPAREN RPAREN'''
  pass
  
def p_listaparam(p):
  '''listaparam : ID tipo 
                | listaparam VIRGULA ID tipo'''
  pass
  
def p_corpo(p):
  '''corpo : LCHAVE stms RCHAVE'''
  pass
  
def p_stms(p):
  '''stms : stm 
          | stm stms'''
  pass
  
def p_stm(p):
  '''stm : listaexp PVIRGULA  
         | declarationvar PVIRGULA
         | declarationvarshort PVIRGULA
         | ifstm 
         | forstm 
         | returnstm'''
  pass
  
def p_returnstm(p):
  '''returnstm : RETURN PVIRGULA 
               | RETURN expbinaria PVIRGULA'''
  pass
  
def p_declarationvarshort(p):
  '''declarationvarshort : ID ATRIBUICAOPONTO expbinaria'''
  pass
  
def p_ifstm(p):
  '''ifstm : IF listaexp corpo ifstm2'''
  pass

def p_ifstm2(p):
  '''ifstm2 : ELSE corpo 
            |'''
  
def p_forstm(p):
  '''forstm : FOR corpo 
            | FOR listaexp corpo 
            | FOR listaexp PVIRGULA listaexp PVIRGULA listaexp corpo'''
  pass
  
def p_tipo(p):
  '''tipo : array 
          | INT 
          | FLOAT 
          | BOOL 
          | STRING'''
  pass
  
def p_array(p):
  '''array : LCOLCHETE listaexp RCOLCHETE tipo LCHAVE params RCHAVE PVIRGULA
           | LCOLCHETE listaexp RCOLCHETE tipo PVIRGULA
           | LCOLCHETE listaexp RCOLCHETE PVIRGULA'''
  pass
  
def p_listaexp(p):
  '''listaexp : expbinaria 
              | expatribui'''
  pass

def p_expbinaria(p):
  '''expbinaria : abreexp terminal operadorbinario expbinaria fechaexp
                | terminal operadorbinario expbinaria 
                | call
                | terminal'''
  pass

def p_abreexp(p):
  '''abreexp : LCOLCHETE
              | LPAREN
              | LCHAVE'''

def p_fechaexp(p):
  '''fechaexp : RCOLCHETE
              | RPAREN
              | RCHAVE'''

  
def p_expatribui(p):
  '''expatribui :  ID operadoratribuicao expbinaria'''
  pass

def p_operadoratribuicao(p):
  '''operadoratribuicao : ATRIBUICAO 
                        | ATRIBUICAOSOMA 
                        | ATRIBUICAOSUB 
                        | ATRIBUICAOMULT 
                        | ATRIBUICAODIV 
                        | ATRIBUICAOMOD 
                        | ATRIBUICAOPONTO'''
  pass

def p_operadorbinario(p): #P[0] = P[1]
  '''operadorbinario : SOMA
                     | ASTERISCO 
                     | MODULO 
                     | DIVISAO 
                     | SUBTRACAO 
                     | MAIORQUE 
                     | MENORQUE 
                     | MAIORIGUAL 
                     | MENORIGUAL 
                     | IGUAL 
                     | DIFERENTE 
                     | CONJUNCAO 
                     | DISJUNCAO'''
  pass

def p_terminal(p):
  '''terminal : INTEIRO 
              | FLUTUANTE 
              | ID 
              | PALAVRA 
              | TRUE 
              | FALSE'''
  pass

def p_call(p):
  '''call : ID LPAREN params RPAREN 
          | ID LPAREN RPAREN'''
  pass

def p_params(p):
  '''params : listaexp VIRGULA params 
            | listaexp''' 
  pass

def p_error(p):
    print("Syntax error in input!", p.value)