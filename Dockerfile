FROM python:3.9-slim

WORKDIR /usr/src/app

COPY newmain.py .
COPY unittest2.py .

CMD [ "python", "newmain.py" ]
