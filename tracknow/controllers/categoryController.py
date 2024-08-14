class CategoryController:
    def __init__(self, model, view) -> None:
        self._model = model
        self._view = view

    def createCategory(self, name: str) -> None:
        if not name:
            print("insira um nome")
            return

        self._model.createCategory(name)

    def listCategories(self) -> None:
        categories = self._model.getCategories()
        self._view.displayCategories(categories)

    def deleteCategory(self, name: str) -> bool or None:
        if not name:
            print("insira um nome valido")
            return
        
        return self._model.removeCategory(name)
