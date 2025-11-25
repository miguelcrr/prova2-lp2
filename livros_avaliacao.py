def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if nota >= 0 and  nota <= 10:
                return nota
            else:
                print('Nota inválida!')
        except ValueError:
            print('Nota inválida!')
def validar_resposta(mensagem):
    while True:
            status = input(mensagem).upper()
            if status == 'LIDO':
                return status
            elif status =='LENDO':
                return status
            elif status =='NA FILA':
                return status
            else:
                print('Status inválido')


with open("livros.txt","r") as livros:
    linhas=livros.readlines()
    for linha in linhas:
        nome=linha.strip()
        n1=ler_nota(f"Dê nota pro filme {linha}: ")
        n2=validar_resposta(f"Qual o status de leitura do livro {linha} 'lido','lendo' ou 'na fila'?: ")
        with open("livros_avaliacao.txt","a") as livros_avaliacao:
            livros_avaliacao.write(f"{nome},{n1}, {n2}\n")
