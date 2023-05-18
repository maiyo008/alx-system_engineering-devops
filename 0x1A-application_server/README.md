## 0x1A. Application server

## Background Context


Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

## Resources
**Read or watch:**

* [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
* [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04 (As mentioned in the video, do not install Gunicorn using virtualenv, just install everything globally)](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-ubuntu-16-04)
* [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
* [Be careful with the way Flask manages slash in route - strict_slashes](https://werkzeug.palletsprojects.com/en/0.14.x/routing/)
* [Upstart documentation](https://upstart.ubuntu.com/cookbook/)

## Tasks

### Task 0. Set up development with Python
<Details>
Let’s serve what you built for [AirBnB clone v2 - Web framework](https://github.com/maiyo008/AirBnB_clone_v2) on web-01. This task is an exercise in setting up your development environment, which is used for testing and debugging your code before deploying it to production.

Requirements:

* Make sure that task #3 of your SSH project is completed for web-01. The checker will connect to your servers.
* Git clone your AirBnB_clone_v2 on your web-01 server.
* Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
* Your Flask application object must be named app (This will allow us to run and check your code).
Example:
```
Window 1:
ubuntu@229-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
35.231.193.217 - - [02/May/2019 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -
```
Window 2:
```
ubuntu@229-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!ubuntu@229-web-01:~/AirBnB_clone_v2$
```
</Details>