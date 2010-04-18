#coding:utf-8
from freshen import *
from freshen.checks import *
from nose.tools import *
from post_pylons_freshen.model import Aluno
from post_pylons_freshen.model.meta import Session
from sqlalchemy.exc import IntegrityError

@Before
def instanciar_aluno(sc):
    scc.aluno = Aluno()

@Given("que estou cadastrando um aluno")
def cadastrando_aluno():
    pass

@When("não digito o nome")
def set_none_in_nome():
    scc.aluno.nome = None

@Then("o cadastro não pode ser completado")
def falhar_cadastro():
    Session.add(scc.aluno)
    assert_raises(IntegrityError, Session.commit)
