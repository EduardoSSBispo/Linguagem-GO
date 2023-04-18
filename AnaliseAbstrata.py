from abc import abstractmethod
from abc import ABCMeta

#class Programa(metaclass = ABCMeta):
#  @abstractmethod
#  def accept(self, visitor):
#    pass

#class programaConcreto(Programa):
#  def __init__(self, ):
#    pass
    
#  def accept(self):
#    pass

class Declaration(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclarationConcreto1(Declaration):
  def __init__(self, declarationvar):
    self.declarationvar = declarationvar

  def accept(self, visitor):
    pass

class DeclarationConcreto2(Declaration):
  def __init__(self, declarationfunc):
    self.declarationfunc = declarationfunc

  def accept(self, visitor):
    pass

class DelarationVar(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclaraVar(Declaration):
  def __init__(self, declara):
    self.declarationvar = declara

  def accept(self, visitor):
    pass

class DeclaraExpBinaria(Declaration):
  def __init__(self, id, expbinaria):
    self.id = id
    self.expbinaria = expbinaria
    
  def accept(self, visitor):
    pass

class Declara(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclaraIdTipo(Declara):
  def __init__(self, tipo):
    self.tipo = tipo
    
  def accept(self, visitor):
    pass

class DeclaraIdTipoExpBinaria(Declara):
  def __init__(self, tipo, expbinaria):
    self.id = id
    self.expbinaria = expbinaria
    
  def accept(self, visitor):
    pass

class DeclarationFunc(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class DeclarationFuncConcreta(DeclarationFunc):
  def __init__(self, assinatura, corpo):
    self.assinatura = assinatura
    self.corpo = corpo
    
  def accept(self, visitor):
    pass

class Assinatura(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class AssinaturaListparam(Assinatura):
  def __init__(self, listaParam, tipo):
    self.listaParam = listaParam
    self.tipo = tipo
    
  def accept(self, visitor):
    pass

class ListaParam(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class ListaParamIdTipo(ListaParam):
  def __init__(self, id, tipo):
    self.id = id
    self.tipo = tipo
    
  def accept(self, visitor):
    pass

class ListaParamPvId(ListaParam):
  def __init__(self, listaParam, id, tipo):
    self.listaParam = listaParam
    self.id = id
    self.tipo = tipo
    
  def accept(self, visitor):
    pass

class Corpo(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class CorpoConcreto(Corpo):
  def __init__(self, stms):
    self.stms = stms
    
  def accept(self, visitor):
    pass

class Stms(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StmsConcreto(Stms):
  def __init__(self, stm, stms):
    self.stm = stm
    self.stms = stms
    
  def accept(self, visitor):
    pass

class Stm(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

class StmsListaExp(Stm):
  def __init__(self, listaExp):
    self.listaExp = listaExp
    
  def accept(self, visitor):
    pass

class StmsDeclarationVar(Stm):
  def __init__(self, declarationVar):
    self.declarationVar = declarationVar
    
  def accept(self, visitor):
    pass


class StmsDeclarationShort(Stm):
  def __init__(self, declarationVarShort):
    self.declarationVarShort = declarationVarShort
    
  def accept(self, visitor):
    pass

class StmsIfstm(Stm):
  def __init__(self, ifStm):
    self.ifStm = ifStm
    
  def accept(self, visitor):
    pass

class StmsForstm(Stm):
  def __init__(self, forStm):
    self.forStm = forStm
    
  def accept(self, visitor):
    pass

class StmsReturnstm(Stm):
  def __init__(self, returnStm):
    self.returnStm = returnStm
    
  def accept(self, visitor):
    pass

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

class AbreExpBinaria(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

#Coloca uma classe pra cada?

class FechaExpBinaria(metaclass = ABCMeta):
  @abstractmethod
  def accept(self, visitor):
    pass

#Coloca uma classe pra cada?

class ExpBinariaCall(ExpBinaria):
  def __init__(self, call):
    self.call = call
    
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