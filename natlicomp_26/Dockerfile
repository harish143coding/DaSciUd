FROM python:3.8

RUN mkdir /natlicomp

COPY requirements.txt ./natlicomp/requirements.txt

RUN pip3 install -r ./natlicomp/requirements.txt

COPY ./app ./natlicomp/app

WORKDIR ./natlicomp/app

CMD ["python", "main.py"]



