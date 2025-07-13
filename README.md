

# daily\_python

A simple collection of Python practice projects.

---

## 1-calculator

This is a simple Python program to learn about:

* Functions
* Conditional statements (`if`, `elif`, etc.)

You can run the program from the terminal using:

```bash
python 1-calculator.py
```

---

## Dockerizing the Calculator Project

You can also run this project in a Docker container.

### Step 1: Project Structure

Create a directory with the following contents:

```
calculator_project/
├── 1-calculator.py
└── Dockerfile
```

### Step 2: Dockerfile Content

Create a Dockerfile using `touch Dockerfile`, then open it with a text editor (`nano Dockerfile`) and paste the following content:

```dockerfile
# Use official Python base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy your calculator script into the container
COPY 1-calculator.py .

# Set the default command to run the calculator
CMD ["python", "1-calculator.py"]
```

---

### Step 3: Build the Docker Image

Run the following command in your terminal:

```bash
docker build -t calculator-app .
```

#### Explanation:

* `-t calculator-app` — Tags the image with the name `calculator-app`.
* `.` — Uses the current directory (which should contain the Dockerfile and `1-calculator.py`) as the build context.

---

### Step 4: Run the Docker Container

Once the image is built, you can run it using:

```bash
docker run -it calculator-app
```

#### Explanation:

* `docker run` — Tells Docker to start a container.
* `-i` — Keeps the input open so you can interact with the program.
* `-t` — Allocates a terminal so input/output behaves like a real console.
* `calculator-app` — The name of the image to run.


