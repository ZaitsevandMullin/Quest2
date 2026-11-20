# ----- ФУНКЦИИ ИНТЕРФЕЙСА -----

def show_menu():
    print("\n--- КОСМИЧЕСКАЯ ЭКСПЕДИЦИЯ ---")
    print("1 - Исследовать планету")
    print("2 - Добыть ресурсы")
    print("3 - Починить корабль")
    print("4 - Проверить инвентарь")
    print("5 - Посмотреть состояние корабля")
    print("6 - Отдохнуть")
    print("7 - Выход из игры")

def show_status(health, energy, resources, turn, inventory):
    print(f"\n[Здоровье: {health} | Энергия: {energy}]")
    print(f"[Ресурсы: {resources} | Ход: {turn}]")
    print(f"[Инвентарь: {', '.join(inventory) if inventory else 'Пусто'}]")

# ----- ИГРОВЫЕ МЕХАНИКИ -----

def apply_damage(health, damage):
    print(f"⚠️ Корабль или экипаж получили урон: {damage} HP!")
    return health - damage

def heal(health, amount):
    print(f"❤️ Здоровье восстановлено на {amount} HP.")
    return min(health + amount, 100)

# НОВАЯ ФУНКЦИЯ: восстановление энергии

def restore_energy(energy, amount):
    print(f"🔋 Вы восстановили {amount} единиц энергии.")
    return min(energy + amount, 100)

# НОВАЯ ФУНКЦИЯ: случайное космическое событие

def space_event():
    events = [
        "Вы обнаружили странный сигнал из глубин планеты.",
        "Рядом с кораблём пролетел метеорит.",
        "Вы нашли следы неизвестной цивилизации.",
        "На горизонте появилась огромная пылевая буря."
    ]

    print("\n🌌 КОСМИЧЕСКОЕ СОБЫТИЕ:")
    print(random.choice(events))

# НОВАЯ ФУНКЦИЯ: информация о корабле

def show_ship_status(health, energy):
    print("\n--- СОСТОЯНИЕ КОСМИЧЕСКОГО КОРАБЛЯ ---")
    print(f"Прочность корабля: {health}/100")
    print(f"Заряд энергии: {energy}/100")

    if health <= 30:
        print("⚠️ Корабль сильно повреждён!")

    elif health <= 60:
        print("Корабль получил некоторые повреждения.")

    else:
        print("✅ Корабль находится в хорошем состоянии.")

# ----- ОБРАБОТКА ИГРОВЫХ ХОДОВ -----

def process_turn(choice, health, energy, resources, inventory):

    new_health = health
    new_energy = energy
    new_resources = resources

    # 1. ИССЛЕДОВАНИЕ ПЛАНЕТЫ
    if choice == "1":

        if new_energy >= 15:
            new_energy -= 15

            print("\n🚀 Вы отправились исследовать поверхность Марса...")

            event = random.choice([
                "artifact", "danger", "nothing", "crystal"
            ])

            if event == "artifact":
                print("🎉 Вы нашли древний инопланетный артефакт!")

                if "Артефакт" not in inventory:
                    inventory.append("Артефакт")

            elif event == "danger":
                print("На вас обрушилась песчаная буря!")
                new_health = apply_damage(new_health, 20)

            elif event == "crystal":
                print("Вы обнаружили редкий энергетический кристалл!")
                if "Кристалл" not in inventory:
                    inventory.append("Кристалл")

            else:
                print("Вы исследовали местность, но ничего не нашли.")

            space_event()

        else:
            print("Недостаточно энергии для исследования!")

    # 2. ДОБЫЧА РЕСУРСОВ
    elif choice == "2":

        print("\n⛏️ Вы начали добывать ресурсы...")

        if new_energy >= 10:
            new_energy -= 10

            amount = random.randint(5, 15)
            new_resources += amount

            print(f"Вы добыли {amount} единиц ресурсов!")

        else:
            print("Недостаточно энергии!")

    # 3. РЕМОНТ КОРАБЛЯ
    elif choice == "3":

        if new_resources >= 10:
            new_resources -= 10
            new_health = heal(new_health, 30)
            print("🔧 Вы успешно отремонтировали корабль!")

        else:
            print("Недостаточно ресурсов для ремонта!")

    # 4. ИНВЕНТАРЬ
    elif choice == "4":

        print("\n--- ИНВЕНТАРЬ ---")

        if not inventory:
            print("Инвентарь пуст.")

        for item in inventory:
            print("- " + item)

    # 5. СОСТОЯНИЕ КОРАБЛЯ
    elif choice == "5":

        show_ship_status(new_health, new_energy)

    # 6. ОТДЫХ
    elif choice == "6":

        new_energy = restore_energy(new_energy, 25)
        print("Вы отдохнули на борту корабля.")

    else:
        print("Неверный выбор. Попробуйте ещё раз.")

    return new_health, new_energy, new_resources

# ----- ГЛАВНЫЙ ЦИКЛ ИГРЫ -----

def main():

    health = 100
    energy = 100
    resources = 20
    turn = 1

    inventory = []

    print("=========================================")
    print("🚀 КОСМИЧЕСКАЯ ЭКСПЕДИЦИЯ: ТАЙНА МАРСА")
    print("Ваша задача — найти древний артефакт!")
    print("Исследуйте планету и берегите корабль.")
    print("=========================================")

    while True:

        show_status(health, energy, resources, turn, inventory)
        show_menu()

        choice = input("\nВаш выбор: ").strip()

        if choice == "7":
            print("\nВы завершили космическую экспедицию. До встречи!")
            break

        health, energy, resources = process_turn(
            choice, health, energy, resources, inventory
        )

        turn += 1

        # ПРОВЕРКА ПОРАЖЕНИЯ

        if health <= 0:
            print("\n💀 Корабль получил критические повреждения!")
            print("ЭКСПЕДИЦИЯ ПРОВАЛЕНА.")
            break

        # ПРОВЕРКА ПОБЕДЫ

        if "Артефакт" in inventory:
            print("\n🎉 ПОБЕДА!")
            print("Вы обнаружили древний артефакт Марса!")
            print("Человечество получило доказательство существования")
            print("древней инопланетной цивилизации!")
            break

        # ПРОВЕРКА ВРЕМЕНИ

        if turn > 20:
            print("\n⏳ Время экспедиции закончилось!")
            print("Корабль должен покинуть орбиту Марса.")
            print("ИГРА ОКОНЧЕНА.")
            break

if __name__ == "__main__":
    main()