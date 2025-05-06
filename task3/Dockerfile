FROM python:latest

COPY search.py config.txt req.txt .

RUN pip3 install -r req.txt

CMD ["python3", "./search.py"]