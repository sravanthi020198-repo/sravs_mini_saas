# Issues & Insights Tracker

A mini SaaS portal to collect, triage, and analyze file-based feedback (issues, bugs, invoices, etc.) with real-time updates, RBAC, analytics, and modern dev-ex.

---

## Features

- **Auth**: Email/password & Google OAuth (JWT, extendable).
- **RBAC**: ADMIN, MAINTAINER, REPORTER roles (API & UI enforcement).
- **Issue CRUD**: Markdown, file upload, severity, status workflow.
- **Realtime**: WebSocket/SSE for live updates.
- **Dashboard**: Chart of open issues per severity.
- **Background job**: Worker aggregates daily stats.
- **API docs**: Swagger at `/api/docs`.
- **Tests**: ≥80% coverage, E2E via Playwright.
- **CI**: GitHub Actions for lint, test, build, migrations.
- **Observability**: Prometheus metrics, structured logging.

---

## Quickstart

```sh
git clone https://github.com/YOURUSER/sravs-mini-saas.git
cd sravs-mini-saas
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend: http://localhost:8000/api/docs
- DB: Postgres 15+ (see `docker-compose.yml`)
- Default users: `admin@example.com`, etc.

---

## Architecture

- **Frontend**: SvelteKit + Tailwind, SSR, chart.js, role-based UI.
- **Backend**: FastAPI, SQLAlchemy, Alembic, JWT auth, file upload, Celery, Prometheus.
- **DB**: Postgres 15+, Alembic for migrations.
- **Worker**: Celery, aggregates issue stats every 30min.
- **Tests**: Pytest/unittest for backend, Playwright for E2E.

---

## Trade-offs & Future Improvements

- Google OAuth is stubbed; extend for production.
- File uploads are on-disk; S3 support is ready to add.
- RBAC is enforced in both router and UI.
- Add dark mode, PDF/image preview (bonus).
- For prod: HTTPS, secrets management, deploy e.g. Fly.io.

---

## Usage of Generative Tools

This project used GitHub Copilot and ChatGPT for code scaffolding, API and UI boilerplate, and best practice references. Full chat logs are available upon request.

---

## License

MIT
