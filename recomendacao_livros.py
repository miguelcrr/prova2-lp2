notas=[]
with open('livros_avaliacao.txt', 'r') as livros_avaliacao:
    linhas=livros_avaliacao.readlines()
    for linha in linhas:
        partes=linha.strip().split(',')
        if len(partes)==5:
            ano, nome, autor, nota, status = partes
            if status ==' LIDO':
                notas.append((nome.strip(), float(nota.strip())))
            elif status ==' LENDO':
                notas.append((nome.strip(), float(nota.strip())))


maiores_notas=sorted(notas,key=lambda x:(-x[1],x[0]))[:5]
with open("livros_recomendados.txt","w") as livros_recomendados:
    for nome, nota in maiores_notas:
        livros_recomendados.write(f"{nome},{nota}\n")

