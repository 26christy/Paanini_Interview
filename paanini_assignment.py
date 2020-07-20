"""
.. :module:: paanini_assignment
   :synopsis: Automate Git process to create a repo and to 
              add and remove files
.. moduleauthor:: Christy M Thomas <26christy@gmail.com> (July 18, 2020)
"""

from github import Github
from github import InputGitTreeElement
import getpass

#enter github credentials. It can also be passed from a separate file
username = input("Enter Github username")
password = getpass.getpass("Password")
git_login = Github(username, password)

#create new repo. If it exists get to the repo else returns error
try:
    repo = git_login.get_user().create_repo('auto-mate', description='paanini assignment')
    repo.create_file("README.md", "init commit", "mock_text")
except:
    repo = git_login.get_user().get_repo('auto-mate')
else:
    print('Repository error')

class GitInteraction:

    def git_commit(self, file_list, file_names, commit_message):
        '''
        To commit the files to git repo.
        Path to the file, file name and commit message
        is passed as the parameters
        '''
        try:
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()

            for i, entry in enumerate(file_list):
                with open(entry) as input_file:
                    data = input_file.read()
                element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
            print("commited to the repo")
        
        except Exception as err:
            print(type(err))
            print(err.args)
            print(err)

    def initial_file(self):
        '''
        commits the intial.txt to the repo
        '''
        f_list = [
            r'path\to\the\file\filename\initial.txt'
        ]

        f_names = [
            'initial.txt'
        ]
        commit_message = 'add initial.txt'

        self.git_commit(f_list, f_names, commit_message)
        print("Added initial.txt")

    def processed_file(self):
        '''
        commits processed.txt and removes initial.txt
        '''
        f_list = [
            r'path\to\the\file\processed.txt'
        ]

        f_names = [
            'processed.txt'
        ]
        commit_message = 'add processed.txt and removed initial.txt'

        self.git_commit(f_list, f_names, commit_message)
        try:
            contents = repo.get_contents('initial.txt')
            repo.delete_file(contents.path, 'remove text', contents.sha)
        except Exception as err:
            print(type(err))
            print(err.args)
            print(err)
        print('Added processed.txt')


if __name__ == '__main__':
    git_object = GitInteraction()
    git_object.initial_file()
    git_object.processed_file()