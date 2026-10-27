from cliente import Cliente
from item import Item
from notificacao.notificacao_facade import NotificacaoFacade
from observador.observador_status import ObservadorStatus
from pagamento.pagamento_factory import PagamentoFactory
from pedido.pedido_delivery import PedidoDelivery

cliente = Cliente("Fulano", "Rua dos Bobos n 0")
item_um = Item("Pizza", 30.00)
item_dois = Item("Refrigerante", 5.00)
itens = [item_um, item_dois]
taxa_entrega = 10.00

pedido = PedidoDelivery(cliente, itens, taxa_entrega)
valor_pedido = pedido.calcular_total()
tipo_pagamento = "pix"

pagamento = PagamentoFactory.criar_pagamento(tipo_pagamento).processar(valor_pedido)
print()

MENSAGEM_PAGO = "Pagamento confirmado!"
MENSAGEM_PREPARANDO = "O pedido está sendo preparado!"
MENSAGEM_ENVIADO = "O pedido para a entrega!"

notificacoes = NotificacaoFacade()
observador = ObservadorStatus(notificacoes)
pedido.adicionar_observadores(observador)

pedido.status = MENSAGEM_PAGO
pedido.status = MENSAGEM_PREPARANDO
pedido.status = MENSAGEM_ENVIADO
