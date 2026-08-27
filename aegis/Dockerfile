FROM python:3.12-slim
ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
WORKDIR /app
# install deps first for layer caching
COPY pyproject.toml ./
RUN pip install --no-cache-dir -e ".[test]"
COPY . .
# never run as root; agent work is untrusted
RUN useradd -m aegis && chown -R aegis /app
USER aegis
EXPOSE 8000
# async API; agent work offloaded to the worker (KEDA-scaled)
CMD ["uvicorn", "aegis.main:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
