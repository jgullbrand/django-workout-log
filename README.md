## Exercise Log - privately log your workouts to keep track of your progress!
https://jgexerciselog.herokuapp.com/accounts/login/

Implemented user authentication - users can register an account, login and logout:


Once logged into the application, users can add workouts to their exercise log. I have the model/form set up to track the workout name (CharField), text description (TextField), and date_posted (DateTimeField). I also included an Owner field that links to the User to the specific posts using ForeignKey.

Design: base html/css files were from Start Bootstrap & W3 Schools.
