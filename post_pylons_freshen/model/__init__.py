"""The application's model objects"""
from post_pylons_freshen.model.meta import Session, metadata
from sqlalchemy import *
from sqlalchemy import orm

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

tabela_alunos = Table('alunos', metadata,
                    Column('id', Integer, primary_key = True),
                    Column('nome', String, nullable = False),
                    Column('data_nascimento', Date)
    )

class Aluno(object):
    def __init__(self, id = None, nome = None, data_nascimento = None):
        super(Aluno, self).__init__()
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento

orm.mapper(Aluno, tabela_alunos)
