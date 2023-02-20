import  git 
import os
from git import Repo
import getpass
getpass.getuser()

global current_dir
current_dir = os.getcwd()


git_response_file = "git_response"

global no_of_git_response 
no_of_git_response = 3


repo_checker_counter = 0

global repo
repo = Repo(current_dir)

def repo_creater(repo):   
    print("entering") 
    # Using readline()
    global git_response_file
    with open(f'{git_response_file}', 'a', encoding='utf-8') as file:
        file.close()
    global repo_checker_counter
    if repo_checker_counter < 1:
        repo_checker_counter += 1
        with open(f'{git_response_file}', 'r', encoding='utf-8') as file1:
        # Get next line from file
            line = file1.readline()
    
        # if line is empty
        if not line:
            print("gdggggggggggggg")
            repo.git.checkout('-b', getpass.getuser())
            with open(f'{git_response_file}', 'a', encoding='utf-8') as file1:
                file1.writelines("True")
                file1.writelines("\nFalse")
                file1.writelines("\nFalse")
                file1.close()
            return True
        elif line[0] == "True":
            print("Yoo")
            file1.close()
            return True
        elif line[0] == "False":
            repo.git.checkout('-b', getpass.getuser())
            file1.close()
            return True
        else:
            file1.close()
            return False
        
        


repo_creater(repo)

origin = repo.remote(name='origin')

if repo.git.diff():
    print("Yes")
    print(repo.git.add('--all'))
    print(repo.git.commit('-m', 'commit message from python script'))
else:
    print("Everyting is up to dated")
    
if origin.push():
    print("Pushed")
else:
    print("Failed")


    