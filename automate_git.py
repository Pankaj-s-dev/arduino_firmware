import  git 
import os


from git import Repo
existing_repo = Repo(os.getcwd())

existing_repo.git.add('--all')
existing_repo.git.commit('-m', 'commit message from python script')
origin = existing_repo.remote(name='origin')
origin.push()