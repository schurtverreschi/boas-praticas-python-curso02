from pagamento.pagamento_cartao import PagamentoCartao
from pagamento.pagamento_pix import PagamentoPIX


class PagamentoFactory:
    @staticmethod
    def criar_pagamento(tipo):
        match tipo:
            case "pix":
                return PagamentoPIX()
            case "cartao":
                return PagamentoCartao()
            case _:
                raise ValueError(f"Tipo de pagamento '{tipo}' não suportado")
