FROM python:3.10.6
RUN mkdir /usr/src/app/
COPY . /app/
WORKDIR /app/
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["pexon.py"]