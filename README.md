### Running Locally

1. clone the repo
1. download and install Docker
1. rename `docker-compose-example.yml` to `docker-compose.yml`
1. update `docker-compose.yml` with your config variables
1. `cd` into project directory and run `docker-compose up -d --build`
1. create admin account with: `docker-compose exec web python manage.py createsuperuser`
1. open project at `localhost:8000`
1. add articles, users, and comments via frontend or at `localhost:8000/admin/`


### Deploying to Heroku
1. Download Heroku CLI
1. `git init`
1. `git add .`
1. `git commit -m "first deploy"`
1. `heroku login`
1. `heroku create appname`
1. `heroku config:set SECRET_KEY=secretkey`
    (do for all, AWS vars, ALLOWED_HOSTS, DEBUG=0, ENVIRONMENT=production, etc)
1. `heroku stack:set container -a appname`
1. `heroku addons:create heroku-postgresql:hobby-dev -a appname`
1. `heroku git:remote -a appname`
1. `git push heroku master`
1. `heroku run python manage.py migrate`
1. `heroku run python manage.py createsuperuser`
1. `heroku open -a appname`
