import unittest
from filtro_livraria import filtrar_livros
from livraria import lista_livros

class TestFiltrarLivros(unittest.TestCase):

    def test_filtrar_por_titulo(self):
        livros = lista_livros()
        resultado = filtrar_livros(
            livros,
            {"titulo": "Dom Casmurro"}
        )
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "Dom Casmurro")

    def test_filtrar_por_autor(self):
        livros = lista_livros()
        resultado = filtrar_livros(
            livros,
            {"autor": "Machado de Assis"}
        )
        self.assertEqual(len(resultado), 2)
        self.assertEqual(resultado[0]["autor"], "Machado de Assis")
        self.assertEqual(resultado[1]["autor"], "Machado de Assis")

    def test_filtrar_por_preco(self):
        livros = lista_livros()
        resultado = filtrar_livros(
            livros,
            {"preco": 25.0}
        )
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["preco"], 25.0)

if __name__ == "__main__":
    unittest.main()