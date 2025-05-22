import Priority_queue as PQ


def test_empty():
    """Проверяет, что новая очередь пуста"""
    pq = PQ.PriorityQueue()
    assert pq.empty() is True


def test_extract_empty():
    """Проверяет извлечение из пустой очереди"""
    pq = PQ.PriorityQueue()
    try:
        pq.extract_max()
        assert False, "Ожидалась ошибка IndexError"
    except IndexError:
        pass


def test_insert_extract_one():
    """Проверяет вставку и извлечение одного элемента"""
    pq = PQ.PriorityQueue()
    pq.insert(5, "Задача A")
    assert not pq.empty()
    assert pq.extract_max() == "Задача A"
    assert pq.empty()


def test_insert_extract_many():
    """Проверяет порядок извлечения нескольких элементов"""
    pq = PQ.PriorityQueue()
    pq.insert(3, "A")
    pq.insert(7, "B")
    pq.insert(5, "C")
    pq.insert(10, "D")
    pq.insert(1, "E")

    assert pq.extract_max() == "D"
    assert pq.extract_max() == "B"
    assert pq.extract_max() == "C"
    assert pq.extract_max() == "A"
    assert pq.extract_max() == "E"
    assert pq.empty()


def test_clear_queue():
    """Проверяет, что очередь пуста после извлечения всех"""
    pq = PQ.PriorityQueue()
    pq.insert(1, "Test")
    pq.extract_max()
    assert pq.empty()


def run_tests():
    tests = [
        test_empty,
        test_extract_empty,
        test_insert_extract_one,
        test_insert_extract_many,
        test_clear_queue
    ]

    print("\n=== НАЧАЛО ТЕСТИРОВАНИЯ ===\n")
    for i, test_func in enumerate(tests, 1):
        try:
            test_func()
            print(f"ТЕСТ #{i}: {test_func.__name__} — пройден")
        except AssertionError as e:
            print(f"ТЕСТ #{i}: {test_func.__name__} провален: {e}")
    print("\n=== ВСЕ ТЕСТЫ ВЫПОЛНЕНЫ ===")


run_tests()
