FROM python:3
ADD . ~/autocomplete
WORKDIR ~/autocomplete
RUN pip install -r requirements.txt
RUN python setup.py install
EXPOSE 5000
CMD ["python","start_server.py"]

