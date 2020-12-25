### Running Locally

1. clone the repo
1. download and install Docker
1. rename `docker-compose-example.yml` to `docker-compose.yml`
1. update `docker-compose.yml` with your config variables
1. `cd` into project directory and run `docker-compose up -d --build`
1. create admin account with: `docker-compose exec web python manage.py createsuperuser`
1. open project at `localhost:8000`
1. add articles, users, and comments via frontend or at `localhost:8000/admin/`
