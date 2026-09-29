# Django DIY Blog
Basic blog site written in Django (part of MDN Django module assessment)
----
This web application creates an very basic blog site using Django. The site allows blog authors to create text-only blogs using the Admin site, and any logged in user to add comments via a form. Any user can list all bloggers, all blogs, and detail for bloggers and blogs (including comments for each blog).

The models for this site are as shown below:

![Django Blog Models](./blog/static/images/diy_django_mini_blog_models.png)


For more information see the associated [MDN assessment page](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/django_assessment_blog).


## Quick Start

To get this project up and running locally on your computer:

1. Set up the [Python development environment](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/development_environment).
   > **Note:** This has been tested against Django 6.1, which requires Python 3.12 or later.
2. Create and activate a Python virtual environment for the project using [venv](https://docs.python.org/3/library/venv.html), the virtual environment tool built into Python:

   ```
   # Linux/macOS
   python3 -m venv django6_env
   source django6_env/bin/activate

   # Windows
   py -3 -m venv django6_env
   django6_env\Scripts\activate
   ```

3. Assuming your virtual environment is active, run the following commands (if you're on Windows you may use `py` or `py -3` instead of `python3` to start Python):

   ```
   pip3 install -r requirements.txt
   python3 manage.py makemigrations
   python3 manage.py migrate
   python3 manage.py collectstatic
   python3 manage.py test # Run the standard tests. These should all pass.
   python3 manage.py createsuperuser # Create a superuser
   python3 manage.py runserver
   ```

4. Open a browser to `http://127.0.0.1:8000/admin/` to open the admin site
5. Create a few test objects of each type.
6. Open tab to `http://127.0.0.1:8000` to see the main site, with your new objects.
