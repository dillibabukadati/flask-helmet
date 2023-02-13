# Created by @dillibk777 at 12/02/23
class FlaskHelmet:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        @app.after_request
        def add_security_headers(response):
            # X-Content-Type-Options header prevents browsers from interpreting files as a different MIME type.
            response.headers['X-Content-Type-Options'] = 'nosniff'

            # X-XSS-Protection header enables the Cross-site scripting (XSS) filter in browsers.
            response.headers['X-XSS-Protection'] = '1; mode=block'

            # X-Frame-Options header prevents browsers from displaying the content of the site in a frame.
            response.headers['X-Frame-Options'] = 'DENY'

            # Strict-Transport-Security header enforces secure (HTTPS) connections to the server.
            response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'

            # Content-Security-Policy header specifies the content sources that the browser should load for the page.
            response.headers['Content-Security-Policy'] = "default-src 'self'"

            # Referrer-Policy header specifies the value of the Referer header sent with requests.
            response.headers['Referrer-Policy'] = 'no-referrer'

            # X-Permitted-Cross-Domain-Policies header controls the delivery of Adobe Flash content, including Flash cookies (LSOs).
            response.headers['X-Permitted-Cross-Domain-Policies'] = 'none'

            # X-Download-Options header tells Internet Explorer 8 and later to prevent file downloads from executing.
            response.headers['X-Download-Options'] = 'noopen'

            # X-DNS-Prefetch-Control header controls browser DNS prefetching.
            response.headers['X-DNS-Prefetch-Control'] = 'off'

            # X-Powered-By header identifies the technology used to build the site.
            response.headers['X-Powered-By'] = 'Flask'

            return response
