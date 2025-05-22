class PriorityQueue:
    def __init__(self):
        # Куча будет храниться в виде списка
        self.heap = []

    def empty(self):
        """Проверяет, пуста ли очередь"""
        return len(self.heap) == 0

    def _swap(self, i, j):
        """Меняет местами элементы"""
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _heapify_down(self, index):
        """Проталкиваем элемент вниз по дереву"""
        size = len(self.heap)
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest = index

            if left_child_index < size and self.heap[left_child_index][0] > self.heap[largest][0]:
                largest = left_child_index
            if right_child_index < size and self.heap[right_child_index][0] > self.heap[largest][0]:
                largest = right_child_index

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break


    def _heapify_up(self, index):
        """Поднимает элемент вверх по дереву"""
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index][0] > self.heap[parent_index][0]:
            self._swap(index, parent_index)
            index = parent_index
            parent_index = (index - 1) // 2

    def insert(self, priority, value):
        """Добавляем элемент в конец и восстанавливаем структуру кучи"""
        self.heap.append((priority, value))
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        """Извлекает и возвращает элемент с максимальным приоритетом"""
        if not self.heap:
            raise IndexError("Очередь пуста")

        # Меняем местами первый и последний элемент
        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()[1]

        # Восстанавливаем структуру кучи
        self._heapify_down(0)

        return max_value
