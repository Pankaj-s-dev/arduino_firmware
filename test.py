# file1 = open(f'{current_dir}git_response_file', 'a+'):
#     file1.close()
# with open('example.txt', 'r', encoding='utf-8') as file:
#     file.close()    
with open('example.txt', 'r+', encoding='utf-8') as file:
    data = file.readlines()
  
print(data[0])
data[1] = "Here is my modified Line 2\n"
  
with open('example.txt', 'w', encoding='utf-8') as file:
    file.writelines(data)