# 200 - Docker

If you want to use Genesis from Docker, you can first build the Docker image as:

```bash
docker build -t genesis -f docker/Dockerfile docker
```

Then you can run the examples inside the docker image (mounted to `/workspace/examples`):

```bash
xhost +local:root # Allow the container to access the display

docker run --gpus all --rm -it \
-e DISPLAY=$DISPLAY \
-v /tmp/.X11-unix/:/tmp/.X11-unix \
-v $PWD:/workspace \
genesis
```
