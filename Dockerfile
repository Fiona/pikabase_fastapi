FROM python:3.8 as base
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app

# Install system requirements
RUN apt-get update && apt-get install -y python3 python3-pip postgresql-client curl

# Upgrade pip
RUN pip3 install -U pip

# Move requirements file
COPY requirements.txt /app/

# -----------------
# Development build target
# -----------------
FROM base as dev

EXPOSE 8000

RUN pip3 install -r requirements.txt

COPY ./ /app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
