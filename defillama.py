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


    def _handle_request(self, url, return_dataframe=False, **kwargs):

        try:
            response = requests.get(url, **kwargs)
            response.raise_for_status()
            if return_dataframe:
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
        url = f'{self.common_base_url}/protocols'
        return self._handle_request(url)

    def historical_tvl_full(self, protocol):
        url = f'{self.common_base_url}/protocol/{protocol}'
        return self._handle_request(url)

    def historical_tvls(self):
        url = f'{self.common_base_url}/historicalChainTvl'
        return self._handle_request(url)

    def historical_tvl(self, chain):
        url = f'{self.common_base_url}/historicalChainTvl/{chain}'
        return self._handle_request(url)

    def current_tvl(self, protocol):
        url = f'{self.common_base_url}/tvl/{protocol}'
        return self._handle_request(url)

    def current_tvls(self):
        url = f'{self.common_base_url}/tvl/{protocol}'
        return self._handle_request(url)

    # coins section
    def current_coins(self, coins):
        url = f'{self.common_base_url}/prices/current/{coins}'
        return self._handle_request(url)

    def historical_prices_by_timestamp(self, timestamp, coins):
        url = f'{self.common_base_url}/prices/historical/{timestamp}/{coins}'
        return self._handle_request(url)

    def batch_historical_prices(self, coins):
        url = f'{self.common_base_url}/batch/historical'
        return self._handle_request(url)

    def price_intervals(self, coins):
        url = f'{self.common_base_url}/batch/intervals/{coins}'
        return self._handle_request(url)

    def price_percentage_change(self, coins):
        url = f'{self.common_base_url}/percentage/{coins}'
        return self._handle_request(url)

    def price_first_record(self, coins):
        url = f'{self.common_base_url}/prices/first/{coins}'
        return self._handle_request(url)

    def closest_block_to_timestamp(self, chain, timestamp):
        url = f'{self.common_base_url}/block/{chain}/{timestamp}'
        return self._handle_request(url)

    # stablecoins section
    def list_stablecoins(self):
        url = f'{self.common_base_url}/stablecoins'
        return self._handle_request(url)

    def stablecoins_charts_all(self):
        url = f'{self.common_base_url}/stablecoins/charts/all'
        return self._handle_request(url)

    def stablecoins_charts_by_chain(self, chain):
        url = f'{self.common_base_url}/stablecoins/charts/{chain}'
        return self._handle_request(url)

    def historical_stablecoin(self, asset):
        url = f'{self.common_base_url}/stablecoin/{asset}'
        return self._handle_request(url)

    def current_stablecoin_chains(self):
        url = f'{self.common_base_url}/stablecoin/chains'
        return self._handle_request(url)

    def historical_stablecoin_prices(self):
        url = f'{self.common_base_url}/stablecoin/prices'
        return self._handle_request(url)

    # yields section
    def latest_pool_data(self, pools):
        url = f'{self.common_base_url}/pools'
        return self._handle_request(url)

    def historical_pool_apys_tvls(self, pool):
        url = f'{self.common_base_url}/chart/{pool}'
        return self._handle_request(url)

    # abi-decoder section
    def fetch_signature_function(self, signature):
        url = f'{self.common_base_url}/fetch/signature/{signature}'
        return self._handle_request(url)

    def fetch_contract_signature(self, contract, address):
        url = f'{self.common_base_url}/fetch/contract/{contract}/{address}'
        return self._handle_request(url)

    # bridges section
    def list_all_bridges(self):
        url = f'{self.common_base_url}/bridges'
        return self._handle_request(url)

    def bridge_summary(self, id):
        url = f'{self.common_base_url}/bridge/{id}'
        return self._handle_request(url)

    def bridge_volume_by_chain(self, chain):
        url = f'{self.common_base_url}/bridge/volume/{chain}'
        return self._handle_request(url)

    def bridge_days_stats(self, timestamp, chain):
        url = f'{self.common_base_url}/bridge/days/stats/{timestamp}/{chain}'
        return self._handle_request(url)

    def bridge_transactions(self, id):
        url = f'{self.common_base_url}/transactions/{id}'
        return self._handle_request(url)


if __name__ == '__main__':

    dl = DefiLlama()
    tvl_protocols = dl.tvl_protocols()

