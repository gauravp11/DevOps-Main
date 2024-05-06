# Use the official Python image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy the source to destination
COPY . .
RUN pip install -r requirements.txt

# Run migrations
RUN python3 manage.py makemigrations about && \
    python3 manage.py migrate about && \
    python3 manage.py makemigrations && \
    python3 manage.py migrate

# Create superuser
RUN python3 manage.py createsuperuser --username admindocker --email admin@admin.com --noinput && \
    echo "from django.contrib.auth.models import User; user = User.objects.get(username='admindocker'); user.set_password('adminpassword'); user.save()" | python3 manage.py shell

# Expose the port that Django runs on
EXPOSE 8000

# Run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
