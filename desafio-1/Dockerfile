FROM python:2.7

COPY ["Dockerfile", "main.py", "requirements.txt", "/app/"]

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

EXPOSE 5000

CMD ["main.py"]