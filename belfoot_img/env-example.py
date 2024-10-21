# Настроить под свою базу данных и переименовать в env.py
import os
def set_env():
    os.environ['SECRET_KEY'] = 'ваш_секретный_ключ'
    os.environ['NAME'] = 'имя_db'
    os.environ['USER'] = 'имя_пользователя'
    os.environ['PASSWORD'] = 'пароль'
    os.environ['HOST'] = '127.0.0.1'
    os.environ['PORT'] = '5432'