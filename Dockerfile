FROM public.ecr.aws/docker/library/python:3.12.1-alpine3.19

WORKDIR /app

COPY . /app

RUN pip install --requirement requirements.txt

CMD ["gunicorn", "-w", "4", "-b", "", "app:app"]
