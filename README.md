# Hood
This web application that allows users to be in the loop about everything happening in their neighborhood. From contact information of different handyman to meeting announcements or even alerts.

[Live Demo](https://mtaaniii.herokuapp.com/)

## Author
[Joseph Kahiga](https://github.com/kahiga2244)

## User Stories
User would like to:

- Sign in with the application to start using.
- Set up a profile, a general location ,neighborhood name.
- Find a list of different businesses in  neighborhood.
- Find Contact Information for the health department supermarkets and Police authorities near Neighborhood.
- Create Posts that will be visible to everyone in neighborhood.
- Change Neighborhood when moving out.
- Only view details of a single neighborhood.

## Installation and Usage Guide:
- Python 3.6.9

- Pip

- Django

- Virtual enviroment

- Cloudinary

### Clone the application 
    $ git clone https://github.com/kahiga2244/django-project3.git
    $ cd hood

### Run the application
- Install virtual environment using 

      $ virtualenv env

- Activate virtual environment using 

      $ . env/bin/activate

- Install all the dependencies from the requirements.txt file by running 

      $python3 pip install -r requirements.txt

- Create a database and edit the database configurations in settings.py to your own credentials.

- Make migrations

      $ python manage.py makemigrations app=hood
      $ python manage.py migrate 
    
- To run the application, in your terminal

      $ python manage.py runserver
      
## Bugs
There are no know bugs at the moment