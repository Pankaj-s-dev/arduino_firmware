import  git 
import os

from git import Repo
existing_repo = Repo(os.getcwd())

print(existing_repo.git.diff())
print(existing_repo.git.add('--all'))
print(existing_repo.git.commit('-m', 'commit message from python script'))
origin = existing_repo.remote(name='origin')
print(origin.push())
