# yoyo_weather
A weather API that returns temperature (min,max,avg and median) forcast in degrees celsius.

## NOTE
* The API uses the public Weather Forecast API. [Click here to view](https://www.weatherapi.com/api-explorer.aspx)

## Getting Started 

* Clone the repository: 

    ```https://github.com/kwanj-k/yoyo_weather.git```

* Navigate to the cloned repo. 

### Prerequisites

```
1. Python3
2. DjangoRest
3. Postman
```

## Installation 
After navigating to the cloned repo;

### Configuration

Create a .env file and add the following

    ```
    source venv/bin/activate
    export DJANGO_SETTINGS_MODULE=yoyo_weather.settings.dev
    export SECRET_KEY=gfhgfhfh
    export WEATHER_API=http://api.weatherapi.com/v1/forecast.json?
    export API_KEY={shared_on_email}
    ```

Create a virtualenv and activate::

    python3 -m venv venv
    source .env

Install the dependencies::

    make install 



## Running Tests
Run:
```
make test
```

### Testing on Postman/Docs
Fire up postman and start the development server by:
  ```
  $  make serve
  ```

To use the docs [click here]( http://127.0.0.1:8000/api/docs/)

### Test endpoint

| EndPoint                                        | Functionality |
|-------------------------------------------------|:-------------:|
| GET      /api/locations/{city}/?days={num_days} | Get Forecast  |