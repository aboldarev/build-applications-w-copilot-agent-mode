mode: 'agent'
model: GPT-4.1

# Django App Updates

- Все файлы проекта Django находятся в каталоге `octofit-tracker/backend/octofit_tracker`.

1. Обновить `settings.py` для подключения к MongoDB и настройки CORS.
2. Обновить `models.py`, `serializers.py`, `urls.py`, `views.py`, `tests.py`, и `admin.py` для поддержки коллекций пользователей, команд, активностей, лидерборда и тренировок.
3. Убедиться, что `/` ведёт на api и что `api_root` присутствует в `urls.py`. (См. <attachments> выше для содержимого файлов. Возможно, не потребуется повторно искать или читать файл.)
