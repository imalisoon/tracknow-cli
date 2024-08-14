class InvoiceController:
    def __init__(self, model, view) -> None:
        self._model = model
        self._view = view

    def listInvoices(self) -> None:
        invoices = self._model.getInvoices()
        self._view.displayInvoices(invoices)
