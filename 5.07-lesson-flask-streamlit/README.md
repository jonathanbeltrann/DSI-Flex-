# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Flask 

---

## Materials We Provide


| Topic | Description | Link |
| --- | --- | --- |
| Lesson | Introduction to Flask Slides | [Link](./flask.pdf)|
| Bonus | Model Pickling Workflow | [Link](./assets/pickle_flow.ipynb)|


> **Dataset description:** Ames.

---

## Learning Objectives

*After this lesson, students will be able to:*
1. Explain what Flask is and what a route is.
2. Spin up a simple web API using the Flask framework.
3. Create app routes to perform a variety of tasks, including serving data to or collecting input from our users.
4. Deploy a simple Flask app to Heroku

---

## Student Requirements

*Before this lesson(s), students should already be able to:*

1. Create basic functions.
2. Perform simple edits to HTML
3. Open files in a text editor

---
## Create a new conda environment

From the command line:

1. `conda deactivate`
1. `conda create -n my_new_env_name python=3.8`
1. `conda activate my_new_env_name`
1. `conda list`
1. `pip install sktime`  # install packages. sktime installs several popular ds packages
1. `pip install jupyterlab`
1. `pip install flask`

---

## Start a local server

From the command line:

1. `python my_app_name.py`
1. View in browser at the location provided.
1. `ctr + c` to stop
1. You will have to restart your server occassionally

---

## Deploy to heroku

1. Install heroku cli.
1. Sign up for a free Heroku account.
1. In a folder not inside a git repo
1. `pip install gunicorn` # server
1. Create a `requirements.txt` file with your pip package versions pinned. `pip freeze > requirements.txt` does this for you, but you will want to delete any extra packages in your environment.
1. Create a _runtime.txt_ file to pin your Python version `python-3.8.7`
1. Create a _Procfile_. This tells Heroku what to do to create your app. `web: gunicorn app:app`
1. Initialize a git repository `git init`
1. Stage changes `git add .`
1. Commit changes `git commit -m 'my_commit_message'`
1. `heroku create`
1. Log in to Heroku with `heroku login`
1. Push your app with `git push heroku master`
1. See your app on the web at your url 🎉 (or troubleshoot) with `heroku open`
1. View your app status in your online Heroku dashboard 



## Other Materials

1. [Flask Deployment Options](https://flask.palletsprojects.com/en/1.1.x/deploying/)
1. [FastAPI](https://fastapi.tiangolo.com/) is perhaps the successor to Flask. It's a similar way to make an API but provides self-documentation and runs faster.
1. [Django](https://www.djangoproject.com/) is another popular web API framework. Flask and FastAPI are lightweight. [Django](https://www.djangoproject.com/) is not.
