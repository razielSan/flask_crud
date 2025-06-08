1. Инициализация Flask приложения

2. Установка HTMX

3.  - Ping
        - on click
        - on ctrl + click
    - Hover
    - HTMX
        - 'hx-trigger="mouseenter"'
        - 'hx-trigger="click[ctrlKey]"'
        - 'hx-swap="outerHTML"'

4. - Clicker via HTMX

5. - Embed clicker into index via HTMX

6. - Handle HTMX boost

7. - Список товаров
   - Создание через форму

8. - Создание через HTMX форму + подгрузка списка
   - Добавление через 'hx-swap="beforeend"' 
   - Обработка out of band элеметнов
   - Использование "hx-swap='none'"
   - Возвращение нескольких кусков для замены: форма и ооb-item

9. - Добавление CSRF (из Flask-WTF) защиты   
   - Обработка фориы Flask-WTF для добавления товара

10. - Добавлние заголовка 'hx-headers'
    - CSRF exempt 