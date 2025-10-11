from abc import ABC, abstractmethod

class Tile(ABC):
    @abstractmethod
    def draw(self, x: int, y: int) -> None:
        pass

class ConcreteTile(Tile):
    def __init__(self, name: str):
        self._name = name
        print(f"[Tile created] {self._name}")

    def draw(self, x: int, y: int) -> None:
        print(f"[{self._name}] at ({x},{y})")

class TileFactory:
    def __init__(self):
        self._cache: dict[str, Tile] = {}

    def get(self, name: str) -> Tile:
        if name not in self._cache:
            self._cache[name] = ConcreteTile(name)
        return self._cache[name]

    def stats(self) -> None:
        print(f"Cached tiles: {list(self._cache.keys())}")

if __name__ == "__main__":
    factory = TileFactory()

    grass1 = factory.get("grass")
    grass2 = factory.get("grass")
    water = factory.get("water")

    print("grass1 is grass2:", grass1 is grass2)

    grass1.draw(0, 0)
    grass2.draw(1, 1)
    water.draw(2, 2)

    factory.stats()