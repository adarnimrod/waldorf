# Waldorf

A Flask and Celery demo app.

## Requirements

- Docker
- Docker Compose

## Usage

Start the application and rebuild if necessary:

```
docker-compose up --build
```

Stop the application:

```
docker-compose down
```

Stop the application and delete volumes (starting from scratch):

```
docker-compose down -v
```

Start a Python interperter inside the Flask web server container:

```
docker-compose exec server python
```

Post a message to the Flask web server for the Celery worker to output:

```
curl -H "Content-Type: application/json" -X post -d '{"message": "foo"}' http://localhost:8080/log
```


## License

This software is licensed under the MIT license (see `LICENSE.txt`).

## Author Information

Nimrod Adar, [contact me](mailto:nimrod@shore.co.il) or visit my [website](
https://www.shore.co.il/). Patches are welcome via [`git send-email`](
http://git-scm.com/book/en/v2/Git-Commands-Email). The repository is located
at: <https://www.shore.co.il/git/>.
