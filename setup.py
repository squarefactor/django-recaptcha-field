from setuptools import setup, find_packages

setup(
    name='django-recaptcha-field',
    version='0.1',
    description='Django recaptcha form field/widget app.',
    long_description = open('README.markdown', 'r').read(),
    author='jordanorelli',
    license='BSD',
    url='https://github.com/jordanorelli/django-recaptcha-field.git',
    packages = find_packages(),
    install_requires = [
        'recaptcha-client'
    ],
    include_package_data=True,
    classifiers = [
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
