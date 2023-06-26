import unittest
import pandas as pd
from unittest.mock import patch

from ctd.utils import get_disease_hierarchy

class TestUtils(unittest.TestCase):
    @patch('ctd.utils.get_data')
    def test_get_disease_hierarchy(self, mock_get_data):
        mock_data = pd.read_csv('tests/test_data/disease_sample.csv')
        mock_get_data.return_value = mock_data

        parent_disease = 'MESH:D010300' # Parkinsons
        expected_hierarchy = ['MESH:D010300', 'OMIM:105500', 'MESH:C562469', 'MESH:C564653', 'MESH:C564345', 'MESH:C564486', 'MESH:C565204', 'OMIM:612953', 'MESH:C567726', 'OMIM:614203', 'OMIM:614251', 'OMIM:615528', 'OMIM:168601', 'OMIM:615530', 'OMIM:616361', 'OMIM:616710', 'OMIM:616840', 'MESH:C537176', 'MESH:C566552', 'MESH:C565324', 'OMIM:613643', 'MESH:C565276', 'MESH:C565238', 'OMIM:607060', 'MESH:C566823', 'OMIM:168600', 'MESH:C564015', 'MESH:C567730', 'MESH:C537179', 'MESH:C537240']

        result = get_disease_hierarchy(parent_disease)

        self.assertEqual(result, expected_hierarchy)
        mock_get_data.assert_called_once_with('Diseases')

if __name__ == '__main__':
    unittest.main()
