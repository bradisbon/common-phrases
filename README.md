# Setup
BEFORE COMMITTING README Test with older versions of python 
## Requirements
- Python 3.8 or newer
- pip3 (should already be installed if you have Python 3.4 or newer)
- venv (should already be installed if you have Python 3.3 or newer)
- curl (optional)

## Installation
1. Clone repo
```bash
git clone https://github.com/bradisbon/common-phrases
```
2. cd into project
```bash
cd common-phrases
```
3. Create virtualenv in project and activate it
```bash
python3 -m venv .venv
source ./.venv/bin/activate
```
4. Install dependencies
```bash
pip install -r requirements.txt
```

# Usage

## Running Tests
Since pytest is installed as a dependency, you only need to run pytest to run all the tests:
```bash
pytest
```

## Starting the server
Uvicorn is an ASGI server that talks to the Python application. To run it:
```bash
uvicorn common_phrases.main:api
```

## Making a request
I'm using curl here but you could also do this from within python or with something like Postman
```bash
curl -X POST http://127.0.0.1:8000/find_common \
-H 'Content-Type: application/json' \
-d '{"text":"a b c! A\nB C"}'
```

You should get back the following response body:
```json
{"most_common":["a b c","b c a","c a b"]}
```
