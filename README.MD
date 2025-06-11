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

11. - Удаление товара
    - Выбор цели
      - Bыбор по ближайшему тегу: "hx-target="contests li"
      - Bыбор по ближайшему классу: "hx-target="contests .product-item"
   - Анимации
      - Загрузка ".htmx-request"
      - Замена ".htmx-swapping"

12. - Обновление товара
      - Put запрос
      - Обработка ошибок (форма)

13. - HTMX push url
    - "hx-target='body'"
    - "hx-confirm"
    
14. - Автоматическая подгрузка в бесконечном списке (с анимацией)
    - "hx-trigger='revealed'"