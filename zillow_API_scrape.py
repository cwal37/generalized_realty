# -*- coding: utf-8 -*-
"""
Created on Tue May 24 22:06:13 2016

@author: Connor
"""

import pandas as pd
import numpy as np
from API_key import *
from pyzillow.pyzillow import ZillowWrapper, GetUpdatedPropertyDetails

# Well, I think I can just iterate on DC-area zillow IDs maybe? The API requires
# specific calls to individual homes, but if I can iterate through them, maybe I
# can record the info I want without actually knowing the homes beforehand.


# Ha, yes. It seems the Zillow IDs are generated iteratively in some fashion,
# so I can at least tease out some basic details on mlutiple home by iterating
# over a relatively small range in a a hack-y API-based scrapign loop.

zillow_data = ZillowWrapper(ZWSID)
updated_property_details_response = zillow_data.get_updated_property_details(4671144)
result = GetUpdatedPropertyDetails(updated_property_details_response)

#print dir(result)

print result.year_built
