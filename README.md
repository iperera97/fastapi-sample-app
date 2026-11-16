## FastAPI Sample App

Minimal FastAPI app with an in-memory items store and CRUD endpoints.

### Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run

```bash
uvicorn main:app --reload
```

The app runs at `http://127.0.0.1:8000`.

### Endpoints

- `GET /health` - health check, returns `{"status": "ok"}`
- `GET /items` - list all items
- `GET /items/{id}` - get a single item
- `POST /items` - create an item
- `PUT /items/{id}` - update an item
- `DELETE /items/{id}` - delete an item
