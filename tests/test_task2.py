import os
import sys
import unittest
import requests
from collections import defaultdict
from unittest.mock import patch


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from task2.solution import get_animal_counts


class AnimalCountsTest(unittest.TestCase):

    @patch('requests.get')
    def test_get_animal_counts_with_valid_page(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.text = """
        <div class="mw-category-group">
          <a href="#">Млекопитающие</a>  <a href="#">Птицы</a></div>
        """
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
        animal_counts = get_animal_counts(url)
        self.assertEqual(animal_counts, {'М': 1, 'П': 1})

    @patch('requests.get')
    def test_get_animal_counts_with_empty_page(self, mock_get):
        mock_response = unittest.mock.Mock()
        mock_response.text = ""
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
        animal_counts = get_animal_counts(url)
        self.assertEqual(animal_counts, defaultdict(int))

    @patch('requests.get')
    def test_get_animal_counts_with_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Error")

        url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
        with self.assertRaises(requests.exceptions.RequestException):
            get_animal_counts(url)


if __name__ == '__main__':
    unittest.main()
