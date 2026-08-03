# magparts-platform

This repository now includes a starter structure for a full-stack platform with:

- a FastAPI backend under backend/
- a Docker Compose setup for backend and PostgreSQL
- a database schema scaffold under database/
- placeholder directories for frontend, bot-max, docs, nginx, and container assets

## Quick start

1. Install Docker and Docker Compose.
2. Copy .env.example to .env if you want to override defaults.
3. Run:

   docker compose up --build

4. Open http://localhost:8000/health to confirm the API is running.

## Project layout

- backend/app: application package for API, auth, database, middleware, models, routers, schemas, services, and utilities
- backend/tests: backend test folder
- database/: SQL schema and migrations
- frontend/: frontend application placeholder
- bot-max/: bot service placeholder
