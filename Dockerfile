FROM python:3.9.13-slim-buster
WORKDIR /rss_annotation_tool
COPY requirements.txt /rss_annotation_tool/
RUN pip install -r requirements.txt
COPY . /rss_annotation_tool/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]