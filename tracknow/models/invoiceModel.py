class InvoiceModel:
    """
    Classe que representa uma fatura
    """
    def __init__(self, name: str, value: float) -> None:
        self._name: str = name
        self._value: float = value

    @property
    def name(self) -> str:
        return self._name

    @property
    def value(self) -> float:
        return self._value


class IncomeModel(InvoiceModel):
    """
    Classe que representa uma fatura \
    do tipo RENDA
    """
    _type = "income"

    def __init__(self, name: str, value: float) -> None:
        super().__init__(name, value)


class ExpenseModel(IncomeModel):
    """
    Classe que representa uma fatura \
    do tipo DESPESA
    """
    _type = "expense"

    def __init__(self, name: str, value: float) -> None:
        super().__init__(name, value)


class InvoiceModelManager:
    def __init__(self) -> None:
        self._invoices: list = list()

    def createInvoice(self, name: str, value: float, type: str) -> InvoiceModel or None:
        if type.lower() == "renda":
            return IncomeModel(name, value)

        elif type.lower() == "despesa":
            return ExpenseModel(name, value)
        return False

    def getInvoices(self) -> list:
        return self._invoices
