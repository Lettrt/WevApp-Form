# WevApp-Form
Web application for identifying completed forms

# Запуск проекта через докер
Установка виртуального окружения
```angular2htm
python3 -m venv venv
```
Активация виртуального окружения
```bash
source venv/bin/activate
```
Установка зависимостей
```bash
pip install -r requirements.txt
```
Так же понадобится создать файл .env
```env
MONGODB_URL=mongodb://mongo:27017/forms_database
```
Запуск docker контейнера:
```bash
docker-compose up --build -d
```
Проверка скрипата на post запрос:
- узнать id контейнера
```bash
docker ps
```
- запустить скрипт
```bash
docker exec -it [id контейнера] python3 app/scrt.py
```
# ОПИСАНИЕ ПРОЕКТА И ИСПОЛЬЗОВАННЫЕ РЕШЕНИЯ.
- Проект реализован с помощью FastAPI
- База данных - Mongodb
- Тесты написаны на pytest, находяться в файле test_.py.
