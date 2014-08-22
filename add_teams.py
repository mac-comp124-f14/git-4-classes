#!/usr/bin/env python -O
#
# This script adds teams to an existing repository.
# Note that the mk_repo.py script already does this, so this
# is only necesary if new students are added after a repo is created.
#

import sys

from config import Config
import my_github

def add_teams_to_repo(gh, reponame, users):
    for username in users:
        username = username.strip()
        if not gh.is_user(username):
            print 'unknown user:', username
            continue
        t = 'team_' + username
        gh.add_team_to_repo(reponame, t)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'usage: %s repo_name1 repo_name2 ...' % sys.argv[0]
        sys.exit(1)

    config = Config()
    gh = my_github.GitHub(config.org, config.owner)
    for name in sys.argv[1:]:
        add_teams_to_repo(gh, name, config.students)
