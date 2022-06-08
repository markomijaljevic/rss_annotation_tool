# rss_annotation_tool
RSS scraper which saves the feeds to a database and lets users interact with the feed.

# Setup
We need to create a virtual environment with the python version >= 3.9. To create a virtual environment we simply run.

```
python -m venv venv
```
After creating a virtual environment it is necessary to activate it:  

On Windows:
```
. venv\Scripts\activate
```
On Linux:
```
source venv\bin\activate
```

All the requirements necessary for the project to run are located in the requirements.txt file.  
To install requirements run:  
```
pip install -r requirements.txt 
```

After successfully activating the environment and installing all the requirements all we have to do now is to run the Django server:  

```
python manage.py runserver
```

## Pre requisites (docker?)
To be able to run this application inside a docker container, Docker needs to be
installed on the machine. When installed, we can build and run the image using the instructions inside the docker file.


# Run the tests
To run the test suite, simply run:
```
python manage.py test 
```
