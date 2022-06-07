class Fila_normal:

    codigo:int = 0
    fila = []
    clientes_atendidos = []
    senha_atual:str = ""

    def gera_senha(self) -> None:
        self.senha_atual = f"NM{self.codigo}"

    def atualiza_codigo(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualiza_fila(self) -> None:
        self.atualiza_codigo()
        self.gera_senha()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa:int) -> str:
        cliente_atual:str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f"Cliente atual: {cliente_atual}, caixa: {caixa}")