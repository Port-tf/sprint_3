# sprint_3
##### Материалы для вебинара

## 1 Часть
##### Шаблон base.html, include, extends, block

### Шаблоны:
base_base.html - неразнесенный html\
base1.html - подключены инклюды(head.html, header_1.html, footer.html), применяется для index_1.html\
base2.html - подключены инклюды(head.html, header_2.html, footer.html), применяется для index_2.html\
index_1.html - имеет три block, содержимое блоков подключено через инклюды из
папки posts/poems/. Блоки специально переданы в хаотичном порядке\
index_2.html - имеет один пустой блок, вывод - дефолтная строка\

### url:
b1/ - обрабатывается view index_1, рендерится шаблон index_1.html без контекста\
b2/ - обрабатывается view index_1, рендерится шаблон index_2.html без контекста\
default/ - обрабатывается view default, возвращает HttpResponse:\
простая передача строки с какой-то информацией

## 2 Часть 
### Модели и База данных
models.py\
Модели Poem и Author (поля, связи, атрибуты)\
admin.py\
Админка\

## 3 Часть
### urls.py, views.py
_В шаблоне base2.html заменить инклюд с header_2.html на header_3.html_
### Урлс базовый, урлс приложения, аргументы в адресе, вьюс приложения, ORM, basename и name

/ - обрабатывается view poems, рендерится шаблон posts/poems.html c контекстом (все произведения)

poems/<str:web_name>/ - аргумент web_name = name_url модели Author, обрабатывается view poem_author,
рендерится шаблон posts/poem_author.html c контекстом (все произведения автора)

poem/<int:argument_id>/ - аргумент argument_id = pk модели Poem, обрабатывается view post_detail,
рендерится шаблон posts/poem_author.html c контекстом (выбранное произведения автора)

users/<str:user_name>/ - аргумент user_name = username модели User, обрабатывается view poem_user,
рендерится шаблон posts/poem_user.html c контекстом (все произведения добавленные пользоваетлем)

biorafy/<str:name>/ - аргумент name = name модели Biografy, обрабатывается view biografy,
рендерится шаблон posts/biografy.html c контекстом (биография автора, последние добавленное произведение автора)

### Бонус:
Примеры запросов с использованием related_name во вью-функции и в шаблоне
