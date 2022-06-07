from fila_normal import FilaNormal
from fila_prioritaria import FilaPrioritaria
from constants import TIPO_FILA_NORMAL, TIPO_FILA_PRIORITARIA


class FilaFactory():
    @staticmethod
    def pega_fila(tipo_fila):
        if (tipo_fila == TIPO_FILA_PRIORITARIA):
            return FilaPrioritaria()
        elif (tipo_fila == TIPO_FILA_NORMAL):
            return FilaNormal()
        else:
            raise Exception("Tipo de fila inválido")