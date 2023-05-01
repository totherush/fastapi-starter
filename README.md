# Demo fastapi-starter
It's a python [fastAPI](https://fastapi.tiangolo.com/) web API.

## Documentation
fastAPI comes with an out of the box openapi doc feature. It's available under:
- http://localhost:8000/docs when you run it locally
- as a json: [openapi.json](https://github.com/BlockSigner/payment-service/blob/main/static/openapi.json) copy & paste it for example to: [https://editor.swagger.io/](https://editor.swagger.io/)

## Requirements
- python version 3.11 installed
- pipenv

## Installation
`pipenv install --dev`

## Run project locally
1. Fill the content from .env.
2. Run `pipenv run uvicorn app.main:app --reload`
3. The server is listen on http://localhost:8000 and has an endpoint ui on: http://localhost:8000/docs

## Configuration tips for VSCode
.vscode/launch.json::
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run & debug",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": ["app.main:app", "--reload"]
    }
  ]
}
```

.vscode/settings.json:
```json
{
  "python.defaultInterpreterPath": "/Users/(your username)/.local/share/virtualenvs/(the created virtualenvs folder)/bin/python",
  "python.envFile": "${workspaceFolder}/.env",
}
```
