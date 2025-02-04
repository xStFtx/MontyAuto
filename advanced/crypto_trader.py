from binance.client import Client
import pandas as pd
import numpy as np
from ta.momentum import RSIIndicator

class TradingBot:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)
        self.rsi_window = 14
    
    def execute_strategy(self, symbol, interval='1h'):
        klines = self.client.get_klines(symbol=symbol, interval=interval)
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume', 
                                         'close_time', 'quote_asset_volume', 'trades', 
                                         'taker_buy_base', 'taker_buy_quote', 'ignore'])
        df['close'] = df['close'].astype(float)
        
        rsi = RSIIndicator(df['close'], window=self.rsi_window).rsi()
        
        current_rsi = rsi.iloc[-1]
        if current_rsi < 30:
            self.place_order(symbol, 'BUY')
        elif current_rsi > 70:
            self.place_order(symbol, 'SELL')
    
    def place_order(self, symbol, side):
        balance = self.client.get_asset_balance(asset='USDT')
        if float(balance['free']) > 10:
            self.client.create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=round(float(balance['free']) / float(self.client.get_symbol_ticker(symbol=symbol)['price']), 5)
            ) 