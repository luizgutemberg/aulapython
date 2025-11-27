'''Crie uma função que receba um nome como argumento (string) e retorne uma mensagem de saudação completa'''


def saudar (nome): # Define uma função chamada 'saudar' que aceita um argumento (parâmetro) chamado 'nome'.
    return f"Olá {nome}! Seja bem vindo ao mundo Python!" # A função retorna uma string formatada (f-string) que inclui a saudação e o valor do parâmetro 'nome'.

nome_usuario = input ("Digite seu nome: ") # Pede ao usuário que digite seu nome e armazena a entrada na variável 'nome_usuario'.

mensagem = saudar (nome_usuario) # Chama a função 'saudar', passando o conteúdo de 'nome_usuario' como argumento, e armazena o valor retornado na variável 'mensagem'.
print (mensagem) # Imprime na tela o conteúdo final da variável 'mensagem'.