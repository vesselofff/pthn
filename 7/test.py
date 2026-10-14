from helpers import logger, caesar_cipher

logger("Тест логгера: всё работает", level="INFO")
logger("Предупреждение", level="WARNING")

original = "Hello, World!"
shifted = caesar_cipher(original, 3)
logger(f"Оригинал: {original}", level="DEBUG")
logger(f"После шифра (+3): {shifted}", level="DEBUG")

decrypted = caesar_cipher(shifted, -3)
logger(f"Дешифровка (-3): {decrypted}", level="DEBUG")
