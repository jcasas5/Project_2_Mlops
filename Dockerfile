# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy your code and dependencies into the container
COPY requirements.txt /app
COPY Assignment_2.py /app
COPY my_project.py /app


# Install dependencies
RUN pip install -r requirements.txt



# Set the entry point for your script
CMD ["python", "Assignment_2.py"]

