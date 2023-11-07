EMPTY_ARR_ELEMENT = None


class DynamicArray:
    def __init__(self, capacity: int):
        assert capacity > 0, f"Capacity value is set to:'{capacity}' and should be > 0!"

        self.arr = [EMPTY_ARR_ELEMENT] * capacity

    def __repr__(self):
        return str(self.arr)

    def get(self, i: int) -> int:
        self.__is_index_corr(i)
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.__is_index_corr(i)
        self.arr[i] = n
        return self.arr[i]

    def pushback(self, n: int) -> None:
        self.__is_index_corr(n)
        self.arr[self.getCapacity() - 1] = self.arr[n]
        self.arr[n] = EMPTY_ARR_ELEMENT

    def popback(self) -> int:
        e = self.arr[self.getCapacity() - 1]
        self.arr[self.getCapacity() - 1] = EMPTY_ARR_ELEMENT
        return e

    def resize(self) -> None:
        self.arr += [EMPTY_ARR_ELEMENT] * self.getCapacity()

    def getSize(self) -> int:
        l = 0
        for e in self.arr:
            if e != 0:
                l += 1
        return l

    def getCapacity(self) -> int:
        return len(self.arr)

    def __is_index_corr(self, i: int) -> bool:
        assert 0 <= i < len(self.arr), "Index is out of bound!"
        return True


da = DynamicArray(5)
da.set(3, 3)
print(da)
