from unittest import TestCase
import src.calculadora_de_cambio as calc

class TestesDaCalculadoraDeCambio(TestCase):
    
    def teste_conversao_cambio_valor_0_taxa_5_03_retorna_0(self):
        # Arrange
        valor = 0
        taxa = 3.37
        resultado_esperado = 0
        
        # Act
        resultado_obtido = calc.converter(valor, taxa)

        # Assert
        self.assertEqual(resultado_obtido, resultado_esperado)