FROM python:3
ADD . ~/autocomplete
WORKDIR autocomplete
EXPOSE 80
CMD ["tail","-f","/dev/null"]
#CMD ["python","run_server.py"]



