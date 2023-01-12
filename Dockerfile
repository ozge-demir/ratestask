FROM  postgres:12
COPY rates.sql /docker-entrypoint-initdb.d/
EXPOSE 5432
ENV POSTGRES_PASSWORD=ratestask

FROM python:3.7

# set the working directory
WORKDIR .

# copy the requirements file
COPY requirements.txt .

# install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# copy the application code
COPY . .

# expose the port
EXPOSE 5000

# run the command
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]