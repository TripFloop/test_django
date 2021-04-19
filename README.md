# test_django
Solved technical problem. 
1. Create an empty Github repository. 2. Create and push an empty Django Project in GitHub, don`t forget about the gitignore. 
3. The Project must be virtualized via pipenv, .pipenv files must also be pushed into the repository. 
4. Create a model “News”, which contains the title and content, as well as the date of publication. 
5. Create an admin panel and customize it. 
6. Connect DRF and create a ModelView, that will allow you to create news, receive news list, update and delete it via REST API. 
7. Connect celery and write a periodic task that creates a random news every 5 mins. ! Each item must be a saparate committee. 
8. Run the application on a digital ocean server. 
9. Write tests that would test the functionality from point 6.  
10. Create an item menu, make a menu bar in the template, with the output of these menu items from the model. There should be a “Home” (with Hello, World!”) and the page with the list of news. The item menu must be output from the context processor.  
11. Create middleware that will prescribe <! - HelloWorld >> before closing the header. 
12. Create another page that displays a list of users and the number of news items written in brackets, next to its username.

Used technologies: Django, Celery, Redis, django-rest-framework, Bootstrap
