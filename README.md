## Caddy Django Demo

A simple Django app to manage golf caddies with create/update/delete from a single page. Built for a quick live demo showing real database connectivity (SQLite by default, optional MySQL).

### Features
- Add, update, and delete `Caddy` records
- Bootstrap UI in `templates/caddy_list.html`
- Admin with search and filters
- Env-based settings; SQLite default, MySQL optional

### Requirements
- Python 3.11+
- pip

### Quick start (SQLite)
```bash
cd /workspace
pip3 install -r requirements.txt
cp -n .env.example .env  # creates .env if missing
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000
```
Open http://localhost:8000

Optional admin user:
```bash
python3 manage.py createsuperuser
```

### Switch to MySQL (for live database demo)
1) Have a reachable MySQL server.
2) Update `.env`:
```
DB_ENGINE=mysql
DB_NAME=caddy_db
DB_USER=youruser
DB_PASSWORD=yourpass
DB_HOST=your.mysql.host
DB_PORT=3306
ALLOWED_HOSTS=localhost,127.0.0.1
```
3) Install driver (already included): PyMySQL is auto-enabled in `caddy_django/__init__.py`.
4) Run migrations:
```bash
python3 manage.py migrate
```

### Demo script (5–7 minutes)
- Home page shows current caddies (empty list initially)
- Add a caddy (name, level, phone, availability)
- Update a caddy inline (level/phone/availability)
- Delete a caddy
- Show Admin: list/search/filter for caddies

### Notes
- Settings pulled from `.env` via python-dotenv
- Default timezone `Europe/Dublin` (override with `TIME_ZONE`)
- For production, set `DEBUG=False`, proper `SECRET_KEY`, and explicit `ALLOWED_HOSTS`
