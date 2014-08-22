#!/usr/bin/env python -O
#
# Creates a new team for every student, and adds all administrators to it.
# This script can be safely rerun - it doesn't recreate existing teams. 
#

import sys

from config import Config
import my_github

def main():
    config = Config()
    gh = my_github.GitHub(config.org, config.owner)

    existing = gh.get_team_names()
    print 'existing teams:', existing

    for name in config.students:
        name = name.strip()
        if not gh.is_user(name):
            print 'unknown user:', name
            continue
        print 'preparing structure for', name
        t = 'team_' + name
        if not t in existing:
            gh.mk_team(t, 'pull')
            for n in config.admins + [name]:
                gh.add_to_team(n, t)
            

if __name__ == '__main__':
    main()
