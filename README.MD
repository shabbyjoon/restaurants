# Restuarants API

A simple application that utilizes a REST API to create, retrieve and delete restaurant records

## Overview
This application utilizes Flask to run a server and implement endpoints. A Restaurants class holds our GET and POST methods
and would include PUT and DELETE methods. For the sake of time, SQLite queries were included within our API methods. Our
Restaurants database includes a restaurants table with the required columns, as well as additional columns (address, phone_number,
takeout, delivery, menu) that can be utilized in the future. For the restaurant ID, we utilize SQLite ROWID as it provides an auto-incrementing
unique ID.

## Requirements

- [Python3] (https://www.python.org/downloads/)
- [SQLite] (https://www.sqlite.org/download.html)



## Installation

1) Download the zip file and navigate to the root directory.
2) To make shell script executable, run
    ```bash
    chmod +x install_restaurants_app.sh
    ```
3) To initalize database, install dependencies and configue environment, run
    ```bash
    ./install_restaurants_app.sh
    ```
4) To start server, run
    ```bash
    python3 server.py


## API Commands

- To get all restuarants
    ```bash
    curl http://127.0.0.1:5000/restaurants 
    ```
- To add a new restaurant, run
    ```bash
    curl -X POST -F name="{RESTAURANT NAME}" -F opening_time="{HH:MM:SS}" -F closing_time="{HH:MM:SS}" http://127.0.0.1:5000/restaurants 
    ```

## Next Steps

For the existing methods, I'd add validation for all the possible fields (ex address, takeout, delivery etc) and specific validation 
around the types of inputs (ie names can only contain alphanumeric letters, phone numbers would need to be 7 digits, validate real addresses). I'd also add error handling around the SQlite connection (ie if the connection could not be estabilished) and add day-of-the-week checking for the is_open flag. I'd implement PUT and
DELETE methods with error handling for a fully functional experience. I'd decouple SQLite queries into it's own file (ex database_helpers.py) and import those into the server file for more modular code. I'd upgrade the server to a production-ready server like NGINX, as its a development server in it's current state. I'd also write unit tests for each REST method.