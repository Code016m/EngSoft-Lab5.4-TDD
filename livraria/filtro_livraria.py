def filtrar_livros(livros, criterios):

    resultado = []

    for livro in livros:

        atendendo_criterios = True

        for chave, valor in criterios.items():
            if livro.get(chave) != valor:
                atendendo_criterios = False
                break

        if atendendo_criterios:
            resultado.append(livro)

    return resultado