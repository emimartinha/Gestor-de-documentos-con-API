# Document Management API

This project is a document/client management system built with FastAPI. It allows basic CRUD operations (Create, Read, Update, Delete) through a REST API, while also supporting a terminal-based interface.
The project demonstrates backend development concepts such as API design, data validation, file-based persistence, and modular architecture.

## Features

* REST API built with FastAPI
* Data validation using Pydantic
* Client management (create, list, search, delete)
* CSV-based data persistence
* Input validation (DNI format and uniqueness)
* Terminal interface for manual interaction
* Automatic API documentation with Swagger

## Technologies Used

* Python 3.13
* FastAPI
* Uvicorn
* Pydantic
* Pytest
* Requests
* Poetry


## API Endpoints

### Get all clients

```http
GET /clientes/
```

### Search client by DNI

```http
GET /clientes/buscar/{dni}
```

### Create a new client

```http
POST /clientes/crear/
```

Body example:

```json
{
  "dni": "123",
  "nombre": "Juan",
  "apellido": "Perez"
}
```

### Delete a client

```http
DELETE /clientes/borrar/{dni}/
```

## Data Storage

Client data is stored in a CSV file:

* `clientes.csv`

This allows simple persistence without requiring a database.

## Testing

Run tests using pytest:

```bash
pytest
```

A separate test database is used:

* `tests/clientes_test.csv`

## Author

Emiliano Martinha
Email: [emimartinha@gmail.com](mailto:emimartinha@gmail.com)
