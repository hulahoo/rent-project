#! /bin/sh

>&2 echo 'Rocket Started. Fly...!'

>&2 echo "Postgres running..."


while ! nc -z "$POSTGRES_HOST" "$POSTGRES_PORT"; do
    sleep 0.1
done

echo "PostgreSQL started"

if echo "$PWD" == "app/"
then
    >&2 echo "Configurations running"
    python3 manage.py makemigrations --no-input
    python3 manage.py migrate --no-input

    python3 manage.py runserver 0.0.0.0:8000

else
    echo "Change directory"
fi;

>&2 echo "Running tests"
pytest
sleep 0.5
>&2 echo "Finished"


>&2 echo 'Success...'

exec "$@"