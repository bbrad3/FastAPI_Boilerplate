# FastAPI_Boilerplate
> This repo is meant as a template for future API's built with FastAPI. It is meant to be lightweight for 

> FastAPI uses Uvicorn as an ASGI server, Starlette as an ASGI framework/toolkit, and Pydantic for type annotations. 
## Setup
1. Fork...clone...open repo
1. Create a venv
    - `python3 -m venv venv`
1. Activate venv
    - `source venv/bin/activate`
1. Install dependencies
    - `pip install -r requirements.txt`
1. Start server using
    - `uvicorn main:app --reload`
1. Your done!