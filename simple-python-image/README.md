## Instructions to run the code

1. open favourite terminal
2. see that you are navigated to the folder "simple-python-image"
3. run "docker build -t <"your tag name"> .", this will create docker image
4. follow the instructions taught in workshop once the image is created to run it by creating a container.

## Once the application is running you should see the below log in the terminal
* Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5000
* Running on http://172.17.0.2:5000

## once the server is running follow the below instructions
1. open any web browser
2. hit the url as "http://localhost:5000/"
3. hit the url as "http://localhost:5000/message?data=sample data"
