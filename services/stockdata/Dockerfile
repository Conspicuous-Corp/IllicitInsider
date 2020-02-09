FROM python:3.7

RUN apt-get update
RUN pip3 install --upgrade pip

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8082

ENTRYPOINT ["python"]

CMD ["stockdata.py"]