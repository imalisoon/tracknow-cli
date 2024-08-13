class CategoryView:
    def displayCategories(self, categories: list) -> None:
        i = 1
        print("\n[+] CATEGORIAS [+]")
        if not categories:
            print("sem categorias, crie uma.")
            return

        for category in categories:
            print(f"{i} - {category.name.title()}")
            i += 1
