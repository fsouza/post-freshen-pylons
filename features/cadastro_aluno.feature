Funcionalidade: Cadastro de Aluno
    Como um secretário
    Eu quero cadastrar um aluno informando nome e data de nascimento
    Para que ele possa ser matriculado em disciplinas

    Cenário: Cadastro de aluno sem nome
        Dado que estou cadastrando um aluno
        Quando não digito o nome
        Então o cadastro não pode ser completado
