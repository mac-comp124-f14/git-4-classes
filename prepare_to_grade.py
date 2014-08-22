#!/usr/bin/env python -O
#
# This script prepares to grade students homework submissions for a particular assignment.
# To do so, it creates a branch on each student's fork equivalent to the original assignment.
# It then creates a pull request against that branch.
#

from config import Config
import my_github
import sys


def main(gh, config, repo):
    for u in config.students:
        u = u.strip()
        if u in config.admins:
            continue
        if not gh.has_repo(u, repo):
            print 'no repo %s/%s' % (u, repo)
            continue
        sha = get_last_shared_hash(gh, u, config.org, repo)
        gh.create_branch(u, repo, sha, 'start')
        gh.pull_between_branches(u, repo, 'start', 'master',
                'Grading pull', 'A pull request for grading purposes')


def get_last_shared_hash(gh, user, org, repo):
    uhashes = gh.get_history_hashes(user, repo)
    ohashes = gh.get_history_hashes(org, repo)
    latest = None
    for i in range(min(len(uhashes), len(ohashes))):
        if uhashes[i] == ohashes[i]:
            latest = uhashes[i]
        else:
            break
    return latest

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'usage: %s repo_name' % sys.argv[0]
        sys.exit(1)
    config = Config()
    gh = my_github.GitHub(config.org, config.owner)
    main(gh, config, sys.argv[1])
