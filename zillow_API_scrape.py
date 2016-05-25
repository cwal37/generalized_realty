# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:06:13 2016

@author: Connor
"""

import pandas as pd
import numpy as np
from API_key import *
from pyzillow.pyzillow import ZillowWrapper, GetUpdatedPropertyDetails

zillow_data = ZillowWrapper(ZWSID)
updated_property_details_response = zillow_data.get_updated_property_details(12940850)
result = GetUpdatedPropertyDetails(updated_property_details_response)

print dir(result)

print result.year_built
