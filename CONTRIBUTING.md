### Codebase structure

Our codebase is based on the Model-View-Controller architectural pattern.     
Here's a simplified tree-view of the repository:

``` bash
.
├── README.md
├── chat-service/
│   ├── model/
│   │   ├── agent-data/
│   │   ├── chat-logs/
│   │   ├── ...
│   ├── static/
│   ├── templates/
|   └── ...
├── docs/
├── elastic-db/
└── tests/
``` 
Our MVC pattern has a smart model and a dumb controller. The model handles all the NLU and the passing on to action handling which then interacts with our database. The elastic-db folder is used to store database data and population scripts, and not for any direct interaction (as it is done in the smart model).

The main controller is the main.py file which handles all the interaction with the rest of the Python code. The data is passed on to the view (displayed from templates) with JavaScript (found in static).
The NLU training data is stored in agent-data. Any processing of it is in the model. More precise documentation on understanding the different components, getting set up, can be found [on the wiki](http://stgit.dcs.gla.ac.uk/tp3-2018-cs01/dissertation/wikis/home).

--------

### How to contribute

In case of git emergencies: [https://wikileaks.org/ciav7p1/cms/page_1179773.html](CIA's Git Hints & Tips)

#### Making a copy of the repository

```bash
git clone http://stgit.dcs.gla.ac.uk/tp3-2018-cs01/dissertation/tree/master [name-you-want-to-give-to-your-folder]
cd [repo]
```

#### Working on an issue

``` bash
# pull latest changes
git pull origin master
## pick an issue: e.g. #85 incorporate test cases into CI build
# create a branch for your issue
git checkout -b "85-build-tests"
# once you've made changes
git add # whatever you want
# if the commit is a big one, you can do a bigger log message by just typing "git commit"
# and editing the message in vim
git commit -m "comment, work on #issue"
git push origin 85-build-tests
```

#### Making a merge request

- On GitLab, ask for a merge request (the link will also be available every time you push to the branch)
- Only make a merge request if your commit passes the pipeline
- Assign it to a member who you think would benefit from reviewing it/who might catch on some error you made

#### Making a code review

- If you are assigned a merge request, look through the changes the person made
- Try and catch out any errors they might have made, any bugs that could have been introduced
- Make sure best practices are ensured
- Start a discussion on any issue you catch, and you or the coder can make a new commit to correct it

#### Deleting a branch locally once merged on the repository

It's not always done automatically...

```bash
git checkout -d name
```
