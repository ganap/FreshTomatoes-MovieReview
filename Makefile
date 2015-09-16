clean:
	rm -f freshTomatoes.sqlite

create_database:
	./manage.py syncdb --noinput
	./manage.py migrate --noinput
	./manage.py createsuperuser --username=superuser --email=superuser@freshTomatoes.com --noinput

make_fixtures:
	./manage.py create_users
	./manage.py create_movies

all: clean create_database make_fixtures