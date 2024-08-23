FROM python:latest
COPY main.py /
ENTRYPOINT ["python", "main.py"]