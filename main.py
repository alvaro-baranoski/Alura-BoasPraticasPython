from fila_factory import FilaFactory

fila_teste = FilaFactory.pega_fila("prioritaria")
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
fila_teste.atualiza_fila()
print(fila_teste.chama_cliente(1))
print(fila_teste.chama_cliente(2))
