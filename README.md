# recipe-app-api
Recipe api source code

## Source code for Backend REST API with Python and Django - Advanced

### Learning from The Course:
  1. Python
  2. Django/Django-Rest Framework
  3. Docker / Docker-compose
  4. Test Driven Development.
 
 ### Additional learning:
  1. Set up Project Using Docker.
  2. Configure flake8
  3. Create endpoints for managing Users and recipe list and ingredients Lists.
  4. Listing and Filtering to our end points.
  5. Upload image.
  6. Wrote lot of Unit test.
  7. 1User Authentication.
  8. Creating Objects.
  9. Filtering and sorting objects.
  10. Uploading and Viewing images

### Getting Started
  1. Set up Docker. (Create Dockerfile and docker-compose file with requirements.txt file where all the dependencies will be saved for the virtual environment
  2. Setup Wirtual Environment.
  3. In that virtual environment install all python dependencies.
  4. Install Django.
  5. Install Django-Rest-Framework
  6. Install Flake8 for Linting errrors.
  7. Install pycopg2.
  8. install Pillow for handle image objects.
  9. Run all the Command in Bash.

## Command like code to Start or Run Unit tests.

 1. Create a New repository in github account.
 2. Clone that github repository to our local desktop.
 3. Create a Access Token Key in _Dockerhub Account_ .(Dokcer.com>>login>>Accounts_Setting>>Security>>Create an Access Token to use the server locally with the github file.
 4. Create a Secret *DockerHub_User* and *DockerHub_Token* (githubacc>>repository>>navigate to github repository settings>> Secrets and Variables>> Actions>> 
    **Create DockerHub_User and save the dockerhub username there and create another file Dockerhub_Token and save access token there from generated access token of DockerHub**)
 
 5. Build DockerFile first and atmost necessary. following command/Bash Line code:
 
      > docker build .
 
 6. Build docker-compose file to install all the dependncies in docker environment.
    
      > _docker-compose build_
  
 7. Create an app folder in project to save all the recipe, ingredients , admin , tags and other file. TO create and build dependencies in app file use this command.
      
      > _docker-compose run app sh -c "django-admin startproject app ."_
   
 8. To run Test cases in the command/bash line and test that the test cases are working fine. command to run the Test:
 
      > _docker-compose run app -sh c "python manage.py"_
 
 9. Now create a core file to create and setup databse models and management migration for the Api.
 
      > _docker-compose run app sh -c "python manage.py makemigrations core"_
  
 10. Install Flake8 for fixing the Linting errors.
      
      > _pip install flake8_
  
 11. Run the test with flake8 to fix the Linting issues.

      > _docker-compose run app sh -c "python manage.py test && flake8"_
 
 12. To run the server in local host. (after running server using bash/cmd line, Use another bash/cmd line to run test and migration on server.
 
      > _docker-compose up_ 

 13. The Api will then be available at 
       
       > _http://127.0.0.1:8000_
