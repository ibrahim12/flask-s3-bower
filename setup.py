"""
Flask-S3
-------------

Easily serve your static files from Amazon S3 and also provision for using Bower.
"""
from setuptools import setup

setup(
    name='Flask-S3-Bower',
    version='0.2',
    url='https://github.com/ibrahim12/flask-s3-bower',
    license='GNU',
    author='Ibrahim Rashid',
    author_email='irashid.com@gmail.com',
    description='Seamlessly serve the static files of your Flask app from Amazon S3 and also use bower for development',
    long_description=__doc__,
    packages=['flask_s3_bower',],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
        'Boto>=2.5.2'
    ],
    download_url = 'https://github.com/ibrahim12/flask-s3-bower/tarball/0.2'
    tests_require=['nose', 'mock'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
