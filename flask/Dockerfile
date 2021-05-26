# Use the Python3.7.2 image
FROM python:3.7.2

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
ADD . /app

RUN apt-get update
RUN apt-get install 'libgl1-mesa-dev' -y
# Install the dependencies
RUN pip install -r requirements.txt

# run the command to start uWSGI
CMD ["uwsgi", "app.ini"]
