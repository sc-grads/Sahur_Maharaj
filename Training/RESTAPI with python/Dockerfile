FROM python:3.11.2
EXPOSE 5000
RUN pip install flask
WORKDIR /RESTAPI with python
COPY . .
CMD ["flask", "run", "--host", "0.0.0.0"]

