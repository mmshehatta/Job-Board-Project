

### adding signup:
### steps:
 1. adding a url to our sign up view that handel signing up proccess , url as * path('accounts/' , include('account.urls' , namespace='account')) * ..Note that accounts path is repeated is this error ? No it is ordinary beacause each path will go different places the first will go to django auth and second will go to my signup function ...**Done**

 2. adding view that handel , signup request ..this view need to send form by context to the template so we need to add forms.py file in account app that amplements form that extends UserCreationForm ..what is creationForm ? well UserCreationForm is : 
    A ModelForm for creating a new user.
    It has three fields: username (from the user model), password1, and password2. It verifies that password1 and password2 match, validates the password using validate_password(), and sets the user’s password using set_password().
**Done**

 3. template containing  signup form (you can copy login.html and edit it ) ..well ..**Done**

 * we don't hard coded the form and implementing form validation and hashing passord but we will extend django userCreataionForm that provides to us all powerful validation and containing all user fields that we need ... this fields actualy exists in user model ..thanks to django

 4. to make the signup user is loged in we can do this in signup view function by authenticat , login and redirect methods thst are built in django


 ### Notes:
  * when we make signup user logedin user the admin session is terminated and new user session is created

  * we note also , that new profile is created when we create new user 