from pagamento.pagamento import Pagamento


class PagamentoCartao(Pagamento):
    def processar(self, valor):
        print(f"Processando o pagamento de R$ {valor:.2f} via cartão")
