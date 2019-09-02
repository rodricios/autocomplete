#FROM python:3
#ADD . ~/autocomplete
#WORKDIR ~/autocomplete
#RUN pip install -r requirements.txt
#RUN python setup.py install
#EXPOSE 8080
#CMD ["python","start_server.py"]

# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /app

# add the current directory to the container as /app
ADD . /app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 80 for the Bottle app to run on
EXPOSE 80

# execute the Flask app
CMD ["python", "app.py"]
