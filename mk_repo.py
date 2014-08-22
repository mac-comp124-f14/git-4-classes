import sys
from config import Config
import my_github

def main(reponame, is_private):
    config = Config()
    gh = my_github.GitHub(config.org, config.owner)
    gh.mk_repo(reponame, is_private)

    for username in config.students:
        username = username.strip()
        if not gh.is_user(username):
            print 'unknown user:', username
            continue
        print 'preparing to add', username, 'to', reponame
        t = 'team_' + username
        gh.add_team_to_repo(reponame, t)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print 'usage: %s repo_name is_private' % sys.argv[0]
    elif sys.argv[2] not in ('True', 'False'):
        print 'is_private must be True or False'
    else:
        main(sys.argv[1], eval(sys.argv[2]))
