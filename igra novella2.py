import random

# Список доступных оружий
weapons = ["лук", "меч", "копье", "булава", "щит"]
armors = ["Нагрудник", "Шлем","Нагрудник + шлем"]

hero = {
    "оружие": "",
    "броня": "",
    "история_действий": []
}


a_dragon_responses = set()


places = ["Рынок", "Вернуться к дракону", "Домой"]

def choose_armor():
    while True:
        print("Выберите броню для героя:")
        for i, armor in enumerate(armors, 1):
            print(f"{i}. {armor}")

        try:
            choice = int(input("Введите номер брони: "))
            if 1 <= choice <= len(armors):
                hero["броня"] = armors[choice - 1]
                break
            else:
                print("Пожалуйста, выберите номер из списка.")
        except ValueError:
            print("Пожалуйста, введите число.")

def choose_weapon():
    while True:
        print("Выберите оружие для сражения с драконом:")
        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon}")

        try:
            choice = int(input("Введите номер оружия: "))
            if 1 <= choice <= len(weapons):
                hero["оружие"] = weapons[choice - 1]
                break
            else:
                print("Пожалуйста, выберите номер из списка.")
        except ValueError:
            print("Пожалуйста, введите число.")

# Функция для сражения с драконом
def battle():
    choose_armor()
    choose_weapon()
    while True:
        dragon_response = input("Герой говорит: 1.Смерть тебе чудовище, 2. Беги пока не поздно чудовище, 3. Герой устал сегодня. Ваш выбор (1 или 2 или 3): ")

        if dragon_response not in ["1", "2", "3"]:
            print("Пожалуйста, введите 1, 2 или 3")
        else:
            a_dragon_responses.add(dragon_response)
            hero["история_действий"].append(dragon_response)

            if dragon_response == "1":
                outcome = random.choice(["Победа героя", "Проигрыш"])
            elif dragon_response == "2":
                outcome = random.choice(["Победа героя, Чудовищи не захотело уходить и проиграло.", "Проигрыш, Чудовищи не захотело уходить и победило.", "Чудовище уходит"])
            elif dragon_response == "3":
                print("Герой решил отдохнуть.")
                while True:
                    print("Выберите, куда пойдет герой после отдыха:")
                    for i, place in enumerate(places, 1):
                        print(f"{i}. {place}")

                    try:
                        choice = int(input("Введите номер места: "))
                        if 1 <= choice <= len(places):
                            chosen_place = places[choice - 1]

                            if chosen_place == "Рынок":
                                print("Герой отправился на Рынок.")
                                # Добавьте здесь код для событий на Рынке, если необходимо
                                print("После посещения Рынка, герой вернулся к выбору места.")
                            elif chosen_place == "Вернуться к дракону":
                                print("Герой вернулся к дракону.")
                                battle()  # Вызываем функцию сражения с драконом снова
                            elif chosen_place == "Домой":
                                print("Герой отправился домой.")
                                while True:
                                    print("Выберите действие:")
                                    print("1. Вернуться к сражению")
                                    print("2. Закончить игру, если дракон побежден.")

                                    try:
                                        choice = int(input("Введите номер действия: "))
                                        if choice == 1:
                                            print("Герой вернулся к сражению.")
                                            battle()  # Вызываем функцию сражения с драконом снова
                                        elif choice == 2:
                                            print("Игра завершена.")
                                            return  # Завершаем игру
                                        else:
                                            print("Пожалуйста, выберите 1 или 2.")
                                    except ValueError:
                                        print("Пожалуйста, введите число.")
                            break
                        else:
                            print("Пожалуйста, выберите номер из списка.")
                    except ValueError:
                        print("Пожалуйста, введите число.")
                return  # Возвращаемся из функции сражения после выбора места

            print(outcome)
            break

# Основной цикл игры
def main():
    while True:
        battle()
        replay = input("Хотите сыграть ещё раз? (да/нет). Введите 1 если да.: ")
        if replay.lower() != "1":
            break

if __name__ == "__main__":
    main()