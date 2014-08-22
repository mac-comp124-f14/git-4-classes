import getpass
import github3  # https://github.com/sigmavirus24/github3.py
import traceback


class GitHub:
    def __init__(self, org, user, password=None):
        self.org = org
        self.user = user
        self.pw = password
        if not self.pw:
            self.pw = getpass.getpass('Password for %s: ' % user)
        self.gh = github3.login(user, password=self.pw)
        self.test()

    def is_team(self, name):
        self.get_org().create_team(name, [], perms)

    def get_team_names(self):
        return set([t.name for t in self.get_org().iter_teams()])

    def mk_team(self, name, perms='push'):
        self.get_org().create_team(name, [], perms)

    def mk_repo(self, reponame, private=False):
        if not self.get_org().create_repo(reponame,
                        auto_init=True,
                        gitignore_template='Java',
                        private=private):
            raise Exception('Creation of repo %s failed' % reponame)

    def get_history_hashes(self, owner, repo):
        """
            Gets the commit hashes associated with a repo and returns them as a list.
            owner can either be a git username or an organization name.
            Hashes are returned in order from oldest to newest.
        """
        hashes = []
        for commit in self.gh.repository(owner, repo).iter_commits():
            hashes.append(commit.sha)
        hashes.reverse()
        return hashes
    
        
    def get_org(self):
        org = self.gh.organization(self.org)
        if not org:
            raise Exception('Unknown org %s' % org)
        return org

    def add_to_team(self, username, teamname):
        if not self.is_user(username):
            raise Exception('Unknown user %s' % user)
        if not self.get_org().add_member(username, teamname):
            raise Exception('adding member %s to team %s failed' % (username, teamname))

    def add_team_to_repo(self, reponame, teamname):
        reponame = self.org + '/' + reponame
        if not self.get_org().add_repo(reponame, teamname):
            raise Exception('adding team %s to repo %s failed' % (teamname, reponame))

    def create_branch(self, owner, repo, sha, name):
        """
            Creates a new branch in the repo with the given owner.
            Branch is named name and starts at revision sha.
        """
        
        r = self.get_repo_or_die(owner, repo)
        if not r.branch(name):
            ref = r.create_ref('refs/heads/' + name, sha)
            if not ref:
                raise Exception('failed to create branch %s in repo %s/%s' % (name, owner, repo))

    def is_user(self, name):
        return self.gh.user(name)

    def has_repo(self, owner, name):
        return self.gh.repository(owner, name)

    def get_repo_or_die(self, owner, name):
        repo = self.gh.repository(owner, name)
        if not repo:
            raise Exception('No such repo: %s/%s' % (owner, repo))
        return repo

    def pull_between_branches(self, owner, repo, from_branch, to_branch, title, desc=None):
        """
            Creates a pull request between branches in the same repo.
        """
        r = self.get_repo_or_die(owner, repo)
        try :
            if not r.create_pull(title, from_branch, to_branch, desc):
                raise Exception('failed to create pull from %s to %s in repo %s/%s' % (from_branch, to_branch, owner, repo))
        except:
            """ For now there seems to be a bug in git repos."""
        
    def test(self):
        u = self.gh.user()
        print 'logged in', u.name, u.login, u.followers

