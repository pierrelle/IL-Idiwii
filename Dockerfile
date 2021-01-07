FROM python:3.7-alpine
RUN apk update && apk add gcc libc-dev make git libffi-dev openssl-dev python3-dev libxml2-dev libxslt-dev 
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 -m spacy download fr_core_news_sm
EXPOSE 5000
CMD python ModelServing.py