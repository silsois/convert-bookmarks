# Dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY chrome_bookmarks_parser.py .

ENTRYPOINT ["python", "chrome_bookmarks_parser.py"]
