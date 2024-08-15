class InvoiceController:
    def __init__(self, model, view) -> None:
        self._model = model
        self._view = view

    def createInvoice(self, name: str, value: float, iType: str) -> None:
        if name and value and iType:
            if value <= 0:
                print("o valor da fatura precisa ser positivo maior que 0.")
                return

            self._model.createInvoice(name, value, iType)
            return

        print("Erro, verifique as informações.")

    def listInvoices(self) -> None:
        invoices = self._model.getInvoices()
        self._view.displayInvoices(invoices)
