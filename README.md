# Multiple Dev Containers

[connect-multiple-containers](https://code.visualstudio.com/remote/advancedcontainers/connect-multiple-containers)

Template repo for developing multiple services in isolated Dev Containers within one project, orchestrated by Docker Compose. Included examples:
- Backend: FastAPI (`backend/`)
- Frontend: node (`frontend/`)

## Project structure
- `docker-compose.yaml`: Defines per-service build contexts, shared volume mount (`.:/app`), and a dedicated `frontend_modules_volume` cache.
- `backend/`: FastAPI sample (`/hello`), Python 3.12 image with `uv` for dependency management.
- `frontend/`: Node LTS base image.
