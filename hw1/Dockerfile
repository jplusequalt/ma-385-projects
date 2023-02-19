# Install base requirements to run the project
FROM python:3.11.2

# Install python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python", "main.py" ]
