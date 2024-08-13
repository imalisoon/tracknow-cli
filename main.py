import os
from tracknow.models.categoryModel import CategoryModelManager
from tracknow.controllers.categoryController import CategoryController
from tracknow.views.categoryView import CategoryView

category_model = CategoryModelManager()
category_view = CategoryView()
category_controller = CategoryController(category_model, category_view)


def get_user_input(text: str or None=None) -> str:
    return input("\n>>> " if text is None else text)

def display_dashboard() -> None:
    print("Bem vindo ao TRACKNOW")
    print()


if __name__ == "__main__":
    os.system("clear")
    while True:
        display_dashboard()
        print("[1] Categoria\n[0] Exit")
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

        else:
            print("Opcao invalida, tente denovo\n")
