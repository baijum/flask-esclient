from setuptools import setup, find_packages

with open('README.rst') as fd:
    long_description = fd.read()

setup(name='Flask-ESClient',
    version='0.1.1',
    description='Flask extension for ESClient (elasticsearch client)',
    long_description=long_description,
    author='Baiju Muthukadan',
    author_email='baiju.m.mail@gmail.com',
    url='https://github.com/baijum/flask-esclient',
    py_modules=['flask_esclient',
                'test_flask_esclient'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'Flask',
        'ESClient',
    ],
    test_suite='test_flask_esclient.suite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
    )
