'''1)Crie um programa que peça ao usuário para digitar números repetidamente. O programa deve parar de pedir números quando o usuário digitar 0. 
A cada número digitado, use um if para verificar se ele é positivo. O programa deve somar apenas os números positivos e, no final, exibir o resultado da soma.'''

soma_positivos = 0          # Inicializa a variável 'soma_positivos' com zero, onde o resultado da soma será armazenado.
numero = -1                 # Inicializa a variável 'numero' com um valor diferente de 0, garantindo que o loop 'while' seja executado pelo menos uma vez.

print("Olá! Vamos somar apenas os números positivos que você digitar.") # Imprime uma mensagem inicial para o usuário.

while numero != 0:          # Inicia um loop que continuará executando enquanto o valor de 'numero' não for igual a 0.
    # Pede o número e converte para inteiro
    entrada = input("Digite um número (0 para parar): ") # Solicita ao usuário que digite um número e armazena a entrada como string na variável 'entrada'.
    try:                    # Inicia um bloco 'try' para tentar executar o código e prever possíveis erros.
        numero = int(entrada) # Tenta converter a string 'entrada' para um número inteiro e armazena o resultado em 'numero'.
    except ValueError:      # Se a conversão para inteiro falhar (o usuário digitou texto, por exemplo), este bloco 'except' é executado.
        print("Entrada inválida. Digite um número inteiro.") # Informa ao usuário que a entrada não é válida.
        continue            # Pula o restante do código dentro do loop e volta para o início do 'while' para solicitar uma nova entrada.
        
    # Usa o if para verificar se o número é positivo antes de somar
    if numero > 0:          # Verifica se o número digitado e convertido é estritamente maior que zero (ou seja, positivo).
        soma_positivos = soma_positivos + numero # Se for positivo, adiciona o valor de 'numero' à variável 'soma_positivos'.

print(f"A soma dos números positivos digitados é: {soma_positivos}") # Após o loop terminar (quando o usuário digitar 0), imprime o resultado final da soma.