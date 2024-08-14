class InvoiceView:
    def displayInvoices(self, invoices: list) -> None:
        i = 1
        print("[+] FATURAS [+]")
        if not invoices:
            print("sem faturas :)")
            return

        for invoice in invoices:
            print(f"--- {i} - {invoice.name} | {invoice.value}")
