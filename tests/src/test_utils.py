# standard library
import os
import sys
import requests
from typing import Optional
import urllib
import unittest
from unittest.mock import patch   

# third party imports
import requests_mock
import pandas as pd
import torch
import numpy as np

# local imports
from src import utils as u



@requests_mock.mock()
def mock_request(m):
    m.get(url, text='success')
    return requests.get(url).text



def test_metrics():
    assert u.calc_recall(8, 2) == 0.8
    assert u.calc_precision(8, 2) == 0.8
    assert u.calc_f1(0.8, 0.8) == 0.8




class TestGazetteer(unittest.TestCase):

    def setUp(self):
        self.gaz = u.Gazetteer(gazetteer_source='nominatim')
    
    @requests_mock.mock()  
    def test_nominatim_query_calls(self, m):

        # set up mock for nominatim api
        # take any location in OSM as dummy that exists in really,eg. Saxony, the only need is to check if nominatim_query() works
        url = "https://nominatim.openstreetmap.org/search?q=Saxony&format=geocodejson&polygon_geojson=1&addressdetails=1&namedetails=1&accept-language=en"
        json_out = '[{"name":"test"}]'
        m.get(url, text=json_out)
        print(m.get(url, text=json_out))
        with patch.object(self.gaz, 'nominatim_query', wraps=self.gaz.nominatim_query) as mock_nom_query:
            _ = self.gaz.nominatim_query('Saxony')   # test mocked nominatim_query() with our Dummy Location "Saxony"; it should give same response as for variable "url"
            mock_nom_query.assert_called()

