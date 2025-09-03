FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

#CMD [ "python", "demo.py" ]

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]