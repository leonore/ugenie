# Branching

Summary:
  - Creating a new branch
  - Switching to branches
  - Merging your branch into the project

In case of emergencies: [https://wikileaks.org/ciav7p1/cms/page_1179773.html](CIA's Git Hints & Tips)

---------
##### Creating a new branch      

```bash
git checkout -b name
```

##### Switching between your branches

```bash
git checkout name # Switched to branch 'name'
git checkout master # Switched to branch 'master'
```

##### Commiting to your new branch

```bash
git checkout name # Switched to branch 'name'
# Watch your folder change to that branch's files...
# Make some changes...
git add *
git commit -m "message"
git push origin name
```

##### Now comes the merge request

- On GitLab, ask for a merge request
-  The project manager (Sam) needs to approve it

##### Deleting a branch (done automatically when merging, only if you want to actually delete it)

```bash 
git checkout -d name
```
