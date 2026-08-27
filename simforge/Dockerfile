# SIMFORGE simulation image
FROM python:3.11-slim
WORKDIR /app
ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1
COPY aegis /app/aegis
COPY causa /app/causa
COPY simforge /app/simforge
COPY simforge/requirements.txt /app/simforge/requirements.txt
COPY evalforge /app/evalforge
COPY run-replay /app/run-replay
COPY agent-sentinel /app/agent-sentinel
RUN pip install --no-cache-dir -r /app/simforge/requirements.txt
RUN pip install --no-cache-dir --no-deps /app/aegis /app/causa /app/simforge /app/evalforge /app/run-replay /app/agent-sentinel
EXPOSE 8002
CMD ["uvicorn", "simforge.server:create_app", "--factory", "--host", "0.0.0.0", "--port", "8002"]
