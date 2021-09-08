# fastapi-nats
Simple App with both HTTP and NATS endpoints

This App implements an uppercase service that can receive requests via HTTP (with FastAPI) and NATS

## Develompent

###  Create and Activate Virtual Environment

```sh 
$ python3 -m venv .venv
$ . .venv/bin/activate
```

### Install pip-tools

```sh
$ pip install -U pip
$ pip install pip-tools
```

### Install dependencies
```sh
$ make pip_sync
```

### Run the service
```sh
$ make run
```
