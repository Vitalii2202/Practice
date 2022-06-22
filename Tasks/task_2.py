"""
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
"""

def authorization_f(users, user_name, user_password):
    for key, value in users.items():
        if key == user_name:
            if value['password'] == user_password and value['activation']:
                return 'Добро пожаловать! Доступ к ресурсу представлен'
            elif value['password'] == user_password \
                    and not value['activation']:
                return 'Учетная запись не активна! Пройдите активацию'
            elif value['password'] != user_password:
                return 'Пароль не верный'
    return 'Данного пользователя не существует'

users = {'ivan': 1234}
user_name = input('введите логин: ')
user_password = input(int('введите пароль: '))
print(authorization_f(users, user_name, user_password))



