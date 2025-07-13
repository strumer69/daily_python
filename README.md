# daily_python
for practicing python

---------------------------------------------------------------------
* 1-calculator : this is a simple program to learn function, Conditional statement (if , elif , ...).
   the pragram can be called from bash by: python 1-calculator.py

  * for dockerizing this proj simply I did the following:
    1- make a directory which include the followng:
    calculator_project/
├── calculator.py
└── Dockerfile

---------------------------------------------------------------------
    2- by (touch Dockerfile) and (nano Dockerfile) write a Docker file which include the following:
# Use official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your calculator script into the container
COPY 1-calculator.py .

# Set the default command to run the calculator
CMD ["python", "1-calculator.py"]

---------------------------------------------------------------------
   3- then simply build you 
   docker build -t calculator-app .

   explanation:
-t stands for tag. You're naming (or tagging) the image as calculator-app. This makes it easier to refer to later when you want to run it (e.g., docker run calculator-app).

. (dot)
This tells Docker to look in the current directory for the Dockerfile and all the files it needs to build the image.

---------------------------------------------------------------------

   4- then it can be used (after cloning) by the following command:
   docker run -it calculator-app
    **explanation**:
docker run
This command tells Docker to start a new container from an image.

-i
This stands for interactive. It keeps the standard input (stdin) open so you can interact with the container (type inputs, like in your calculator).

-t
This stands for tty (teletypewriter). It allocates a pseudo-terminal, which basically means it makes the container's command line behave like a real terminal. This is important for interactive programs.

calculator-app
This is the name (tag) of the Docker image you want to run. It should be the image you built earlier using docker build -t calculator-app .


  
