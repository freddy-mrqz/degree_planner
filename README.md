# Depaul Graduate Degree Planner

DGDP is a web application developed by a team of students in a software projects class. The app helps Computer Science or Information Systems graduate students plan out their Masters program path. Students may register, browse courses, create/store degree paths, and change majors/concentration if needed.

# Prerequisites for developers

Make sure these are installed locally on your computer 

Windows 10 Pro:
* Docker for Windows 

Any other Windows:
* Docker Toolbox

### Installing, Running and Development with Docker

Docker containers have been set up for our app and database. Docker has tons of tags and commands to learn. So, A Makefile has been created for convenience.

upon initial setup, run

```
make docker 
```
This will create our app and database containers. this will take a couple minutes. Once this has been completed run

```
make up_build_d
```
to get our images and containers up and running in the background. you can now access our app at localhost:8000 (or 127.0.0.1:8000)

Development can be done as you would normally do. Docker will reflect the changes done on our app in real time. When changes have been made that require migrations to be run on our app, (e.g. creating/editing models) access our containers by running

```
make exec
```
You are now inside the docker container. You can run commands like 
```
./manage.py makemigrations
./manage.py migrate
```
to exit the container, just type ```exit```. 

When you are done with development, it is best practice to shut down our containers by running
```
make down
```

whenever you want to start them up again, simply run 
```
make up_build_d
```
and start developing :).

**Note: This replaces `mkvirtualenv`, and any other installation instructions. This is best used if you are familiar with Docker and docker-compose.***



#### Development best practices 

The master branch should be kept clean of errors and must always be able to run at least locally for now. In order to avoid breaking our app, all changes must be done in seperate branches and pushed to the master branch after it has been closely reviewed and tested. To create a new branch for development,

Before making ANY changes, make sure your local repo is updated with the remote repo on GitHub.
```bash
cd to/your/project/
git fetch
git merge origin/master
```
Now you can create and checkout a new branch based on master.
```bash
git checkout -b your-branch-name
```
Once the branch is ready to be pushed to master, create a pull request manually on github and notify each developer to review the feature. If all requirements are met, the branch can be merged onto master.
