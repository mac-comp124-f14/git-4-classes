git-4-classes
=============

A collection of utilities for instructors using GitHub in the classroom. The general workflow for preparing, posting, and grading assignments is:

* The instructor creates an organizational educational account that supports private repos.
* Each student registers on GitHub and shares their username with the instructor.
* The instructor creates a separate organizational "team" for each student.
* The instructor posts an assignment, and makes it available to all students / teams.
* Students fork the assignment, complete the assignment on their fork, and push their finished work.
* The instructor creates a pull request in the student's fork against the original assignment and comments on the student's work.


###Preparing 
1. Request a free [GitHub organizational education account](https://github.com/edu).
2. Ask all your students to create github accounts and get their github usernames.
3. Install https://github.com/sigmavirus24/github3.py and clone this repo:

```bash
pip install github3.py
git clone https://github.com/mac-comp124-f13/teachers.git
```

###Configure your installation
Collect github usernames for your students. Then edit config.txt to reflect your course. The default config.txt looks like:
```
org=mac-comp124-f13
owner=shilad
admin=shilad
admin=rgold1
student=jack
student=jill
```
The format is self-explanatory. All values are to the right of the equals sign are github usernames. The admin accounts will have read/write access to all homework forks.

###Creating teams

You'll need to create a separate team for each user. To do so, run:
```bash
python ./mk_teams.py
```
This command can be safely re-run on existing teams when students are added to `config.txt`.

###Creating an assignment
First, create an empty github project.
```bash
python ./mk_repo.py hw0 True
```

The last argument (`True` or `False`) specifies whether the repo is private. 
You'll want to make assignments private, but activities can be public.
Git organizations have a cap on the number of private repos (e.g. a silver plan has 20).
Note that a fork of a private repo doesn't count towards your cap.

Clone the newly created project out and create the homework assignment.
Edit README.md to contain the homework instructions.
Push your work to master when you're done.

###Student process for completing an assignment
To complete an assignment, a student:

1. Creates a private fork of an assignment.
2. Creates a local clone of their forked repo.
3. Completes the assignment and pushes their changes to master on the forked repo.

###Grading student assignments

Run the prepare_to_grade.py script:

```bash
python ./prepare_to_grade.py hw0
```

For each student fork of hw0, this will create a branch called "start" that is identical to the original forked assignment. It will then make a pull request against the assignment. The instructor and grader can comment on each pull request.

###Adding new students to existing assignments
If you create a new team / student after an assignment is already created, you can run the following script:
```bash
python ./add_teams.py hw0 hw2 ....
```
Each repo must already exist. This command can be safely re-run.
