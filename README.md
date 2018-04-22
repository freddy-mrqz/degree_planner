# Depaul Graduate Degree Planner

DGDP is a web application developed by a team of students in a software projects class. The app helps Computer Science or Information Systems graduate students plan out their Masters program path. Students may register, browse courses, create/store degree paths, and change majors/concentration if needed.

# Prerequisites for developers

Make sure these are installed locally on your computer 

* Python 3.6
* Postgresql (cli, gui, or DaaS)
* virtualenvwrapper ("virtualenvwrapper-win" for windows)


For the sake of being brief, we will assume virtualenvwrapper has been added to the users path and can use commands like ```workon``` and ```deactivate```.

### Installing

With virtualenvwrapper installed, create a virtual environment for the project and copy the requirements into your new environment. It will activate automatically.

```bash
mkvirtualenv degree_planner
cd to/your/projects/directory/
git clone https://github.com/freddy-mrqz/degree_planner.git
pip install -r requirements.txt
```

### Running Locally

Run the app's server to ensure the it has been installed correctly,
```bash
python3 manage.py runserver
```
If no errors occur, start up a browser and go to http://127.0.0.1:8000/ to see the app running locally on your computer.

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
