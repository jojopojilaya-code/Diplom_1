☼ Diplom_1

√ Юнит-тесты для сервиса Stellar Burgers https://stellarburgers.education-services.ru

Проект представляет собой набор модульных тестов для API приложения Stellar Burgers, которые обеспечивают проверку базовых моделей системы и ключевых сценариев бизнес-логики.
Тесты хранятся в директории \tests.

☺ Инструменты тестирования:

pytest - основной фреймворк для тестирования
unittest.mock - создание mock-объектов
pytest-cov - измерение покрытия кода
parametrize - параметризованное тестирование

☺ Особенности реализации:

1. Полное покрытие всех ключевых моделей (Bun, Ingredient, Burger)
2. Тестирование граничных условий и обработки ошибок
3. Независимые тесты с изолированными фикстурами
4. Параметризация для проверки разных сценариев
5. Разделение тестовых данных и логики

☺ Структура проекта:

Diplom_1
│
├── praktikum
│   ├── bun.py
│   ├── burger.py
│   ├── database.py
│   ├── ingredient.py
│   └── ingredient_types.py
├── tests
│   ├── test_bun.py
│   ├── test_ingredient.py
│   ├── test_burger.py
│   └── test_database.py
├── conftest.py
├── data.py
├── praktikum.py
├── requirements.txt
└── README.txt

☺ Запуск тестов:

pytest -v
pytest -cov