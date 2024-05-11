## Домашняя работа
### 20.2 Шаблонизация в Django

1. Для подключения к БД внесите правильные значения в поля _NAME_, _USER_, _PASSWORD_ параметра __'default'__ секции __DATABASES__ в файле __config/settings.py__
2. Выполните миграции командой: ___python3 manage.py migrate___
3. Создайте суперпользователя для входа в панель администратора: ___python3 manage.py createsuperuser___
4. Выполните команду заполнения БД: ___python3 manage.py fill_db___
5. Запустите сервер командой ___python3 manage.py runserver___ и в браузере откройте страницу с адресом: __http://127.0.0.1:8000__ (или другую, в соответствии с вашими параметрами запуска сервера)


В задании 4 шаблонный тег __url_media_tag__ применён в шаблоне _catalog/main.html_, а шаблонный фильтр __url_media_filter__ в шаблоне _catalog/product_detail.html_
