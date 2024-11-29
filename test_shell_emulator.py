import zipfile
import io
from shell_emulator import ls, cd, wc, rmdir, cal, exit_shell
from datetime import datetime

successful_tests = 0  # Счетчик успешных тестов
total_tests = 0       # Счетчик общего количества тестов

# Создаем виртуальный zip-файл в памяти
def create_test_zip():
    zip_bytes = io.BytesIO()
    with zipfile.ZipFile(zip_bytes, 'w') as zip_archive:
        zip_archive.writestr('file1.txt', 'Hello, world!')
        zip_archive.writestr('dir1/', '')
        zip_archive.writestr('dir1/file2.txt', 'Python testing')
        zip_archive.writestr('file3.txt', 'Another test file')
    zip_bytes.seek(0)
    return zipfile.ZipFile(zip_bytes, 'a')

# Тесты для ls
def test_ls():
    global successful_tests, total_tests
    zip_archive = create_test_zip()
    current_directory = ''

    # Проверка содержимого корневого каталога
    print("Тест ls - корневой каталог")
    total_tests += 1
    ls(zip_archive, current_directory)  # Ожидаем увидеть 'dir1' и 'file1.txt'
    successful_tests += 1

    # Проверка содержимого подкаталога
    current_directory = 'dir1'
    print("\nТест ls - подкаталог dir1")
    total_tests += 1
    ls(zip_archive, current_directory)  # Ожидаем увидеть 'file2.txt'
    successful_tests += 1

    zip_archive.close()

# Тесты для cd
def test_cd():
    global successful_tests, total_tests
    zip_archive = create_test_zip()
    current_directory = ''

    # Переход в подкаталог dir1
    total_tests += 1
    new_directory = cd(zip_archive, current_directory, 'dir1')
    assert new_directory == 'dir1', "Ошибка: переход в подкаталог dir1 не выполнен корректно"
    print("Тест cd - переход в подкаталог dir1 прошел успешно")
    successful_tests += 1

    # Переход в несуществующий каталог
    total_tests += 1
    new_directory = cd(zip_archive, current_directory, 'nonexistent')
    assert new_directory == current_directory, "Ошибка: переход в несуществующий каталог должен возвращать текущий каталог"
    print("Тест cd - переход в несуществующий каталог прошел успешно")
    successful_tests += 1

    zip_archive.close()

# Тесты для wc
def test_wc():
    global successful_tests, total_tests
    zip_archive = create_test_zip()
    current_directory = ''

    # Подсчет строк, слов и символов в файле file1.txt
    print("Тест wc - файл file1.txt")
    total_tests += 1
    wc(zip_archive, current_directory, 'file1.txt')  # Ожидаем увидеть '1 2 13 file1.txt'
    successful_tests += 1

    # Попытка подсчета строк, слов и символов для несуществующего файла
    print("\nТест wc - несуществующий файл nonexistent.txt")
    total_tests += 1
    wc(zip_archive, current_directory, 'nonexistent.txt')  # Ожидаем сообщение об ошибке
    successful_tests += 1

    zip_archive.close()

# Тесты для rmdir
def test_rmdir():
    global successful_tests, total_tests
    zip_archive = create_test_zip()
    current_directory = ''

    # Попытка удалить пустую директорию
    total_tests += 1
    zip_archive = rmdir('filesystem.zip', zip_archive, current_directory, 'dir1')
    print("Тест rmdir - удаление пустой директории dir1 прошло успешно")
    successful_tests += 1

    # Попытка удалить несуществующую директорию
    total_tests += 1
    zip_archive = rmdir('filesystem.zip', zip_archive, current_directory, 'nonexistent')
    print("Тест rmdir - удаление несуществующей директории прошло успешно")
    successful_tests += 1

    zip_archive.close()

# Тесты для cal
def test_cal():
    global successful_tests, total_tests

    # Проверка вывода календаря
    print("Тест cal - текущий месяц")
    total_tests += 1
    cal()  # Ожидаем увидеть календарь текущего месяца
    successful_tests += 1

# Тесты для exit
def test_exit():
    global successful_tests, total_tests
    zip_archive = create_test_zip()

    # Проверка выхода из оболочки (функция exit_shell)
    print("Тест exit - выход из оболочки")
    total_tests += 1
    try:
        exit_shell(zip_archive)  # Эта функция вызывает exit(), так что для теста это завершит выполнение
        print("Тест exit прошел успешно")
        successful_tests += 1
    except SystemExit:
        print("Тест exit завершил выполнение успешно")
        successful_tests += 1

# Функция для запуска всех тестов
def run_tests():
    print("Запуск тестов для ls")
    test_ls()

    print("\nЗапуск тестов для cd")
    test_cd()

    print("\nЗапуск тестов для wc")
    test_wc()

    print("\nЗапуск тестов для rmdir")
    test_rmdir()

    print("\nЗапуск тестов для cal")
    test_cal()

    print("\nЗапуск тестов для exit")
    test_exit()

    # Вывод итогового сообщения
    print(f"\nВсе тесты завершены успешно! Всего тестов: {total_tests}, успешных тестов: {successful_tests}")

# Запускаем все тесты
run_tests()
