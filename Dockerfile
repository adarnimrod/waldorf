FROM python:3.8
WORKDIR /opt/waldorf
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY *.py ./
USER nobody
