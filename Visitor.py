from abstractVisitor import AbstractVisitor
from AnaliseSintatica import *

class Visitor(AbstractVisitor):
  def visitDeclarationConcreto1(self, DeclarationConcreto1):
    DeclarationConcreto1.declarationvar.accept(self)

  def visitDeclarationConcreto2(self, DeclarationConcreto2):
    DeclarationConcreto2.declarationfunc.accept(self)

  def visitDeclaraVar(self, DeclaraVar):
    DeclaraVar.declarationvar.accept(self)

  def visitDeclaraExpBinaria(self, DeclaraExpBinaria):
    print(DeclaraExpBinaria.id, end='', sep='')
    DeclaraExpBinaria.expbinaria.accept(self)

  def visitDeclaraIdTipo(self, DeclaraIdTipo):
    DeclaraIdTipo.tipo.accept(self)

  def visitDeclaraIdTipoExp(self, DeclaraIdTipoExp):
    print(DeclaraIdTipoExp.id, end='', sep='')
    DeclaraIdTipoExp.expbinaria.accept(self)

  def visitDeclarationFuncConcreta(self, DeclarationFunc):
    print(DeclarationFunc.id, end='', sep='')
    DeclarationFunc.assinatura.accept(self)
    DeclarationFunc.corpo.accept(self)

  def visitAssinaturaListParam(self, AssinaturaListParam):
    AssinaturaListParam.listaParam.accept(self)
    AssinaturaListParam.tipo.accept(self)

  def visitListaParamIdTipo(self, ListaParamIdTipo):
    print(ListaParamIdTipo.id, end='', sep='')
    ListaParamIdTipo.tipo.accept(self)

  def visitListaParamPvId(self, ListaParamPvId):
    ListaParamPvId.listaParam.accept(self)
    print(ListaParamPvId.id, end='', sep='')
    ListaParamPvId.tipo.accept(self)    

  def visitCorpoConcreto(self, CorpoConcreto):
    CorpoConcreto.stms.accept(self)

  def visitStmsConcreto(self, StmsConcreto):
    StmsConcreto.stm.accept(self)
    StmsConcreto.stms.accept(self)

  def visitstmConcreto(self, stmConcreto):
    stmConcreto.stm.accept(self)