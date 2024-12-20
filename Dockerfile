FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements and install them
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Install ngrok configuration manually
RUN mkdir -p /root/.ngrok2 && echo "authtoken: ${NGROK_AUTH_TOKEN}" > /root/.ngrok2/ngrok.yml

# Expose the port for Streamlit
EXPOSE 8501

# Command to run your app
CMD ["streamlit", "run", "app.py"]
