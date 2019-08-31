FROM python:3
ADD . ~/autocomplete
WORKDIR ~/autocomplete
#CMD ["tail","-f", "/dev/null"]
#CMD ["pip3","install","bottle"]
CMD ["python","setup.py","install"]
CMD ["python","start_server.py"]
EXPOSE 8080

