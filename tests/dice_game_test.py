import unittest
from unittest.mock import patch
from io import StringIO
import importlib
import sys

class TestSuite(unittest.TestCase):

    @patch("builtins.input", side_effect=[
        # usuario juega 2 veces, ve resultados y sale
        "1", "1", "2", "3"
    ])
    @patch("random.randint", side_effect=[
        # primera partida datos usuario vs computadora
        2, 4, 3, 2,

        # segunda partida datos usuario vs computadora
        3, 3, 6, 1,
    ])
    def test_dice_game(self, mock_input, mock_random):
        with patch("sys.stdout", new_callable = StringIO) as fake_out:
            
            import src.dice_game
            output = fake_out.getvalue() 

            assert "Cantidad de partidas jugadas: 2\n" in output
            assert "Puntaje total usuario: 12\n" in output
            assert "Puntaje total computadora: 12\n" in output
