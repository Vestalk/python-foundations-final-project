# Console Assistant Bot

## Запуск

```bash
python3 main.py
```

Адресна книга автоматично завантажується з `addressbook.pkl` при старті
(якщо файл існує) і зберігається туди ж при виході командою `close`/`exit`.

## Команди

| Команда | Опис |
|---|---|
| `add [name] [phone]` | Додати новий контакт або новий телефон до існуючого |
| `change [name] [old phone] [new phone]` | Змінити номер телефону |
| `remove-phone [name] [phone]` | Видалити номер телефону з контакту |
| `phone [name]` | Показати телефони контакту |
| `all` | Показати всі контакти |
| `delete [name]` | Видалити контакт |
| `add-birthday [name] [DD.MM.YYYY]` | Додати/оновити день народження |
| `show-birthday [name]` | Показати день народження контакту |
| `birthdays` | Показати іменинників на найближчі 7 днів |
| `hello` | Привітання |
| `help` | Список команд |
| `close` / `exit` | Зберегти адресну книгу і вийти |

## Приклад сесії

```
Enter a command: add John 1234567890
Contact added.
Enter a command: add-birthday John 25.08.1990
Birthday added for John.
Enter a command: all
Contact name: John, phones: 1234567890, birthday: 25.08.1990
Enter a command: exit
Good bye!
```
