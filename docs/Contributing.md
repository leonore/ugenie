### Contributors

Mohammad Alnakhli - 2229683a@student.gla.ac.uk      
James Conway - 2247492c@student.gla.ac.uk       
Sam Cook - 2254258h@student.gla.ac.uk     
Leonore Papaloizos - 2264897v@student.gla.ac.uk     

### Structure & Roles

#### Informal roles (issue label "manager")

`Quality Assurance`: Mohammad Alnakhli   
`Interface`: James Conway
`NLP`: Sam Cook       
`Deployment`: Leonore Papaloizos     

#### Formal roles

Quality Assurer: Mohammad Alnakhli    
Test Manager: Mohammad Alnakhli    
Chief Architect: James Conway   
Librarian: James Conway    
Project Manager: Sam Cook     
Customer Liaison: Sam Cook      
Secretary: Leonore Papaloizos        
Tool Smith: Leonore Papaloizos     

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
