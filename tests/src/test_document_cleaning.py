import json
from unittest import TestCase
from unittest.mock import patch

import numpy as np
import pandas as pd

from src import document_cleaning as dc



def test_extract_citation_info():
    assert dc.extract_citation_info("Koks et al 2022 - Flood impacts") == ("Koks ", "2022","Flood impacts")
    

