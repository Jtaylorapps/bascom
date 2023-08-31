FROM python

WORKDIR /opt/project/
COPY /app .

RUN pip install -r requirements.txt

ENTRYPOINT python app.py
