FROM python:2.7-slim-buster

RUN apt-get update -qq && apt-get install -qq \
  build-essential \
  git

# Set the working directory
WORKDIR /app

# Improve cache invalidations by only running pip/npm if requirements have indeed changed
COPY requirements.txt .
RUN pip install -r requirements.txt

# Application source code
COPY . .

# Expose ports
EXPOSE 8000

# Setup entrypoint permissions and run it!
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "s_francesinhas.wsgi:application"]
