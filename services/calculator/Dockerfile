FROM python:3.7

RUN apt-get update
RUN pip3 install --upgrade pip

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install -U flask-cors

EXPOSE 8083

ENTRYPOINT ["python"]

CMD ["calculator.py"]