#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = True
import argparse
import pandas as pd
import numpy as np
from datetime import datetime as dt
from datetime import timezone
import time
import requests
import logging



class DefiLlama():

    def __init__(self):
        self.common_base_url = 'https://api.llama.fi'
        self.coins_base_url = 'https://coins.llama.fi'
        self.stablecoins_base_url = 'https://stablecoins.llama.fi'
        self.yields_base_url = 'https://yields.llama.fi'
        self.abidecoder_base_url = 'https://abi-decoder.llama.fi'
        self.bridges_base_url = 'https://bridges.llama.fi'


    def _handle_request(self, url, dataframe=True, **kwargs):

        try:
            response = requests.get(url, **kwargs)
            response.raise_for_status()
            if dataframe:
                return pd.DataFrame(response.json())
            else:
                return response.json()

        except requests.HTTPError as e:
            logging.error(f"HTTP error: {e} - Status code: {e.response.status_code}")
        except requests.ConnectionError as e:
            logging.error("Connection error: ", e)
        except requests.Timeout as e:
            logging.error("Request timed out: ", e)
        except requests.RequestException as e:
            logging.error("Error during request: ", e)
        return None
                
            

    def protocols(self):
        
        url = f'{self.tvl_base_url}/protocols'
        response 
        response = pd.DataFrame(requests.get(url).json())
        print(response)


if __name__ == '__main__':

    dl = DefiLlama()
    dl.protocols()