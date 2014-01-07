git-4-classes
=============

A collection of utilities for instructors using GitHub in the classroom.


####Preparing 
1. Request a free [GitHub organizational education account](https://github.com/edu).
2. Ask all your students to create github accounts and get their github usernames.
3. Install https://github.com/sigmavirus24/github3.py and clone this repo:

```bash
pip install github3.py
git clone https://github.com/mac-comp124-f13/teachers.git
```

####Creating teams

You'll need to create a separate team for each user. Add git usernames to `usernames.txt`
```bash
python ./mk_teams.py
```
This command can be safely re-run on existing teams when `usernames.txt` is updated.

####Instructor process for creating an assignment
First, create an empty github project.
```bash
python ./mk_repo.py hw0 True
```

The last argument (`True` or `False`) specifies whether the repo is private. 
You'll want to make it private for an assignment, but activities can be public.
Git organizations have a cap on the number of private repos (e.g. a silver plan has 20).
Note that a fork of a private repo doesn't count towards your cap.

Clone the newly created project out and create the homework assignment.
Edit README.md to contain the homework instructions.
Push your work to master when you're done.

####Make the assignment readable to students
Once the homework assignment is ready for students, you need to add each student's team as a collaborator with pull permissions.
```bash
python ./add_teams.py hw0 game-of-life activity1 ....
```
Each repo must already exist. This command can be safely re-run on existing teams when `usernames.txt` is updated.

####Student process for completing an assignment
To complete an assignment, a student:

1. Creates a private fork of an assignment.
2. Removes access to their fork for all teams but their own. (TODO: write a script to do this).
3. Creates a local clone of their forked repo.
4. Completes the assignment and pushes their changes to master on the forked repo.

####Grading student assignments
