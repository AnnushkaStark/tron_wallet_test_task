# tron_wallet_test_task


## Тестовое задание

Написать микросервис, который будет выводить информацию по адресу в сети трон, его bandwidth, energy, и баланс trx, ендпоинт должен принимать входные данные - адрес.
Каждый запрос писать в базу данных, с полями о том какой кошелек запрашивался.
Написать юнит/интеграционные тесты
У сервиса 2 ендпоинта
- POST
- GET для получения списка последних записей из БД, включая пагинацию,
2 теста
- интеграционный на ендпоинт
- юнит на запись в бд
Примечания: использовать FastAPI, аннотацию(typing), SQLAlchemy ORM, для удобства с взаимодействию с троном можно использовать tronpy, для тестов Pytest


## Запуск приложения

- Создать виртуальное окружение
Windows

```
python -m venv venv

```
Linux

```
python3.11 -m venv venv


- Активировать окружение
Windows

```
venv/Scripts/activate.ps1

```

Linux

```
source/venv/bin/activate

```

- Установить зависимости

```
python -r requirements.txt

```

- Запуск тестов (из директории src)

```
cd src
pytest

```

- Запуск миграций (из директории  src)

```
alembic revision --autogenerate -m "create all"
alembic upgrade head

```

- Запуск приложения (из директории src)

```
uvicorn main:app --reload

```

## Примечание

- Сваггер будет доступен по адресу

```
127.0.0.1:8000/wallet/docs

````

- для теста получения информации о кошельке по адресу в сети tron используется реальный адрес кошелька пользователя с сервиса TRONSCAN
