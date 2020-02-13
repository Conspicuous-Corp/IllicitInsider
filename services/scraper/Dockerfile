FROM python:3.7

RUN apt-get update
RUN pip3 install --upgrade pip

WORKDIR services/scraper

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 8081

ENTRYPOINT ["python"]

CMD ["scraper.py"]