
### 18 - adding profile to each user

### steps: 
   1. adding new url in account app urls.py to profile page say: **Path('profile' , view.profile , name='profile')**

   2. adding view in account app views.py that handel this request say : **def profile(request):**

   3. adding template that render this context sendsfrom profile view say:**profile.html** 

