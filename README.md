# Flask-Helmet

[![PyPI version](https://badge.fury.io/py/flask-helmet.svg)](https://badge.fury.io/py/flask-helmet)

Flask-Helmet is a Flask extension that makes it easy to add security headers to your HTTP responses. The goal of this project is to help you build more secure web applications by providing a simple and flexible API for adding headers that improve the security of your application.

## Installation
You can install Flask-Helmet using pip:
```
pip install flask-helmet
```

## Usage

To use Flask-Helmet in your Flask application, you need to do the following:

Import the extension:

```python
from flask_helmet import FlaskHelmet
```
Initialize the extension:
```python
helmet = FlaskHelmet()
helmet.init_app(app)
```
# Headers
Flask-Helmet supports the following headers: \
`X-XSS-Protection`: This header is used to configure the browser's XSS \
`X-Content-Type-Options`: This header is used to prevent browsers from interpreting files as a different MIME type.\
`Content-Security-Policy`: This header is used to control the resources that a browser is allowed to load for a given page. \
`X-Frame-Options`: This header prevents browsers from displaying the content of the site in a frame. \
`Strict-Transport-Security`: This header enforces secure (HTTPS) connections to the  server.  
`Referrer-Policy`: This header specifies the value of the Referer header sent with requests. \
`X-Permitted-Cross-Domain-Policies`: This header controls the delivery of Adobe Flash content, including Flash cookies (LSOs). \
`X-Download-Options`: This header tells Internet Explorer 8 and later to prevent file downloads from executing. \
`X-DNS-Prefetch-Control`: This header controls browser DNS prefetching. \
`X-Powered-By`: This header identifies the technology used to build the site. 
                
For more information on the headers supported by Flask-Helmet, see the [official documentation.](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers)


## Contributing
If you want to contribute to Flask-Helmet, you can do so by submitting a pull request on Github. Before submitting your pull request, be sure to run the tests and make sure that your code follows the [PEP 8 style guide.](https://www.python.org/dev/peps/pep-0008/)

1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and write tests for them.
4. Submit a pull request.

## License
Flask-Helmet is released under the MIT License. See the LICENSE file for more information.

We welcome contributions to this library. If you have an idea for a new feature or have found a bug, please open an issue on Github.

## Buy me a Coffee
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/dillibabukadati)

