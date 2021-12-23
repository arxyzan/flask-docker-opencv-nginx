# Flask-OpenCV-Docker
Stream IP camera frames in local network using Flask, Docker and OpenCV.

## Overview
this is a simple Flask web app running on top of a Docker container. The app also has Nginx configured which lets users in your local network access the app using your local IP address.

## Requirements
If you want to run the app on docker the only thing you need is Docker-ce and Docker-compose.
follow the official [guide]("https://docs.docker.com/engine/install/ubuntu/") on installing Docker on Ubuntu. 

If you only want to run the python program use the following command to install requirements.

```
cd flask/
pip install -r requirements.txt
```
### Run
Flask web app only: cd to `flask` directory and run the following:

```
python run.py
```
Run the whole thing on Docker and Nginx: cd to the project root directory and run:

```
docker-compose up
```
**Note**: Make sure you change the `CAMERA_STREAM_URL` in docker compose file under Flask service. Default is 0 but webcams are not accessible from a Docker container out of the box! So an RTSP url is required. 

It might take some time to download required docker images and then it will run the containers and you and other users in the local network can access the page on any device. Just type the local IP address of your machine in the browser and that's it! 
