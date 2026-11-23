"""核对交换资料的字段和数值关系。"""
import json
from pathlib import Path
import unittest

import numpy as np


class ExchangeTests(unittest.TestCase):
    def setUp(self):
        source = Path(__file__).resolve().parents[1] / "data" / "exchange.json"
        self.data = json.loads(source.read_text(encoding="utf-8"))

    def test_exchange_data(self):
        cols = self.data['columns']
        self.assertEqual(cols[0]['g'],cols[1]['g'])
        self.assertLess(cols[0]['cap'][0],cols[0]['cap'][-1])
        self.assertGreater(self.data['windows'][0]['queries'][-1],self.data['event_update']['time'])
