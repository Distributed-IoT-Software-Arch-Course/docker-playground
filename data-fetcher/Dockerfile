FROM python:3.9-slim-buster

# Copy Application Files & Requirements to /app
COPY ./app /app
COPY requirements.txt /app/requirements.txt

# Set the target container working directory to /app
WORKDIR /app

# Install Python Application Requirements
RUN pip3 install -r requirements.txt

# Python Container Application Configurations
ENV PYTHONPATH "/app/"
ENV PYTHONUNBUFFERED 1

# Run the target application
CMD [ "python3", "data_fetcher.py" ]
