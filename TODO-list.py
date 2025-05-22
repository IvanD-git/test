import Priority_queue as PQ

'''TODO-lis'''

def TODO():
    pq = PQ.PriorityQueue()

    while True:
        print("\n=== TODO-list ===")
        print("1. Добавить новое дело")
        print("2. Получить дело с максимальным приоритетом")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            name = input("Введите название дела: ")
            priority = int(input("Введите приоритет (целое число): "))
            pq.insert(priority, name)
            print(f"Добавлено дело '{name}' с приоритетом {priority}.")

        elif choice == "2":
            try:
                task = pq.extract_max()
                print(f"Выполняется дело: '{task}'")
            except IndexError:
                print("Список дел пуст.")

        elif choice == "3":
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    TODO()
