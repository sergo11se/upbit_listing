import random

# Заглушка — в будущем сюда подключается API анализа (CoinGecko, Upbit и т.д.)
async def check_upbit_signals():
    dummy_coins = ["TOKENA", "TOKENB", "TOKENC", "TOKEND"]
    # Симуляция вероятности "листинга"
    return random.sample(dummy_coins, k=random.randint(0, 2))