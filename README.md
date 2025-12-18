# py-realworld-backend

A FastAPI backend implementation of the RealWorld (Conduit) API.

## Tech Stack
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- JWT authentication

## Run
```bash
pip install -r requirements.txt
cp .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

## API Docs
- http://127.0.0.1:8000/docs


