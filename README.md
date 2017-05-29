URBAN MUSEUM 


Urban museum is the most completed project from all the course. It mixed all issues when managing a digital project: ideation, research, planning, designing and developing. The very beginning of this project happened when I created my Instagram account a few months ago. At this moment, I decided that I wanted to share good pictures with my friends so I tried to select carefully the content by choosing only the beautiful thing I see. Then I realised that I just share graffitis and urban art pictures and I enjoyed that and my friends as well as they used to like that. So that is how I had the idea of the project. 

I wanted to created a space where people can create pictures galleries of the urban Art from their cities or places they visit so that a virtual museum is created. Then, they can share it with their friends and let them enjoy as if they are visiting it. 

It is a Django project base on a strong Back End Logic which allow users to created content but most important make it shareable by a other user content search engine.

http://urban-museum-23.herokuapp.com/

How it works?


When a user visit the website for the first time, registering is necessary. Once they are inside, the first thing they will see it is other people content so they can enjoy Urban Art from the very beginning. The search engine is inspired on Spotify so Users can search by places, name of the museums or usernames. But if they don´t know where to begging, both the latest upload and most popular content will appear in this page. 

After visiting some pictures, Users can start interacting with the app so they can go to “create a museum” and they can fill the forms in order to set their owns museums. Once the museums is created, They can add the pictures which will feed the gallery. 

If people wan to collaborate with the project, making a donation is possible by accessing to “make a donation”, users can invite us to a coffee which help us to be awake and work more on that project. 


Back End

All the Back End logic is based on the MCV model and on the Django framework. The first task was to created the authenticate logic in which users can register and log in. 

The most important part it is the creation of the museums and its galleries. Thinking as if It is a blog, I created to python apps: one for created the museums and other for creating the picture galleries. Dealing with foreign and primary keys, I manage to associated pictures to a specific museums. 

The next part was about make the content shareable. For that missions, Discover page was created. It this view, I had to select the data from the latest museums created (ordering the queue by date) and from the most popular. For that I insert into the modal the field views and all time users (when not the creator) visit a museum, a view will be added. Then, I had to display that information ordering by views. For the last, a search box input was added so that, the next page will be display the result will match with the word users tape on the input. 

For the last, a little e-commerce was created in order to let users to make the donations by buying a “virtual” coffee for us. In that way, product and cart modals were created, so I can store that information in our database and let people make payments by stripe. 

Front End

The layout was thought in order to created a intuitive UX experience. With a minimalist design, icons have big importance in all pages so that users can understand the process easily. 

It work with a Bootstrap template but It was totally redefined in order to reach a personalised style. 


Technologies used:


Languages : HTML , CSS , JavaScript

Frameworks : Bootstrap , Python, Django.

Library and Plugins : Jquery, Postgress SQL. 

Hosting : Heroku






