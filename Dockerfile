FROM python:3
ADD . ~/autocomplete
WORKDIR autocomplete
EXPOSE 80
CMD ["python","setup.py","install"]
CMD ["python","run_server.py"]


