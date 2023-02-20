import  git 

from git import Repo
existing_repo = Repo('/home/logi/dev_ws/arduino_firmware')

existing_repo.git.add('--all')
existing_repo.git.commit('-m', 'commit message from python script')
origin = existing_repo.remote(name='origin')
origin.push()