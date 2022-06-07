from fila_base import FilaBase


class FilaPrioritaria(FilaBase):

    def gera_senha(self) -> None:
        self.senha_atual = f"NM{self.codigo}"

    def atualiza_fila(self) -> None:
        self.atualiza_codigo()
        self.gera_senha()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa: int) -> str:
        cliente_atual: str = self.fila.pop(0)
        self.clientes_atendidos.append(cliente_atual)
        return(f"Cliente atual: {cliente_atual}, caixa: {caixa}")
