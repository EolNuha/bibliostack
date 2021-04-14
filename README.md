#                                                BIBLIOSTACK
BiblioStack is a question and answer platform, with the options to upload documentation and images for all students and professionals in Kosovo. 

### - How BiblioStack works?
- BiblioStack is run by users, you users ask the questions and other users will help you answer it.

- Each user has it’s own profile with his/her data (Full Name, Username, Email and a profile image)

- You can also search for different questions and make comments to that question anonymously without an account.

- BiblioStack is not a forum site, its all about getting answers, and not about discussions. The best answer can be up voted and rise to the top. The person that   asked the question can then mark an answer as accepted.

- All questions are tagged with their subject areas. Each can have up to 5 tags, since a question might be related to several subjects. Click a tag to see a list   of questions belonging to that tag.

 

### - The technologies that were used?
The BiblioStack development is divided into three parts: Backend, Frontend and Database

1. The backend is developed using the Python language and the Python framework Django.

   - With Python and Django was developed the logic to handle all BiblioStack’s functionalities like:

     - User register and login authentication.

     - Being able to post, update and delete questions.

     - Being able to up vote or down vote a question.

     - Tags were created using a Django library called “django-taggit“.

     - Sending emails was used Django’s email configuration.

     - The search engine was created using Postgresql’s querying mixed with Django’s own search functions.

2. The frontend is developed using different languages and libraries, like HTML&CSS, JavaScript, BootStrap,  JQuery etc…

   - HTML was used for structuring the websites look.

   - For styling was used mostly bootstrap except for some of our own changes.

   - JavaScript was used for making the website interactive with the user, together with its library JQuery.

3. For the functionality of tags input field was used a package named “bootstrap-tagsinput”.

   - For storing the users data, questions and answers of those users was used the PostgreSQL database.

   - The Postgresql database is stored in a remote server separate from the website and then linked from there.

   - The database has three tables:

     - User table (for storing user’s data)

     - Post table (for storing questions)

     - Comment table (for storing questions answers)

   - Postgresql is also used in making queries so that the search engine is more powerful.


