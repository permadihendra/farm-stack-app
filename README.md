# farm-stack-docker
FARM Stack Docker: developing stack with FastAPI, React Js, and MongoDB


# Build the fastapi docker
1. Build the fastapi image
```
docker build -t fastapi -f Dockerfile.fastapi .
```
2. Run the fastapi docker and make editable
```
docker run --name fastapi -p 8000:8000 -v "$(pwd):/app" fastapi
```
