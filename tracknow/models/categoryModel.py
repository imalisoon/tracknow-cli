class CategoryModel:
    def __init__(self, name: str) -> None:
        self._name: str = name

    @property
    def name(self) -> str:
        return self._name


class CategoryModelManager:
    def __init__(self) -> None:
        self._categories: list = list()

    def createCategory(self, name: str) -> None:
        category = CategoryModel(name)
        self._categories.append(category)

    def getCategories(self) -> list:
        return self._categories
