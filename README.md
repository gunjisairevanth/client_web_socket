
# Project Analysis

As per the Doc shared, I need to get three crypto currency data (BTC, ETH and MATIC) from three exchanges channel and generate a OHLC Format
 by averaging all 3 exchanges rate for each crypto.

 


## Deveoper

- [@Sai Revanth](https://github.com/gunjisairevanth)




## Project Setup

creating virtual environment
```bash
virtualenv venv -p python3
```
enable the virtual env and installing the pre-requirement packages
```bash
source venv/bin/activate
pip3 install -r requirements.txt
python3 client.py
```

## Roadmap




![Logo](https://i.ibb.co/TLfw5PK/Untitled-Diagram-drawio.png)




 - FTX : https://docs.ftx.com/?python#websocket-api
 - Binance : https://binance-docs.github.io/apidocs/spot/en/#websocket-market-streams
 - Huobi: https://huobiapi.github.io/docs/spot/v1/en/#websocket-market-data

## Doubts

As i seen, there is no specific channel mentioned in docs for consuming the Crypto currenct timeseries trading data. So need a clarity on that.

binance provide Candlestick stream data based on interval. But there are not provide the informtaion that, how to send the cryto currency code in payload (Ref :https://binance-docs.github.io/apidocs/spot/en/#kline-candlestick-streams)

huobiapi also providing the Candlestick stream data based on time interval. but symbol format for crypto currency was not updated in docs (Ref : https://huobiapi.github.io/docs/spot/v1/en/#market-candlestick)

ftx providing only orderbook,trades and ticker data and using this data. calucating the dynamic OHLC data and storing was a bit diffiuclt and can't do it in a single python script. Because, it may leads to data lose and leads to more error rate in average margin values. A better system design required to provide a better solution for this task.

## Basic Pseudocode



```bash
  async def get_binance_channel_rate(currency, socket_session, timestamp):
    '''
        Here, we are fetching the currency rate for evey second

            currency refers the crypto_currency_code
            socket_session refer the socker connection

    '''
    response = await socket_session.get({"currency" : currency, "channel" : "XXX", "timestamp" : timestamp})
    return response

    # ------------------------------------------------------------

    async def get_huobi_channel_rate(currency, socket_session, timestamp):
    '''
        Here, we are fetching the currency rate for evey second

            currency refers the crypto_currency_code
            socket_session refer the socker connection

    '''
    response = await socket_session.get({"currency" : currency, "channel" : "XXX", "timestamp" : timestamp})
    return response

    # ------------------------------------------------------------

    async def get_ftx_channel_rate(currency, socket_session, timestamp):
    '''
        Here, we are fetching the currency rate for evey second

            currency refers the crypto_currency_code
            socket_session refer the socker connection

    '''
    response = await socket_session.get({"currency" : currency, "channel" : "XXX", "timestamp" : timestamp})
    return response

    # ------------------------------------------------------------

    async def process_data(data, currency_code):
        response = dict()
        response.asset=currency_code
        response.timestamp = data.timestamp
        response.open = (data.binance_data.open+data.ftx_data.open+data.huobi_data.open)/3
        response.high = (data.binance_data.high+data.ftx_data.high+data.huobi_data.high)/3
        response.low = (data.binance_data.low+data.ftx_data.low+data.huobi_data.low)/3
        response.close = (data.binance_data.close+data.ftx_data.close+data.huobi_data.close)/3
        return response


    async def get_currency_data():
        while True: # self looping
            result_set = list()
            for currency_code in ["BTC","ETH","MATIC"]:
                data = dict() # dictonay
                data.timestamp = currenct_time_stamp()
                data.ftx_data = await get_ftx_channel_rate(currency_code,socket_session = websockets.connect("wss://ftx.com/ws/"), timestamp)
                data.huobi_data = await get_huobi_channel_rate(currency_code,socket_session = websockets.connect("wss://ftx.com/ws/"), timestamp)
                data.binance_data = await get_binance_channel_rate(currency_code,socket_session = websockets.connect("wss://ftx.com/ws/"), timestamp)
                response = await process_data(data, currency_code)
                result_set.append(response)


     asyncio.get_event_loop().run_until_complete(get_currency_data())
        

```



