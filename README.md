# Console Assistant Bot

## Запуск

```bash
python3 main.py
```

Адресна книга автоматично завантажується з `addressbook.pkl` при старті
(якщо файл існує) і зберігається туди ж при виході командою `close`/`exit`.

## Автодоповнення команд

Під час введення консольний помічник показує доступні команди.

- Почніть вводити назву команди, щоб побачити підказки.
- Натисніть **Tab**, щоб доповнити команду.
- Використовуйте **↑** і **↓**, щоб переглядати історію введених команд.

Список підказок автоматично оновлюється на основі зареєстрованих команд.


## Команди

| Команда                                      | Опис                                                     |
| -------------------------------------------- |----------------------------------------------------------|
| `add [name] [phone]`                         | Додати новий контакт або новий телефон до існуючого      |
| `change [name] [old phone] [new phone]`      | Змінити номер телефону                                   |
| `remove-phone [name] [phone]`                | Видалити номер телефону з контакту                       |
| `phone [name]`                               | Показати телефони контакту                               |
| `all`                                        | Показати всі контакти                                    |
| `delete [name]`                              | Видалити контакт                                         |
| `search [name]`                              | Знайти контакти за повним або частковим ім’ям            |
| `add-address [name] [address]`               | Додати або оновити адресу контакту                       |
| `add-email [name] [email]`                   | Додати або оновити електронну пошту контакту             |
| `add-birthday [name] [DD.MM.YYYY]`           | Додати/оновити день народження                           |
| `show-birthday [name]`                       | Показати день народження контакту                        |
| `birthdays [days]`                           | Показати дні народження протягом вказаної кількості днів |
| `add-note [name] "text" [tags...]`           | Додати нотатку з тегами                                  |
| `show-notes [name]`                          | Показати всі нотатки контакту                            |
| `find-notes-tag [tag]`                       | Знайти нотатки за тегом                                  |
| `search-notes [text]`                        | Знайти нотатки за текстом                                 |
| `group-notes-tags`                           | Згрупувати нотатки за тегами                        |
| `edit-note [name] [number] "text" [tags...]` | Редагувати нотатку                                       |
| `delete-note [name] [number]`                | Видалити нотатку                                         |
| `clear`                                      | Очистити консоль                                    |
| `help`                                       | Список команд                                            |
| `close` / `exit`                             | Зберегти адресну книгу і вийти                           |

## Приклад сесії

```text
Enter a command: add John 1234567890
Contact added.

Enter a command: add-birthday John 25.08.1990
Birthday added for John.

Enter a command: add-note John "Call bank tomorrow" finance important
Note added.

Enter a command: show-notes John
1. Call bank tomorrow [finance, important]

Enter a command: find-notes-tag finance
John: Call bank tomorrow [finance, important]

Enter a command: group-notes-tags
finance:
John: Call bank tomorrow [finance, important]

important:
John: Call bank tomorrow [finance, important]

Enter a command: all
Contact name: John, phones: 1234567890, birthday: 25.08.1990

Enter a command: clear

Enter a command: exit
Good bye!
```