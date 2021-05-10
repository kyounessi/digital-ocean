FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY ./src/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 2345
CMD ["python", "main.py"]