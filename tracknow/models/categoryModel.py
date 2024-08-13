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

    def removeCategory(self, name: str) -> bool:
        for i in range(len(self._categories)):
            if self._categories[i].name == name:
                self._categories.pop(i)
                return True

        return False
