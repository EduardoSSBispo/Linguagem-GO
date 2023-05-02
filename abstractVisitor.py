from abc import abstractmethod, ABCMeta

class AbstractVisitor(metaclass = ABCMeta):
  
  @abstractmethod
  def visitDeclarationConcreto1(self, DeclarationConcreto1):pass
    
  @abstractmethod
  def visitDeclarationConcreto2(self, DeclarationConcreto2):pass

  @abstractmethod
  def visitDeclaraVar(self, DeclaraVar):pass

  @abstractmethod
  def visitDeclaraExpBinaria(self, DeclaraExpBinaria):pass

  @abstractmethod
  def visitDeclaraIdTipo(self, DeclaraIdTipo):pass

  @abstractmethod
  def visitDeclaraIdTipoExp(self, DeclaraIdTipoExp):pass

  @abstractmethod
  def visitDeclarationFuncConcreta(self, DeclarationFunc):pass
    
  @abstractmethod
  def visitAssinaturaListParam(self, AssinaturaListParam):pass

  @abstractmethod
  def visitListaParamIdTipo(self, ListaParamIdTipo):pass

  @abstractmethod
  def visitListaParamPvId(self, ListaParamPvId):pass

  @abstractmethod
  def visitCorpoConcreto(self, CorpoConcreto):pass

  @abstractmethod
  def visitStmsConcreto(self, StmsConcreto):pass

  @abstractmethod
  def visitstmConcreto(self, stmConcreto):pass