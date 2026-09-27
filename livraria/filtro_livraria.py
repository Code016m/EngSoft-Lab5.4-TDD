def filtrar_livros(livros, criterios):
    resultado = []

    for livro in livros:
        if livro["titulo"] == criterios["titulo"]:
            resultado.append(livro)

    return resultado