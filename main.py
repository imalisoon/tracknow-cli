import os
from tracknow.models.categoryModel import CategoryModelManager
from tracknow.models.invoiceModel import InvoiceModelManager
from tracknow.controllers.categoryController import CategoryController
from tracknow.controllers.invoiceController import InvoiceController
from tracknow.views.categoryView import CategoryView
from tracknow.views.invoiceView import InvoiceView

category_model = CategoryModelManager()
category_view = CategoryView()
category_controller = CategoryController(category_model, category_view)

invoice_model = InvoiceModelManager()
invoice_view = InvoiceView()
invoice_controller = InvoiceController(invoice_model, invoice_view)


def get_user_input(text: str or None=None) -> str:
    return input("\n>>> " if text is None else text)

def display_dashboard() -> None:
    print("Bem vindo ao TRACKNOW")
    print()


if __name__ == "__main__":
    os.system("clear")
    while True:
        display_dashboard()
        print("[1] Categorias\n[2] Faturas\n[0] Exit")
        option = get_user_input()

        if option == "0":
            print("Saindo...")
            break

        elif option == "1":
            while True:
                print("[+] Gerencie as categorias [+]\n[1] Nova categoria\n[2] Lista categorias\n[3] Deletar categoria\n[0] Voltar")
                option_category = get_user_input()

                if option_category == "0":
                    break

                elif option_category == "1":
                    name = get_user_input("Nome da categoria: ")
                    category_controller.createCategory(name)

                elif option_category == "2":
                    category_controller.listCategories()
                    print()

                elif option_category == "3":
                    category_name = get_user_input("Nome da categoria a ser deletada: ")
                    if category_controller.deleteCategory(category_name):
                        print(f"{category_name} excluida.")

        elif option == "2":
            while True:
                print("[+] Gerencie suas faturas [+]")
                print("[2] Listar Faturas\n[0] Voltar")
                option_invoice = get_user_input()
                if option_invoice == "0":
                    break

                elif option_invoice == "2":
                    invoice_controller.listInvoices()

        else:
            print("Opcao invalida, tente denovo\n")
