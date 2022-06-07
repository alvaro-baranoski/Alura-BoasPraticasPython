class FilaBase:

    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def atualiza_codigo(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1
