FROM python:3.10-slim-buster

RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         ca-certificates \
         curl \
         git-lfs \
        python3-dev \
        gcc && \
        apt-get clean \
        && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/app/

RUN pip install --upgrade pip

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH "/opt/app:${PATH}"

COPY . /opt/app/
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
EXPOSE 8082

CMD ["uvicorn", "--host", "0.0.0.0", "--port", "8082", "--workers", "2", "--reload", "wsgi:app"]