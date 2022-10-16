pybabel-extract:
	venv/bin/pybabel extract -F babel.cfg -k lazy_gettext -o app/translations/messages.pot .

pybabel-update:
	venv/bin/pybabel update -i app/translations/messages.pot -d app/translations

pybabel-compile:
	venv/bin/pybabel compile -d app/translations
