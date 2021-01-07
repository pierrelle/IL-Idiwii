FROM python:3.7-slim-buster
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN python3 -m spacy download fr_core_news_sm
CMD python Server.py