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

if __name__ == "__main__":
    unittest.main()