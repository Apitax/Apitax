# Use Ubuntu 18.04
FROM tiangolo/uwsgi-nginx-flask:python3.6

# Update repo listings
RUN apt-get update

# Install system level things
RUN apt-get -y install git pandoc

RUN apt-get -y install build-essential

# Set the working directory to /app
WORKDIR /app

# Get pip setup
RUN pip install wheel setuptools

# Install Apitax
RUN pip install apitax==2.2.16 --no-cache

RUN cd /app && touch __init__.py
RUN cd /app && touch project.py
RUN cd /app && touch config.txt

COPY main.py /app/main.py

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 443

