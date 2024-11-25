FROM python:3.10

RUN pip install -U pip
RUN pip install pipenv 

WORKDIR  /app

COPY ["Pipfile", "Pipfile.lock","./"]

RUN pipenv install --system --deploy --verbose

COPY ["predict.py","model.bin", "scaler.bin","./"]

EXPOSE 9696

ENTRYPOINT [ "gunicorn","--bind=0.0.0.0:9696","predict:app"]