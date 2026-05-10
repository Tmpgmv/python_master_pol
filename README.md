# Санкт-Петербургское государственное бюджетное профессиональное образовательное учреждение "Политехнический колледж городского хозяйства"

## 09.02.07 Информационные системы и программирование (Программист)

---

## Экзаменационная работа `Мастер пол`
Выполнил: Граблевский Михаил Владимирович

Напольные покрытия


## Создание виртуального окружения
```bash 
python -m venv .venv
```

## Активация виртуального окружения
```bash 
.venv\Scripts\activate  # Windows

source .venv/bin/activate # Linux/MacOS
```

## Установка зависимостей
```bash 
pip install --no-index --find-links=D:\dependencies -r requirements.txt
```

## Применение миграций
```bash
python manage.py migrate
```

## Создать суперпользователя (по необходимости)
```bash
python manage.py createsuperuser
```

## Создать пользователей
```bash
python manage.py createusers
```


## Запуск сервера
```bash
python manage.py runserver
```

## Выполнение тестов
```bash
python manage.py test
```

