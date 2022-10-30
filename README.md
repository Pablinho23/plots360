# plots360
Project creates plots for 360 grade

1. Activate python venv

source web360/bin/activate (env in gitignore)

2. Launch gunicorn

gunicorn --workers 3 --bind 0.0.0.0:4567 wsgi:app

3. Plots creates from googlesheets by pushing the button

4. Enjoy
