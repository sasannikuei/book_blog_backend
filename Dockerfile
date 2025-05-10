FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=backend.settings.dev

WORKDIR /django

COPY requirements.txt /django/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /django/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


