FROM python:latest

COPY search.py config.txt req.txt /tmp/

RUN pip3 install -r /tmp/req.txt

CMD ["python3", "/tmp/search.py"]