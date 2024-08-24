# Base image for Python
FROM python:3.9-slim

# Install required Python packages and curl
RUN pip install requests && \
    apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Copy the fuzz test script into the container
COPY fuzz_test.py /fuzz_test.py
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Set the working directory
WORKDIR /

# Run the fuzz test script
CMD ["/wait-for-it.sh", "http://msvc-cursos:8002/cursos", "--", "python", "/fuzz_test.py > /logs/fuzz_test_log.txt 2>&1 && sleep infinity"]
