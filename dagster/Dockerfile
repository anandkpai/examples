# Dagster’s official user-code base image
FROM dagster/user-code-example:1.12.1

# Set working directory
WORKDIR /workspace

# Copy your dagster code
COPY code ./dagster

# If hello.py uses ANY libs (pandas, requests, etc.)
# Add them here:
# RUN pip install --no-cache-dir pandas

# Start the Dagster user code server
CMD ["dagster", "api", "grpc", "--host", "0.0.0.0", "--port", "3030", "--python-file", "/workspace/dagster/hello.py"]
