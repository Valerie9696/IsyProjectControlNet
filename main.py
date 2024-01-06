from lemon import api
import requests
from datetime import datetime, timezone
import json
import utility as ut


#halara 231211215135483976

market_data_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsZW1vbi5tYXJrZXRzIiwiaXNzIjoibGVtb24ubWFya2V0cyIsInN1YiI6InVzcl9yeUdmUXFxQ0NIR1lYVjU4bExIbEJWU21wTVkzS3FOS0JyIiwiZXhwIjoxNzEzODc2NjEwLCJpYXQiOjE2ODIzNDA2MTAsImp0aSI6ImFwa19yeUdmUTk5Tk5QRlc2N0JEOTZEOEtoaFFmU0w0dGZGYzFZIiwibW9kZSI6Im1hcmtldF9kYXRhIn0.gKKc6EDI5Pg9zm1KiNFBN2qIP2hoK0UlwwdWW2hJZDo'
trading_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsZW1vbi5tYXJrZXRzIiwiaXNzIjoibGVtb24ubWFya2V0cyIsInN1YiI6InVzcl9yeUdmUXFxQ0NIR1lYVjU4bExIbEJWU21wTVkzS3FOS0JyIiwiZXhwIjoxNzEzODkzNDQ4LCJpYXQiOjE2ODIzNTc0NDgsImp0aSI6ImFwa19yeUdmV21tNzczWHhiUFJIMmZiZkdRc1ZEYjJsOTh3VjEzIiwibW9kZSI6InBhcGVyIn0.oo9V3jc9mUPPe6tZhbndEeGjsXM9TnIMIk1riD0l6As'

request = requests.get("https://data.lemon.markets/v1/instruments?search=Coinbase",
                       headers={"Authorization": f"Bearer {market_data_key}"})

request = requests.get("https://data.lemon.markets/v1/ohlc/d1?isin=US88160R1014&from=2021-11-01&limit=10",
          headers={"Authorization": f"Bearer {market_data_key}"})

print(request.json())

client = api.create(
    market_data_api_token=market_data_key,
    trading_api_token=trading_key,
    env='paper'  # or env='live'
)

#client.market_data.ohlc.get()
response = client.market_data.ohlc.get(period='d1', isin=['US88160R1014'], from_=datetime(2022, 1, 1, 0, 0, tzinfo=timezone.utc), to=datetime(2022, 2, 28, 0, 0, tzinfo=timezone.utc))
d = response.dict()
ut.to_df(response.results)
print(response.results[0].dict())
#for res in response.auto_iter():
 #   print(res)

