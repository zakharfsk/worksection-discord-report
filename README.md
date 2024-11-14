## Worksection report to discord

Для початку використання треба створити файл `.env` в корені проекту, змінні взяти з файлу `.env.example` та вставити в `.env` і заповнити.

### Де взяти `DISCORD_USER_TOKEN`?
Для цього треба залогінитися в веб discord, відкрити `Інспектор ---> Network`. В списку запросів шукаємо запрос `science` і в заголовках запросу находимо `Authorization`, копіюємо його значення і вставляємо в `DISCORD_USER_TOKEN`.

### Що таке `HEADLESS_MODE`?
Якщо ви хочете, щоб браузер відкривався і ви могли спостерігати за процесом, то встановіть `HEADLESS_MODE=False`, якщо не хочете, щоб браузер відкривався, то встановіть `HEADLESS_MODE=True`.
Якщо ви запускаєте в докері то завжди буде `HEADLESS_MODE=True`.

### Як запустити?
1. Встановити залежності `pip install -r requirements.txt`
2. Встановити браузер `playwright install --with-deps chromium`
3. Запустити `python main.py`

В канал в який хочете відправити репорт прописуєте команду `.report`

Можна запустити в докері: `docker-compose up -d --build`