
### 19 - Enable edit profile feature 

### steps;
   1. in **profile** view we need to send to the template **profile.html** user info and profile info in it's context because the  profile info exits in 2 tables (user and profile) so we need to render 2 form to edit this info and save edit data by one edit button.

   2. to do that we need to make to forms classes U_info_form and P_info form that extends model forms that enables form takes all fields from needed model as (User and Profile) 

   3. don't forget instance=user.request in u_info_form and instance=profile in p_info_form ..i need to search about this 

   4. don't forget request.FILES if form containing images or files and in form tag you must use **</ enctype="multipart/form-data /">** attribue to save image ...i exhusted to know that  

