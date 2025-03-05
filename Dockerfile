FROM python:3.13-slim

# Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY . .

RUN pip install --user -r requirements.txt --no-cache-dir

CMD ["/bin/bash"]
