FROM python:3.8
RUN pip install --upgrade pip
COPY . . 
RUN python -m venv venv
RUN pip install -r requirements.txt
CMD ["python", "-m", "src.main"]