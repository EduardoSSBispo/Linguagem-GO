from abc import abstractmethod
from abc import ABCMeta

class Declaration(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclarationConcreto1(Declaration):
  def __init__(self, declarationvar):
    self.declarationvar = declarationvar

  def accept(self, visitor):
    return visitor.visitDeclarationConcreto1(self)

class DeclarationConcreto2(Declaration):
  def __init__(self, declarationfunc):
    self.declarationfunc = declarationfunc

  def accept(self, visitor):
    return visitor.visitDeclarationConcreto2(self)

class DelarationVar(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclaraVar(Declaration):
  def __init__(self, declara):
    self.declarationvar = declara

  def accept(self, visitor):
    return visitor.visitDeclaraVar(self)

class DeclaraExpBinaria(Declaration):
  def __init__(self, id, expbinaria):
    self.id = id
    self.expbinaria = expbinaria
    
  def accept(self, visitor):
    return visitor.visitDeclaraExpBinaria(self)

class Declara(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclaraIdTipo(Declara):
  def __init__(self, tipo):
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitDeclaraIdTipo(self)

class DeclaraIdTipoExpBinaria(Declara):
  def __init__(self, tipo, expbinaria):
    self.id = id
    self.expbinaria = expbinaria
    
  def accept(self, visitor):
    return visitor.visitDeclaraIdTipoExp(self)

class DeclarationFunc(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclarationFuncConcreta(DeclarationFunc):
  def __init__(self, id, assinatura, corpo):
    self.id = id
    self.assinatura = assinatura
    self.corpo = corpo
    
  def accept(self, visitor):
    return visitor.visitDeclarationFuncConcreta(self)

class Assinatura(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class AssinaturaListparam(Assinatura):
  def __init__(self, listaParam, tipo):
    self.listaParam = listaParam
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitAssinaturaListParam(self)

class ListaParam(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ListaParamIdTipo(ListaParam):
  def __init__(self, id, tipo):
    self.id = id
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitListaParamIdTipo(self)

class ListaParamPvId(ListaParam):
  def __init__(self, listaParam, id, tipo):
    self.listaParam = listaParam
    self.id = id
    self.tipo = tipo
    
  def accept(self, visitor):
    return visitor.visitListaParamPvId(self)

class Corpo(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CorpoConcreto(Corpo):
  def __init__(self, stms):
    self.stms = stms
    
  def accept(self, visitor):
    return visitor.visitCorpoConcreto(self)

class Stms(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StmsConcreto(Stms):
  def __init__(self, stm, stms):
    self.stm = stm
    self.stms = stms
    
  def accept(self, visitor):
    return visitor.visitStmsConcreto(self)

class Stm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class stmConcreto(Stm):
  def __init__(self, stm):
    self.stm = stm
  def accept(self, visitor):
    return visitor.visitstmConcreto(self)
    #Até aquiiiiii
    
# class StmListaExp(Stm):
#   def __init__(self, listaExp):
#     self.listaExp = listaExp
    
#   def accept(self, visitor):
#     pass

# class StmDeclarationVar(Stm):
#   def __init__(self, declarationVar):
#     self.declarationVar = declarationVar
    
#   def accept(self, visitor):
#     pass


# class StmDeclarationShort(Stm):
#   def __init__(self, declarationVarShort):
#     self.declarationVarShort = declarationVarShort
    
#   def accept(self, visitor):
#     pass

# class StmIfstm(Stm):
#   def __init__(self, ifStm):
#     self.ifStm = ifStm
    
#   def accept(self, visitor):
#     pass

# class StmForstm(Stm):
#   def __init__(self, forStm):
#     self.forStm = forStm
    
#   def accept(self, visitor):
#     pass

# class StmReturnstm(Stm):
#   def __init__(self, returnStm):
#     self.returnStm = returnStm
    
#   def accept(self, visitor):
#     pass

class ReturnStm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class Return(ReturnStm):
  def __init__(self, expBinaria):
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    pass

class DeclarationVarShort(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclaraShort(DeclarationVarShort):
  def __init__(self, id, expBinaria):
    self.id = id
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    pass

class IfStm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class IfListaExp(IfStm):
  def __init__(self, listaExp, corpo, ifStm2):
    self.listaExp = listaExp
    self.corpo = corpo
    self.ifStm2 = ifStm2
    
  def accept(self, visitor):
    pass

class IfStm2(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class IfListaExp2(IfStm2):
  def __init__(self, corpo):
    self.corpo = corpo
    
  def accept(self, visitor):
    pass

class ForStm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ForCorpo(ForStm):
  def __init__(self, listaExp, corpo):
    self.listaExp = listaExp
    self.corpo = corpo
    
  def accept(self, visitor):
    pass

class ForListaExp(ForStm):
  def __init__(self, listaExp1, listaExp2, listaExp3, corpo):
    self.listaExp1 = listaExp1
    self.listaExp2 = listaExp2
    self.listaExp3 = listaExp3
    self.corpo = corpo
    
  def accept(self, visitor):
    pass

class tipo(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class tipoArray(tipo):
  def __init__(self, array):
    self.array = array

  def accept(self, visitor):
    pass

class tipoInt(tipo):
  def __init__(self, intValue):
    self.intValue = intValue

  def accept(self, visitor):
    pass

class tipoFloat(tipo):
  def __init__(self, floatValue):
    self.floatValue = floatValue

  def accept(self, visitor):
    pass

class tipoBool(tipo):
  def __init__(self, boolValue):
    self.boolValue = boolValue

  def accept(self, visitor):
    pass

class tipoString(tipo):
  def __init__(self, stringValue):
    self.stringValue = stringValue

  def accept(self, visitor):
    pass
#tipo, operatribuicao, operadorbinario, terminal, será colocado igual o exemplo de "program" em SUE?

class Array(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ArraySimples(Array):
  def __init__(self, listaExp, tipo):
    self.listaExp = listaExp
    self.tipo = tipo
    
  def accept(self, visitor):
    pass

class ArrayComposto(Array):
  def __init__(self, listaExp, tipo, params):
    self.listaExp = listaExp
    self.tipo = tipo
    self.params = params 
    
  def accept(self, visitor):
    pass

class ListaExp(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ListaExpBinaria(ListaExp):
  def __init__(self, expBinaria):
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    pass

class ListaExpAtribui(ListaExp):
  def __init__(self, expAtribui):
    self.expAtribui = expAtribui
    
  def accept(self, visitor):
    pass

class ExpBinaria(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class AbreExpBinariaTerminalFecha(ExpBinaria):
  def __init__(self, abre, terminal, operadorBinario, expBinaria, fecha):
    self.abre = abre
    self.terminal = terminal
    self.operadorBinario = operadorBinario
    self.expBinaria = expBinaria
    self.fecha = fecha
    
  def accept(self, visitor):
    pass

class ExpBinariaTerminal(ExpBinaria):
  def __init__(self, terminal, operadorBinario, expBinaria):
    self.terminal = terminal
    self.operadorBinario = operadorBinario
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    pass

class ExpBinariaApenasTerminal(ExpBinaria):
  def __init__(self, terminal):
    self.terminal = terminal
    
  def accept(self, visitor):
    pass

class ExpBinariaCall(ExpBinaria):
  def __init__(self, call):
    self.call = call
    
  def accept(self, visitor):
    pass

class AbreExpBinaria(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class abreParen(AbreExpBinaria):
  def __init__(self, lParen):
    self.lParen = lParen
  def accept(self, visitor):
    pass

class abreChave(AbreExpBinaria):
  def __init__(self, lChave):
    self.lChave = lChave
  def accept(self, visitor):
    pass

class abreColch(AbreExpBinaria):
  def __init__(self, lColch):
    self.lColch = lColch
  def accept(self, visitor):
    pass

class FechaExpBinaria(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class fechaParen(FechaExpBinaria):
  def __init__(self, rParen):
    self.rParen = rParen
  def accept(self, visitor):
    pass

class fechaChave(FechaExpBinaria):
  def __init__(self, rChave):
    self.rChave = rChave
  def accept(self, visitor):
    pass

class fechaColch(FechaExpBinaria):
  def __init__(self, rColch):
    self.rColch = rColch
  def accept(self, visitor):
    pass

class ExpAtribui(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ExpAtribuiConcreta(ExpAtribui):
  def __init__(self, id, operadorAtribui, expBinaria):
    self.id = id
    self.operadorAtribui = operadorAtribui
    self.expBinaria = expBinaria
    
  def accept(self, visitor):
    pass

class operadorAtribuicao(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class atribuicao(operadorAtribuicao):
  def __init__(self, atribuicao):
    self.atribuicao = atribuicao

  def accept(self, visitor):
    pass

class atribuicaoSoma(operadorAtribuicao):
  def __init__(self, atribuicaoSoma):
    self.atribuicaoSoma = atribuicaoSoma

  def accept(self, visitor):
    pass

class atribuicaoSub(operadorAtribuicao):
  def __init__(self, atribuicaoSub):
    self.atribuicaoSub = atribuicaoSub

  def accept(self, visitor):
    pass

class atribuicaoMul(operadorAtribuicao):
  def __init__(self, atribuicaoMul):
    self.atribuicaoMul = atribuicaoMul

  def accept(self, visitor):
    pass
    
class atribuicaoDiv(operadorAtribuicao):
  def __init__(self, atribuicaoDiv):
    self.atribuicaoDiv = atribuicaoDiv

  def accept(self, visitor):
    pass

class atribuicaoMod(operadorAtribuicao):
  def __init__(self, atribuicaoMod):
    self.atribuicaoMod = atribuicaoMod

  def accept(self, visitor):
    pass

class atribuicaoPonto(operadorAtribuicao):
  def __init__(self, atribuicaoPonto):
    self.atribuicaoPonto = atribuicaoPonto

  def accept(self, visitor):
    pass

class operadorBinario(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class operadorSoma(operadorBinario):
  def __init__(self, soma):
    self.soma = soma

  def accept(self, visitor):
    pass

class operadorAsterisco(operadorBinario):
  def __init__(self, asterisco):
    self.asterisco = asterisco

  def accept(self, visitor):
    pass

class operadorModulo(operadorBinario):
  def __init__(self, mod):
    self.mod = mod

  def accept(self, visitor):
    pass

class operadorDivisao(operadorBinario):
  def __init__(self, div):
    self.div = div

  def accept(self, visitor):
    pass

class operadorSubtracao(operadorBinario):
  def __init__(self, sub):
    self.sub = sub

  def accept(self, visitor):
    pass

class operadorMaiorQue(operadorBinario):
  def __init__(self, maior):
    self.maior = maior

  def accept(self, visitor):
    pass

class operadorMenorQue(operadorBinario):
  def __init__(self, menor):
    self.menor = menor

  def accept(self, visitor):
    pass

class operadorMaiorIgual(operadorBinario):
  def __init__(self, maiorigual):
    self.maiorigual = maiorigual

  def accept(self, visitor):
    pass

class operadorMenorIgual(operadorBinario):
  def __init__(self, menorigual):
    self.menorigual = menorigual

  def accept(self, visitor):
    pass

class operadorIgual(operadorBinario):
  def __init__(self, igual):
    self.igual = igual

  def accept(self, visitor):
    pass

class operadorDiferente(operadorBinario):
  def __init__(self, dif):
    self.dif = dif

  def accept(self, visitor):
    pass

class operadorConjuncao(operadorBinario):
  def __init__(self, conj):
    self.conj = conj

  def accept(self, visitor):
    pass

class operadorDisjuncao(operadorBinario):
  def __init__(self, dis):
    self.dis = dis

  def accept(self, visitor):
    pass

class terminal(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class terminalInt(terminal):
  def __init__(self, intValue):
    self.intValue = intValue
  def accept(self, visitor):
    pass

class terminalFloat(terminal):
  def __init__(self, floatValue):
    self.floatValue = floatValue
  def accept(self, visitor):
    pass

class terminalID(terminal):
  def __init__(self, id):
    self.id = id
  def accept(self, visitor):
    pass

class terminalString(terminal):
  def __init__(self, stringValue):
    self.stringValues = stringValue
  def accept(self, visitor):
    pass

class terminalBool(terminal):
  def __init__(self, boolValue):
    self.boolValue = boolValue
  def accept(self, visitor):
    pass

class Call(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CallId(Call):
  def __init__(self, id, params):
    self.id = id
    self.params = params
    
  def accept(self, visitor):
    pass

class Params(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ParamsLista(Params):
  def __init__(self, listaexp):
    self.listaexp = listaexp
    
  def accept(self, visitor):
    pass

class ParamsListaParams(Params):
  def __init__(self, listaexp, params):
    self.listaexp = listaexp
    self.params = params
    
  def accept(self, visitor):
    pass