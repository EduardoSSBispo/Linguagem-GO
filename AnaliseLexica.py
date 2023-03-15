import ply.lex as lex

reservadas = {
  'float' : 'FLOAT', 
  'int' : 'INT', 
  'bool':'BOOL', 
  'string':'STRING', 
  'break':'BREAK', 
  'func':'FUNC', 
  'interface':'INTERFACE', 
  'case':'CASE', 
  'go':'GO', 
  'goto':'GOTO',
  'defer':'DEFER', 
  'map':'MAP', 
  'struct':'STRUCT', 
  'chan':'CHAN', 
  'else':'ELSE', 
  'package':'PACKAGE', 
  'switch':'SWITCH', 
  'const':'CONST', 
  'fallthrough':'FALLTHROUGH', 
  'if':'IF', 
  'range':'RANGE', 
  'type':'TYPE', 
  'continue':'CONTINUE', 
  'for':'FOR', 
  'import':'IMPORT', 
  'return':'RETURN', 
  'var':'VAR', 
  'default':'DEFAULT', 
  'nil':'NULL', 
  'true':'TRUE', 
  'false':'FALSE'
}

tokens = ['SOMA', 'SUBTRACAO', 'ASTERISCO', 'DIVISAO', 'ID', 'INTEIRO', 'FLUTUANTE', 'FLUTUANTEDOBRO', 'IGUAL', 'DIFERENTE', 'MAIORQUE', 'MENORQUE', 'MAIORIGUAL', 'MENORIGUAL', 'CONJUNCAO', 'MODULO', 'DISJUNCAO', 'ATRIBUICAO', 'ATRIBUICAOSOMA', 'ATRIBUICAOMULT', 'ATRIBUICAOSUB', 'ATRIBUICAODIV', 'ATRIBUICAOMOD', 'ATRIBUICAOPONTO', 'LPAREN', 'RPAREN', 'LCHAVE', 'RCHAVE', 'LCOLCHETE', 'RCOLCHETE', 'VIRGULA', 'PVIRGULA', 'PONTO', 'DOISPONTOS', 'PALAVRA', 'COMENTARIO', 'ENDERECO']  + list(reservadas.values())

t_SOMA = r'\+'
t_SUBTRACAO = r'-'
t_ASTERISCO = r'\*'
t_DIVISAO = r'/'
t_MODULO = r'%'
t_IGUAL = r'=='
t_DIFERENTE = r'!='
t_MAIORQUE = r'>'
t_MENORQUE = r'<'
t_MAIORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_ENDERECO = r'&'
t_CONJUNCAO = r'&&'
t_DISJUNCAO = r'\|\|'
t_ATRIBUICAO = r'='
t_ATRIBUICAOSOMA = r'\+='
t_ATRIBUICAOSUB = r'-='
t_ATRIBUICAOMULT = r'\*='
t_ATRIBUICAODIV = r'/='
t_ATRIBUICAOMOD = r'%='
t_ATRIBUICAOPONTO = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCHAVE = r'{'
t_RCHAVE = r'}'
t_LCOLCHETE = r'\['
t_RCOLCHETE = r'\]'
t_VIRGULA = r','
t_PVIRGULA = r';'
t_PONTO = r'\.'
t_DOISPONTOS = r':'
t_PALAVRA = r'"(.*?)"'

t_ignore = ' \t\n'

def t_FLUTUANTE(t):
  r'[-]?[0-9]+[.][0-9]+'
  t.value = float(t.value)
  return t

def t_INTEIRO(t):
  r'[-]?[0-9]+'
  t.value = int(t.value)
  return t

def t_ID(t):
  r'[_]{0,}[a-zA-Z][a-zA-Z0-9_]*'
  t.type = reservadas.get(t.value,'ID')
  return t

def t_COMENTARIO(t):
  r'(//.*)|(/\*(.|\n)*?\*/)'
  pass

def t_error(t):
  print('Error', t.value)
  t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()
#lexer.input('for j:= 0; j<= 2; j--{ -38.2 - 123}')
lexer.input('func main() { <- r := rect{width: 10*5, height: 5}\nrp := &&r\n fmt.Println("area: ", rp.area())\n fmt.Println("perim:", rp.perim())} ')

for tok in lexer:
  print(tok.value, tok.type)