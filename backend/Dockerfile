FROM python:3.12-slim
# FROM python:3.12-slim-trixie

# The installer requires curl (and certificates) to download the release archive
RUN apt-get update && apt-get install -y --no-install-recommends curl ca-certificates net-tools git

# Download the latest installer
ADD https://astral.sh/uv/install.sh /uv-installer.sh

# Run the installer then remove it
RUN sh /uv-installer.sh && rm /uv-installer.sh

# Ensure the installed binary is on the `PATH`
ENV PATH="/root/.local/bin/:$PATH"
WORKDIR /app

COPY pyproject.toml ./
RUN uv lock
# RUN pip install -r requirements.txt
RUN uv sync
COPY . .

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
