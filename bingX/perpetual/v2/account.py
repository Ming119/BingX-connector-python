'''
bingX.perpetual.v2.account
'''

from bingX import ClientError

def balance(self,
    recvWindow: int = None,
) -> dict:
    ''' Get Perpetual Swap Account Asset Information
    GET /openApi/swap/v2/user/balance

    https://bingx-api.github.io/docs/swapV2/account-api.html#_1-get-perpetual-swap-account-asset-information
    '''
    res = self.get("/openApi/swap/v2/user/balance", params={
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']

def positions(self,
    symbol: str,
    recvWindow: int = None,
) -> dict:
    ''' Perpetual Swap Positions
    GET /openApi/swap/v2/user/positions

    https://bingx-api.github.io/docs/swap/account-api.html#_2-perpetual-swap-positions
    '''
    res = self.get("/openApi/swap/v2/user/positions", params={
        "symbol": symbol,
        "recvWindow": recvWindow,
    })

    if 'code' in res and res['code']:
        raise ClientError(res['code'], res['msg'])
    return res['data']
