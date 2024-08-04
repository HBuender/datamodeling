# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.13.0b4-slim

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /bpf


# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY . bpf
WORKDIR /bpf

EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "./manage.py"]
CMD ["runserver", "0.0.0.0:8000"]