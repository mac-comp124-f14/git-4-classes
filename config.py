# A simple configuration module for courses

import sys

class Config:
    def __init__(self, config_path='config.txt'):
        self.org = None
        self.owner = None
        self.admins = []
        self.students = []
        for line in open(config_path):
            line = line.strip()
            if line.startswith('org='):
                self.org = line[4:]
            elif line.startswith('owner='):
                self.owner = line[6:]
            elif line.startswith('admin='):
                self.admins.append(line[6:])
            elif line.startswith('student='):
                self.students.append(line[8:])
        self.log('')
        self.log('using git-4-classes config:')
        self.log('\torg = %s' % self.org)
        self.log('\towner = %s' % self.owner)
        self.log('\tadmins = %s' % (self.admins,))
        if not self.students:
            self.log('\t%0 students')
        else:
            self.log('\t%d students from %s to %s'
                    % (len(self.students), self.students[0], self.students[-1]))
        self.log('')
    

    def log(self, message):
        sys.stderr.write(message + '\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        config = Config(sys.argv[1])
    else:
        config = Config()
