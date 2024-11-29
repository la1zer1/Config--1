# Shell Emulator

Эмулятор командной строки для UNIX-подобной операционной системы. Программа работает с виртуальной файловой системой, предоставленной в виде ZIP-архива, и поддерживает базовые команды оболочки.

---

## Функциональность

Эмулятор поддерживает следующие команды:

1. **`ls`**  
   Отображает содержимое текущей директории.

2. **`cd <path>`**  
   Переходит в указанную директорию. Можно использовать относительные или абсолютные пути.

3. **`wc <file>`**  
   Подсчитывает количество строк, слов и символов в файле.

4. **`rmdir <path>`**  
   Удаляет указанную директорию (включая её содержимое).

5. **`cal [month] [year]`**  
   Отображает календарь для текущего или указанного месяца и года.

6. **`exit`**  
   Завершает работу эмулятора.

---

### Запуск

1. Создайте виртуальную файловую систему в виде ZIP-архива. Например:
```python
vfs.zip
├── file1.txt
├── dir1/
│   └── file2.txt
```

Запуск
Выполните следующую команду:
```bash
    python shell_emulator.py <hostname> <path_to_vfs.zip>
```
    <hostname>: Имя хоста, отображаемое в командной строке (например, myhost).
    <path_to_vfs.zip>: Путь к ZIP-архиву виртуальной файловой системы.
Пример:
```bash
    python shell_emulator.py myhost vfs.zip
```
Запуск тестов
Убедитесь, что тесты находятся в одном каталоге с shell_emulator.py.
Выполните:
```bash
    python test_shell_emulator.py
```
[Скриншот тестов](photo/Снимок%20экрана%202024-11-21%20224958.png)