# Ratestask API

This project is an HTTP-based API that returns the average prices for each day on a route between port codes origin and destination, it also allows you to query for average prices per day between geographic groups of ports.


## Requirements

* Python 3.7 or higher
* Flask 2.2 or higher
* PostgreSQL 9.5 or higher
* Docker 18.09.0 or higher (if you want to use Docker)

## Setup


### 1. Clone the repository
```
git clone https://github.com/ozge-demir/ratestask.git
```  

### 2. Build the Docker image
```
docker build -t ratestask .
```

### 3. Start the Docker container
```
docker run -p 0.0.0.0:5432:5432 --name ratestask ratestask
```
This will start the PostgreSQL and the Flask app containers. The app will be running on http://127.0.0.1:5000/.

### 4. (Optional) Run the tests
Run the following command under project directory:
```
python -m unittest test_app
```

## Usage
You can access the API by sending a GET request to http://127.0.0.1:5000/rates with the following query parameters:

* `date_from`: The start date for the price range, in the format YYYY-MM-DD.
* `date_to`: The end date for the price range, in the format YYYY-MM-DD.
* `origin`: The origin port code or region slug.
* `destination`: The destination port code.


Example Request:

```
curl "http://127.0.0.1:5000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main"

```

This will return a list of average prices for each day on the route between the origin and destination ports, for the specified date range.


## Stopping the application
To stop the application and the containers, simply press `CTRL + C` or `docker kill ratestask` command.


### Caveats
* API does not give the correct output.
* Database connection closes after each request. So, debugger needs a restart.
* Unit tests are not performed since module name cannot be found.

