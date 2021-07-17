

### 15 : adding login , logout and change password
### Steps: we will use django built in auth stytem
1. adding django site authentication urls(for login , logout , password management)
 urlpatterns+=[
     path('accounts/' , include('djando.contrib.auth.urls'))
 ] 
after this if we go to localhost:8000/accounts/ .. we will find the login,logout,pass_change and much more ..works if you add their templates

2. we will create the **template folder** as django needs and make **registration** folder inside it and inside rigisteration put all template pages with names as django need , so django able to find them..ok so manage_level>>templates>>registration

3. we start adding pages as djago need
  * login.html and you can add mdn code to test with it and you can customise it 
  * logout.html as above you can use mdn code
  * password_reset_form.html as abvoe
  * password_reset_done as above
  * password_reset_email.html as above
  * password_reset_confirm.html as above
  * password_reset_complete.html as above
  * password_change_form.html ..this page not found in mdn but we will copy pass_reset_from.html as change some code
  
4. add accounts app in INSTALLED_APPS In setting.py file and to show the result we will go to this urls in our browser ..we will find error in extended page so we need to correct page name with our project base page name and if rename block body to block content...OOPs! after we go to password reset we find that it go to admin reset password not our user ..and we fix that by replace apps position becouse django start from top-to-buttom and admin app was before , accounts so this confilct occur as urls if you remeber order is required.

5. to make this pages extends my base page we will create page that this page extends it <base_generic.html> and adding add job page and replace form secction with block content to replace it later with each page content






### Notes:
   * django provides to us a good built in auth system..but you need to understand it to know how you can to customise it
   the best place you should to visit them  after search about "django user authentication" ..are <django docs> and <mdn: django tutorial part8> is best than docs as per mahmoud ahmed

