from typing import Any, Iterable, List, Optional, Union

Item = Any


class NamedList:
    def __init__(self, iterable: Optional[Iterable] = None,
                 keyattr: str = 'label'):
        self.keyattr = keyattr
        self._items = []
        self._indices = {}

        if iterable is not None:
            for item in iterable:
                self.append(item)

    def labels(self) -> List[str]:
        return [getattr(item, self.keyattr) for item in self._items]

    def index(self, label: str) -> int:
        return self._indices[label]

    def get(self, key: Union[int, str]) -> Item:
        if isinstance(key, str):
            return self._items[self._indices[key]]
        else:
            return self._items[key]

    def insert(self, index: int, value: Item) -> None:
        label = getattr(value, self.keyattr)
        if label in self._indices:
            raise KeyError('duplicate label \'{}\''.format(label))
        self._items.insert(index, value)
        index = self._items.index(value)
        self._indices[label] = index

    def remove(self, key: Union[int, str]) -> None:
        if isinstance(key, str):
            self._items.pop(self._indices[key])
            del self._indices[key]
        else:
            item = self._items[key]
            del self._indices[getattr(item, self.keyattr)]
            self._items.remove(item)

    def pop(self, key: Optional[Union[int, str]] = None) -> Item:
        item = self.get(key)
        self.remove(key)
        return item

    def append(self, item: Item) -> None:
        self.insert(len(self), item)

    def __getitem__(self, key: Union[int, str]) -> Item:
        return self.get(key)

    def __setitem__(self, index: int, value: Item):
        if index not in range(len(self)):
            raise IndexError('list assignment index out of range')
        label = getattr(value, self.keyattr)
        if label in self._indices:
            raise KeyError('duplicate label \'{}\''.format(label))
        del self._indices[getattr(self._items[index], self.keyattr)]
        self._items[index] = value
        self._indices[label] = index

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self):
        return repr(self._items)

    def __str__(self):
        return str(self._items)
