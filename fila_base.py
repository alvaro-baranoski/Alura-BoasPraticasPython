import abc
from constants import TAMANHO_PADRAO_MAXIMO, TAMANHO_PADRAO_MINIMO


class FilaBase(metaclass=abc.ABCMeta):

    codigo: int = 0
    fila = []
    clientes_atendidos = []
    senha_atual: str = ""

    def atualiza_codigo(self) -> None:
        if self.codigo >= TAMANHO_PADRAO_MAXIMO:
            self.codigo = TAMANHO_PADRAO_MINIMO
        else:
            self.codigo += 1

    @abc.abstractmethod
    def gera_senha(self):
        ...

    def atualiza_fila(self):
        self.atualiza_codigo()
        self.gera_senha()
        self.fila.append(self.senha_atual)

    @abc.abstractmethod
    def chama_cliente(self, caixa: int):
        ...
