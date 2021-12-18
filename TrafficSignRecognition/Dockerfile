FROM python:3.9
LABEL Developers="Nitish Ranjan,Akshay Sharma,Vyoman Jain,Aman Kumar Singh"
WORKDIR /trafficsign
COPY . /trafficsign
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python","manage.py","runserver","0.0.0.0:8000"]