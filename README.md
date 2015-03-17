Flask-S3-Bower
========

Seamlessly serve the static assets of your Flask app from Amazon S3 and Support for Bower without modifying your template.

Flask-Bower needs template changes as you need to use ** bower_url_for **, but in Flask-S3-Bower you don't have to do that. 

Enable Bower support in your app settings by setting 

```
USE_BOWER = True

```

- **Flask-S3** allows you to easily serve all your `Flask`_ application's
static assets from `Amazon S3`_, without having to modify your
templates.


-  **Flask-Bower** allows you to server static files using bower, but you need to modify you template.

Merging and modifying the functionality from both repository, 

In **Flask-S3-Bower** you don't have to modify the templates. Use defualt ``url_for`` for serving file from both s3, bower and default static folder. 

.. _Amazon S3: http://aws.amazon.com/s3
.. _Flask: http://flask.pocoo.org/


How it works
============

Flask-S3-Bower has two main functions:

 1. Walk through your application's static folders, gather all your
    static assets together, and upload them to a bucket of your choice
    on S3;
    It also includes ``BOWER_COMPONENTS_ROOT`` folder if it is placed outside static folder via 
    ``BOWER_COMPONENTS_ROOT``  in settings;

 2. Replace the URLs that Flask's :func:`flask.url_for` function would
    insert into your templates, with URLs that point to the static
    assets in your S3 bucket.

The process of gathering and uploading your static assets to S3 need
only be done once, and your application does not need to be running for
it to work. The location of the S3 bucket can be inferred from Flask-S3
`settings`_ specified in your Flask application, therefore when your
application is running there need not be any communication between the
Flask application and Amazon S3.

Internally, every time ``url_for`` is called in one of your
application's templates, `flask_s3.url_for` is instead invoked. If the
endpoint provided is deemed to refer to static assets, then the S3 URL
for the asset specified in the `filename` argument is instead returned.
Otherwise, `flask_s3.url_for` passes the call on to `flask.url_for`.

By default in production mode it will use S3 ``url_for``, and in development mode 
with ``USE_BOWER=True`` has set, it will use bower ``url_for``.


Installation
============

If you use pip then installation is simply::

    $ pip install flask-s3-bower

or, if you want the latest github version::

    $ pip install git+git://github.com/ibrahim12/flask-s3-bower.git

You can also install Flask-S3 via Easy Install::

    $ easy_install flask-s3-bower


Documentation
-------------
Flask-S3-Bower documentaion will be found in [here](https://flask-s3-bower.readthedocs.org/en/latest/).


Maintainers
-----------

Flask-S3-Bower is maintained by @ibrahim12
