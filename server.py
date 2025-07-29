import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/l4chsalter/api/alternative-me-crypto'

mcp = FastMCP('alternative-me-crypto')

@mcp.tool()
def listings() -> dict: 
    '''Overview of all available crypto currencies, use the returned id to retrieve more data on a specific crypto currency on the ticker endpoint.'''
    url = 'https://l4chsalter-alternative-me-crypto-v1.p.rapidapi.com/v2/listings/'
    headers = {'x-rapidapi-host': 'l4chsalter-alternative-me-crypto-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_ticker(limit: Annotated[Union[int, float, None], Field(description='Limit the number of returned results. The default value is 100.')] = None,
              start: Annotated[Union[int, float, None], Field(description='Sets the first element to be fetched, all requests are ordered by the Marketcap. That means the order of the returned elements can change over time.')] = None,
              convert: Annotated[Union[str, None], Field(description="In addition to the USD values the converted values will be deliveredin the requested currency. Possible fiat conversion target values are: ' USD', 'EUR', 'GBP', 'RUB', 'JPY', 'CAD', 'KRW', 'PLN' it is also possible to convert to other cryptocurrencies like: 'BTC', 'ETH', 'XRP', 'LTC' and 'BCH'.")] = None) -> dict: 
    '''Coin and token prices updated every 5 minutes.'''
    url = 'https://l4chsalter-alternative-me-crypto-v1.p.rapidapi.com/v1/ticker/'
    headers = {'x-rapidapi-host': 'l4chsalter-alternative-me-crypto-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'start': start,
        'convert': convert,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_tickert_for_specific_currency(convert: Annotated[Union[str, None], Field(description="In addition to the USD values the converted values will be deliveredin the requested currency. Possible fiat conversion target values are: ' USD', 'EUR', 'GBP', 'RUB', 'JPY', 'CAD', 'KRW', 'PLN' it is also possible to convert to other cryptocurrencies like: 'BTC', 'ETH', 'XRP', 'LTC' and 'BCH'.")] = None) -> dict: 
    '''Coin and token prices updated every 5 minutes.'''
    url = 'https://l4chsalter-alternative-me-crypto-v1.p.rapidapi.com/v1/ticker/'
    headers = {'x-rapidapi-host': 'l4chsalter-alternative-me-crypto-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'convert': convert,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v1_global(convert: Annotated[Union[str, None], Field(description="In addition to the USD values the converted values will be deliveredin the requested currency. Possible fiat conversion target values are: ' USD', 'EUR', 'GBP', 'RUB', 'JPY', 'CAD', 'KRW', 'PLN' it is also possible to convert to other cryptocurrencies like: 'BTC', 'ETH', 'XRP', 'LTC' and 'BCH'.")] = None) -> dict: 
    '''In addition to the USD values the converted values will be deliveredin the requested currency. Possible fiat conversion target values are: ' USD', 'EUR', 'GBP', 'RUB', 'JPY', 'CAD', 'KRW', 'PLN' it is also possible to convert to other cryptocurrencies like: 'BTC', 'ETH', 'XRP', 'LTC' and 'BCH'.'''
    url = 'https://l4chsalter-alternative-me-crypto-v1.p.rapidapi.com/v1/global/'
    headers = {'x-rapidapi-host': 'l4chsalter-alternative-me-crypto-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'convert': convert,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_ticker(limit: Annotated[Union[int, float, None], Field(description="Limit the number of returned results. The default value is 100, use '0' for all available data.")] = None,
              start: Annotated[Union[int, float, None], Field(description='Sets the first element to be fetched, all requests are ordered by the Marketcap. That means the order of the returned elements can change over time.')] = None,
              convert: Annotated[Union[str, None], Field(description="In addition to the USD values the converted values will be deliveredin the requested currency. Possible fiat conversion target values are: ' USD', 'EUR', 'GBP', 'RUB', 'JPY', 'CAD', 'KRW', 'PLN' it is also possible to convert to other cryptocurrencies like: 'BTC', 'ETH', 'XRP', 'LTC' and 'BCH'.")] = None,
              structure: Annotated[Union[str, None], Field(description="sets the structure of the data field as either array or name-value pair style. Possible values are 'dictionary' for name-value pair style and 'array' for array style.")] = None,
              sort: Annotated[Union[str, None], Field(description="returned results can be sorted by: 'id', 'rank' (means marketcap), 'volume_24h', 'percent_change_24h' default sorting is by rank. In addition it can be sorted by: 'price', 'percent_change_1h', 'percent_change_7d', 'circulating_supply' and 'name'.")] = None) -> dict: 
    '''Coin and token prices updated every 5 minutes.'''
    url = 'https://l4chsalter-alternative-me-crypto-v1.p.rapidapi.com/v2/ticker/'
    headers = {'x-rapidapi-host': 'l4chsalter-alternative-me-crypto-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'limit': limit,
        'start': start,
        'convert': convert,
        'structure': structure,
        'sort': sort,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_ticker_for_specific_currency() -> dict: 
    '''Get ticker data of a specified coin by providing the 'id' or the 'website_slug' of the coin as can be found by calling listings endpoint.'''
    url = 'https://l4chsalter-alternative-me-crypto-v1.p.rapidapi.com/v2/ticker/(id,name)'
    headers = {'x-rapidapi-host': 'l4chsalter-alternative-me-crypto-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_global(convert: Annotated[Union[str, None], Field(description="In addition to the USD values the converted values will be deliveredin the requested currency. Possible fiat conversion target values are: ' USD', 'EUR', 'GBP', 'RUB', 'JPY', 'CAD', 'KRW', 'PLN' it is also possible to convert to other cryptocurrencies like: 'BTC', 'ETH', 'XRP', 'LTC' and 'BCH'.")] = None) -> dict: 
    '''Get global market information at a glance.'''
    url = 'https://l4chsalter-alternative-me-crypto-v1.p.rapidapi.com/v2/global/'
    headers = {'x-rapidapi-host': 'l4chsalter-alternative-me-crypto-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'convert': convert,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
