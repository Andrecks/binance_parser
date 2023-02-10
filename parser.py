import ccxt
import time

exchange = ccxt.binance()
symbol = 'XRP/USDT'

# Получаем максимальную цену за последний час
ohlcv = exchange.fetch_ohlcv(symbol, '1h')

last_hour_candles = ohlcv[-60:]

max_price = max(candle[2] for candle in last_hour_candles)
print(max_price)

if __name__ == '__main__':

    while True:
        # Получаем текущую цену
        ticker = exchange.fetch_ticker(symbol)
        current_price = ticker['last']
        print(current_price)
        
        # Проверяем, не упала ли цена на 1%
        if current_price / max_price < 0.99:
            print("Price fell by 1% from the maximum price in the last hour")
        
        # Задержка перед следующим опросом
        time.sleep(3)