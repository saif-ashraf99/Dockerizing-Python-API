# Building the Image and Running the Container:<br>
To build the Docker image, follow these steps:

### Navigate to the working directory where your Dockerfile is located.

Run the following command to build the Docker image, replacing your_docker_image_name with the desired name for your image:
`docker build -t your_docker_image_name -f Dockerfile .`

* This command creates a Docker image based on the instructions in the Dockerfile.

With the image built, you're ready to run the container:

Run the Docker container with the following command, replacing your_docker_image_name again:

`docker run -d -p 5000:9007 your_docker_image_name`
The -p flag maps port 5000 on your host machine to port 9007 within the container.

If everything is set up correctly, you should get a response when accessing the following URL in your browser:

http://localhost:5000/?url=https://image.shutterstock.com/z/stock-photo-at-o-clock-at-the-top-of-the-mountains-sunrise-1602307492.jpg

The response will be similar to:

{
    "burlywood": 0.1212,
    "cornsilk": 0.0257,
    "darksalmon": 0.229,
    "darkslategrey": 0.0928,
    "indianred": 0.1663,
    "lemonchiffon": 0.021,
    "lightsalmon": 0.0479,
    "navajowhite": 0.0426,
    "rosybrown": 0.097,
    "wheat": 0.0308
}
