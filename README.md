## Exercise Log - privately log your workouts to keep track of your progress!
https://jgexerciselog.herokuapp.com/accounts/login/

Implemented user authentication - users can register an account, login and logout:

![screen shot 2019-02-10 at 6 59 04 pm](https://user-images.githubusercontent.com/40340806/52541820-2e1c5180-2d67-11e9-89d5-75467d26549e.png)

Once logged into the application, users can add workouts to their exercise log. I have the model/form set up to track the workout name (CharField), text description (TextField), and date_posted (DateTimeField). I also included an Owner field that links to the User to the specific posts using ForeignKey.

Design: base html/css files were from Start Bootstrap & W3 Schools.
