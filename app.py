import MetaTrader5 as mt5

# Inicializa la conexión a MetaTrader 5
mt5.initialize()

# Obtén la lista de símbolos disponibles
symbols = mt5.symbols_get()

# Imprime los nombres de los símbolos
print("Símbolos disponibles:")
for symbol in symbols:
    print(symbol.name)

# Cierra la conexión a MetaTrader 5
mt5.shutdown()


