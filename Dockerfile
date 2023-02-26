FROM python:3.10.2 
#COPY files from the current directory to the container directory /app
COPY . /app
#Set the working directory to /app
WORKDIR /app
#Run the command inside your image filesystem
RUN pip install -r requirements.txt
#Assign the port number to the environment variable PORT
EXPOSE $PORT
#Run the specified command within the container
CMD ["python", "app.py"]