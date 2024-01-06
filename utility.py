import pandas as pd
from datetime import datetime, timezone, timedelta
from lemon import api
import os

market_data_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsZW1vbi5tYXJrZXRzIiwiaXNzIjoibGVtb24ubWFya2V0cyIsInN1YiI6InVzcl9yeUdmUXFxQ0NIR1lYVjU4bExIbEJWU21wTVkzS3FOS0JyIiwiZXhwIjoxNzEzODc2NjEwLCJpYXQiOjE2ODIzNDA2MTAsImp0aSI6ImFwa19yeUdmUTk5Tk5QRlc2N0JEOTZEOEtoaFFmU0w0dGZGYzFZIiwibW9kZSI6Im1hcmtldF9kYXRhIn0.gKKc6EDI5Pg9zm1KiNFBN2qIP2hoK0UlwwdWW2hJZDo'
trading_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJsZW1vbi5tYXJrZXRzIiwiaXNzIjoibGVtb24ubWFya2V0cyIsInN1YiI6InVzcl9yeUdmUXFxQ0NIR1lYVjU4bExIbEJWU21wTVkzS3FOS0JyIiwiZXhwIjoxNzEzODkzNDQ4LCJpYXQiOjE2ODIzNTc0NDgsImp0aSI6ImFwa19yeUdmV21tNzczWHhiUFJIMmZiZkdRc1ZEYjJsOTh3VjEzIiwibW9kZSI6InBhcGVyIn0.oo9V3jc9mUPPe6tZhbndEeGjsXM9TnIMIk1riD0l6As'

CSV_DIR = 'ohcl_csv'


class Collector:
    def __init__(self, isin, period, start_date, end_date):
        if not os.path.isdir(CSV_DIR):
            os.mkdir(CSV_DIR)
        self.client = api.create(
                            market_data_api_token=market_data_key,
                            trading_api_token=trading_key,
                            env='paper'  # or env='live'
                            )
        self.isin = isin
        self.period = period
        self.start_date = start_date
        self.end_date = end_date
        self.results_df = self.collect()

    def collect(self):
        dates = get_date_intervals(start_date=self.start_date, end_date=self.end_date)
        dfs = []
        for d in dates:
            response = self.client.market_data.ohlc.get(period=self.period, isin=self.isin,
                                                   from_=d[0],
                                                   to=d[1])
            dfs.append(to_df(response.results))
        full_df = pd.concat(dfs)
        full_df.to_csv(os.path.join(CSV_DIR, str(self.isin[0])+'_'+str(self.period)+'_'+self.start_date.strftime('%Y%m%d')+'_'+self.end_date.strftime('%Y%m%d')))
        print(full_df)
        return full_df


def to_df(response_results):
    df = pd.DataFrame()
    for rr in response_results:
        df = pd.DataFrame.from_records([rr.dict() for rr in response_results])
    return df


def get_date_intervals(start_date, end_date):
    interval = timedelta(days=60)
    one_day = timedelta(days=1)
    current_date = start_date
    dates = []
    while current_date < end_date:
        if end_date-current_date > timedelta(days=59):
            dates.append((current_date, current_date+interval))
        else:
            dates.append((current_date, current_date+(end_date-current_date)))
        current_date = current_date+interval+one_day
    return dates

c=Collector(isin=['US88160R1014'], period='d1', start_date=datetime(year=2022, month=1, day=1), end_date=datetime(year=2022, month=5, day=1), )
#dates = get_date_intervals(start_date=datetime.datetime(year=2020, month=1, day=1), end_date=datetime.datetime(year=2022, month=12, day=4))
#print(dates)

